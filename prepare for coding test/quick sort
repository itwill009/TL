def quicksort(x,start,end):
    
    if start < end:
        
        pivot = partition(x,start,end)
        
        quicksort(x,start,pivot-1)
        quicksort(x,pivot+1,end)
        
    return x

def partition(x,start,end):
    
    pivot = end
    wall = start
    left = start
    
    while left < pivot:
        
        if x[left] < x[pivot]:
            x[wall],x[left] = x[left],x[wall]
            wall += 1
            
        left += 1
        
    x[wall],x[pivot] = x[pivot],x[wall]
     
    pivot = wall
     
    return pivot

list = [8, 13, 2, 6, 1, 4]
print(quicksort(list,0,len(list)-1))
