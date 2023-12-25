from collections import deque
def bfs(si, sj, ei, ej):
    q = deque()
    v = [[0]*M for _ in range(N)]

    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        if (ci,cj) == (ei,ej):  # 정답 처리가 필요한 경우 이자리에서..
            return v[ei][ej]

        # 4방향, 범위내, 조건에 맞으면: arr == 1, v == 0
        for di,dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==1 and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj]+1

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
ans = bfs(0, 0, N-1, M-1)
print(ans)