# AI Text Summarizer

## Overview
AI Text Summarizer is a project that leverages AI technology to automatically summarize text content. This tool can process various text inputs and generate concise, meaningful summaries.

## Features
- 📝 Automatic text summarization
- 🚀 Fast processing
- 💻 User-friendly interface
- 🔒 Secure API key management

## Project Structure
```
AI Text Summarizer/
├── src/
│   ├── app.py              # Main application
│   └── summarizer.py       # Summarization logic
├── frontend/
│   └── frontend.py         # Frontend interface
├── keys/
│   └── .env               # Environment variables (not tracked)
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup
1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/AI-Text-Summarizer.git
cd "AI Text Summarizer"
```

2. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
# Create keys/.env file with your API keys
API_KEY=your_api_key_here
```

## Usage
Run the application:
```bash
python src/app.py
```

## Configuration
- Keep API keys in `keys/.env` (not tracked by Git)
- Update `requirements.txt` when adding new dependencies

## Contributing
1. Create a feature branch
2. Commit your changes
3. Push to GitHub
4. Submit a pull request

## License
MIT License

## Contact
For questions or support, please open an issue on GitHub.
