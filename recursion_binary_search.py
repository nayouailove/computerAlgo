
def binary_search(a, left, right, K):
    if right >= left:

        mid= (left+right) //2 #중간숫자 인덱스 찾기

        if a[mid] ==K: #탐색 성공
             return True
    
        elif a[mid] > k: #앞부분에서 K찾기
            return binary_search(a, left, mid-1, K)
        
        else: #뒷부분에서 K찾기
            return binary_search(a, mid+1, right, K)
        
    else:
        return False #실패~
