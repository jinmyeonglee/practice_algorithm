#include <cstdio>
#include <vector>

int global_id = 0;

struct Node
{
    int id;
    int weight[1000];
    int next[1000];
    int cnt;

    Node() {
        id = global_id++;
        cnt = 0;
    }
};

int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);
    Node list[100001];

    for(int i = 0; i < m; i++) {
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);
        list[u].weight[list[u].cnt] = w;
        list[u].next[list[u].cnt++] = v;
    }
    return 0;
}

// int dfs(int n, int point) {
//
// }
