# Lab Session Instructor Guide
**CS 290 Week 1: Comprehensive Hands-On Lab (Slides 34-50)**

## Pre-Session Preparation

### **Technical Setup** ⚙️
- [ ] Verify classroom computers have Python 3.8+
- [ ] Test internet connectivity for API calls
- [ ] Prepare OpenAI API key distribution method
- [ ] Set up shared code repository/templates
- [ ] Test sample API calls from classroom network

### **Materials Preparation** 📋
- [ ] Print troubleshooting reference sheets
- [ ] Prepare parameter reference cards
- [ ] Set up collaboration groups (3-4 students each)
- [ ] Prepare extension activities for fast finishers

### **Room Setup** 🏫
- [ ] Arrange desks for peer collaboration
- [ ] Ensure projector/screen visibility from all seats
- [ ] Test audio for code explanations
- [ ] Prepare whiteboard for debugging help

## Session Flow & Timing

### **Part 1: Environment Setup (30-40 minutes)**
**Slides 34-37**

#### **Slide 34: Python Environment Verification (10 min)**
**Instructor Actions:**
- Walk through verification checklist together
- Demonstrate commands on main screen
- Identify students with issues early
- Pair students with working environments with those having problems

**Common Issues & Solutions:**
- Python not in PATH → Show PATH addition process
- Multiple Python versions → Guide to specific version selection
- Permission issues → Demonstrate `--user` flag usage

**Student Support:**
- Circulate to help individual students
- Use peer mentoring for common issues
- Keep spare laptops ready for critical failures

#### **Slide 35: LiteLLM Installation (10-15 min)**
**Instructor Actions:**
- Demonstrate installation command first
- Show both pip and pip3 methods
- Explain virtual environment benefits (optional)
- Verify installation with import test

**Teaching Tips:**
- Emphasize the importance of verification steps
- Show how to interpret error messages
- Encourage documentation of successful commands

#### **Slide 36: API Key Setup (10-15 min)**
**Instructor Actions:**
- **CRITICAL**: Distribute API keys securely
- Demonstrate environment variable setup for each OS
- Show .env file creation and usage
- Emphasize security best practices

**Security Reminders:**
- Never commit API keys to version control
- Don't share keys with classmates
- Rotate keys after class if using personal accounts

#### **Slide 37: Connection Test (5-10 min)**
**Instructor Actions:**
- Run the "Hello World" example live
- Celebrate successful connections class-wide
- Help troubleshoot connection failures
- Mark this as major milestone achievement

**Troubleshooting Priority:**
1. Check API key configuration
2. Verify internet connectivity
3. Test with minimal example
4. Check firewall/proxy issues

### **Part 2: Basic API Operations (90-100 minutes)**
**Slides 38-43**

#### **Slide 38: Text Completion Template (15-20 min)**
**Interactive Approach:**
- Students fill in template blanks together
- Encourage creative prompt ideas
- Share interesting results with class
- Discuss parameter choices

**Facilitation Tips:**
- Ask students to share their prompts
- Demonstrate how parameter changes affect output
- Encourage experimentation and iteration

#### **Slide 39: Text Completion Practice (20-25 min)**
**Structured Practice:**
- Run examples together first
- Give students time for independent practice
- Compare outputs and discuss variations
- Analyze parameter impact together

**Learning Enhancement:**
- Create mini-competitions for most creative output
- Discuss unexpected or interesting results
- Help students understand parameter effects

#### **Slide 40: Summarization Task (25-30 min)**
**Deep Dive Activity:**
- Provide same article to all students
- Compare summarization approaches
- Discuss quality indicators
- Analyze system message effectiveness

**Assessment Opportunities:**
- Review student summaries for accuracy
- Discuss what makes a "good" summary
- Compare different prompt approaches

#### **Slide 41: Translation Task (20-25 min)**
**Multilingual Exploration:**
- Test multiple language pairs
- Discuss cultural nuances
- Compare formal vs. informal translations
- Address accuracy concerns

**Cultural Learning:**
- Invite multilingual students to verify translations
- Discuss cultural context in translation
- Explore limitations of automated translation

#### **Slide 42: Text Rewriting (25-30 min)**
**Style Workshop:**
- Use same source text for all students
- Create different target audiences
- Compare style transformations
- Discuss audience awareness

**Creative Extension:**
- Students exchange texts for style challenges
- Vote on most effective style adaptations
- Discuss professional applications

#### **Slide 43: Error Handling (15-20 min)**
**Debugging Practice:**
- Deliberately introduce errors for practice
- Demonstrate debugging process
- Show error message interpretation
- Practice graceful error recovery

**Professional Skills:**
- Emphasize importance in production code
- Show professional error handling patterns
- Discuss user experience considerations

