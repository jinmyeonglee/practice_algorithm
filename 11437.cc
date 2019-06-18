#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

vector<vector<int> > v(50001);
int p[50001];
int d[50001];
bool check[50001] = {false, };

int LCA(int a, int b) {
    while(d[a] != d[b]) {
        if(d[a] > d[b]) {
            a = p[a];
        }
        else {
            b = p[b];
        }
    }
    while(a != b) {
        a = p[a];
        b = p[b];
    }
    return a;
}

void makeTree(void) {
    queue<int> q;
    check[1] = true;
    d[1] = 0;
    p[1] = 1;
    q.push(1);

    while(!q.empty()) {
        int now = q.front();
        q.pop();
        for(int i = 0; i < v[now].size(); i++) {
            int next = v[now][i];
            if(!check[next]) {
                check[next] = true;
                d[next] = d[now] + 1;
                p[next] = now;
                q.push(next);
            }
        }
    }
}

int main(void) {
    int N, M;
    scanf("%d", &N);
    for(int i = 0; i < N - 1; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        v[a].push_back(b);
        v[b].push_back(a);
    }

    makeTree();

    scanf("%d", &M);
    for(int i = 0; i < M; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        int re = LCA(a, b);
        printf("%d\n", re);
    }
    return 0;
}