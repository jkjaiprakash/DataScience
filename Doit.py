# n=int(input("Enter number of rows: "))
# for i in range (n,0,-1):
#     print((n-i) * ' ' + i * '*')

# n=int(input("Enter number: "))
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# print("Reverse of the number:",rev)

# def check(n):
#     if (n < 2):
#         return (n % 2 == 0)
#     return (check(n - 2))
# n=int(input("Enter number:"))
# if(check(n)==True):
#       print("Number is even!")
# else:
#       print("Number is odd!")

# n=int(input("Enter a number:"))
# tot=0
# while(n>0):
#     dig=n%10
#     tot=tot+dig
#     n=n//10
# print("The total sum of digits is:",tot)

# l=[]
# def sum_digits(b):
#     if(b==0):
#         return l
#     dig=b%10
#     l.append(dig)
#     sum_digits(b//10)
# n=int(input("Enter a number: "))
# sum_digits(n)
# print(sum(l))

test_string=input("Enter string:")
l=[]
l=test_string.split()
wordfreq=[l.count(x) for x in l]
print(dict(zip(l,wordfreq)))