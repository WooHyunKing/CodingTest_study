import sys

input = sys.stdin.readline

# N명의 인원이 참여하는 스터디
# 3개의 대회, 모든 구성원이 각 대회에 참여
# 참가자는 각 대회에서 0이상 1000이하의 정수인 점수를 얻음
# 한 대회에서 둘 이상의 참가자가 동점이 나오는 경우도 있음

# 각 대회 별로 등수 및 최종 등수를 매김
# 동점인 경우에는 공동 등수, 아닌 경우에는 일반 등수
# 즉, 등수 = 나보다 점수가 높은 사람의 수 +  1

# 각 참가자의 대회별 등수 / 최종 등수 출력
# 입력 최대 범위 : 10^5

n = int(input())

score_list = []
sum_list = [0] * n

for _ in range(3):
    init = list(map(int,input().split()))

    for i, score in enumerate(init):
        sum_list[i] += score
        
    scores = sorted(init,reverse=True)

    score_dict = dict()
    rank = 1
    count = 1

    for i, score in enumerate(scores):
        if i == 0:
            score_dict[score] = count
        else:
            if scores[i-1] == score:
                score_dict[score] = rank
                count += 1
            else:
                rank += count
                score_dict[score] = rank
                count = 1
    for i in range(n):
        print(score_dict[init[i]],end=" ")
    print()

rank, count = 1, 1
sorted_sum_list = sorted(sum_list,reverse=True)
score_dict2 = dict()

for i, score in enumerate(sorted_sum_list):
    if i == 0:
        score_dict2[score] = count
    else:
        if sorted_sum_list[i-1] == score:
            score_dict2[score] = rank
            count += 1
        else:
            rank += count
            score_dict2[score] = rank
            count = 1

for i in range(n):
    print(score_dict2[sum_list[i]],end=" ")