#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

int main() {
    int n, m;
    vector<int> v;
    unordered_set<int> s;
    cin >> n >> m;

    for(int i = 0; i < m; i++) {
        int temp;
        cin >> temp;
        v.push_back(temp);
    }

    for(int i = 0; i < v.size(); i++) {
        for(int num = v[i]; num <= n; num += v[i]) {
            s.insert(num);
        }
    }

    int sum = 0;

    for(int num: s) {
        sum += num;
    }
    cout << sum << endl;

    return 0;
}