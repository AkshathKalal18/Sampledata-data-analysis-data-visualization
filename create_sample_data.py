"""
Create sample Netflix data for analysis
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def create_sample_netflix_data():
    """Create sample Netflix dataset for analysis"""
    
    # Sample data
    titles = [
        "Stranger Things", "The Crown", "Money Heist", "Dark", "Ozark",
        "The Witcher", "Bridgerton", "Squid Game", "Wednesday", "Wednesday",
        "The Queen's Gambit", "Tiger King", "Outer Banks", "Emily in Paris",
        "Cobra Kai", "The Umbrella Academy", "You", "Sex Education",
        "The Good Place", "Black Mirror", "Narcos", "House of Cards",
        "Orange is the New Black", "13 Reasons Why", "Riverdale",
        "The Haunting of Hill House", "Russian Doll", "Dead to Me",
        "Grace and Frankie", "Unbreakable Kimmy Schmidt"
    ]
    
    directors = [
        "Duffer Brothers", "Peter Morgan", "Álex Pina", "Baran bo Odar",
        "Jason Bateman", "Lauren Schmidt", "Chris Van Dusen", "Hwang Dong-hyuk",
        "Tim Burton", "Scott Frank", "Eric Goode", "Josh Pate",
        "Darren Star", "Jon Hurwitz", "Steve Blackman", "Greg Berlanti",
        "Sera Gamble", "Laurie Nunn", "Michael Schur", "Charlie Brooker",
        "Carlo Bernard", "Beau Willimon", "Jenji Kohan", "Brian Yorkey",
        "Roberto Aguirre-Sacasa", "Mike Flanagan", "Leslye Headland",
        "Liz Feldman", "Marta Kauffman", "Tina Fey"
    ]
    
    countries = [
        "United States", "United Kingdom", "Spain", "Germany", "South Korea",
        "Canada", "France", "Italy", "Brazil", "Mexico", "India", "Japan",
        "Australia", "Netherlands", "Sweden", "Norway", "Denmark", "Poland",
        "Czech Republic", "Hungary"
    ]
    
    ratings = ["TV-MA", "TV-14", "TV-PG", "TV-Y7", "TV-Y", "R", "PG-13", "PG", "G"]
    
    # Generate sample data
    data = []
    
    for i in range(100):
        title = random.choice(titles)
        show_type = random.choice(["Movie", "TV Show"])
        
        if show_type == "Movie":
            duration = f"{random.randint(80, 180)} min"
        else:
            duration = f"{random.randint(1, 5)} Season{'s' if random.randint(1, 5) > 1 else ''}"
        
        release_year = random.randint(2010, 2024)
        date_added = datetime.now() - timedelta(days=random.randint(1, 1000))
        
        data.append({
            'show_id': f"s{i+1}",
            'type': show_type,
            'title': title,
            'director': random.choice(directors),
            'cast': f"Actor {random.randint(1, 10)}, Actor {random.randint(11, 20)}",
            'country': random.choice(countries),
            'date_added': date_added.strftime('%B %d, %Y'),
            'release_year': release_year,
            'rating': random.choice(ratings),
            'duration': duration,
            'listed_in': f"Action, Adventure, {random.choice(['Drama', 'Comedy', 'Thriller', 'Romance'])}",
            'description': f"A {random.choice(['compelling', 'entertaining', 'gripping', 'funny'])} {show_type.lower()} about {random.choice(['love', 'adventure', 'mystery', 'friendship'])}."
        })
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Save to CSV
    df.to_csv('netflix_titles.csv', index=False)
    print(f"Sample Netflix dataset created with {len(df)} records!")
    print("Dataset saved as 'netflix_titles.csv'")
    
    return df

if __name__ == "__main__":
    create_sample_netflix_data() 