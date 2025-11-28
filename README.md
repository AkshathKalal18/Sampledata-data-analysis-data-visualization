# Task 1: Working with Data - Data Analysis and Visualization

## Objective
Learn how to manipulate and analyze data using Python libraries such as Pandas and NumPy. Perform data manipulation tasks, create visualizations, and work with real-world datasets.

## Features Implemented

### Data Manipulation
- **Pandas Operations**: Data loading, cleaning, filtering, and transformation
- **NumPy Operations**: Numerical computations and array operations
- **Data Cleaning**: Handle missing values, data type conversions
- **Data Filtering**: Filter by multiple criteria (year, type, country, rating)
- **Data Grouping**: Group by categories and calculate aggregations
- **Data Aggregation**: Statistical summaries and calculations

### Data Visualization
- **Line Chart**: Display trends over time (content added over years)
- **Area Chart**: Show distribution with filled areas (content type over time)
- **Bar Chart**: Compare categories (content by rating)
- **Histogram**: Show data distribution (release year distribution)
- **Scatter Plot**: Show correlations (release year vs year added)
- **Pie Chart**: Show proportions (content type distribution)
- **Heatmap**: Show magnitude relationships (rating by type)
- **Box Plot**: Show distribution and outliers (release year by type)

## Files Included

1. **`data_analysis.py`** - Main data analysis script
   - Data loading and exploration
   - Data cleaning and preprocessing
   - Filtering operations
   - Grouping and aggregation
   - Data export functionality

2. **`data_visualization.py`** - Visualization script
   - Creates 8 different chart types
   - Saves charts as PNG files
   - Demonstrates various visualization techniques

3. **`create_sample_data.py`** - Sample data generator
   - Creates realistic Netflix dataset
   - 100 sample records with various attributes
   - Includes movies and TV shows

4. **`requirements.txt`** - Required packages
   - pandas==2.0.3
   - numpy==1.24.3
   - matplotlib==3.7.2
   - seaborn==0.12.2
   - requests==2.31.0

## Installation and Setup

```bash
# Install required packages
pip install -r requirements.txt

# Generate sample data
python create_sample_data.py

# Run data analysis
python data_analysis.py

# Create visualizations
python data_visualization.py
```

## Sample Output

### Data Analysis Output
```
=== NETFLIX DATA ANALYSIS ===
Dataset loaded successfully! Shape: (100, 12)

=== DATA EXPLORATION ===
Dataset shape: (100, 12)
Columns: ['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description']

Data types:
show_id         object
type            object
title           object
director        object
cast            object
country         object
date_added      object
release_year     int64
rating          object
duration        object
listed_in       object
description     object

=== FILTERING TASKS ===
Movies released after 2010: 45
TV Shows with multiple seasons: 12
US content: 15

=== GROUPING AND AGGREGATION ===
Content by type:
Movie      55
TV Show    45

Content by rating:
TV-MA      25
TV-14      20
TV-PG      15
TV-Y7      10
TV-Y        8
R           8
PG-13       6
PG          5
G           3

=== AGGREGATION TASKS ===
Average release year by type:
Movie      2017.2
TV Show    2018.1

Content added by year:
2019    15
2020    20
2021    25
2022    30
2023    10
```

### Generated Files
- `netflix_titles.csv` - Sample dataset
- `recent_movies.csv` - Filtered recent movies
- `multi_season_shows.csv` - TV shows with multiple seasons
- `us_content.csv` - US-produced content
- `type_counts.csv` - Content by type
- `rating_counts.csv` - Content by rating
- `yearly_content.csv` - Content by release year
- `country_counts.csv` - Content by country

### Visualization Files
- `line_chart_content_over_time.png`
- `area_chart_content_type_distribution.png`
- `bar_chart_content_by_rating.png`
- `histogram_release_year_distribution.png`
- `scatter_plot_release_vs_added.png`
- `pie_chart_content_type_distribution.png`
- `heatmap_rating_by_type.png`
- `box_plot_release_year_by_type.png`

## Data Source Information

### Dataset: Netflix Movies and TV Shows
- **Source**: Sample data generated for demonstration
- **Real-world equivalent**: Netflix Movies and TV Shows dataset from Kaggle
- **Size**: 100 records
- **Format**: CSV
- **Features**: 12 columns including show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description

### Data Features
- **show_id**: Unique identifier for each title
- **type**: Movie or TV Show
- **title**: Name of the content
- **director**: Director(s) of the content
- **cast**: Main cast members
- **country**: Country of origin
- **date_added**: Date added to Netflix
- **release_year**: Year of original release
- **rating**: Content rating (TV-MA, TV-14, etc.)
- **duration**: Length of content
- **listed_in**: Categories/genres
- **description**: Brief description of content

## Learning Outcomes

### Technical Skills Demonstrated
- ✅ **Pandas**: Data manipulation, filtering, grouping, aggregation
- ✅ **NumPy**: Numerical operations and array handling
- ✅ **Matplotlib**: Basic plotting and chart customization
- ✅ **Seaborn**: Advanced statistical visualizations
- ✅ **Data Cleaning**: Handling missing values and data type conversions
- ✅ **Data Analysis**: Statistical summaries and insights
- ✅ **Data Visualization**: Multiple chart types and techniques

### Analysis Techniques
- **Exploratory Data Analysis (EDA)**: Understanding data structure and patterns
- **Data Filtering**: Extracting subsets based on conditions
- **Data Grouping**: Organizing data by categories
- **Statistical Aggregation**: Calculating means, counts, and summaries
- **Data Visualization**: Creating meaningful charts and graphs

## Real-World Applications

This task demonstrates skills that are directly applicable to:
- **Data Science**: Analyzing large datasets
- **Business Intelligence**: Creating reports and dashboards
- **Market Research**: Understanding customer preferences
- **Content Analysis**: Analyzing media and entertainment data
- **Statistical Analysis**: Drawing insights from data

## Next Steps

To extend this project:
1. Use real Netflix dataset from Kaggle
2. Add more advanced visualizations (3D plots, interactive charts)
3. Implement machine learning analysis
4. Create a dashboard application
5. Add data export functionality for different formats 