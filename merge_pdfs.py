import os
import re
from PyPDF2 import PdfMerger

def natural_sort_key(filename):
    """
    Sort filenames naturally, considering numbers in the filename
    e.g., slide1, slide2, slide10, slide11 instead of slide1, slide10, slide11, slide2
    """
    # Extract numbers from filename for natural sorting
    parts = re.split(r'(\d+)', filename)
    for i in range(1, len(parts), 2):
        parts[i] = int(parts[i])
    return parts

def merge_pdfs_from_slides(slides_dir='slides', output_filename='w09_LLM.pdf'):
    """Merge all PDF files in slides directory into one file, ordered by filename"""
    
    # Get all PDF files in the slides directory, excluding the output file
    pdf_files = []
    for filename in os.listdir(slides_dir):
        if filename.endswith('.pdf') and filename != output_filename:
            pdf_files.append(filename)
    
    if not pdf_files:
        print("No PDF files found in the slides directory!")
        return
    
    # Sort files naturally by filename
    pdf_files.sort(key=natural_sort_key)
    
    print(f"Found {len(pdf_files)} PDF files to merge:")
    for i, pdf_file in enumerate(pdf_files, 1):
        print(f"{i:2d}. {pdf_file}")
    
    # Create PDF merger
    merger = PdfMerger()
    
    try:
        # Add each PDF file to the merger
        for pdf_file in pdf_files:
            pdf_path = os.path.join(slides_dir, pdf_file)
            print(f"Adding {pdf_file}...")
            merger.append(pdf_path)
        
        # Write the merged PDF
        output_path = os.path.join(slides_dir, output_filename)
        with open(output_path, 'wb') as output_file:
            merger.write(output_file)
        
        print(f"\nSuccessfully merged {len(pdf_files)} PDFs into: {output_path}")
        
    except Exception as e:
        print(f"Error during PDF merging: {e}")
    finally:
        merger.close()

if __name__ == "__main__":
    merge_pdfs_from_slides()
