 #a=10
#b=12
#print (a+b)

#c=5.5
#print(c)
#print(type(c))


#var=10
#var1=10.5  
#print(var+var1)

## Print statements

#var="dhoni"
#var1="7"
#print(var+str(var1))  # explicit typrcasting
#var="dhoni"
#var1=100
#print("%s Scored %d runs " % (var,var1))
#print(var,"scored",var1,"runs")
#print("{} scored {} runs".format(var,var1))      
      
#a="INDIA"
#b= 350
#c= 50
#d="Srilnka"
#print("%s scored %d runs against %s in %d overs " % (a,b,d,c))
#print(a,"score",b,"runs against",d)

##Slicing##

#a="India"
#c=a[2:][-3]
#print(c)

#var="India"
#print(var[2])

#var='Samsung'
#print(var[2],var[-2]) #  Printing m and n

#a='Ms Dhoni'
#print(a[3])

#a=' Ms Dhoni'
#print(a[-4])
# Negative indexing

#Country='India'        #In syntax [1:4] 1 place stands for Index and 4 stands for value or 1 plus index
#print(Country[1:4])    

#var='Gangguly'
#print(var[1:4])
#print(var[4:7])

#var='Ganguly'
#print(var[-6:-4])

#var='Ganguly'
#print(var[-4:-1])

#var='Gambhir'
#print(var[2:4])
#print(var[-5:-2])
      
#var='Gambhir'
#print(var[4:6])  In negative index the last value cant be addressed so we leave as blank so that it takes till  the end
#print(var[-3:])

#Var="Gambhir"
#print(Var[2:-2])
#print(Var[-3:7])


Name="Rahul"
print(Name[1:4])
print(Name[1:-1])          # The  types  of slicing which are possible
print(Name[-4:-1])
print(Name[-4:4])
print(Name[2])
print(Name[-3])
print(Name[2:-2])
print(Name[-3:3])
print(Name[2:3])
print(Name[-3:-2])

##a='rahul'
##print(a[2:])
##print(a[-3:])
##print(a[2:5])
##print(a[-3:5])'

##var='America'
##print(var[::-1])      #   reverse  a string

##var='America'
##print(var[::-2])        # Skips value  of the value given

##var='America'
##print(var[::1])
##
##var='America'
##print(var[::2])

##var='America'
##print(var[1:6:2])    #In this the 1 is start index 6 is  stop value and 2 is seperator


##var='india intention india'
##print(var.count("in"))                     #counts the times of in the string
##print(var.count("in",3))                    #3 is the index value so it starts lookking after the index
##print(var.count("in",8,20))      

##var='india intention india'
##print(var.find("in"))                     #find  
##print(var.find("in",3))                 
##print(var.find("in",8,20))
##
##
##print(var.index("in"))                    #
##print(var.index("in",3))                    
##print(var.index("in",8,20))

##var='westindies'
##print(var.find("z"))        Find if no  value  present it returns negative  value
##print(var.index("z"))

##Var='India is my country'
##print(Var.split("is"))
##print(Var.partition("is"))

##var='India is my countey'
##print(len(var))

##var='!India is my countey!'
##print(var.strip("!"))
##print(var.lstrip("!"))
##print(var.rstrip("!"))
##


##var='!India is my countey!'      #strip  only does in from front and back
##print(var.strip("i"))


##var='India is  my  country India'    #  STRIP func
##print(var.strip("India"))
##print(var.lstrip("India"))
##print(var.rstrip("India"))

#var="india is my country"
#print(var.upper())
#print(var.lower())
#print(var.title())
#print(var.capitalize())


#var="india is my country"
#print(var.isupper())
#print(var.islower())
#print(var.istitle())

#var="india is my country"
#print(var.startswith("india"))
#print(var.endswith("country"))
#print("is"in var)

#var='india'
#var[1]='m'
#print(var)

#var='india'
#print(var.replace("n","m"))       ## STRINNG MANIPULATION OVER

        ## LIST ##
#var=["dhoni","kholi",10,7]
#print(var)
#print(type(var))

#var=["dhoni","kholi",10,7]
#print(var[1])
#print(var[-3])
#print(var[-3:2])
#print(var[1:-2])
#print(var[1:2])
#print(var[-3:-2])

##var=["dhoni","kholi",10,7]
##print(var[1][3])

#var=["dhoni","kholi",10,7]
#var[11="yuvi"
#print(var)

#var=["dhoni","kholi",10,7]
#var[1][0]="m"
#print(var)

#var=["dhoni","kholi","azar","rahul"]      APPEND
#var.append("jadeja")
#print(var)

#var=["dhoni","kholi","azar","rahul"]      APPEND 
#var.append(["yuvi","cris"])
#print(var)

#var=["dhoni","kholi","azar","rahul"]      EXTEND
#var.extend(["yuvi","cris"])
#print(var)

#var=["dhoni","kholi","azar","rahul"]     INSERT
#var.insert(1,"yuvi")
#print(var)

#var=["dhoni","kholi","azar","rahul"]     POP
#var.pop()
#print(var)

#var=["dhoni","kholi","azar","rahul"] 
#var.pop(2)
#print(var)

#var=["dhoni","kholi","azar","rahul"]     REMOVE
#var.remove("azar")
#print(var)

#var=["dhoni","kholi","azar","rahul"]     SORT
#var.sort()
#print(var)

#var=["dhoni","kholi","azar","rahul"]   True is boolean
#var.sort(reverse=True)
#print(var)

#var=["dhoni","kholi","azar","rahul"]
#print(sorted(var))

#var=["dhoni","kholi","azar","rahul"]
#print(sorted(var,reverse=True))

#var=["dhoni","kholi","azar","rahul"]    LENGTH
#print(len(var))

#var=["dhoni","kholi","azar","rahul"]    CLEAR
#var.clear()
#print(var)

