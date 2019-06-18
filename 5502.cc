#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main(void) {
    int LCS[2][5001];
    int length;
    string s, cmp;
    scanf("%d", &length);
    cin >> s;
    cmp = s;
    reverse(cmp.begin(), cmp.end());

    for(int i = 1; i <= length; i++) {
        for(int j = 1; j <= length; j++) {
            if(s[i-1] == cmp[j-1]) {
                LCS[1][j] = LCS[0][j-1] + 1;
            }
            else {
                LCS[1][j] = max(LCS[1][j-1], LCS[0][j]);
            }
        }
        for(int j = 0; j<= length; j++) {
            LCS[0][j] = LCS[1][j];
        }
    }
    printf("%d\n", length - LCS[0][length]);

    return 0;
}
