import requests
from collections import Counter

def run_analysis():
    url = "https://dmachek.github.io/meteorites-homework/meteorite_landings.json"
    
    # Get the data
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"Connection error: {e}")
        return

    print(f"Total entries: {len(data)}")

    # Find the heaviest meteorite
    heaviest_name = ""
    max_mass = 0.0

    for item in data:
        # Check if 'mass' exists and isn't empty
        if 'mass' in item and item['mass']:
            current_mass = float(item['mass'])
            if current_mass > max_mass:
                max_mass = current_mass
                heaviest_name = item['name']

    print(f"Heaviest meteorite: {heaviest_name} ({max_mass}g)")

    # Find the most frequent year
    years = []
    for item in data:
        if 'year' in item and item['year']:
            # Take the first 4 characters (the year) from the date string
            year_only = item['year'][:4]
            years.append(year_only)

    if years:
        # Counter counts how many times each year appears
        most_common = Counter(years).most_common(1)
        year, count = most_common[0]
        print(f"Most frequent year: {year} (found {count} times)")

if __name__ == "__main__":
    run_analysis()