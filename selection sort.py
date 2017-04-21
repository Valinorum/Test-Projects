#take an array
arr=[]
n=int(input('Enter the number of element in the array: '))

for i in range(0,n,1):
    b=int(input("Enter the elements:"))
    arr.append(b)               
print (arr)

#sorting with selection sort
for j in range(len(arr)):
    #find the minimum element in the array
    min_idx=j

    for k in range (j+1, len(arr)):
        if arr[min_idx]>arr[k]:
            min_idx = k

    #swap the elements
    arr[j], arr[min_idx] = arr[min_idx], arr[j]


#result
print ('Sorted array is \n')
print(arr)
