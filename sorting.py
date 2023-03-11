# Bubble sort
##var=[5,7,12,3,6]
##for x in range(len(var)-1,0,-1):
##    for y in range(x):
##        if(var[y]>var[y+1]):
##            var[y],var[y+1]=var[y+1],var[y]
##print(var)            


##Merge sort

##def merge_sort(a):
##    if(len(a)>1):
##        mid=len(a)//2
##        L=a[:mid]
##        R=a[mid:]
##        merge_sort(L)
##        merge_sort(R)
##        a.clear()
##        while (len(L)>0 and len(R)):
##            if(L[0]<=R[0]):
##                a.append(L[0])
##                L.pop(0)
##            else:
##                a.append(R[0])
##                R.pop(0)
##        for x in L:
##            a.append(x)
##        for x in R:
##            a.append(x)
##a=[5,7,12,3,6]
##merge_sort(a)
##print(a)

#Insertion sort

##a=[5,12,7,3,6]
##for x in range(1,len(a)):
##    second=a[x]
##    pos=x
##    while(pos>0 and (a[pos-1]>second)):
##        a[pos]=a[pos-1]
##        pos=pos-1
##    if(pos!=x):
##        a[pos]=second
##print(a)

### SELECTION SORT

##def selection_sort(a):
##    length=len(a)
##    for i in range(length-1):
##        min=i
##        for j in range(i+1,length):
##            if(a[j]<a[min]):
##                min=j
##        a[i],a[min]=a[min],a[i]
##a=[2,6,33,3]
##selection_sort(a)
##print(a)