#var=["dhoni","kholi","azar","rahul"]    DELETE  var so  while printing there will be no var element so  it gives error
#del(var)
#print(var)

### Dictionary  ###

##var={"name":"dhoni","age":40}
##print(var)
##print(type(var))

##var={"1":"dhoni","2":40}
##print(var)
##print(type(var))

##var={"name":"dhoni","age":40}
##print(var["name"])               SINCE it  is mapped with key  value so it needs to   first called to  access the value  dhoni

##var={"name":"dhoni","age":40}
##print(var["name"][1])     

##var={"name":["dhoni","kholi"],"age":[40,35]}
##print(var)
##print(type(var))
##

##
##var={"name":["dhoni","kholi"],"age":[40,35]}
##print(var["name"][1])
##print(var["name"][1][1])

##var={"name":{"name":"dhoni","age":10},"age":{1:40,2:35}}
##print(type(var))
##print(var["name"]["name"][1:4])

##var={'name':'dhoni','age':30}
##var['name']='kholi'
##print(var)

##var={'name':'dhoni','age':30}
##var['name'][2]='m'             We cant change string's particular value
##print(var)

##var={'name':'dhoni','age':30}     ##MANIPULATION STARTS
##print(var.keys())         
##print(var.values())
##var.pop('age')              ## In pop we have to use key value to pop and since  its mutable we have to perform after the  change is  made 
##print(var)

#var={'name':'dhoni','age':30}
##print(var['gender'])         ## This throws error if not available

##print(var.get('gender'))       ## So need to  use get method so error will not  apper and shows none
#print(var.get('age'))

##a=[10,7,8]
##b=[6,5,4]
##a.extend(b)
##print(a)

##var1={'name':'dhoni','age':30}    ## Same key  values will replace
##var2={'name':'yuvi','age':40}
##var1.update(var2)
##print(var1)

##var1={'name':'dhoni','age':30}       ## Different keys adds to the dict
##var2={'name1':'yuvi','age1':40}
##var1.update(var2)
##print(var1)

##var1={'name':'dhoni','age':30}       ## LENGTH
##var2={'name':'yuvi','age':40}
##print(len(var2))

##var={'name':'dhoni','age':30}
##print(var['name'].count('d'))
##print(var['name'].index('d'))

##var={'name':['dhoni','kholi'],'age':[30,40]}
##var['name'].append('yuvi')
##print(var)

##var={'name':['dhoni','kholi'],'age':[30,40]}
##var['name'].extend('yuvi')
##print(var)

##var={'name':['dhoni','kholi'],'age':[30,40]}
##var['name'].pop(1)
##print(var)

### TUPLES ###

##var=("dhoni",7)
##print(var)
##print(type(var))

##var=("dhoni",7)
##print(var[0])
##print(var[0:1])

##var=('dhoni')
##print(type(var))

##var=('dhoni',)
##print(type(var))

##var=('dhoni',7)
##print(var[0][0])
##print(var[-2][0])
##print(var[0])
##print(var[-2])
##print(var[-2][-5])
##print(var[0][-5])
##print(var[-2])
##print(var[0][-5])

##var=('dhoni',7)
##var[0]='kholi'           # Tuple is immmutable
##print(var)

##var=('dhoni',7)
##print(var.count('dhoni'))     # Tuples contains only count  and index
##print(var.index('dhoni'))
##print(var.find('dhoni'))

#### SETS  #####

##var={'india','azar',10,7,'kholi'}
##print(var)
##print(type(var))

##var={'india','azar',10,7,'kholi'}     No sliccing operations can bee  peerformed
##print(var[1])

##var={'india','azar',10,7,'kholi'}
##var.add(11)                               # Set ADD 
##print(var)

##var={'india','azar',10,7,'kholi'}
##var.pop()                                   # POP (random value)                           
##print(var)

##var={'india','azar',10,7,'kholi'}
##var.remove('azar')                               # Set Remove 
##print(var)

##var={'india','azar',10,7,'kholi'}          # LENGTH
##print(len(var))# Len LENGTH

##var={'india','azar',10,7,'kholi'}           #CLEAR
##var.clear()
##print(var)

##var={'india','azar',10,7,'kholi'}          #DELETE
##del(var)                          
##print(var)

#var=['india','azar',10,7,'kholi']
#print(set(var))

##var=['india','azar',10,7,'kholi']
##a=set(var)
##print(a)
##a.add('azar')
##print(a)

##var=['india','azar',10,7,'kholi']
##a=frozenset(var)
##print(a)
##a.add('jaddu')
##print(a)

##var=['india','azar',10,7,'kholi']
##var1=var[1].capitalize()               
##print(var1)

                        #### ITERATORS/LOOPINNG ####

                                ##  For LOOP ##

                                ##  IF  ##

#var='india'
#for x in var:
#    print(x)

##var='samsung'
##for i in var:
##    print(i)

##var=['dhoni','azar','kholi','yuvi']
##for x in  var:
##    print(x)

##var=['dhoni','azar','kholi','yuvi']
##for  x in var:
##    if(x=='azar'):
##        print(x)

##var='dhoni'
##for x in var:
##    if(x=='n'):
##        print(x)

##var='samsung'
##for x in var:
##    if(x=='s'):
##        print(x)

##var='samsung'
##for x in var:      
##    if(x=='s'):
##        print(x)
##        break           ## BREAK  ##

##var='samsung'
##for x in var:
##    if(x=='m'):
##        print('Available')

##var='ganguly'
##for x in var:
##    if(x=='n'):
##        print('Avail')
##    else:
##        print('Unavail')

##var='gambhir'
##for x in var:
##    if (x=='a'):
##        print('Present')
##    elif (x=='b'):                ##  ELIF  ##
##        print('Avail')
##    else:
##        print('Not  present')

