cnt = 0

def quick(arr):
    global cnt
    if arr==[] :
        return []
    m=arr[0]
    left=[]
    right=[]
    for k in arr[1:]:
        if k<m:
            left.append(k)
        else:
            right.append(k)
        cnt+=1
    return quick(left)+[m]+quick(right)