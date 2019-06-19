#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <numeric>
#include <utility>

using namespace std;

int Answer;
vector<int> v[200001];

int main(int argc, char** argv)
{
    int T, test_case;

    cin >> T;
    for(test_case = 0; test_case  < T; test_case++)
    {
        int n, m;
        queue<int> q;

        cin >> n >> m;
        Answer = n;

        for(int i = 0; i < m; i++) {
            int a, b;
            cin >> a >> b;
            v[a].push_back(b);
            v[b].push_back(a);
        }

        for(int i = 1; i <= n; i++) {
            if(v[i].size() == 2) {
                q.push(i);
            }
        }

        for(int i = 0; i < q.size(); i++) {
            int cur = q.front(); q.pop();

            if(v[cur].size() != 2) {
                continue;
            }
            bool check = false;
            for(int j = 0; j < v[v[cur][0]].size(); j++) {
                if(v[v[cur][0]][j] == v[cur][1]) {
                    check = true;
                    break;
                }
            }
            if(check) {
                for(int j = 0; j < v[v[cur][0]].size(); j++) {
                    if (v[v[cur][0]][j] == cur) {
                        v[v[cur][0]].erase(v[v[cur][0]].begin() + j);
                        break;
                    }
                }
                for(int j = 0; j < v[v[cur][0]].size(); j++) {
                    if (v[v[cur][1]][j] == cur) {
                        v[v[cur][1]].erase(v[v[cur][1]].begin() + j);
                        break;
                    }
                }
                v[cur].clear();
                Answer--;
            }
        }

        for(int i = 0; i < 200001; i++) {
            if(!v[i].empty()) {
                v[i].clear();
            }
        }

        cout << "Case #" << test_case+1 << endl;
        cout << Answer << endl;
    }

    return 0;//Your program should return 0 on normal termination.
}