##var='india'
##for x in var:                   ## To  print i  d  a
##    if (x=='i'):
##        print(x)
##    elif (x=='d'):
##        print(x)  
##    elif (x=='a'):
##        print(x)

##var='india'
##a=0
##for x in var:
##    if(a%2==0):
##        print(x)
##    a=a+1

##var='india'
##a=0
##for x in var:
##    if(a%2!=0):
##        print(x)
##    a=a+1 

##var='india'                   ## ENUMERATE ##
##for x in  enumerate(var):
##    print(x)

##var='india'
##for x,y in  enumerate(var):
##    print(x)    

##var='india'
##for x,y in  enumerate(var):
##    if(x%2==0):
##        print(y)
       
##var='india'
##for x,y in  enumerate(var):
##    if(x%2!=0):
##        print(y)

##var='aaaabbbbbccdeef'
##for x in var:
##    if (x=='a'):
##        print(x)
##        break
##    elif(x=='b'):
##        print(x)
##    elif(x=='c'):
##        print(x)
##    elif(x=='d'):
##        print(x)
##    elif(x=='e'):
##        print(x)
##    elif(x=='f'):
##        print(x)

##var='aaaabbbbbccdeef'
##a=set(var)
##print(a)
##b=list(a)
##b.sort()
##new=''
##for x in b:
##    new=new+x
##print(new)

##var=
##new=''
##for x in var:
##    if  x not in new:

##var='india'
##for x in var:         ## PASS ##
##    if(x=='d'):
##        pass
##    print(x)

##var='india'
##for x in var:             ## CONTINUE ##
##    if(x=='d'):
##        continue
##    print(x)

##var=[10,7,2,5]
##a=[]
##for x in var:
##    if (x%2==0):
##        a.append(x)
##        print(a)

##var=[7,8,6,4,2]
##a=0
##for x,y in enumerate(var):
##    a=(a+y)
##print(a)

##var=587                        ## Integer adding using  for ###
##a=str(var)
##b=0
##for x in a:
##    b=b+int(x)
##print(b)

##var=587
##a=str(var)
##print(a[::-1])

##a=2
##if(a<10):
##    print(a)
##    a=a+2

## For loop works on str and list etc but not on INTEGER
##If only works on 1 iteration
## While wworks on integer and it runs infinite if condition satisfies


                            ###  WHILE LOOOOOPPPP   ###

##a=2
##while(a<10):
##    print(a)
##    a=a+2

##var='india'
##for x in var:
##    while(x=='d'):
##        print(x)

##var='india'
##for x in var:
##    if(x=='d'):
##        print(x)

##var=587                         ## Adding interger using WHILE ####
##a=0
##while(var>0):
##    digit=var%10
##    a=a+digit
##    var=var//10
##print(a)

##for x in range(10):       ### RANGE Function   ####
##    print(x)

#for x in range(-1,10):
#    print(x)

##for x in range(2,10,2):
##    print(x)

#for x in range(10,2,-1):      ### In range fuction decending order values should be given a seperator with negative indexing
#    print(x)

        ### DYNAMICALLY TYPING #########

##a=input("Enter your name:")
#print(a)
#print(type(a))

##a=input("Enter your number:")
##print(a)
##print(type(a))

#a=int(input("Enter your number:"))
#print(a)
#print(type(a))

#a=float(input("Enter your number:"))
#print(a)
#print(type(a))

##a=[]
##for x in range(1,6):
##    a.append(x*5)
##print(a)

##b=[]
##for x in range(1,6):
##    for y in range(5,6):
##        b.appendappend(x,y)
##print(b)

##a=[]
##for x in range(0,3):
##    for y in range(0,3):
##        for z in range(0,3):
##            a.append([x,y,z])
##print(a)            
            
##a=[]
##for x in range(5,8):
##    for y in range(5,8):
##        for z in range(5,8):
##            a.append([x,y,z])
##print(a)            
            
##a=5
##b=6
##c=7
##d=[]
##d.append(a)
##d.append(b)
##d.append(c)
##print(d)

##a=5
##b=6
##c=7
##d=[]
##d.append(a)
##d.append(b)
##d.append(c)
##for x in range(0,3):
##    for y in range(0,3):
##        for z in range(0,3):
##            if(d[x]!=d[y]and d[y]!=d[z]and d[z]!=d[x]):
##                print(d[x],d[y],d[z])
##

                            #####   FUNCTIONS  #####
#It  is a group of related statement thatcaan perform any specific  task
#it can  be exeecuted only if we call the funntion it by  its name
#Addvantags
#Secure
#Compact
#Better  understand
#Reusable

#def  new():
#    print('Success')  ### Funtion with zero argument
#new()

#def fun(a):
#    print(a)            ### Function with one argument 
#fun(10)    

#def nxt(a,b):           ### Funnction with 2 or multiple argument
#    print(a+b)
#nxt(30,40)    

##def nxt(a,b):
##    print(a+b)
##nxt(30,40)
##nxt(10,20)
##nxt(-10,50)

#def nxt(a,b):
#    print(a,'scores',b,'runs')
#nxt('dhoni',100)    

##def nxt(a,b):
#    print(a,'scores',b,'runs')    ###  Must definne th number arguments defined in  def else error ccomes
#nxt('dhoni',100,20)

##def nxt(a,b):
##    print(a,'scores',b,'runs')
##nxt(100,'dhoni')

##def nxt(a,b=100):
##    print(a,'scores',b,'runs')
##nxt('dhoni')

#ef nxt(a='dhoni',b):           ## Error as the value replaces the a  and b has no value so always assign values to the eend of the argumentt 
#    print(a,'scores',b,'runs')
#nxt(100)

#def nxt(b,a='dhoni'):
#    print(a,'scores',b,'runs')
#nxt(100)

##def fun(*a):
##    print(a)
##fun(10)
##fun(10,20)
##fun(10,20,30)

