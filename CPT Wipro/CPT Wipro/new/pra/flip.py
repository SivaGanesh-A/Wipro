def flip(arr, k):
    return arr[:k+1][::-1]+ arr[k+1:]
def pancake(arr):
    n= len(arr)
    for size in range(n, 1, -1):
        max_index= arr.index(max(arr[:size]))
        if max_index != size-1:
            if max_index != 0:
                arr= flip(arr, max_index)
                print(f"Flip at {max_index+1}: {arr}")
            arr= flip(arr, size-1)
            print(f" Flip at {size}: {arr}")
    return arr
nums= list(map(int, input("enter numbers separated with space:").split()))
sorted_nums= pancake(nums)
print("sorted", sorted_nums)
    
nums= list(map(int,input("enter numbers seperated with space").split()))
