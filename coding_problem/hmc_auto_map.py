N = 3


def calc_score(N):
    cols = rows = 2**N
    score = 0

    for y in range(rows):
        for x in range(cols):
            if ((y == 0 and x == 0) or 
                (y == rows - 1 and x == cols - 1) or
                (y == rows - 1 and x == 0) or
                (y == 0 and x == cols - 1)):
                score += 2.25
            elif (y == 0 or x == 0 or x == cols - 1 or y == rows - 1):
                score += 1.5
            else:
                score += 1

    return int(score)

def calc_score(N):
    cols = rows = 2**N
    score = 0

    for y in range(N):
        for x in range(N):
            if ((y == 0 and x == 0) or 
                (y == rows - 1 and x == cols - 1) or
                (y == rows - 1 and x == 0) or
                (y == 0 and x == cols - 1)):
                score += 2.25
            elif (y == 0 or x == 0 or x == cols - 1 or y == rows - 1):
                score += 1.5
            else:
                score += 1



#include <cstdio>
# int N,ans=2;
# int main(){
#    scanf("%d",&N);
#    while(N--) ans = 2*(ans-1)+1;
#    printf("%d",ans*ans);
# }


score = 2
N = 1
while N:
    score = 2*(score - 1) + 1;
    N -= 1

print(score*score)
# print(81 == calc_score(3))
# print(289 == calc_score(4))


