import sys
sys.stdin=open('input.txt','r')

def rotate(arr):
    arr_r = [[0]*N for _ in range(N)] #반환 배열 생성
                # [1,2,3] 인 상황이면
                # [4,5,6]
                # [7,8,9]
    for i in range(N):          # N = 3
        for j in range(N): # N=2-1-j , j= 0~2 , 3-1-0, 3-1-1, 3-1-2, = [2][0],[1][0],[0][0] 변화
            arr_r[i][j] = arr[N-1-j][i]
    return arr_r

T = int(input())
for tc in range(1,T+1):

    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    arr1 = rotate(arr) # 원본을 90도
    arr2 = rotate(arr1) # 90도를 90도 = 180도
    arr3 = rotate(arr2) # 180도를 90도 = 270도

    print(f'#{tc}')
    for a,b,c in zip(arr1,arr2,arr3): #zip으로 arr1,2,3 묶어서 a,b,c,에 한 행씩 받기
        print(f'{"".join(map(str,a))} {"".join(map(str,b))} {"".join(map(str,c))}')
        #map으로 str로 변환해서 join함수 사용해서 빈 문자열과 결합