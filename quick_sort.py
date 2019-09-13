def quick_sort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    less = []
    greater = []
    #print("Length: ", len(array))
   
    for lNum in array[1:]:
        if lNum < pivot:
            less.append(lNum)
            
    for gNum in array[1:]:
        if gNum > pivot:
            greater.append(gNum)
    print("Pivot: ", pivot)
    print("Less ", less)
    print("Greater ", greater)
    result = quick_sort(less) + [pivot] + quick_sort(greater)
    # 4,6,9,5 + 10 + []
    #[] + 4 + 6,9,5 +10
    # 4 + 5 + 6 + 9 +10
    print("Result: ", result)
    return result

numbers = [10,4,6,9,5]
print(quick_sort(numbers))
            
    
        
   
    
