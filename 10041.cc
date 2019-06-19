#include <iostream>
#include <vector>
#include <utility>
#include <cstdlib>

using namespace std;

int main() {
    int w, h, n;
    vector< pair<int, int> > v;

    cin >> w >> h >> n;
    for(int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        v.emplace_back(pair<int, int>(a, b));
    }

    int ans = 0;
    for(int i = 1; i < v.size(); i++) {
        if((v[i].first < v[i - 1].first && v[i].second < v[i - 1].second)
        || (v[i].first > v[i - 1].first && v[i].second > v[i - 1].second)) {
            ans += max(abs(v[i].first - v[i-1].first), abs(v[i].second - v[i-1].second));
        }
        else {
            ans += abs(v[i].first - v[i-1].first) + abs(v[i].second - v[i-1].second);
        }
    }
    cout << ans << endl;

    return 0;
}