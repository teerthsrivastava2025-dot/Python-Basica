products = ["Rice", "Milk", "Petrol", "Books"]

prices = [40, 30, 100, 200]
quantities_demanded = [500, 300, 150, 100]
quantities_supplied = [450, 280, 170, 120]

demand_change_rate = [-0.2, -0.3, -0.05, -0.6]
supply_change_rate = [0.25, 0.3, 0.1, 0.5]

print("Available Products:")
i = 0
while i < len(products):
    print(i + 1, ".", products[i])
    i = i + 1

choice = int(input("Select a product number: "))
index = choice - 1

price = prices[index]
qd = quantities_demanded[index]
qs = quantities_supplied[index]

price_change = 5
new_price = price + price_change

new_qd = qd + (qd * demand_change_rate[index])
new_qs = qs + (qs * supply_change_rate[index])

ped = ((new_qd - qd) / qd) / ((new_price - price) / price)
pes = ((new_qs - qs) / qs) / ((new_price - price) / price)

print("Product Selected:", products[index])
print("Original Price:", price)
print("New Price:", new_price)
print("Price Elasticity of Demand:", ped)
print("Price Elasticity of Supply:", pes)
