# 🤖 CrewAI Researcher

An intelligent research automation system powered by CrewAI that uses multiple AI agents to conduct comprehensive research and generate detailed reports on any topic.

## ✨ Features

- **Multi-Agent Research**: Two specialised AI agents work together - a Research Analyst and a Content Strategist
- **Automated Web Search**: Leverages search tools to gather the latest information
- **Structured Reports**: Generates well-formatted, comprehensive research reports
- **Sequential Processing**: Agents work in sequence for optimal research flow
- **Customisable Topics**: Research any subject by simply changing the topic variable

## 🚀 Quick Start

### Prerequisites
- Python 3.11+ (recommended for compatibility)
- OpenAI API key (or other supported LLM provider)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/crew-ai-researcher.git
   cd crew-ai-researcher
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install crewai[tools] python-dotenv
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file
   echo OPENAI_API_KEY=your_api_key_here > .env
   ```

5. **Run the researcher**
   ```bash
   python main.py
   ```

## 🤖 Architecture

### Agents

- **Research Analyst**: Specialises in finding and analysing information using search tools
- **Content Strategist**: Transforms research findings into compelling, structured reports

### Process Flow

1. Research Agent conducts comprehensive topic analysis
2. Content Agent receives findings and creates polished report
3. Final output is a well-structured markdown report

## 🤖 Configuration

### Customising Research Topics
Edit the `topic_to_research` variable in `main.py`:
```python
topic_to_research = 'Your Research Topic Here'
```

### Agent Customisation
Modify agent roles, goals, and backstories in the agent definitions for different research styles.

## 🔧 Dependencies

- `crewai`: Multi-agent AI framework
- `crewai-tools`: Search and utility tools
- `python-dotenv`: Environment variable management

## 📊 Example Output

The system generates comprehensive reports including:
- Key trends and developments
- Market dynamics analysis
- Innovation insights
- Structured narrative with introduction, body, and conclusion

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 Licence

This project is licensed under the MIT Licence - see the [LICENCE](LICENCE) file for details.

## 🤖 Acknowledgements

- Built with [CrewAI](https://github.com/joaomdmoura/crewAI)
- Powered by OpenAI and other LLM providers

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the CrewAI documentation
- Ensure your Python version is compatible

---

**Made with ❤️ using CrewAI**
