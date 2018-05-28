def mergeSort(x):
    
    # 재귀적으로 두 부분으로 나눈 후 반대로 작은 값부터 병합
    
    print('split ',x)
    
    if len(x) > 1:
        
        mid = len(x)//2
        lx, rx = x[:mid], x[mid:]
        
        mergeSort(lx)
        mergeSort(rx)

        
        li, ri, i = 0, 0, 0
        
        while li < len(lx) and ri < len(rx):
            
            if lx[li] < rx[ri]:
                x[i] = lx[li]
                li += 1
            else:
                x[i] = rx[ri]
                ri += 1
            i += 1
            
            
        x[i:] = lx[li:] if li != len(lx) else rx[ri:]
        
    print('merge ',x)
        
alist = [6,2,4,1,3,7,5,8]
mergeSort(alist)
