# mealCost = float(input())
# tipPercent = int(input())
# taxPercent = int(input())
mealCost = 10.25
tipPercent = 17
taxPercent = 5
tip = mealCost * (tipPercent/float(100))
tax = mealCost * (taxPercent/float(100))
totalCost = int(round(mealCost + tip + tax, 0))
print(tip)
print(tax)
print(mealCost + tip + tax)
print(round(mealCost + tip + tax, 0))

print("The total meal cost is {} dollars.".format(totalCost))
# 10.25
# 17
# 5