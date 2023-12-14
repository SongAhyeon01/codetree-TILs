# 리스트에 저장
# 리스트를 돌면서 일단 카운트를 1한다
# 근데 != 뒤에꺼일 경우에 카운트를 초기화한다
# 만약 카운트가 4인데 초기화됐다?
# 그럼 안됨
# 그래서 최대 카운트 수를 저장해야한다
# != 를 만나면 현재 카운트를 최대 카운트와 비교하고 최대보다 크면 바꾼다

n = int(input())
list = [int(input()) for _ in range(n)]

max_cnt = 1
cnt = 1
for i in range(n):
    if i==0 or list[i] != list[i-1]:
        if cnt >= max_cnt:
            max_cnt = cnt
            cnt = 1
    else:
        cnt += 1
        if cnt >= max_cnt:
            max_cnt = cnt
            
print(max_cnt)