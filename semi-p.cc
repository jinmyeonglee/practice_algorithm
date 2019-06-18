#include <cstdio>
#include <vector>
#include <set>
#include <string>
#include <algorithm>

using namespace std;

bool check(string qq) {
    string com = qq;
    reverse(com.begin(), com.end());
    return (com == qq);
}

int main(void) {
    int n, k, l;
    string w;
    vector<set<string>> sets;
    double theta;

    scanf("%d %d %d", &n, &k, &l);
    theta = k / l;
    cin >> w;
    char st = w[0];

    set<string> temp;
    for(int i = 1; i < n; i++) {
        if(st == w[i]) {
            temp.insert(w.substr(0, i + 1));
            st = w[i+1];
        }
    }
    sets.push_back(temp);

    return 0;
}
