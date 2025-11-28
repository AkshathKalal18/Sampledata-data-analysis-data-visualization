"""
Task 1: Working with Data - Data Analysis Script
Objective: Learn how to manipulate and analyze data using Python libraries
"""

import pandas as pd
import numpy as np
import requests
import os
from datetime import datetime

class DataAnalyzer:
    def __init__(self):
        self.df = None
        self.dataset_path = "netflix_titles.csv"
        
    def download_dataset(self):
        """Download Netflix dataset if not available"""
        if not os.path.exists(self.dataset_path):
            print("Downloading Netflix dataset...")
            # Using a sample Netflix dataset URL
            url = "https://raw.githubusercontent.com/krishnaik06/Netflix-Data-Analysis/master/netflix_titles.csv"
            try:
                response = requests.get(url)
                with open(self.dataset_path, 'wb') as f:
                    f.write(response.content)
                print("Dataset downloaded successfully!")
            except Exception as e:
                print(f"Error downloading dataset: {e}")
                print("Please download the dataset manually from Kaggle")
        else:
            print("Dataset already exists!")
    
    def load_data(self):
        """Load the Netflix dataset"""
        try:
            self.df = pd.read_csv(self.dataset_path)
            print(f"Dataset loaded successfully! Shape: {self.df.shape}")
            return True
        except FileNotFoundError:
            print("Dataset file not found. Please run download_dataset() first.")
            return False
    
    def explore_data(self):
        """Basic data exploration"""
        print("\n=== DATA EXPLORATION ===")
        print(f"Dataset shape: {self.df.shape}")
        print(f"\nColumns: {list(self.df.columns)}")
        print(f"\nData types:\n{self.df.dtypes}")
        print(f"\nMissing values:\n{self.df.isnull().sum()}")
        print(f"\nFirst 5 rows:")
        print(self.df.head())
    
    def data_cleaning(self):
        """Clean the dataset"""
        print("\n=== DATA CLEANING ===")
        
        # Handle missing values
        print("Handling missing values...")
        self.df['director'].fillna('Unknown', inplace=True)
        self.df['cast'].fillna('Unknown', inplace=True)
        self.df['country'].fillna('Unknown', inplace=True)
        self.df['rating'].fillna('Unknown', inplace=True)
        
        # Convert date_added to datetime
        self.df['date_added'] = pd.to_datetime(self.df['date_added'], errors='coerce')
        
        # Extract year from release_year for analysis
        self.df['release_year'] = pd.to_numeric(self.df['release_year'], errors='coerce')
        
        print("Data cleaning completed!")
    
    def filtering_tasks(self):
        """Perform filtering tasks"""
        print("\n=== FILTERING TASKS ===")
        
        # Filter movies released after 2010
        recent_movies = self.df[(self.df['type'] == 'Movie') & (self.df['release_year'] > 2010)]
        print(f"Movies released after 2010: {len(recent_movies)}")
        
        # Filter TV shows with duration > 1 season
        tv_shows = self.df[self.df['type'] == 'TV Show']
        multi_season_shows = tv_shows[tv_shows['duration'].str.contains('Season', na=False)]
        print(f"TV Shows with multiple seasons: {len(multi_season_shows)}")
        
        # Filter by country (US content)
        us_content = self.df[self.df['country'].str.contains('United States', na=False)]
        print(f"US content: {len(us_content)}")
        
        return recent_movies, multi_season_shows, us_content
    
    def grouping_tasks(self):
        """Perform grouping and aggregation tasks"""
        print("\n=== GROUPING AND AGGREGATION ===")
        
        # Group by type and count
        type_counts = self.df.groupby('type').size()
        print(f"Content by type:\n{type_counts}")
        
        # Group by rating and count
        rating_counts = self.df.groupby('rating').size().sort_values(ascending=False)
        print(f"\nContent by rating:\n{rating_counts}")
        
        # Group by release year and count
        yearly_content = self.df.groupby('release_year').size()
        print(f"\nContent by release year (last 10 years):\n{yearly_content.tail(10)}")
        
        # Group by country and count (top 10)
        country_counts = self.df.groupby('country').size().sort_values(ascending=False).head(10)
        print(f"\nContent by country (top 10):\n{country_counts}")
        
        return type_counts, rating_counts, yearly_content, country_counts
    
    def aggregation_tasks(self):
        """Perform aggregation tasks"""
        print("\n=== AGGREGATION TASKS ===")
        
        # Average release year by type
        avg_year_by_type = self.df.groupby('type')['release_year'].mean()
        print(f"Average release year by type:\n{avg_year_by_type}")
        
        # Content added by year
        self.df['year_added'] = self.df['date_added'].dt.year
        yearly_additions = self.df.groupby('year_added').size()
        print(f"\nContent added by year:\n{yearly_additions}")
        
        # Rating distribution by type
        rating_by_type = self.df.groupby(['type', 'rating']).size().unstack(fill_value=0)
        print(f"\nRating distribution by type:\n{rating_by_type}")
        
        return avg_year_by_type, yearly_additions, rating_by_type
    
    def save_processed_data(self):
        """Save processed data for visualization"""
        print("\n=== SAVING PROCESSED DATA ===")
        
        # Save filtered datasets
        recent_movies, multi_season_shows, us_content = self.filtering_tasks()
        
        recent_movies.to_csv('recent_movies.csv', index=False)
        multi_season_shows.to_csv('multi_season_shows.csv', index=False)
        us_content.to_csv('us_content.csv', index=False)
        
        # Save aggregated data
        type_counts, rating_counts, yearly_content, country_counts = self.grouping_tasks()
        
        type_counts.to_csv('type_counts.csv')
        rating_counts.to_csv('rating_counts.csv')
        yearly_content.to_csv('yearly_content.csv')
        country_counts.to_csv('country_counts.csv')
        
        print("Processed data saved successfully!")
    
    def run_analysis(self):
        """Run complete data analysis"""
        print("=== NETFLIX DATA ANALYSIS ===")
        
        # Download and load data
        self.download_dataset()
        if not self.load_data():
            return
        
        # Perform analysis tasks
        self.explore_data()
        self.data_cleaning()
        self.filtering_tasks()
        self.grouping_tasks()
        self.aggregation_tasks()
        self.save_processed_data()
        
        print("\n=== DATA ANALYSIS COMPLETED ===")
        print("All analysis tasks completed successfully!")
        print("Check the generated CSV files for processed data.")

if __name__ == "__main__":
    analyzer = DataAnalyzer()
    analyzer.run_analysis() 