##def fun(a=20,b=10):
##    print(a+b)
##fun()

##def nxt(a,b):
##    print(a,'scores',b,'runs')
##nxt(b=100,a='dhoni')

##def fun(**a):
##    print(a)
##fun(a=10)
##fun(b=10,c=20)
##fun(b=10,c=20,d=30)

#def fun(a,b):                    ### RETURN FUNCTION ###
#    print(a+b)                     
#    return(a+b)
#c=fun(10,2)
#print(c*5)

##def fun(a,b):
##    print(a+b)
##    print('good')
##    return " success "
##fun(10,20)

##def fun(a,b):
##    print(a+b)
##    print('good')
##    return "success "
##print(fun(10,20))

##def fun(a,b):
##    print(a+b)
##    print('good')
##    return "success "
##z=fun(10,20)
##print(z)

##def fun(a,b):
##    print(a+b)
##    return " success "
##    print('good')
##print(fun(10,20))

##def fun(a,b):                 ##  Return will end the function 
##    return " success "        ## So always  usse at  the  end
##    print(a+b)
##    print('good')
##print(fun(10,20))

#############  ASSETS

##a=[]
##assert(len(a)>1)
##b=sum(a)
##c=b/len(a)
##print(c)

##a=[]
##assert(len(a)>1),"Empty"
##b=sum(a)
##c=b/len(a)
##print(c)

##a=[1,2,3,4,5]
##assert(len(a)>1)
##b=sum(a)
##c=b/len(a)
##print(c)



                            #### MULTITHREADING ####
##import time
##def fun():
##    print('One')
##    print(time.ctime())        
##    time.sleep(2)                   ## Time Library ##
##def fun1():
##    print('Two')
##    print(time.ctime())
##fun()
##fun1()

##import time
##import threading       
##def fun():
##    print('One')
##    print(time.ctime())        
##    time.sleep(2)
##def fun1():
##    print('Two')
##    print(time.ctime())
##t1=threading.Thread(target=fun)
##t2=threading.Thread(target=fun1)
##t1.start()
##t2.start()

##  Threading with  Arguments ##

##import time
##import threading
##def fun(name):
##    print(name,time.ctime())
##def fun1(name):
##    print(name,time.ctime())
##t1=threading.Thread(target=fun,args=('dhoni',))
##t2=threading.Thread(target=fun1,args=('kholi',))
##t1.start()
##t2.start()

##import time                   ## Delay in threading
##import threading
##def fun(name,delay):
##    count=0
##    while(count<5):
##        print(name,time.ctime())
##        time.sleep(delay)
##        count=count+1
##t1=threading.Thread(target=fun,args=('dhoni',2))
##t2=threading.Thread(target=fun,args=('kholi',4))
##t1.start()
##t2.start()

##import time
##import threading
##def fun(name):
##    new()
##    print(name,x)
##x=0
##def new():
##    global x
##    x=x+1
##t1=threading.Thread(target=fun,args=('dhoni',))
##t2=threading.Thread(target=fun,args=('kholi',))
##t1.start()
##t2.start()

##import threading
##def fun(name,L):
##    L.acquire()
##    new()
##    print(name,x)
##    L.release()
##x=0
##def new():
##    global x
##    x=x+1
##L=threading.Lock()    
##t1=threading.Thread(target=fun,args=('dhoni',L))
##t2=threading.Thread(target=fun,args=('kholi',L))
##t1.start()
##t2.start()

              #### Threading  over ####

##from datetime import datetime
##var=datetime.now()
##print(var)

##from datetime import datetime
##var=datetime.now()
##print(var)
##var1=var.replace(microsecond=0)
##print(var1)

##from datetime import datetime
##from datetime import timedelta   ## Timedelta lib to add time  
##var=datetime.now()
##print(var)
##var1=var.replace(microsecond=0)
##print(var1)
##var2=var1+timedelta(minutes=120)
##print(var2)

##from datetime import datetime     ## Timedelta lib to minus time
##from datetime import timedelta
##var=datetime.now()
##print(var)
##var1=var.replace(microsecond=0)
##print(var1)
##var2=var1-timedelta(minutes=120)
##print(var2)

##from datetime import datetime     ## Timedelta lib to minus time
##from datetime import timedelta
##var=datetime.now()
##print(var)
##var1=var.replace(microsecond=0)
##print(var1)
##fmt=" %d/%m/%y   %H-%M-%S "
##var4=datetime.strftime(var1,fmt)
##print(var4)

##from datetime import datetime
##from datetime import timedelta
##var=datetime.now()
##print(var-timedelta(microsecond=120))
##print(var)

                    #### Filehandling ####

##var=open("new.txt","w")
##var.write("Tech")
##var.close()

##var=open("new.txt","a")
##var.write("Beasant")
##var.close()

##var=open("new.txt","r")
##a=var.read()
##print(a)

##var=open("new.txt","w+")
##var.write("hello")
##a=var.read()
##print(a)

##var=open("new.txt","w+")
##var.write("hello")
##var.seek(0)
##a=var.read()
##print(a)

##var=open("new.txt","r+")
##print(var.read())
##var.write("new")
##var.close()
##var=open("new.txt","r+")
##print(var.read())

##var=open("new.txt","a+")
##var.write("new")
##var.close()
##var=open("new.txt","r+")
##var.seek(0)
##print(var.read())

##var=open('new.txt','a+')
##var.write("Kholi")
##var.write("dhoni")
##var.write("Yuvi")
##var.close()

#var=open("new.txt","r")
#print(var.read())

##var=open("new.txt","r")
##print(var.readline())

##var=open("new.txt","r")
##print(var.readline(2))

##var=open("new.txt","r")
##print(var.readlines())

##with open("new.txt","r") as var:
##    print(var.read())

##with open("new.txt","w") as var:
##    var.write("Ganguly")   

