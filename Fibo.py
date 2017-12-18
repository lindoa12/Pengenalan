list = []
masukan = int(input("Masukan banyak bilangan fibonacci :"))
n = range(1,masukan+1)

for index, data in enumerate(n):
	if data==1:
		list.append(data)
		list.append(data)
	else:
		hasil = list[index-1]+list[index]
		list.append(hasil)
		
print(list)