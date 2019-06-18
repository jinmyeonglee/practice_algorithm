#include <stdio.h>

int main(){
    int a, b, n, w;
    int x, y;
    scanf("%d %d %d %d", &a, &b, &n, &w);
    if(a == b) {
        if(w%a==0&&w/a==2&&n==2) printf("1 1\n");
        else printf("-1\n");
        return 0;
    }
    y = (w - a * n) / (b - a);
    x = n - y;

    if(y > 0 && x > 0 && (w - a * n) % (b - a) == 0) printf("%d %d\n", x, y);
    else printf("-1\n");

    return 0;
}
