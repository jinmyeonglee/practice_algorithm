#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    string str;

    cin >> n;
    cin >> str;
    int n_l = 0;
    for(auto c: str) {
        if(c == 'L') {
            n_l++;
        }
    }
    cout << min(n, (n + 1) - (n_l / 2)) << endl;
    return 0;
}