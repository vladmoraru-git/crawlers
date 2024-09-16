
calculation_to_hours = 24
name_of_unit = "hours"
user_input = []


def days_to_units(num_of_days, name_of_unit):
    if name_of_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} {name_of_unit}"
    elif name_of_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} {name_of_unit}"
    elif name_of_unit == "seconds":
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60} {name_of_unit}"
    elif name_of_unit == "days":
        return f"{num_of_days} days are {num_of_days} {name_of_unit}"
    else:
        return "unit not specified"


def validate_and_execute (days_and_unit_dic):
    try:
        user_input_number = int(days_and_unit_dic["days"])
        # check indent
        if user_input_number > 0:
            user_input_int = int()
            calculated_value = days_to_units(user_input_number, days_and_unit_dic["unit"])
            print(calculated_value)
        else:
            print("str, no bueno")
    except ValueError:
        print("not a valid number.")

user_input_message="Add days to be converted in hours and conversion unit:\n"