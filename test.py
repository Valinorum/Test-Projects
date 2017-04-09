#function to check the element. If not found it will return -1
def binsearch(arr, l, r, x):
    #test the base case
    if r>=l:
        mid= l+(r-l)/2
        #if the element is the middle element
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binsearch(arr, l, mid-1, x)
        else:
            return binsearch(arr, mid+1, r,x)
    else:
        return -1

arr=[]
n=int(input('Enter the number of elements in the array: ')
for i in range(0,n,1):
    b=int(input("Enter the elements:"))
    arr.append(b)               
print (arr)
x=int(input('Enter the number you wish to search: ')

result=binsearch(arr, 0, len(arr)-1, x)

if result!=-1:
      print "Element is present at index %d" % result
else:
      print "Element is not present"
      
            
