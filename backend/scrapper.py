# # from flask import Flask, request, jsonify
# # from DrissionPage import ChromiumPage
# # from bs4 import BeautifulSoup
# # from flask_cors import CORS

# # app = Flask(__name__)
# # CORS(app)


# @app.route("/process", methods=["POST"])
# def process_data():
#     # Parse the JSON input
#     data = request.get_json()

#     # Assuming the input JSON contains a 'query' field for the search term
#     query = data.get("query", "")
#     p = ChromiumPage()

#     p.get("https://www.udemy.com/")
#     p.ele("@class:ud-text-input").input(query)
#     p.ele('xpath://*[@id="__next"]/div/div/div[4]/div[2]/form/button').click()

#     a = p.eles(
#         "tag:div@class=course-card-module--main-content--pEiUr course-card-module--has-price-text--g6p85"
#     )
#     b = a[:2]
#     b1 = b[0].inner_html
#     b2 = b[1].inner_html
#     c = []
#     c.append(b1)
#     c.append(b2)
#     soup = BeautifulSoup(c[0], "html.parser")

#     # Extract the desired information for the first course
#     title = soup.find("h3", {"data-purpose": "course-title-url"}).text.strip()
#     rating = soup.find("span", {"data-testid": "seo-rating"}).text.strip()
#     instructor = soup.find(
#         "div", {"data-purpose": "safely-set-inner-html:course-card:visible-instructors"}
#     ).text.strip()
#     price = soup.find(
#         "div",
#         {"class": "course-card-module--price-text-base-price-text-component--Q-Ucg"},
#     ).text.strip()
#     lecture_hours = soup.find("span", {"data-testid": "seo-content-info"}).text.strip()

#     # Extracting reviews with a fallback for when the span is not found
#     reviews_element = soup.find("span", {"aria-label": "4305 reviews"})
#     reviews = reviews_element.text.strip() if reviews_element else "no-reviews"

#     soup1 = BeautifulSoup(c[1], "html.parser")

#     # Extract the desired information for the second course
#     title1 = soup1.find("h3", {"data-purpose": "course-title-url"}).text.strip()
#     rating1 = soup1.find("span", {"data-testid": "seo-rating"}).text.strip()
#     instructor1 = soup1.find(
#         "div", {"data-purpose": "safely-set-inner-html:course-card:visible-instructors"}
#     ).text.strip()
#     price1 = soup1.find(
#         "div",
#         {"class": "course-card-module--price-text-base-price-text-component--Q-Ucg"},
#     ).text.strip()
#     lecture_hours1 = soup1.find(
#         "span", {"data-testid": "seo-content-info"}
#     ).text.strip()

#     # Extracting reviews with a fallback for when the span is not found
#     reviews_element1 = soup1.find("span", {"aria-label": "4305 reviews"})
#     reviews1 = reviews_element1.text.strip() if reviews_element1 else "no-reviews"

#     # Create the desired dictionary for Udemy courses
#     data1 = {
#         "0": {
#             "title": title,
#             "rating": rating,
#             "instructor": instructor,
#             "price": price,
#             "lecture_hours": lecture_hours,
#             "reviews": reviews,
#         },
#         "1": {
#             "title": title1,
#             "rating": rating1,
#             "instructor": instructor1,
#             "price": price1,
#             "lecture_hours": lecture_hours1,
#             "reviews": reviews1,
#         },
#     }

#     p.close()

#     # Now let's fetch data from another website (SWAYAM)
#     s = ChromiumPage()
#     s.get("https://swayam.gov.in/")
#     s.ele('xpath://*[@id="header"]/div[2]/div/div[2]/div/a[2]').click()
#     s.ele(
#         "@class:form-control style-scope course-explorer ui-autocomplete-input"
#     ).input(query)
#     s.ele("@class:search_keyword style-scope course-explorer").click()
#     a = s.eles("tag:div@class=content style-scope course-card")

#     # Extract the text data for the first two courses
#     x = a[:2]
#     x1 = x[0].text
#     x2 = x[1].text

#     # Step 1: Parse the text for the first course
#     lines1 = x1.split("\n")

#     # Initialize variables with None for the first course
#     name = None
#     instructor = None
#     college = None
#     institute = None
#     type_of_course = None

#     # Check if there are enough lines to parse for the first course
#     if len(lines1) >= 4:
#         name = lines1[0].strip() if lines1[0] else None
#         instructor = lines1[1].strip() if lines1[1] else None
#         college = lines1[2].strip() if lines1[2] else None

#         # Splitting the fourth line to get institute and type
#         institute_type_line = lines1[3].split("\t")
#         institute = institute_type_line[0].strip() if institute_type_line[0] else None
#         type_of_course = (
#             institute_type_line[1].strip()
#             if len(institute_type_line) > 1 and institute_type_line[1]
#             else None
#         )

#     # Step 2: Parse the text for the second course
#     lines2 = x2.split("\n")

#     # Initialize variables with None for the second course
#     name1 = None
#     instructor1 = None
#     college1 = None
#     institute1 = None
#     type_of_course1 = None

#     # Check if there are enough lines to parse for the second course
#     if len(lines2) >= 4:
#         name1 = lines2[0].strip() if lines2[0] else None
#         instructor1 = lines2[1].strip() if lines2[1] else None
#         college1 = lines2[2].strip() if lines2[2] else None

#         # Splitting the fourth line to get institute and type
#         institute_type_line1 = lines2[3].split("\t")
#         institute1 = (
#             institute_type_line1[0].strip() if institute_type_line1[0] else None
#         )
#         type_of_course1 = (
#             institute_type_line1[1].strip()
#             if len(institute_type_line1) > 1 and institute_type_line1[1]
#             else None
#         )

#     # Create the desired dictionary for SWAYAM courses
#     data2 = {
#         "2": {
#             "title": name,
#             "rating": instructor,
#             "price": college,
#             "lecture_hours": institute,
#             "reviews": type_of_course,
#         },
#         "3": {
#             "title": name1,
#             "rating": instructor1,
#             "price": college1,
#             "lecture_hours": institute1,
#             "reviews": type_of_course1,
#         },
#     }

#     # Combine data from both sources
#     combined_data = {}
#     combined_data.update(data1)
#     combined_data.update(data2)

#     # closing the opened browser
#     s.close()
#     # Serialize to JSON and return the response
#     return jsonify(combined_data)


# if __name__ == "__main__":
#     app.run(debug=True, port=5000)
