#Lets learn about lists

supplies = ["tent", "sleeping bags", "water", "raspberry pi", "coffee",
"knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]


camp_site = ["Crystal Lake", 404, 98.3, True]

# supplies.extend(["toilet paper", "bidet", "Ram"])
# supplies = supplies + ["toilet paper", "bidet", "Ram"]

supplies.insert(2, "bidet")

for s in supplies:
    print(s)
