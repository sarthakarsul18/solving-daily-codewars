def expression_matter(a, b, c):
    values = [a + b + c,
    a * b * c,
    a + b * c,
    a * b + c,
    a * (b + c),
    (a + b) * c]
    return max(values)