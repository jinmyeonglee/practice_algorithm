#include <cstdio>
#include <string>
#include <map>
#include <utility>
#include <vector>

using namespace std;

int main(void) {
    int T;
    scanf("%d", &T);

    for(int t = 0; t < T; t++) {
        int L;
        int cnt = 0;
        int num = 0;
        scanf("%d", &L);
        char A[52];
        char B[52];
        scanf("%s", A);
        scanf("%s", B);

        vector < map< char, int > > sto_A;
        vector < map< char, int > > sto_B;
        for(int i = 0; i < L; i++) {
            for(int j = i+1; j < L+1; j++) {
                map<char, int> com_A;
                map<char, int> com_B;
                for(int k = i; k < j; k++) {
                    auto it = com_A.find(A[k]);
                    if(it != com_A.end()) {
                        com_A[A[k]]++;
                    }
                    else {
                        com_A.insert(pair<char, int>(A[k], 1));
                    }
                }
                for(int k = i; k < j; k++) {
                    auto it = com_B.find(B[k]);
                    if(it != com_B.end()) {
                        com_B[B[k]]++;
                    }
                    else {
                        com_B.insert(pair<char, int>(B[k], 1));
                    }
                }
                sto_A.push_back(com_A);
                sto_B.push_back(com_B);
                num++;
            }

        }
        bool check = false;
        for(int it = 0; it < num; it++) {
            for(int jt = 0; jt < num; jt++) {
                if(sto_A[it] == sto_B[jt]) {
                    cnt++;
                    check = true;
                    break;
                }
            }
        }
        printf("Case #%d: %d\n", t+1, cnt);
    }
}
