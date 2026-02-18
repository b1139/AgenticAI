# Calculator Crew - Multi-Agent Calculator

A multi-agent system using CrewAI and Ollama to generate a calculator application.

## Requirements

- Python 3.11+
- Ollama with gemma3:4b model

## Installation

1. Install dependencies:
```bash
pip install -e .
```

Or use the venv:
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
pip install crewai
```

2. Install and start Ollama:
```bash
ollama pull gemma3:4b
ollama serve
```

## Usage

Run the agent system to generate the calculator:
```bash
python agentic.py
```

This will create `final_calculator.py` with all calculator functions.

Run the generated calculator:
```bash
python final_calculator.py
```

## Project Structure

- `agentic.py` - Multi-agent system orchestrator
- `final_calculator.py` - Generated calculator (created by agents)
- `pyproject.toml` - Project dependencies

## Agents

1. **Addition Agent** - Creates add() function
2. **Subtraction Agent** - Creates subtract() function
3. **Multiplication Agent** - Creates multiply() function
4. **Division Agent** - Creates divide() function
5. **File Writer Agent** - Combines all functions into final output
