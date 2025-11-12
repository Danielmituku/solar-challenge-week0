# Solar Challenge Week 0 - West Africa Solar Data Analysis

**Repository:** [https://github.com/Danielmituku/solar-challenge-week0](https://github.com/Danielmituku/solar-challenge-week0)

This repository contains a comprehensive analysis of solar irradiance data from three West African countries (Benin, Sierra Leone, and Togo), including exploratory data analysis, statistical comparisons, and an interactive Streamlit dashboard.

## Setup Environment

Follow these steps to reproduce the development environment:

### Prerequisites

- **Python 3.13** (or compatible version)
- **pip** (Python package installer)
- **Git** (for version control)

### Installation Steps

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone https://github.com/Danielmituku/solar-challenge-week0.git
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

## Project Deliverables

### Main Branch Links

All deliverables are available on the main branch:

- **📊 EDA Notebooks:** See `notebooks/` directory
  - `benin_eda.ipynb` - Benin exploratory data analysis
  - `sierra_leone_eda.ipynb` - Sierra Leone exploratory data analysis
  - `togo_eda.ipynb` - Togo exploratory data analysis

- **📁 Cleaned Datasets:** See `data/` directory
  - `benin_clean.csv` - Cleaned Benin dataset
  - `sierra_leone_clean.csv` - Cleaned Sierra Leone dataset
  - `togo_clean.csv` - Cleaned Togo dataset

- **🔧 Reusable Modules:** See `src/` directory
  - `data_loader.py` - Data loading functionality
  - `data_cleaner.py` - Data cleaning functionality
  - `data_exporter.py` - Data export functionality
  - See `src/README.md` for module documentation


For a complete list of deliverables, see [DELIVERABLES.md](DELIVERABLES.md).

## Using Reusable Modules

Instead of procedural code in notebooks, you can use the modular functions:

```python
from src import load_solar_data, clean_solar_data, export_cleaned_data

# Load data
df = load_solar_data('data/benin-malanville.csv')

# Clean data
df_cleaned, report = clean_solar_data(
    df,
    outlier_columns=['GHI', 'DNI', 'DHI'],
    z_threshold=3.0
)

# Export cleaned data
export_cleaned_data(df_cleaned, 'data/benin_clean.csv')
```

See `scripts/example_usage.py` for more examples.

## Documentation

- **[Source Code Modules](src/README.md)** - Detailed module documentation with usage examples
- **[Commit Message Guide](docs/COMMIT_MESSAGE_GUIDE.md)** - Best practices for commit messages
- **[Streamlit Dashboard](docs/STREAMLIT_DASHBOARD.md)** - Planned dashboard interface documentation
- **[Cross-Country Synthesis](scripts/cross_country_synthesis.py)** - Script for aggregating country data
