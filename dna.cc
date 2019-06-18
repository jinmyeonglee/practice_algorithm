#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Trie {
    Trie *go[4];
    Trie * fail;
    char label;
    bool output;
    int child;

    Trie() {
        fill(go, go+4, nullptr);
        output = false;
        child = 0;
    }
    ~Trie() {
        for(int i = 0; i < 4; i++) {
            if(go[i]) delete go[i];
        }
    }

    void insert(string str) {
        int len = str.length();
        if(len == 0) {
            output = true;
            return ;
        }
        // lable = str[0];
        if(go[child] != 0) {
            
        }
    }
};

int main(void) {
    int T;
    scanf("%d", &T);
    for(int t = 0; t < T; t++) {
        int n,m;
        int ans = 0;
        string str, marker;
        vector<string> v;

        scanf("%d %d", &n, &m);
        cin >> str;
        cin >> marker;
        v.push_back(marker);

        for(int i = 0; i < m; i++) {
            for(int j = i + 1; j < m; j++) {
                string temp;
                if(i == 0) {
                    string sec = marker.substr(0, j);
                    reverse(sec.begin(), sec.end());
                    temp = sec + marker.substr(j);
                }
                else {
                    string sec = marker.substr(i, j-i+1);
                    reverse(sec.begin(), sec.end());
                    temp = marker.substr(0, i) + sec + marker.substr(j+1);
                }
                v.push_back(temp);
            }
        }
        reverse(marker.begin(), marker.end());
        v.push_back(marker);

        sort(v.begin(), v.end());
        v.erase(unique(v.begin(), v.end()), v.end());

        // for(int i = 0; i < n - m + 1; i++) {
        //     if(find(v.begin(), v.end(), str.substr(i, m)) != v.end()) {
        //         ans += 1;
        //     }
        // }
        // printf("%d\n", ans);

        for(auto i : v) {

        }
    }
    return 0;
}
