#Input 
grocery_list = [
    ['apple',1.0,5],
    ['orange', 10.0, 5],
    ['apple', 10.0, 5]
]

# totalselling
total = {}
for item in grocery_list:
    name , price, quan = item
    selling_price = price * quan
    if name in total:
        total[name] += selling_price
    else:
        total[name] = selling_price
        
#highest total
highest_tot = max(total, key=total.get)
print(highest_tot)

total_price = sum(total.values())
print(total_price)

avg_price = total_price/len(total)
print(avg_price)
