#string * num 
w,x, txt = 2,3,"@"
print(w*txt*x)

# str+str
y,z,text = "2",3,"@"
print((y+text)*z)

#numeric values can use all operators
j,k,l = 2,3,4
print(j*k-l)

#int operator float = float
m,n = 3,5.5
print(m+n)

#result of / is float
q,s = 5,1
print(q/s)

# Integer divison //  diplays float ans as int by rounding of to floor
a,b,c,d = 12,-12,5,-5
print("12//5 :", a//c )
print("-12//5 :", b//c )
print("12//-5 :", a//d )
print("-12//-5 :", b//d )

#remainder is negative only when denominator is negative
print("12%5 :", a%c )
print("-12%5 :", b%c )
print("12%-5 :", a%d )
print("-12%-5 :", b%d )
