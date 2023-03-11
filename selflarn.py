##class print1():
##    def __init__(self):
##        self.string=""
##
##    def get(self):
##        self.string=input("Enter string: ")
## 
##    def put(self):
##        print("String is:")
##        print(self.string)
## 
##obj=print1()
##obj.get()
####obj.put()

##import datetime
##now = datetime.datetime.now()
##print(now)
##year = lambda x: x.year
##month = lambda x: x.month
##day = lambda x: x.day
##t = lambda x: x.time()
##print(year(now))
##print(month(now))
##print(day(now))
##print(t(now))
##
##def remove_words(list1, remove_words):
##    result = list(filter(lambda word: word not in remove_words, list1))
##    return result
##        
##colors = ['orange', 'red', 'green', 'blue', 'white', 'black']
##remove_colors = ['orange','black']
##print("Original list:")
##print(colors)
##print("\nRemove words:")
##print(remove_colors)
##print("\nAfter removing the specified words from the said list:")
##print(remove_words(colors, remove_colors))

##nums = [2, 4, 6, 9 , 11]
##n = 2
##print("Original list: ", nums)
##print("Given number: ", n)
##filtered_numbers=list(map(lambda number:number*n,nums))
##print(filtered_numbers)

var=[5,7,12,3,6]
a=[]
for x in var:
    if(a<x):
        a.append()
        
