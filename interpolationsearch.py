#imports required
import sys #to get the size of the array

#main function
def interpolation_search(arr, x):
      lo=0
      hi=len(arr)-1
      #since array is sorted it should be in the range of corner value
      while (lo<=hi and x>=arr[lo] and x<=arr[hi]):
          pos= lo + int(((hi-lo)*(x-arr[lo]))/(arr[hi]-arr[lo]))
          if (arr[pos]==x):
              return pos              
          elif arr[pos]<x:
              lo=pos+1                
          else:
              hi=pos-1
      return -1

        
#main driver function
arr=[]
n=int(input('Enter the number of elements in the array: '))
for i in range(0,n,1):
    b=int(input("Enter the elements:"))
    arr.append(b)               
print (arr)
x=int(input('Enter the number you wish to search: '))

result=interpolation_search(arr, x)

if result!=-1:
      print ("Element is present at index %d" % result)
else:
      print ("Element is not present")




      
