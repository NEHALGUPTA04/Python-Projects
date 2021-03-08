
list = list([4,8,24,35,55,67,88,90])
x = int(input("Enter the key to search in list: "))
def binary_search(list,x):
    mid = 0
    low = 0
    high = len(list) -1

    while low <= high:
        mid = (low+high)//2

        if list[mid] < x:
            low= mid + 1
        elif list[mid]>x:
            high = mid - 1
        else :
            return mid

    return -1
result = binary_search(list,x)
if result == -1:
    print("Key not present in list!!")
else:
    print("Key is present in list ", str(result))