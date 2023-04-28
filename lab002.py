print ("Введіть число" )
a = int(float(input()))
a = abs(a)
a %= 10000
print(a//1000%10)
print(a//100%10)
print(a//10%10)
print(a%10)