#take an array
arr=[]
n=int(input('Enter the number of element in the array: '))

for i in range(0,n,1):
    b=int(input("Enter the elements:"))
    arr.append(b)               
print (arr)

#function for the bubble sort

def bubble(arr):
    n=len(arr)

    #traverse through all the element
    for i in range (n):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

#call the function
bubble(arr)
print('Sorted array is \n')
print(arr)
