from itertools import count
from turtle import hideturtle
from xml.dom.minidom import Element

from numpy import append


data1 = [2, 4, 6, 3, 9]
data2 = [1, 3, 5, 7, 8, 9,] 
yang_sama = []
hitung  = []
jumlah = 0 

for i in data1:
    for j in data2:
        if i == j:
            yang_sama.append(i)
for x in yang_sama: 
    jumlah += 1           

print(yang_sama)
print(jumlah)