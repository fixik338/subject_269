M = int(input("Кол-во строк = "))

z = input("Введите слог = ").lower()
i = 0
while(i < M):
 arr = input("Введите строку = ").lower()
 arr = arr.replace(z, "")
 print(arr)
 i+=1


