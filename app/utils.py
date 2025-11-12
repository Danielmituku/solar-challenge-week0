import pandas as pd
import numpy as np
from pathlib import Path


def load_all_countries_data(data_dir='data'):
    """
    Load all cleaned country datasets and combine them.
    Optimized for performance.
    
    Args:
        data_dir: Directory containing cleaned CSV files
        
    Returns:
        DataFrame: Combined dataset with Country column
    """
    data_path = Path(data_dir)
    
    # Load each country's cleaned CSV with optimized parsing
    benin_df = pd.read_csv(
        data_path / 'benin_clean.csv',
        parse_dates=['Timestamp'],
        infer_datetime_format=True
    )
    sierra_leone_df = pd.read_csv(
        data_path / 'sierra_leone_clean.csv',
        parse_dates=['Timestamp'],
        infer_datetime_format=True
    )
    togo_df = pd.read_csv(
        data_path / 'togo_clean.csv',
        parse_dates=['Timestamp'],
        infer_datetime_format=True
    )
    
    # Add country identifier before concatenation (more efficient)
    benin_df['Country'] = 'Benin'
    sierra_leone_df['Country'] = 'Sierra Leone'
    togo_df['Country'] = 'Togo'
    
    # Combine all datasets (more efficient than multiple concats)
    all_countries_df = pd.concat(
        [benin_df, sierra_leone_df, togo_df], 
        ignore_index=True
    )
    
    # Set Timestamp as index for faster date filtering (optional optimization)
    # all_countries_df.set_index('Timestamp', inplace=True)
    
    return all_countries_df


def filter_data_by_countries(df, selected_countries):
    """
    Filter dataframe by selected countries.
    
    Args:
        df: Combined dataframe
        selected_countries: List of country names to include
        
    Returns:
        DataFrame: Filtered dataframe
    """
    if not selected_countries:
        return df
    
    return df[df['Country'].isin(selected_countries)]


def create_summary_table(df):
    """
    Create summary statistics table for top regions.
    
    Args:
        df: Filtered dataframe
        
    Returns:
        DataFrame: Summary table with statistics by country
    """
    summary = df.groupby('Country').agg({
        'GHI': ['mean', 'median', 'std'],
        'DNI': ['mean', 'median', 'std'],
        'DHI': ['mean', 'median', 'std'],
        'Timestamp': ['min', 'max', 'count']
    }).round(2)
    
    # Flatten column names
    summary.columns = [
        'GHI_Mean', 'GHI_Median', 'GHI_Std',
        'DNI_Mean', 'DNI_Median', 'DNI_Std',
        'DHI_Mean', 'DHI_Median', 'DHI_Std',
        'Date_Min', 'Date_Max', 'Record_Count'
    ]
    
    # Sort by average GHI (descending)
    summary = summary.sort_values('GHI_Mean', ascending=False)
    
    # Reset index to make Country a column
    summary = summary.reset_index()
    
    # Rename columns for display
    summary.columns = [
        'Country',
        'Avg GHI (W/m²)', 'Median GHI (W/m²)', 'Std Dev GHI',
        'Avg DNI (W/m²)', 'Median DNI (W/m²)', 'Std Dev DNI',
        'Avg DHI (W/m²)', 'Median DHI (W/m²)', 'Std Dev DHI',
        'Start Date', 'End Date', 'Records'
    ]
    
    return summary