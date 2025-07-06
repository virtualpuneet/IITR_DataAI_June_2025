# To convert number in your Base to your Base 10
m = int(input ('your base:'))
n = int(input ('your base number:'))
fin_out=0
#split the number as seperate digits and multiply base to the power 0, 1, 2 and ...
str_num = str(n)
str_len = len(str_num)
for i in str_num:
    str_len=str_len-1
    out=int(int(i)*(m**str_len))
    fin_out=fin_out+out
print("Base 10 equivalent is: ", fin_out)