### **Part 3: Advanced Prompt Engineering (80-90 minutes)**
**Slides 44-47**

#### **Slide 44: Role Prompting Workshop (25-30 min)**
**Character Development:**
- Students create unique professional personas
- Test role consistency across interactions
- Compare different role implementations
- Share most effective role designs

**Interactive Elements:**
- Role-playing exercises with AI assistants
- Peer testing of role implementations
- Discussion of role boundaries and ethics

#### **Slide 45: Chain-of-Thought Implementation (20-25 min)**
**Reasoning Practice:**
- Start with mathematical problems
- Progress to logical reasoning tasks
- Compare with/without reasoning steps
- Analyze reasoning quality

**Critical Thinking:**
- Evaluate reasoning accuracy
- Identify flaws in AI reasoning
- Discuss reasoning transparency benefits

#### **Slide 46: Parameter Tuning Lab (30-35 min)**
**Scientific Experimentation:**
- Set up controlled experiments
- Document parameter effects
- Create comparison charts
- Analyze optimal settings for different tasks

**Data Collection:**
- Students record experimental results
- Class compiles aggregate findings
- Discuss parameter selection strategies

#### **Slide 47: Advanced Techniques Combination (25-30 min)**
**Integration Mastery:**
- Combine multiple learned techniques
- Create sophisticated prompts
- Test complex scenarios
- Evaluate technique synergies

**Mastery Assessment:**
- Students demonstrate technique integration
- Peer review of advanced implementations
- Discussion of when to use combined techniques

### **Part 4: Creative Applications & Wrap-up (40-50 minutes)**
**Slides 48-50**

#### **Slide 48: Build Your Own AI Assistant (25-30 min)**
**Capstone Project:**
- Students design personalized assistants
- Implement unique specializations
- Test and refine functionality
- Prepare demonstrations

**Creativity Encouragement:**
- Showcase diverse assistant concepts
- Encourage innovative applications
- Support ambitious implementations

#### **Slide 49: Production Best Practices (10-15 min)**
**Professional Development:**
- Review security considerations
- Discuss cost optimization
- Address scalability concerns
- Preview enterprise applications

#### **Slide 50: Lab Wrap-up & Next Steps (5-10 min)**
**Session Conclusion:**
- Celebrate student achievements
- Preview homework assignment
- Tease next week's advanced topics
- Collect feedback on lab experience

## Assessment Strategies

### **Formative Assessment** 📊
- Completion checkpoints at each slide
- Peer code reviews and collaboration
- Real-time troubleshooting assistance
- Progress tracking through interactive exercises

### **Summative Assessment** 🎯
- Final AI assistant demonstration
- Code quality and error handling implementation
- Creativity and functionality of personal projects
- Understanding of best practices and production considerations

## Student Support Strategies

### **Differentiated Learning** 🎓
- **Fast Finishers**: Extension challenges and helper roles
- **Struggling Students**: Peer mentoring and simplified tasks
- **Diverse Backgrounds**: Multiple approach explanations
- **Different Learning Styles**: Visual, auditory, and kinesthetic elements

### **Collaboration Encouragement** 🤝
- Paired programming for complex tasks
- Group problem-solving for debugging
- Shared celebration of successes
- Peer teaching opportunities

## Troubleshooting Quick Reference

### **Common Technical Issues** 🔧
| Issue | Quick Solution | Prevention |
|-------|---------------|------------|
| API Key Invalid | Verify key format and environment setup | Test keys before class |
| Import Errors | Check Python path and installation | Verify installations pre-session |
| Network Issues | Test alternative networks/hotspots | Backup connectivity plans |
| Code Errors | Step-by-step debugging process | Provide tested code templates |

### **Learning Challenges** 📚
| Challenge | Support Strategy | Resources |
|-----------|-----------------|----------|
| Conceptual confusion | Visual explanations and analogies | Diagram references |
| Coding difficulties | Peer mentoring and pair programming | Code templates |
| Overwhelm | Break tasks into smaller steps | Progress checklists |
| Lack of engagement | Creative challenges and competitions | Extension activities |

## Success Metrics

### **Technical Proficiency** ✅
- 90%+ students complete environment setup
- 85%+ students create working AI assistant
- 80%+ students implement error handling
- 75%+ students integrate multiple techniques

### **Engagement Indicators** 📈
- Active participation in discussions
- Creative and unique project implementations
- Peer collaboration and mutual support
- Positive feedback on learning experience

### **Learning Outcomes** 🎯
- Understanding of LLM API integration
- Competency in prompt engineering techniques
- Awareness of production considerations
- Enthusiasm for continued learning

---

**Remember**: The goal is hands-on learning with support for all skill levels. Maintain energy, celebrate successes, and ensure every student leaves with working code and new skills!