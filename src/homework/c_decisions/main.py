#
import decisions

options = float(input("Enter option"))
total = float(input("Enter total"))

ratio = decisions.get_options_ratio(options, total)

result = decisions.get_faculty_rating(ratio)

print (result)
