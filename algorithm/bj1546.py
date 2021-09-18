n = int(input())
scores = [int(n) for n in input().split(' ')]

max_scores = max(scores)
scores = [score / max_scores * 100 for score in scores]

print(sum(scores) / n)