##with open("new.txt","a+") as var:
##    var.write("Dhoni"'\n')
##    var.write("Kholi"'\n')

##with open("new.txt","w") as var:
##    var.write("Dhoni"'\n')
##    var.write("Kholi"'\n')

##with open("new.txt","w+") as var:
##    var.write("Dhoni"'\n')
##    var.seek(0)
##    var.read()

##var=["dhoni","azar","kholi","yuvi"]
##for x in var:
##    var1=open("best.txt","a+")
##    a=var1.read()
##    length=len(a)
##    if (length>0):
##        var1.write("\n")
##        var1.write(x)
##        var1.close()
##    else:
##        var1.write(x)
##        var1.write("\n")
##        var1.close()


##var=list(input("Enter  the name  :"))
##for x in var:
##    var1=open("best.txt","a+")
##    a=var1.read()
##    length=len(a)
##    if (length>0):
##        var1.write("\n")
##        var1.write(x)
##        var1.close()
##    else:
##        var1.write(x)
##        var1.write("\n")
##        var1.close()

                     ###   Exception Handliinng
                ### The process of hndling erors is called exception handling###

#TYPE 1

##var=10/0
##print(var)

##try:
##    var=10/0
##    print(var)
##except:
##    print("error")

##try:
##    var=10/0
##    print(var)
##except(ZeroDivisionError):
##    print("error")

##try:
##    var=10+"a"
##    print(var)
##except(ZeroDivisionError):
##    print("error")
##except(TypeError):
##    print("good")

##try:
##    var=a
##    print(var)
##except(ZeroDivisionError):
##    print("error")
##except(TypeError):
##    print("good")

##try:
##    var=a
##    print(var)
##except(ZeroDivisionError):
##    print("error")
##except(TypeError):
##    print("good")
##except:
##    print("Good")

##try:
##    var=a
##    print(var)
##except(ZeroDivisionError,TypeError):
##    print("error")
##except:
##    print("good")

##try:
##    var=10+20
##    print(var)
##except(ZeroDivisionError,TypeError):
##    print("error")
##except:
##    print("good")

##try:
##    var=10+20
##    print(var)
##except(ZeroDivisionError,TypeError):
##    print("error")
##except:
##    print("good")
##else:
##    print('new')

##try:
##    var=a
##    print(var)
##except(ZeroDivisionError,TypeError):
##    print("error")
##except:
##    print("good")
##else:
##    print("new")

##try:
##    var=a
##    print(var)
##except(ZeroDivisionError,TypeError):
##    print("error")
##except:
##    print("good")
##else:
##    print('new')
##finally:
##    print('bad')

##try:
##    var=10
##    print(var)
##except(ZeroDivisionError,TypeError):
##    print("error")
##except:
##    print("good")
##else:
##    print('new')
##finally:
##    print('bad')

## TYPE 2

##try:
##    var=10+'a'
##    print(var)
##except ZeroDivisionError as a:
##    print(a)

##try:
##    var=10+'a'
##    print(var)
##except Error as a:
##    print(a)

##try:                          ## Dynamic  Approach
##    var=10+'a'
##    print(var)
##except Exception as a:
##    print(a)

##try:
##    var=10/0
##    print(var)
##except ZeroDivisionError as a:
##    print(a)

##try:
##    def fun(a,b):
##        print(a+b)
##    fun()
##except Exception as a:
##    print(a)

## TYPE 3   USER Defined exception  (we creeat  the exception to pass into except)

##try:
##    var=10
##    if(var>10):
##        raise TypeError
##except TypeError as a:
##    print(a)

##try:
##    var=10
##    if(var>5):
##        raise TypeError('good')
##except TypeError as a:
##    print(a)
##    print(a)

##try:
##    var=10
##    if(var>5):
##        raise Exception('Good')
##except Exception as a:
##    print(a)

##try:
##    var=10
##    if(var>5):
##        raise Error('Good')
##except Exception as a:
##    print(a)

##class  Error (Exception):         # Changing a word to a keyword
##    var='Good'
##try:
##    var=10
##    if(var>5):
##        raise Error
##except Error as a:
##    print(a.var)

                        ##### COMPREHENSION #####

# list dict set genator

##var=[10,7,2,3,12]
##var1=[]
##for x in var:
##    var1.append(x)
##print(var1)

##var=[10,7,2,3,12]
##var1=[]
##for x in var:
##    var1.append(x)
##    var1.sort()
##print(var1)

##var=[10,7,2,3,12]
##z=[x for x in var]
##print(z)

##var=[10,7,2,3,12]
##var1=[]
##for  x  in var:
##    a=x*x*x
##    var1.append(a)
##print(var1)

##var=[10,7,2,3,12]
##z=[x**3 for x in var]
##print(z)

##var=[10,7,2,3,12]
##a=[]
##for x  in var:
##    if(x>5):
##        a.append(x)
##print(a)        

##var=[10,7,2,3,12]
##z=[x for x  in var  if(x>5)]
##print(z)

##var=[10,7,2,3,12]
##z=[x for x  in var  if(x%2==0)]
##print(z)


##var=[10,7,2,3,12]
##a=[]
##b=[]
##for x  in var:
##    if(x%2==0):
##        a.append(x)
##    else:
##        b.append(x)
##print(a)
##print(b)

##var=[10,7,2,3,12]
##z=["even" if(x%2==0) else "odd" for  x in var]
##print(z)

##b=[]
##for x in range(1,6):
##    for y in range(5,6):
##        b.append(x*y)
##print(b)

##z=[x*y for x in range(1,6) for y in range(5,6)]
##print(z)

## DICTIONARY COMPREHENSION

##var=[5,7,12,3]
##a={}
##for x in var:
##    a[x]=x
##print(a)

##var=[5,7,12,3]
##z={x:x for  x in var}
##print(z)

