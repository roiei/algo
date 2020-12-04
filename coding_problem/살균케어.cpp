#include <stdio.h>


typedef struct {
    int y;
    int x;
} coord_type;

int main(void) {
    int i, j, k, si, sj, t, h, w;
    int N, L, M;
    coord_type* coords = nullptr;

    scanf("%d %d %d", &N, &L, &M);
    coords = new coord_type[110];
    for (i = 0; i < M; i++) {
        scanf("%d %d", &coords[i].y, &coords[i].x);
    }

    auto max = 0;
    for (auto h = 1; h < L/2; h++) {
        auto w = L/2 - h;
        for (auto i = 0; i < M; i++) {
            for (auto j = i; j < M; j++) {
                auto sy = coords[i].y > coords[j].y ? coords[j].y : coords[i].y;
                auto sx = coords[i].x > coords[j].x ? coords[j].x : coords[i].x;
                auto cnt = 0;
                for (auto k = 0; k < M; k++) {
                    if ((sy <= coords[k].y && sy+h >= coords[k].y) && (sx <= coords[k].x && sx+w >= coords[k].x)) {
                        cnt += 1;
                    }
                }

                max = max > cnt ? max : cnt;
            }
        }
    }

    delete coords;
    printf("%d", max);
    return 0;
}

