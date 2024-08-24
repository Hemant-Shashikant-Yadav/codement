import json
from bs4 import BeautifulSoup

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the data
title_tag = soup.find('h3', class_='ud-heading-md course-card-title-module--course-title--wmFXN')
title = title_tag.get_text(separator=' ', strip=True) if title_tag else None

description_tag = soup.find('p', class_='ud-text-sm course-card-module--course-headline--v-7gj')
description = description_tag.get_text(strip=True).replace('<strong>', '').replace('</strong>', '') if description_tag else None

instructor_tag = soup.find('div', class_='course-card-instructors-module--instructor-list--cJTfw')
instructor = instructor_tag.get_text(separator=', ', strip=True) if instructor_tag else None

rating_tag = soup.find('span', class_='ud-heading-sm star-rating-module--rating-number--2-qA2')
rating = rating_tag.get_text(strip=True) if rating_tag else None

reviews_tag = soup.find('span', class_='ud-text-xs course-card-ratings-module--reviews-text--1z0l4')
reviews = reviews_tag.get_text(strip=True).strip('()') if reviews_tag else None

total_hours_tag = soup.find('span', string='46 total hours')
total_hours = total_hours_tag.get_text(strip=True) if total_hours_tag else None

lectures_tag = soup.find('span', string='305 lectures')
lectures = lectures_tag.get_text(strip=True) if lectures_tag else None

current_price_tag = soup.find('div', class_='base-price-text-module--price-part---xQlz course-card-module--price-text-base-price-text-component-discount-price--Xztnd')
current_price = current_price_tag.get_text(strip=True) if current_price_tag else None

original_price_tag = soup.find('div', class_='base-price-text-module--price-part---xQlz base-price-text-module--original-price--C6BJt')
original_price = original_price_tag.find('s').get_text(strip=True) if original_price_tag else None

# Create a dictionary with the extracted data
course_data = {
    "title": title,
    "description": description,
    "instructor": instructor,
    "rating": rating,
    "reviews": reviews,
    "total_hours": total_hours,
    "lectures": lectures,
    "current_price": current_price,
    "original_price": original_price
}

# Convert the dictionary to JSON format
course_data_json = json.dumps(course_data, indent=4)

# Print the JSON data
print(course_data_json)

# Optionally, save the JSON data to a file
with open('course_data.json', 'w', encoding='utf-8') as json_file:
    json_file.write(course_data_json)
