#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {
    string s, cmp;
    int total_l = 0;
    int length;
    int cnt = 0;
    cin >> s;
    cmp = s;
    length = s.length();
    reverse(cmp.begin(), cmp.end());

    for(int i = 0; i < length; i++) {
        for(int j = 0; j < length; j++) {
            if(i < length - 1 && j < length - 1 && s[i] == cmp[j]
               && s[i+1] == cmp[j+1]) {
                cnt++;
                while(i < length && j < length && s[i] == cmp[j]) {
                    printf("s%c %d c%c %d: %d\n", s[i], i, cmp[j], j, total_l);
                    total_l++;
                    j++;
                    i++;
                }
            }
        }
    }

    printf("%d %d %d\n", length - total_l + cnt, total_l, cnt);
    return 0;
}
