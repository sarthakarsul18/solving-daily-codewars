def calculate_years(principal, interest, tax, desired):
    years = 0
​
    while principal < desired:
        yearly_interest = principal * interest
        yearly_tax = yearly_interest * tax
        principal += (yearly_interest - yearly_tax)
        years += 1
​
    return years