##var=[5,7,12,3]
##a={}
##for x in var:
##    a[x]=x**2
##print(a)

##var=[5,7,12,3]
##z={x:x**2 for  x in var}
##print(z)

##var=[5,7,12,3]
##a={}
##for x in var:
##    if(x%2==0):
##        a[x]=x   
##print(a)

##var=[5,7,12,3]
##z={x:x for  x in var if(x%2==0)}
##print(z)

##var=['csk','mi','rcb']
##var1=['dhoni','rohit','virat']
##a=zip(var,var1)
##print(a)


##var=['csk','mi','rcb']           ## ZIP Combines the inndex vaalues
##var1=['dhoni','rohit','virat']
##a={}
##z=list(zip(var,var1))
###print(z)
##for x,y in z:
##    a[x]=y
##print(a)    
    
##var=['csk','mi','rcb']           
##var1=['dhoni','rohit','virat']
##z={x:y for x,y in zip(var,var1)}
##print(z)

            ### SET  COMPREHENSION

##var=[10,7,2,3]
##a=set()
##for x in var:
##    a.add(x)
##print(a)

##var=[10,7,2,3]
##z={x for x in var}
##print(z)

                ### GENERATOR  CoMPREHENION

##var=[10,7,2,5]
##a=tuple(var)
##print(a)

##var=[10,7,2,5]
##z=(x for x in var if(x%2==0))
##print(z)

##var=[10,7,2,5]                    ## TUPLES ah convert panna mudiyathu 
##z=(x for x in var)
##print(z)
##for x in z:
##    print(x)

                         ###### LAMDA , FITER , MAP , REDUCE  ######


##def fun(a):
##    print(a)
##fun(10)

##LAMBDA  is an anonamays function which imitate behaviour of the functions

##var=lambda a:a
##print(var(10))

##def fun(a):
##    b=a*a
##    print(b)
##fun(10)    

##var=lambda a:a*a
##print(var(10))

### FILTER ###              FOR ONLY CONDITION

##var=[10,7,5,2]
##z=list(filter(lambda x:x%2==0,var))
##print(z)

### MAP ###                 FOR ONLY MATHEMATICAL OPERATION

##var=[10,7,5,2]
##z=list(map(lambda x:x**2,var))
##print(z)

##var=[10,7,5,2]
##z=list(map(lambda x:x%2==0,var))
##print(z)

##from  functools import reduce
##var=[10,7,5,2]
##z=reduce(lambda x,y:x+y,var)
##print(z)

                                ####  CLASS  #####
#Class is a way, procedure or blueprint to create an object
#because python is an OOPS  language

#Class  is an group of related staementsthat can perform any  task
#it can  execute only if we call class by its name
#in python there are 2 types of classes
# Bounded and Unbounded

##Adavantage
##Reusable
##Compact
##BBetter understandning
##Secure

#Unbounded Class

##class new():
##    var=10
##    print(var)
##new()    

##class new():
##    var=10
##print(new.var)

##class nxt:
##    def  fun(a,b):
##        print(a+b)
##nxt.fun(10,20)

##class nxt:
##    def fun(a,b):
##        print(a,'scored',b,'runs')
##nxt.fun('dhoni',100)        

##class new:
##    def fun():
##        print('success')          # Same func  name repllaces the  memorey wit the  new one
##    def  fun(a,b):
##        print(a+b)
##new.fun()        

##class new:
##    def fun():
##        print('success')         
##    def  __fun(a,b):
##        print(a+b)
##new.fun()
##new.__fun()

##count=10
##class new:
##    count=20
##    def fun(a,b):
##        print('success')
##        print(a+b)
##new.fun(10,20)
##print(count)
##print(new.count)
    
##count=10
##class new:
##    global count
##    count=20
##    def fun(a,b):
##        print('success')        
##        print(a+b)
##new.fun(10,20)
##print(count)
##print(new.count)                # Count becomes global so it does not belong to  func

##class new:
##    def fun():
##        print('Success')
##    def fun1(a,b):
##        print(a+b)
##new.fun1(10,20)
##new.fun()

##class new:
##    def fun(a,b):
##        print(a+b)
##    def fun1(a,b):
##        for x in fun1(a,b):
##            if a==b:
##                print('True')
##new.fun(10,20)
##new.fun1(10,10)

                        ### INHERTANCE   ###
     ## Single Inhertane ##

##class old:
##    def fun():
##        print('Scucces')
#### First is always parent and  the following is child  class
#### Child can inherit but parent cant inherit child         
##class new(old):
##    def fun1(a,b):
##        print(a+b)
##new.fun()
##new.fun1(10,20)

     ##  Multiple inheritance
##class a:
##    def fun():
##        print('a')
##class b(a):
##    def fun():
##        print('b')
##class c(b,a):
##    def fun():
##        print('c')
##class d(c,b):
##    def fun():
##        print('d')
##d.fun()

## If no fun available in it goes to parent class if available it prints D

##class a:
##    def fun():
##        print('a')
##class b(a):
##    def fun():
##        print('b')
##class c(b,a):
##    def fun():
##        print('c')
##class d(c,b):
##    pass
##d.fun()

##class a:
##    def fun1():
##        print('a')
##class b(a):
##    def fun2():
##        print('b')
##class c(b,a):
##    def fun3():
##        print('c')
##class d(c,b):
##    def fun4():
##        print('d')
##d.fun1()

##class  new:
##    def fun(ip,pwd):
##        print(ip,pwd)
##    def  fun1(ip,pwd,code):
##        print(ip,pwd,code)
##new.fun("127.0.0.1",999)
##new.fun1("127.0.0.1",999,'ipconfig')

##class new:
##    def __init__(self,ip,pwd):
##        self.a=ip
##        self.b=pwd
##    def fun(self):
##        print(self.a,self.b)
##    def fun1(self):
##        print(self.a,self.b)
##c=new("127.0.0.1",999)
##c.fun()
##c.fun1()

