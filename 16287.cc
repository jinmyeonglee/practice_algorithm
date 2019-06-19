#include <iostream>
#include <vector>

using namespace std;

int main() {
    int w, n;
    vector<int> v;

    cin >> w >> n;

    for(int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        v.push_back(tmp);
    }


    return 0;
}