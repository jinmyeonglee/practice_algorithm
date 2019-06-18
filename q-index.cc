#include <cstdio>
#include <vector>
#include <algorithm>

int main(void) {
    int n;
    int tmp;
    int paper[1001];
    scanf("%d", &n);

    for(int i = 0; i < n; i++) {
        scanf("%d", &paper[i]);
    }
    std::sort(paper, paper+n);

    tmp = n;

    for(int i = 0; i < n; i++) {
        if(tmp == 0) break;
        if(paper[i] >= tmp) {
            if(n - i == tmp || n - i - 1 == tmp) {
                break;
            }
            else {
                tmp -= 1; i = 0;
            }
        }
        else if (i == n - 1) {
            tmp -= 1; i = 0;
        }
    }
    printf("%d\n", tmp);

    return 0;

}
