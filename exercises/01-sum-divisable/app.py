sum_result = 0

# TODO: Write your solution here.
# Sum all numbers below 1000 that are divisible by 3 or 5.
for num in range(1000):
    if num % 3 == 0 or num % 5 == 0:
        sum_result += num
# Use print to show the result
print(sum_result)
