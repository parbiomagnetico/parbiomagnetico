import json
from datetime import datetime, timedelta

def update_review_dates():
    with open('src/data/reviews.json', 'r', encoding='utf-8') as f:
        reviews = json.load(f)

    # Sort by date descending (initially)
    reviews.sort(key=lambda x: x['date'], reverse=True)

    # Assign recent dates in 2025 to the top reviews
    now = datetime(2025, 5, 20, 10, 0, 0)
    
    for i, review in enumerate(reviews):
        # Shift dates to be more recent
        # Top 3 will be in 2025
        if i == 0:
            review['date'] = "2025-05-15 11:20:15"
        elif i == 1:
            review['date'] = "2025-04-22 09:45:00"
        elif i == 2:
            review['date'] = "2025-03-10 16:30:22"
        elif i == 3:
            review['date'] = "2025-02-12 18:15:45"
        elif i == 4:
            review['date'] = "2025-01-20 12:10:05"
        # Others move up a bit too
        elif "2024" in review['date']:
            review['date'] = review['date'].replace("2024", "2024") # Keep as is or move? User said "haya tambien en el 2025"
        elif "2022" in review['date']:
             review['date'] = review['date'].replace("2022", "2024")
        elif "2021" in review['date']:
             review['date'] = review['date'].replace("2021", "2023")
        elif "2020" in review['date']:
             review['date'] = review['date'].replace("2020", "2022")

    # Re-sort to ensure latest is first
    reviews.sort(key=lambda x: x['date'], reverse=True)

    with open('src/data/reviews.json', 'w', encoding='utf-8') as f:
        json.dump(reviews, f, ensure_ascii=False, indent=2)

    print("Updated review dates to include 2025.")

if __name__ == "__main__":
    update_review_dates()
