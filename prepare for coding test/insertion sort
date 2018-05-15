a = [4,6,1,3,5,2]

# 수열의 왼쪽부터 순서대로 정렬, 우측의 미탐색 영역에서 정렬이 끝난 수열과 비교

for idx, value in enumerate(a):
    
    i = idx
    
    while i > 0 and a[i-1] > value:
        
        a[i-1],a[i] = a[i],a[i-1]
        i -= 1
