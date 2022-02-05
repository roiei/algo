N, K = 5, 3
scores = [10, 50, 20, 70, 100]
query = [
    [1, 3],
    [3, 4],
    [1, 5],
]


for start, end in query:
    print('{:.2f}'.format(sum(scores[start - 1: end])/(end - start + 1)))