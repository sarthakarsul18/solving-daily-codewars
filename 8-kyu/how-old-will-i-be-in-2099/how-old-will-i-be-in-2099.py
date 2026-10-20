def calculate_age(year_of_birth, current_year):
    if  year_of_birth == current_year:
        return "You were born this very year!"
    elif year_of_birth>current_year and abs(year_of_birth - current_year) ==1:
        return f"You will be born in {abs(year_of_birth - current_year)} year."
    elif year_of_birth>current_year and abs(year_of_birth - current_year) !=1:
        return f"You will be born in {abs(year_of_birth - current_year)} years."
    elif abs(year_of_birth - current_year)==1:
        return f"You are {abs(year_of_birth - current_year)} year old."
    else:
        return f"You are {abs(year_of_birth - current_year)} years old."