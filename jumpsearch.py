#write the imports
import math #to do the square root
#write the main funtion
def jumpsearch(arr, x):
    s=len(arr)
    #finding the block size to be jumped
    step=int((math.sqrt(s))) #getting the step size
    
    #finding the block where the element is
    prev=0
    while (arr[min(step, s)-1] < x):
        prev=step
        step +=math.floor(math.sqrt(s))
        if prev >= s:
            return -1

    #time for the linear search
    for prev in range (prev-1,s,1):
        if arr[prev]==x:
            return prev
            break       
    

#main program
arr=[]
n=int(input('Enter the number of elements in the array: '))

for i in range(0,n,1):
    b=int(input("Enter the elements:"))
    arr.append(b)               
print (arr)
x=int(input('Enter the number you wish to search: '))
result=jumpsearch(arr, x)+1

if result!=0:
      print ("Element is present at index %d" % result)
else:
      print ("Element is not present")
