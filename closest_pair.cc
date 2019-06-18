#include <cstdio>
#include <algorithm>
#include <utility>
#include <map>

#define abs(N) ((N<0)?(-N):(N))

using namespace std;

int main(void) {
    int n, m;
    int c1, c2;
    int v_p[500001];
    int v_q[500001];
    map<int, int> mym;
    map<int, int>::iterator it;

    scanf("%d %d", &n, &m);
    scanf("%d %d", &c1, &c2);
    for(int i = 0; i < n; i++) {
        scanf("%d", &v_p[i]);
    }
    for(int i = 0; i < m; i++) {
        scanf("%d", &v_q[i]);
    }

    sort(v_p, v_p + n);
    sort(v_q, v_q + m);

    int i, j;
    bool check = false;
    i = 0; j = 0;

    while(i < n && j < m) {
        int d = v_p[i] - v_q[j];
        //printf("%d\n", d);
        it = mym.find(abs(d));
        if(it != mym.end()) {
            mym[abs(d)]++;
        }
        else {
            mym.insert(pair<int, int>(abs(d), 1));
        }

        if(d > 0) {
            j++;
        }
        else {
            if(check == false)
            i++;
        }
    }

    auto it_an = mym.begin();
    int h = c1 - c2;
    printf("%d %d\n", (it_an->first) + abs(h), it_an->second);
    return 0;
}
