# solar-challenge-week0
This repo has been created for learning-purpose only.

## Setup Environment

Follow these steps to reproduce the development environment:

### Prerequisites

- **Python 3.13** (or compatible version)
- **pip** (Python package installer)
- **Git** (for version control)

### Installation Steps

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <repository-url>
   cd solar-challenge-week0
   ```

2. **Create a virtual environment**:
   
   On Windows:
   ```bash
   python -m venv venv
   ```
   
   On macOS/Linux:
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:
   
   On Windows (PowerShell):
   ```bash
   .\venv\Scripts\Activate.ps1
   ```
   
   On Windows (Command Prompt):
   ```bash
   venv\Scripts\activate.bat
   ```
   
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Verify the installation**:
   ```bash
   python --version
   pip list
   ```

### Project Structure

```
solar-challenge-week0/
├── data/              # Data files
├── notebooks/         # Jupyter notebooks
├── scripts/           # Utility scripts
├── src/               # Source code
├── tests/             # Test files
├── venv/              # Virtual environment (gitignored)
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

### Running Tests

To run tests using pytest:
```bash
pytest tests/
```

### Notes

- The virtual environment (`venv/`) is excluded from version control (see `.gitignore`)
- Make sure to activate the virtual environment before working on the project
- If you encounter any issues, ensure you're using Python 3.13 or a compatible version
