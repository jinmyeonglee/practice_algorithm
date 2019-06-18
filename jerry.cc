#include <cstdio>
#include <vector>
struct Point {
    int y = 0;
    int x = 0;
    Point(int _x, int _y) {
        x = _x; y = _y;
    }
    Point(){}
};
int main(void) {
    int n, k, h, m;
    Point conners[1001];
    Point holes[51];
    Point mice[251];
    scanf("%d %d %d %d", &n, &k, &h, &m);

    for(int i = 0; i< n; i++) {
        scanf("%d %d", &conners[i].x, &conners[i].y);
    }
    for(int i = 0; i< h; i++) {
        scanf("%d %d", &holes[i].x, &holes[i].y);
    }
    for(int i = 0; i< m; i++) {
        scanf("%d %d", &mice[i].x, &mice[i].y);
    }
    return 0;
}
