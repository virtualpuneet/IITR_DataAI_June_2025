# Program to convert any base to any base

# Function to convert number in your Base to your Base 10 (Decimal)
def base_to_dec(m,n):
    #m = int(input ('your base:'))
    #n = int(input ('your base number:'))
    fin_out=0
    #split the number as seperate digits and multiply base to the power 0, 1, 2 and ...
    str_num = str(n)
    str_len = len(str_num)
    for i in str_num:
        str_len=str_len-1
        out=int(int(i)*(m**str_len))
        fin_out=fin_out+out
    return (fin_out)


# Function to convert Base 10 (Decimal) number to your Base
def dec_to_base(m,n):
    #m = int(input ('your base:'))
    #n = int(input ('Base 10 number:'))
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
    return(int(fin_out))

a = int (input ('enter your current base: '))
input_num = int (input ('enter your current number: '))
b = int (input ('enter the desired base: '))

b2d=base_to_dec(a,input_num)
d2b=dec_to_base(b,b2d)
print ("number in your desired based is:" , d2b)

