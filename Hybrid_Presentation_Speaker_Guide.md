# Custom Week 1 LLMs & Prompting - Hybrid Presentation Guide

## Overview

This hybrid presentation combines the best elements of both the original and enhanced Week 1 LLM presentations, creating a comprehensive 33-slide educational experience for sophomore Computer Science students.

## Presentation Structure

### **Part I: LLM Fundamentals (Slides 1-10)**
*From Enhanced Version - Duration: ~25 minutes*

1. **Enhanced Cover** - Professional title slide with learning objectives
2. **Enhanced Objectives** - Clear learning outcomes and session structure
3. **What Are LLMs Enhanced** - Comprehensive introduction to large language models
4. **Major LLM Families Enhanced** - Overview of GPT, Claude, Llama, and other major models
5. **LLM Architecture Enhanced** - Technical deep-dive into transformer architecture
6. **Applications Enhanced** - Real-world applications with concrete examples
7. **Text Generation Process Enhanced** - Step-by-step explanation of how LLMs generate text
8. **Tokenization Enhanced** - Detailed tokenization concepts with visual aids
9. **Tokenization Examples Enhanced** - Practical tokenization demonstrations
10. **Next Token Prediction Enhanced** - Core mechanism explanation

### **Part II: Context Windows & Memory (Slides 11-16)**
*From Enhanced Version - Duration: ~15 minutes*

11. **Context Windows Intro** - Introduction to context limitations
12. **GPT Context Windows** - GPT-specific context window capabilities
13. **Claude Context Windows** - Claude's extended context features
14. **Mistral Context Windows** - Mistral model context specifications
15. **Llama Context Windows** - Llama model context capabilities
16. **Context Comparison Table** - Side-by-side comparison of all major models

### **Part III: API Fundamentals (Slides 17-27)**
*From Enhanced Version - Duration: ~30 minutes*

17. **API Basics** - Introduction to LLM APIs
18. **Message Format** - Request/response structure
19. **API Parameters** - Temperature, max_tokens, and other parameters
20. **Error Handling** - Common errors and troubleshooting
21. **LiteLLM Installation** - Setting up the unified interface
22. **Basic Completion** - Your first API call
23. **Summarization Task** - Practical example #1
24. **Translation Task** - Practical example #2
25. **Text Rewriting** - Practical example #3
26. **Parameter Tuning** - Optimizing API calls
27. **Capabilities & Limitations** - Understanding model boundaries

### **Part IV: Advanced Prompting Techniques (Slides 28-31)**
*From Original Version - Enhanced with Professional Design - Duration: ~20 minutes*

28. **Zero-Shot Prompting** - Direct task instructions without examples
   - Key principles and best practices
   - Practical examples: classification, code generation, summarization

29. **Few-Shot Prompting** - Learning from examples
   - Why it works and when to use it
   - Detailed sentiment analysis example
   - Best practices for example selection

30. **Chain-of-Thought Reasoning** - Step-by-step problem solving
   - Why it's effective for complex reasoning
   - Before/after comparison with mathematical example
   - Best applications: math, logic, multi-step analysis

31. **Advanced Techniques** - Professional prompting patterns
   - Role prompting for focused responses
   - System messages for persistent behavior
   - Best practices and prompt engineering patterns

### **Part V: Hands-On Session (Slides 32-33)**
*From Enhanced Version - Duration: ~10 minutes*

32. **Hands-On Overview** - Lab session introduction
33. **Lab Structure** - Detailed lab guide and expectations

## Key Educational Improvements

### **Enhanced Content Integration**
- **Comprehensive Coverage**: Combines enhanced technical depth with detailed prompting techniques
- **Logical Flow**: Seamless progression from theory to practice
- **Professional Design**: Consistent blue color scheme throughout all slides

### **Prompting Techniques Deep Dive**
- **Four Detailed Slides**: Replaces single overview with comprehensive coverage
- **Practical Examples**: Real code examples and step-by-step demonstrations
- **Best Practices**: Professional patterns for effective prompting
- **Visual Consistency**: Enhanced slides styled to match presentation aesthetics

### **Technical Depth**
- **Context Windows**: Detailed comparison across all major LLM providers
- **API Fundamentals**: Comprehensive coverage of practical implementation
- **Error Handling**: Real-world troubleshooting guidance
- **Parameter Tuning**: Optimization strategies for production use

## Timing and Delivery Recommendations

### **Total Duration: 1.5 Hours Lecture + 2 Hours Hands-On**

