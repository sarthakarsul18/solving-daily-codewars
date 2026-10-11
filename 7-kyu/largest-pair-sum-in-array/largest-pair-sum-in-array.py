def largest_pair_sum(numbers): 
    return max(numbers) + sorted(numbers)[-2]