def get_days_in_month(month):
    if month == 1:  # January
        return "31 days"
    elif month == 2:  # February
        return "28 or 29 days"  # February can have 28 or 29 days
    elif month == 3:  # March
        return "31 days"
    elif month == 4:  # April
        return "30 days"
    elif month == 5:  # May
        return "31 days"
    elif month == 6:  # June
        return "30 days"
    elif month == 7:  # July
        return "31 days"
    elif month == 8:  # August
        return "31 days"
    elif month == 9:  # September
        return "30 days"
    elif month == 10:  # October
        return "31 days"
    elif month == 11:  # November
        return "30 days"
    elif month == 12:  # December
        return "31 days"
    else:
        return "Invalid month"  # If the number is not between 1 and 12

# Example usage:
month = int(input("Enter the month number (1-12): "))
print("The number of days:", get_days_in_month(month))
