# GPT Agent Prototype

This project is a small prototype that demonstrates how an AI agent can be realized using OpenAI's GPT models. It serves as an educational and experimental showcase of how modern large language models (LLMs) can reason about tasks and autonomously select and invoke predefined tools (functions) to complete them.

## Purpose

The aim of this project is to illustrate how AI agents can be implemented with minimal code, offering functionality such as:
- Understanding natural language input
- Deciding which tools (functions) to use
- Calling these tools with appropriate arguments

As a software developer fascinated by new technologies like AI, this prototype reflects my curiosity and openness to learning and applying emerging methods in real-world scenarios.

## Features

- Integration with OpenAI's GPT model using the `openai` Python package
- Tool definition via structured JSON for function calling
- Support for function execution via dynamic dispatch
- Simple built-in tools:
  - `get_weather(location)`: Returns mocked weather data
  - `send_email(receiver, subject, body)`: Simulates sending an email

## Example Output

Example interactions are included in the repository as `example output 1.txt` and `example output 2.txt`.

## Project Structure

```
gpt-agent-prototype/
├── .gitignore
├── example output 1.txt
├── example output 2.txt
└── src/
    └── gpt_agent_prototype.py
```

## Requirements

- Python 3.8+
- `openai` Python package

Install dependencies:
```bash
pip install openai
```

## Running the Prototype

1. Set your OpenAI API key via environment variable:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```
2. Run the script:
   ```bash
   python src/gpt_agent_prototype.py
   ```

## Disclaimer

This is a prototype and not intended for production use. The weather data and email functionality are simulated for demonstration purposes only.

## License

This project is provided under the MIT License.

## Author

Developed by a passionate software developer eager to explore and apply the capabilities of modern AI systems. Feel free to connect with me on [GitHub](https://github.com/thees-k).
