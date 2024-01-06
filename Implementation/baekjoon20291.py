import sys
from collections import Counter
input = sys.stdin.readline

n = int(input().rstrip())

texts = [input().rstrip().split(".")[1] for _ in range(n)]

for name, count in sorted(list(dict(Counter(texts)).items()),key=lambda x: x[0]):
    print(f"{name} {count}")