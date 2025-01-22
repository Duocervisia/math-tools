# Number of people in each category
total_peoples = 55

# Define the categories and their respective counts
categories = {
    'category1': 35,
    'category2': 27,
    'category3': 12
}

# Number of athletes in multiple categories
people_in_two_categories = {
    'category1_and_category2': 13,
    'category1_and_category3': 7,
    'category2_and_category3': 5
}
people_in_three_categories = {
    'category1_and_category2_and_category3': 2
}

# Calculate the number of athletes training in a different category
other_category = total_peoples
print(f"Lösung = {other_category} - (", end=" ")
for category, count in categories.items():
    other_category -= count
    if count == list(categories.values())[-1]:
        print(f"{count}", end=" ")
    else:
        print(f"{count} + ", end=" ")

print(f") + (", end=" ")
for count in people_in_two_categories.values():
    other_category += count
    if count == list(people_in_two_categories.values())[-1]:
        print(f"{count}", end=" ")
    else:
        print(f"{count} + ", end=" ")

print(f") - (", end=" ")
for count in people_in_three_categories.values():
    other_category -= count
    if count == list(people_in_three_categories.values())[-1]:
        print(f"{count}", end=" ")
    else:
        print(f"{count} + ", end=" ")
print(f")")

# Print the result
print(f"Anzahl der Personen, die in einer anderen Kategorie zugehörig sind: {other_category}")