##class new:
##    def __init__(self,ip,pwd,code):
##        self.a=ip
##        self.b=pwd
##        self.c=code
##    def fun(self):
##        print(self.a,self.b)
##    def fun1(self):
##        print(self.a,self.b)
##    def  fun2(self):
##        print(self.a,self.b,self.c)
##c=new("127.0.0.1",999,'ab12')
##c.fun()
##c.fun1()
##c.fun2()

##class new:
##    def __init__(self,ip,pwd):
##        self.a=ip
##        self.b=pwd
##    def fun(self):
##        print(self.a,self.b)
##    def fun1(self):
##        print(self.a,self.b)
##    def  fun2(self,code):
##        print(self.a,self.b,code)
##c=new("127.0.0.1",999)
##c.fun()
##c.fun1()
##c.fun2('ipconfig')

##class old:
##    def __init__(self,name,age):
##        self.a=name
##        self.b=age
##    def fun(self):
##        print(self.a,self.b)
##class new(old):
##    def __init__(self,name,age):
##        self.a=name
##        self.b=age
##    def fun1(self):
##        print(self.a,self.b)
##c=new("Dhoni",30)
##c.fun()
##c.fun1()

##class old:
##    def __init__(self,name,age):
##        self.a=name
##        self.b=age
##    def fun(self):
##        print(self.a,self.b)
##class new(old):
##    def __init__(self,name,age):
##        self.a1=name
##        self.b1=age
##    def fun1(self):
##        print(self.a1,self.b1)
##c=new("Dhoni",30)
##c.fun1()
##c.fun()

##class old:
##    def __init__(self,name,age):
##        self.a=name
##        self.b=age
##    def fun(self):
##        print(self.a,self.b)
##class new(old):
##    def __init__(self,name,age):
##        self.a1=name
##        self.b1=age
##    def fun1(self):
##        print(self.a1,self.b1)
##c=new("Dhoni",30)
##c.fun1()
##c.fun()

##class old:
##    def __init__(self,name,age):
##        self.a=name
##        self.b=age
##    def fun(self):
##        print(self.a,self.b)
##class new(old):
##    def __init__(self,name,age):
##        old.__init__(self,name,age)         ## Inherits  the parent generator
##        self.a1=name
##        self.b1=age
##    def fun1(self):
##        print(self.a1,self.b1)
##c=new("Dhoni",30)
##c.fun1()
####c.fun()
##
##class old:
##    def __init__(self,name):
##        self.a=name
##    def fun(self):
##        print(self.a)
##    def fun1(age):
##        print(age)
##c=old("Dhoni")
##c.fun()
##c.fun1(40)
##
####class new:
##    def __init__(self,name,age):
##        self.a=name
##        self.b=age
##    def fun(self):
##        print(self.a,self.b)
##    def fun1(salary):
##        if(salary>5000):
##            print('valid')
##c=new("Dhoni",30)
##c.fun()
##c.fun1(7000)
                ###   DECORATERS     ####

##class new:
##    def __init__(self,name,age):
##        self.a=name
##        self.b=age
##    def fun(self):
##        print(self.a,self.b)
##    @staticmethod                   ## Decoraters used  to serperate a func
##    def fun1(salary):
##        if(salary>5000):
##            print('valid')
##c=new("Dhoni",30)
##c.fun()
##c.fun1(7000)

##class new:
##    def __init__(self,name,age):
##        self.a=name
##        self.b=age
##    def fun(self):
##        print(self.a,self.b)
##    @staticmethod
##    def fun1(salary):
##        if(salary>5000):
##            print('valid')
##    @classmethod
##    def fun2(cls,name,age):
##        return cls(name,age)
##c=new("Dhoni",30)
##c.fun()
##c.fun1(7000)
##d=new.fun2('kholi',30)
##d.fun()


                        ### ENCAPSULATION ###


##class new:
##    def __init__(self,name,age):
##        self.a=name
##        self.b=age
##    def fun(self):
##        print(self.name,self.age)
##c=new("Dhoni",30)
##c.fun()
##print(c.name)
##print(c.age)

##class new:
##    def __init__(self,name,age):
##        self.name=name
##        self.age=age
##    def fun(self):
##        print(self.name,self._age)
##c=new("Dhoni",30)
##c.fun()
##print(c.name)
##print(c._age)

##class new:
##    def __init__(self,name,age):
##        self.name=name
##        self.__age=age
##    def fun(self):
##        print(self.name,self.__age)
##c=new("Dhoni",30)
##c.fun()
##print(c.name)
##print(c.__age)

##class new:
##    def __init__(self,name,age):
##        self.name=name
##        self.__age=age
##    def fun(self):
##        print(self.name,self.__age)
##    def getage(self):
##        print(self.__age)
##    def setage(self,age):
##        self.__age==age
##c=new("Dhoni",30)
##c.fun()
##c.getage()
##c.setage(35)
##c.getage()

                    ### POLYMORPHISM ###

##class apple:
##    def  type(self):
##        print("Fruit")
##    def color(self):
##        print("Red")
##class tomato:
##    def  type(self):
##        print("vegetable")
##    def color(self):
##        print("Red")
##c=apple()
##d=tomato()
##c.type()
##c.color()
##d.type()
##d.color()

##class apple:
##    def  type(self):
##        print("Fruit")
##    def color(self):
##        print("Red")
##class tomato:
##    def  type(self):
##        print("vegetable")
##    def color(self):
##        print("Red")
##def fun(obj):
##    obj.type()
##    obj.color()
##a=apple()
##b=tomato()
##fun(a)
##fun(b)


                    ####    COLLECTIOBNS####

##  Named tuple Immutble


##
##from collections import namedtuple
##a=namedtuple("Students",['name','age','gender'])
##b=a('dhoni','40','male')
##print(b)


