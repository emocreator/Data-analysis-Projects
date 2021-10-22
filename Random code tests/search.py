def search(arr, n, x): 
  
    for i in range (0, n): 
        if (arr[i] == x): 
            return i; 
    return -1; 

arr = []
number=int(input("Enter array length"))
for i in range(number):
    data=int(input())
    arr.append(data)
    
x = int(input("What number you looking for? ")); 
n = len(arr); 
result = search(arr, n, x) 
if(result == -1): 
    print("Element is not present in array") 
else: 
    print("Element is present at index", result); 
