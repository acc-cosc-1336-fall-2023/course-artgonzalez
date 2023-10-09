#
def get_options_ratio(option, total):
    ratio = option / total
    return ratio

def get_faculty_rating(ratio):
    ratio = ratio * 10
    print(ratio)
    rating = ""

    if(ratio >= 9 and ratio <=10):
        rating = "Excellent"
    elif(ratio >= 8):
        rating = "Very Good"
    elif(ratio >= 7):
        rating = "Good"
    elif(ratio >= 6):
        rating = "Needs Improvement"
    elif(ratio >= 0):
        rating = "Unacceptable"
    else:
        rating = "Invalid ratio"

    return rating