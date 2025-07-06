# To convert Base 10 (decimal) number to your Base
m = int(input ('your base:'))
n = int(input ('Base 10 number:'))
fin_out=str()
while n//m != 0:
    rem=n%m
    #print (rem)
    out=str(rem)
    fin_out = out+fin_out
    #print(fin_out)
    n= n//m

#print (str(n%m))
out=str(n%m)
fin_out = out+fin_out
print("Number in Base", m, "is equal to: ", (int(fin_out)))