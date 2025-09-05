import asyncio
from playwright.async_api import async_playwright
import os

async def convert_html_with_js_to_pdf(html_file, output_pdf, wait_time=2000):
    """Convert HTML with JavaScript to PDF using Playwright"""
    
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Set viewport to match A4 proportions for better scaling
        await page.set_viewport_size({"width": 794, "height": 1123})
        
        # Navigate to HTML file
        file_path = f"file://{os.path.abspath(html_file)}"
        await page.goto(file_path, wait_until='networkidle')
        
        # Wait for JavaScript to execute
        await page.wait_for_timeout(wait_time)
        
        # Add CSS to ensure content scales properly and override centering
        await page.add_style_tag(content="""
            @page {
                size: A4;
            }
            body {
                transform-origin: top left !important;
                align-items: flex-start !important;
                justify-content: flex-start !important;
                padding-top: 0 !important;
                margin-top: 0 !important;
            }
            .slide {
                height: auto !important;
                min-height: auto !important;
            }
            * {
                box-sizing: border-box;
            }
        """)
        
        # Generate PDF with optimized settings
        await page.pdf(
            path=output_pdf,
            format='A4',
            print_background=True,
            prefer_css_page_size=True,
            margin={
                'top': '0.1in',
                'right': '0.1in', 
                'bottom': '0.1in',
                'left': '0.1in'
            },
            scale=0.8  # Scale down content to fit better while allowing page breaks
        )
        
        await browser.close()
        print(f"PDF with JavaScript effects generated: {output_pdf}")

async def batch_convert_html_to_pdf(slides_dir='slides'):
    """Batch convert all HTML files in slides directory to PDF"""
    
    # Get all HTML files in the slides directory
    html_files = []
    for filename in os.listdir(slides_dir):
        if filename.endswith('.html'):
            html_files.append(filename)
    
    print(f"Found {len(html_files)} HTML files to convert")
    
    # Convert each HTML file to PDF
    for html_file in sorted(html_files):
        html_path = os.path.join(slides_dir, html_file)
        pdf_file = html_file.replace('.html', '.pdf')
        pdf_path = os.path.join(slides_dir, pdf_file)
        
        print(f"Converting {html_file} to {pdf_file}...")
        try:
            await convert_html_with_js_to_pdf(html_path, pdf_path)
        except Exception as e:
            print(f"Error converting {html_file}: {e}")
    
    print("Batch conversion completed!")

# Usage - batch convert all HTML files in slides directory
#asyncio.run(batch_convert_html_to_pdf())
asyncio.run(convert_html_with_js_to_pdf('slides/slide01_enhanced_cover.html', 'slides/slide01_enhanced_cover.pdf')    )