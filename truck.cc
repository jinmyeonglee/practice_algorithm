#include <cstdio>
#include <queue>
#include <algorithm>

int main(void) {
    int n, w, l;
    int sum = 0;
    int cnt = 0;
    int time = 0;
    int truck[1001];
    int j = 0; // 다리에 가장 앞에 있는 트럭 번호
    scanf("%d %d %d", &n, &w, &l);

    for(int i = 0; i < n; i++) {
        scanf("%d", &truck[i]);
    }
    sum = truck[0];
    cnt += 1;
    time += 1;
    for(int i = 1; i < n; i++) {
        if(cnt < w && sum + truck[i] < l) {
            printf("tr : %d\n", truck[i]);
            sum += truck[i];
            cnt += 1;
        }
        else {
            sum -= truck[j];
            time = w - cnt + 1;
            cnt -= 1;
            j += 1;
            i -= 1;
        }
    }
    if(cnt != 0) {
        time += w - cnt;
    }
    printf("%d\n", time+1);

    return 0;
}
