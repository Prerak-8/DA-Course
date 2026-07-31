import datetime

def date_diff(date_1, date_2):
    date_1_obj = datetime.datetime.strptime(date_1, "%d-%m-%Y")
    date_2_obj = datetime.datetime.strptime(date_2, "%d-%m-%Y")

    difference = abs(date_2_obj - date_1_obj)

    return difference.days