with open("currencydata.txt") as f:
    lines=f.readlines()

currencydict={}
for line in lines:
    parsed=line.split("\t")
    print(parsed)
    currencydict[parsed[0]]=parsed[1]
    


amount=int(input("enter amount:\n"))
print("enter the name of currency you want to converyt this amount to? availsble options:")
[print(item) for item in currencydict.keys()]
currency=input("please enter one of these values:\n")
print(f"{amount} INR is equal to {amount*float(currencydict[currency])} {currency}")