import datetime
​
def check_coupon(entered_code, correct_code, current_date: str, expiration_date: str) -> bool:
    if entered_code == correct_code and type(entered_code)==type(correct_code):
        current = datetime.datetime.strptime(current_date, "%B %d, %Y")
        expiration = datetime.datetime.strptime(expiration_date, "%B %d, %Y")
​
        if current <= expiration:
            return True
​
    return False