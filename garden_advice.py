"""
Garden Advice App

This program gives gardening advice based on the month entered by the user.
It demonstrates basic Python logic, functions, dictionaries, and user input.
"""
# Function responsible for returning gardening advice for a given month.
# Dictionary storing gardening advice for each month
GARDEN_ADVICE = {
    "january": "Plan your garden layout and order seeds.",
    "february": "Start indoor seedlings for spring planting.",
    "march": "Prepare soil and begin planting cool-season vegetables.",
    "april": "Plant flowers, herbs, and vegetables as the weather improves.",
    "may": "Water plants regularly and remove weeds.",
    "june": "Check plants for pests and support growing vegetables.",
    "july": "Water deeply during hot weather and harvest summer crops.",
    "august": "Continue harvesting and prepare for autumn planting.",
    "september": "Plant autumn vegetables and clean garden beds.",
    "october": "Collect leaves for compost and protect sensitive plants.",
    "november": "Prepare the garden for winter.",
    "december": "Clean tools and plan improvements for next year."
}


def get_garden_advice(month):
    """
    Return gardening advice for a given month.

    Args:
        month (str): The month entered by the user.

    Returns:
        str: Gardening advice or an error message.
    """
    month = month.lower().strip()

    if month in GARDEN_ADVICE:
        return GARDEN_ADVICE[month]

    return "Invalid month. Please enter a valid month name."


def main():
    """
    Main function that asks the user for a month and displays gardening advice.
    """
    print("Welcome to the Garden Advice App")
    user_month = input("Enter a month: ")
    advice = get_garden_advice(user_month)
    print(advice)


if __name__ == "__main__":
    main()
