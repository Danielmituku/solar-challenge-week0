# Source Code Modules

This directory contains reusable, modular code for solar data processing. The modules are designed to replace procedural notebook code with reusable functions and classes.

## Modules

### `data_loader.py`
Handles loading and preprocessing of solar data files.

**Classes:**
- `SolarDataLoader`: Class for loading and managing solar data

**Functions:**
- `load_solar_data()`: Convenience function to load data

**Example:**
```python
from src.data_loader import load_solar_data

df = load_solar_data('data/benin-malanville.csv')
```

### `data_cleaner.py`
Handles data cleaning operations including missing value imputation and outlier detection/treatment.

**Classes:**
- `SolarDataCleaner`: Class for cleaning solar data

**Functions:**
- `clean_solar_data()`: Convenience function to clean data

**Example:**
```python
from src.data_cleaner import clean_solar_data

df_cleaned, report = clean_solar_data(
    df,
    numeric_columns=['GHI', 'DNI', 'DHI'],
    outlier_columns=['GHI', 'DNI', 'DHI'],
    z_threshold=3.0
)
```

### `data_exporter.py`
Handles exporting cleaned datasets to CSV files.

**Classes:**
- `SolarDataExporter`: Class for exporting data

**Functions:**
- `export_cleaned_data()`: Convenience function to export data

**Example:**
```python
from src.data_exporter import export_cleaned_data

export_cleaned_data(df_cleaned, 'data/benin_clean.csv')
```

## Usage in Notebooks

Instead of procedural code, notebooks can now use these modules:

```python
# Old procedural way:
# df = pd.read_csv('data/benin-malanville.csv')
# df['Timestamp'] = pd.to_datetime(df['Timestamp'])
# ... many lines of cleaning code ...

# New modular way:
from src import load_solar_data, clean_solar_data, export_cleaned_data

df = load_solar_data('data/benin-malanville.csv')
df_cleaned, report = clean_solar_data(df, outlier_columns=['GHI', 'DNI', 'DHI'])
export_cleaned_data(df_cleaned, 'data/benin_clean.csv')
```

## Benefits

1. **Reusability**: Same code can be used across multiple notebooks
2. **Maintainability**: Changes to cleaning logic only need to be made in one place
3. **Testability**: Unit tests can verify module functionality
4. **Modularity**: Each module has a single, clear responsibility

## Running Tests

```bash
pytest tests/
```

## Examples

See `scripts/example_usage.py` for complete usage examples.

