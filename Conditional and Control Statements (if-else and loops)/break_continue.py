# Task: Given a dictionary with the book prices and a list of courses, calculate the total cost of books

books = {"calculus": 300, "physics": 220, "math": 330, "english": 120 }
my_courses = ["physics", "english", "history", "math"]

total_cost = 0

for course in my_courses:

    if course not in books.keys():
        # print(f"skipped {course}")
        continue

    total_cost += books[course]

print("Total cost of available books is: $", total_cost)