**Lecture Breakdown:**
- **Minutes 0-25**: LLM Fundamentals (Slides 1-10)
- **Minutes 25-40**: Context Windows (Slides 11-16)
- **Minutes 40-70**: API Fundamentals (Slides 17-27)
- **Minutes 70-90**: Prompting Techniques (Slides 28-31)
- **Minutes 90-100**: Lab Setup (Slides 32-33)

**Interactive Elements:**
- **Slide 9**: Live tokenization demonstration
- **Slide 16**: Context window comparison discussion
- **Slides 22-25**: Live API demonstrations
- **Slides 28-31**: Prompting exercise with class participation

## Speaker Notes and Key Points

### **Critical Concepts to Emphasize**

**Context Windows (Slides 11-16):**
- Explain why context limits matter for practical applications
- Demonstrate how to choose the right model for different use cases
- Show real examples of context overflow and how to handle it

**API Integration (Slides 17-27):**
- Live demonstration is crucial for these slides
- Have backup examples ready in case of API failures
- Emphasize error handling and debugging practices

**Prompting Techniques (Slides 28-31):**
- **Interactive Approach**: Have students suggest examples for each technique
- **Live Comparison**: Show zero-shot vs few-shot results in real-time
- **Chain-of-Thought**: Walk through the math example step-by-step
- **Advanced Techniques**: Connect to real-world software engineering practices

### **Common Student Questions**

**"How do I know which prompting technique to use?"**
- Start with zero-shot for simple, clear tasks
- Use few-shot when you need specific formatting or style
- Apply chain-of-thought for complex reasoning or math problems
- Advanced techniques for specialized or production applications

**"Why are context windows important in practice?"**
- Cost implications for API usage
- Processing speed differences
- Application design considerations
- Real-world limitations students will encounter

**"How do I debug when prompts don't work?"**
- Systematic approach: start simple, add complexity gradually
- Use chain-of-thought to understand model reasoning
- Check for ambiguous language or unclear instructions
- Iterate based on failure modes

## Technical Requirements

### **Equipment Needed**
- Reliable internet connection for live API demonstrations
- Code editor with syntax highlighting
- Terminal access for LiteLLM installation demonstration
- Backup slides/examples in case of technical difficulties

### **Preparation Checklist**
- [ ] Test all API keys and endpoints before class
- [ ] Verify LiteLLM installation works on classroom system
- [ ] Prepare backup examples for each prompting technique
- [ ] Load presentation in full-screen mode for best visual impact
- [ ] Have code examples ready to copy-paste for live demonstrations

## Assessment Integration

### **Formative Assessment Opportunities**
- **Slide 16**: Quick poll on context window preferences
- **Slide 27**: Discuss real-world limitation scenarios
- **Slide 31**: Students create their own role-based prompts

### **Connection to Lab Activities**
- **Slides 28-31** directly prepare students for hands-on prompting exercises
- **API fundamentals** provide foundation for lab API integration tasks
- **Context window awareness** helps students design efficient solutions

## Differentiation Strategies

### **For Advanced Students**
- Challenge them to predict output quality differences between techniques
- Encourage exploration of prompt engineering patterns beyond the slides
- Provide additional resources for LLM fine-tuning and customization

### **For Students Needing Support**
- Focus on practical, concrete examples rather than theoretical concepts
- Provide template prompts for common tasks
- Pair programming approach during hands-on activities

## Additional Resources

### **Recommended Reading**
- OpenAI API Documentation
- Anthropic Claude API Guide  
- LiteLLM Documentation
- "The Prompt Engineering Guide" - comprehensive online resource

### **Practice Exercises**
- Zero-shot prompting challenges
- Few-shot example creation exercises
- Chain-of-thought problem-solving practice
- Role-based prompt development

---

## Presentation Controls

### **Navigation**
- **Arrow Keys**: Navigate slides in presentation mode
- **Spacebar**: Advance to next slide
- **Escape**: Exit presentation mode
- **F**: Toggle fullscreen

### **View Modes**
- **Grid View**: Overview of all slides
- **List View**: Detailed sequential view
- **Presentation Mode**: Full-screen teaching mode

### **Interactive Features**
- Click any slide thumbnail to jump to that slide in presentation mode
- Progress bar shows current position in presentation
- Slide counter displays current and total slide numbers

---

*Created by MiniMax Agent - Custom hybrid presentation combining enhanced technical depth with comprehensive prompting techniques for optimal educational impact.*