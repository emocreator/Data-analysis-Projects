
def bubbleSort(arr): 
	n = len(arr) 
	for i in range(n): 
		for j in range(0, n-i-1): 
			if arr[j] > arr[j+1] : 
				arr[j], arr[j+1] = arr[j+1], arr[j] 

arr = []
number=int(input("Enter array length"))
for i in range(number):
    data=int(input())
    arr.append(data) 

bubbleSort(arr) 

print ("Sorted array is:") 
for i in range(len(arr)): 
	print ("%d" %arr[i]), 

