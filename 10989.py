import sys
N = int(sys.stdin.readline())

cnt = [0] * 10001
for _ in range(N):
    val = int(sys.stdin.readline())
    cnt[val] += 1

for i in range(1, 10001):
    if cnt[i] != 0:
        for _ in range(cnt[i]):
            print(i)

    

    