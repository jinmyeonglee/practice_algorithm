#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> v;
    vector<int> q(k, n + 1);

    for(int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        v.push_back(temp);
    }

    for(auto it = v.rbegin(); it != v.rend(); it++) {
        bool chk = false;
        for(int i = 0; i < k; i++) {
            if(*it < q[i]) {
                q[i] = *it;
                chk = true;
                break;
            }
        }
        if(!chk) {
            cout << "NO" << endl;
            return 0;
        }
    }

    cout << "YES" << endl;
    return 0;
}