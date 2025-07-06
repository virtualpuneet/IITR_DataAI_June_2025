# To convert number in your Base to your Base 10
m = int(input ('your base:'))
n = int(input ('your base number:'))
#fin_out=str()
#split the number as seperate digits and multiply base to the power 0, 1, 2 and ...

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