import csv
import matplotlib.pyplot as plt
import numpy as np

cupcake = open("CupcakeInvoices.csv")
myCsv = csv.reader(cupcake)
count = 0
# for data in myCsv:
#     print(data[2])



# for data in myCsv:
#     total = int(data[3]) * float(data[4])
#     newtotal = "{:.2f}".format(total)
#     print(newtotal)
# for data in myCsv:
#     count += float(data[3])
#     newCount = "{:.2f}".format(count)
# print(newCount)
str_count = 0
choc_count = 0
vanil_count = 0
for data in myCsv:
    if data[2] == "Strawberry":
        str_count += float(data[4]) * int(data[3])
    if data[2] == "Chococate":
        choc_count += float(data[4]) * int(data[3])
    if data[2] == "Vanilla":
        vanil_count += float(data[4]) * int(data[3])

# print(count)
x = np.array(["Strawberry", "Chocolate", "Vanilla"])
y = np.array([str_count, choc_count, vanil_count])
plt.bar(x,y)
plt.show()