##from collections import namedtuple
##a=namedtuple("Students",['name','age','gender'])
##b=a('dhoni','40','male')
##print(b)
##print(b[1])
##print(b.gender)

##from collections import namedtuple
##a=namedtuple("Students",['name','age','gender'])
##b=a('dhoni','40','male')
##print(b)
##print(b[1])
##print(b.gender)
##print(getattr(b,"name"))

##from collections import namedtuple
##a=namedtuple("Students",['name','age','gender'])
##b=a('dhoni','40','male')
##print(b)
##print(b[1])
##print(b.gender)
##print(getattr(b,"name"))
##li=['yuvi','40','male']
##print(a._make(li))
##di={'name':'rahul','age':'40','gender':'male'}
##print(a(**di))

##from collections import namedtuple
##a=namedtuple("Students",['name','age','gender'])
##b=a('dhoni','40','male')
##print(b)
##print(b[1])
##print(b.gender)
##print(getattr(b,"name"))
##li=['yuvi','40','male']
##print(a._make(li))
##di={'name':'rahul','age':'40','gender':'male'}
##print(a(**di))
##print(b._asdict)

##from collections import namedtuple
##a=namedtuple("Students",['name','age','gender'])
##b=a('dhoni','40','male')
##print(b)
##print(b[1])
##print(b.gender)
##print(getattr(b,"name"))
##li=['yuvi','40','male']
##print(a._make(li))
##di={'name':'rahul','age':'40','gender':'male'}
##print(a(**di))
##print(b._asdict)
##print(b._fields)
##print(b._replace(name='Hart'))
#-----------------------------------------------------------------------#

### DEQUE

##from collections import deque
##a=deque((10,11,12))
##print(a)

##from collections import deque
##a=deque((10,11,12))
##print(a)
##print(a[1]

##from collections import deque
##a=deque((10,11,12))
##print(a)
##print(a[1])
##a[1]=13
##print(a)
##a.append(13)
##print(a)
##a.appendleft(9)
##print(a)
##a.extend([14,15])
##print(a)

##from collections import deque
##a=deque((10,11,12))
##print(a)
##print(a[1])
##a[1]=13
##print(a)
##a.append(13)
##print(a)
##a.appendleft(9)
##print(a)
##a.extend([14,15])
##print(a)
##a.extendleft([20,151])
##print(a)
##a.pop()
##print(a)
#------------------------------------------------------------------------------#

##Counter

##from collections import Counter
##var='India is my country'
##a=Counter(var)
##print(a)

## ChainMap

##from collections import ChainMap
##a=[1,2,3]
##b=[1,2,3]
##c=ChainMap(a,b)
##print(c)

##from collections import ChainMap
##a=[1,2,3]
##b=(4,5,0)
##c=ChainMap(a,b)
##print(c)

##from collections import OrderedDict
##a=OrderedDict()
##a[0]='a'
##a[1]='b'
##a[2]='c'
##print(a)
##print(a[1])
##a.pop(1)
##print(a)
##a[1]="New"
##print(a)

##from collections import OrderedDict
##a=OrderedDict()
##a[0]='a'
##a[1]='b'
##a[2]='c'
##print(a)
##print(a[1])
##a.pop(1)
##print(a)
##a[1]="New"
##print(a)
##print(a[4])

##from collections import OrderedDict
##a={}
##a[0]='a'
##a[1]='b'
##a[2]='c'
##print(a)
##print(a[1])
##a.pop(1)
##print(a)
##a[1]="New"
##print(a)
##print(a[4])

#----------------------------------------------------------------------------#

## DEFAULT DICT

##from collections import defaultdict
##def fun():
##    return"No key"
##a=defaultdict(fun)
##a[0]='a'
##a[1]='b'
##a[2]='c'
##print(a)

##from collections import defaultdict
##def fun():
##    return"No key"
##a=defaultdict(fun)
##a[0]='a'
##a[1]='b'
##a[2]='c'
##print(a)
##print(a[6])

##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# DJango
#Is a frame work for creating backend

#Google  contains Ports and IP
#2008 founded  1.0
#2017 latest    2.0


#Points
##Complete-----Batteries included  architecture
##versatile----client side framework (Combines  iwth all html, css, etc)
##scalable----- shhared nothing arch    "MVT"  Loosely copuled
##secure----To do right things   "" Crypographic hash func""
##maintainable
##portable

#by using  djabndi we can create  complte website because battery included arch

#Django

#######################
##class new:
##    def __init__(self,name,age):
##        self.a=name
##        self.b=age
##    def fun(self):
##        print(self.a,self.b)
##    def fun1(self):
##        print(self.a,self.b)
##c=new('dhoni',40)
##c.fub()

##class new:
##    def __init__ (self,name,age):
##        self.a=name
##        self.__=age
##    def fun(self)

##class cal():
##    def __init__(self,a,b):
##        self.a=a
##        self.b=b
##    def add(self):
##        return self.a+self.b
##    def mul(self):
##        return self.a*self.b
##    def div(self):
##        return self.a/self.b
##    def sub(self):
##        return self.a-self.b
##a=int(input("Enter first number: "))
##b=int(input("Enter second number: "))
##obj=cal(a,b)
##choice=1
##while choice!=0:
##    print("0. Exit")
##    print("1. Add")
##    print("2. Subtraction")
##    print("3. Multiplication")
##    print("4. Division")
##    choice=int(input("Enter choice: "))
##    if choice==1:
##        print("Result: ",obj.add())
##    elif choice==2:
##        print("Result: ",obj.sub())
##    elif choice==3:
##        print("Result: ",obj.mul())
##    elif choice==4:
##        print("Result: ",round(obj.div(),2))
##    elif choice==0:
##        print("Exiting!")
##    else:
##        print("Invalid choice!!")
##print()
