w = int(input("insert your weight, kg :"))
h = int(input("insert your height, sm :"))/100
bmi = (w)/(h**2)
print(w," kg")
print(h," m")
print(bmi," bmi")
ind = int(bmi//10)
print(ind)
scale = ["20", "===", "===", "===", "===", "===", "===", "50"]
scale.insert(ind, "|")
print("".join(scale))

