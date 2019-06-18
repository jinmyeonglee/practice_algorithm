#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

int main(void) {
    int d, t;
    vector<int> v;
    scanf("%d %d", &d, &t);
    v.push_back(1);
    v.push_back(1);

    for(int i = 2; i <= t; i++) {
        int sum = 0;
        int j = (i - d > 0 ? i - d : 0);
        for(; j < k; j++) {
            sum += v[j];
        }
        v.push_back(sum);
    }
    int ans = v.back();
    printf("%d\n", ans);

    return 0;
}
