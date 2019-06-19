#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <unordered_map>
#include <cstdlib>

using namespace std;


int main() {
    vector<string> v;
    unordered_map<char, pair<int, int> > hash;
    string arr[4] = {"ABCD", "EFGH", "IJKL", "MNO."};

    for(int i = 0; i < 4; i++) {
        string temp;
        cin >> temp;
        v.push_back(temp);
        for(int j = 0; j < 4; j++) {
            hash[arr[i][j]] = pair<int, int>(i, j);
        }
    }
    int ans = 0;

    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            if(v[i][j] == '.') continue;
            ans += abs(hash[v[i][j]].first - i) + abs(hash[v[i][j]].second - j);
        }
    }
    cout << ans << endl;

    return 0;
}