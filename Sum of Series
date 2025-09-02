import math
def performance_series(p0, k, terms = 6):
    total = 0
    for n in range(terms):
        denom = math.factorial(n*n if n != 0 else 1)
        total += (k**n) / denom
    return p0 * total

p0 = int(input("Enter initial performance score (e.g., 100): "))
k = float(input("Enter difficulty factor (e.g., 2.0): "))
terms = int(input("Enter number of terms to consider: "))

final_score = performance_series(p0, k, terms)
print("Predicted Performance Score: ", final_score)
