#include <vector>
#include <cstdio>
#include <queue>
#include <algorithm>
using namespace std;
struct Node {
    int label;
    int ch[100001];
    int ch_w[100001];
    int ch_cnt;
    Node(int i) {
        label = i;
    }
};
int vis[100001];
vector<Node> alls;
int bfs_robot(int from, int to) {
    queue<Node> q;
    q.push(alls[from]);
    vis[from] = 1;
    int cnt = 0;
    while(q.empty()) {
        Node now = q.front();
        q.pop();
        for(int i=0 ; i<now.ch_cnt; i++) {
            Node next = now.ch_w[i];
            if(next.label == to){

                return cnt;

            }
            if(!vis[next.label]){
                cnt += now.ch_w[i];
                q.push(next);
            }

        }

    }
    return cnt;
}

int main(void) {
    int n, m;
    vector<int> ans;
    int robots[3];
    scanf("%d %d", &n, &m);
    alls.push_back(Node(0));
    for(int i = 0; i < n; i++) {
        alls.push_back(Node(i+1));
    }
    for(int i = 0; i < m; i++) {
        int sr, dst, w;
        scanf("%d %d %d", &sr, &dst, &w);
        alls[sr].ch_w[alls[sr].ch_cnt] = w;
        alls[sr].ch[alls[sr].ch_cnt++] = dst;
        alls[dst].ch_w[alls[dst].ch_cnt] = w;
        alls[dst].ch[alls[sr].ch_cnt++] = sr;
    }

    for(int i = 0; i < 3; i++) {
        scanf("%d", &robots[i]);
    }

    for(int i = 1; i <= n; i++) {
        int weight = 0;
        for(int j = 0; j < 3; j++) {
            int temp = bfs_robot(robots[j], i);
            if(temp > weight) weight = temp;
        }
        ans.push_back(weight);
    }
    int ii = max_element(ans.begin(), ans.end())-ans.begin();
    printf("%d\n", ii);
    return 0;
}
