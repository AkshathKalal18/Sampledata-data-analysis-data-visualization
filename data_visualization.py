"""
Task 1: Working with Data - Data Visualization Script
Objective: Create various types of data visualizations using Matplotlib and Seaborn
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

class DataVisualizer:
    def __init__(self):
        self.df = None
        self.setup_style()
        
    def setup_style(self):
        """Setup visualization style"""
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
        plt.rcParams['figure.figsize'] = (12, 8)
        plt.rcParams['font.size'] = 10
        
    def load_data(self):
        """Load the processed Netflix data"""
        try:
            self.df = pd.read_csv("netflix_titles.csv")
            print("Data loaded successfully!")
            return True
        except FileNotFoundError:
            print("Please run data_analysis.py first to generate the dataset.")
            return False
    
    def line_chart(self):
        """Line Chart: Display trends over time"""
        print("Creating Line Chart: Content Added Over Time")
        
        # Prepare data
        self.df['date_added'] = pd.to_datetime(self.df['date_added'], errors='coerce')
        self.df['year_added'] = self.df['date_added'].dt.year
        yearly_additions = self.df.groupby('year_added').size()
        
        plt.figure(figsize=(12, 6))
        plt.plot(yearly_additions.index, yearly_additions.values, marker='o', linewidth=2, markersize=6)
        plt.title('Netflix Content Added Over Time', fontsize=16, fontweight='bold')
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Number of Titles Added', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('line_chart_content_over_time.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def area_chart(self):
        """Area Chart: A line chart with area between axis and line filled with color"""
        print("Creating Area Chart: Content Type Distribution Over Time")
        
        # Prepare data
        self.df['date_added'] = pd.to_datetime(self.df['date_added'], errors='coerce')
        self.df['year_added'] = self.df['date_added'].dt.year
        
        yearly_by_type = self.df.groupby(['year_added', 'type']).size().unstack(fill_value=0)
        
        plt.figure(figsize=(12, 6))
        plt.stackplot(yearly_by_type.index, yearly_by_type.values.T, 
                     labels=yearly_by_type.columns, alpha=0.7)
        plt.title('Netflix Content Type Distribution Over Time', fontsize=16, fontweight='bold')
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Number of Titles', fontsize=12)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('area_chart_content_type_distribution.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def bar_chart(self):
        """Bar Chart: Display trends with multiple variables"""
        print("Creating Bar Chart: Content by Rating")
        
        rating_counts = self.df.groupby('rating').size().sort_values(ascending=False)
        
        plt.figure(figsize=(12, 6))
        bars = plt.bar(range(len(rating_counts)), rating_counts.values, 
                       color=sns.color_palette("husl", len(rating_counts)))
        plt.title('Netflix Content by Rating', fontsize=16, fontweight='bold')
        plt.xlabel('Rating', fontsize=12)
        plt.ylabel('Number of Titles', fontsize=12)
        plt.xticks(range(len(rating_counts)), rating_counts.index, rotation=45)
        
        # Add value labels on bars
        for i, v in enumerate(rating_counts.values):
            plt.text(i, v + max(rating_counts.values) * 0.01, str(v), 
                    ha='center', va='bottom', fontweight='bold')
        
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.savefig('bar_chart_content_by_rating.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def histogram(self):
        """Histogram: Display the shape and spread of a continuous dataset sample"""
        print("Creating Histogram: Release Year Distribution")
        
        plt.figure(figsize=(12, 6))
        plt.hist(self.df['release_year'].dropna(), bins=30, alpha=0.7, edgecolor='black')
        plt.title('Distribution of Netflix Content Release Years', fontsize=16, fontweight='bold')
        plt.xlabel('Release Year', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('histogram_release_year_distribution.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def scatter_plot(self):
        """Scatter Plot: Show correlation in a dataset"""
        print("Creating Scatter Plot: Release Year vs Year Added")
        
        # Prepare data
        self.df['date_added'] = pd.to_datetime(self.df['date_added'], errors='coerce')
        self.df['year_added'] = self.df['date_added'].dt.year
        
        # Filter out NaN values
        plot_data = self.df.dropna(subset=['release_year', 'year_added'])
        
        plt.figure(figsize=(12, 6))
        plt.scatter(plot_data['release_year'], plot_data['year_added'], 
                   alpha=0.6, s=30, c=plot_data['type'].map({'Movie': 'blue', 'TV Show': 'red'}))
        plt.title('Release Year vs Year Added to Netflix', fontsize=16, fontweight='bold')
        plt.xlabel('Release Year', fontsize=12)
        plt.ylabel('Year Added to Netflix', fontsize=12)
        plt.grid(True, alpha=0.3)
        
        # Add legend
        from matplotlib.lines import Line2D
        legend_elements = [Line2D([0], [0], marker='o', color='w', 
                                 markerfacecolor='blue', markersize=8, label='Movie'),
                          Line2D([0], [0], marker='o', color='w', 
                                 markerfacecolor='red', markersize=8, label='TV Show')]
        plt.legend(handles=legend_elements)
        
        plt.tight_layout()
        plt.savefig('scatter_plot_release_vs_added.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def pie_chart(self):
        """Pie Chart: Show the contribution of data point to a whole dataset"""
        print("Creating Pie Chart: Content Type Distribution")
        
        type_counts = self.df.groupby('type').size()
        
        plt.figure(figsize=(10, 8))
        colors = ['#ff9999', '#66b3ff']
        explode = (0.05, 0.05)
        
        plt.pie(type_counts.values, labels=type_counts.index, autopct='%1.1f%%',
                startangle=90, colors=colors, explode=explode, shadow=True)
        plt.title('Netflix Content Type Distribution', fontsize=16, fontweight='bold')
        plt.axis('equal')
        plt.tight_layout()
        plt.savefig('pie_chart_content_type_distribution.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def heatmap(self):
        """Heat Map: Show magnitude of a phenomenon"""
        print("Creating Heatmap: Rating Distribution by Type")
        
        rating_by_type = self.df.groupby(['type', 'rating']).size().unstack(fill_value=0)
        
        plt.figure(figsize=(12, 6))
        sns.heatmap(rating_by_type, annot=True, fmt='d', cmap='YlOrRd', cbar_kws={'label': 'Count'})
        plt.title('Rating Distribution by Content Type', fontsize=16, fontweight='bold')
        plt.xlabel('Rating', fontsize=12)
        plt.ylabel('Content Type', fontsize=12)
        plt.tight_layout()
        plt.savefig('heatmap_rating_by_type.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def box_plot(self):
        """Box Plot: Show distribution and outliers"""
        print("Creating Box Plot: Release Year by Content Type")
        
        plt.figure(figsize=(10, 6))
        self.df.boxplot(column='release_year', by='type', figsize=(10, 6))
        plt.title('Release Year Distribution by Content Type', fontsize=16, fontweight='bold')
        plt.suptitle('')  # Remove default suptitle
        plt.xlabel('Content Type', fontsize=12)
        plt.ylabel('Release Year', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('box_plot_release_year_by_type.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def create_all_visualizations(self):
        """Create all visualizations"""
        print("=== CREATING ALL DATA VISUALIZATIONS ===")
        
        if not self.load_data():
            return
        
        # Create all chart types
        self.line_chart()
        self.area_chart()
        self.bar_chart()
        self.histogram()
        self.scatter_plot()
        self.pie_chart()
        self.heatmap()
        self.box_plot()
        
        print("\n=== ALL VISUALIZATIONS COMPLETED ===")
        print("All charts have been saved as PNG files in the current directory.")
        print("Generated files:")
        print("- line_chart_content_over_time.png")
        print("- area_chart_content_type_distribution.png")
        print("- bar_chart_content_by_rating.png")
        print("- histogram_release_year_distribution.png")
        print("- scatter_plot_release_vs_added.png")
        print("- pie_chart_content_type_distribution.png")
        print("- heatmap_rating_by_type.png")
        print("- box_plot_release_year_by_type.png")

if __name__ == "__main__":
    visualizer = DataVisualizer()
    visualizer.create_all_visualizations() 