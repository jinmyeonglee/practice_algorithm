#include <cstdio>
#include <algorithm>

#define DOWN 'D'
#define SIDE 'S'
#define DIOG 'G'

int main(void) {
    int T, C, D, d;
    scanf("%d", &T);
    for(int t = 0; t < T; t++) {
        int A[101];
        int B[101];
        int dp[101][101];
        char bt[101][101];
        scanf("%d %d %d", &C, &D, &d);
        int n_A = 0;
        while(true) {
            int temp;
            scanf("%d", &temp);
            if(temp == 0) {
                break;
            }
            else {
                A[n_A++] = temp;
            }
        }
        int n_B = 0;
        while(true) {
            int temp;
            scanf("%d", &temp);
            if(temp == 0) {
                break;
            }
            else {
                B[n_B++] = temp;
            }
        }
        for(int i = 1; i <= (n_B > n_A ? n_B : n_A); i++) {
            dp[0][i] = dp[i][0] = /*C * i*/ D + i * d;
            bt[0][i] = SIDE;
            bt[i][0] = DOWN;
        }
        int y, x;
        y = x = 0;
        for(int i = 1; i <= (n_B > n_A ? n_B : n_A); i++) {
            for(int j = 1; j <= (n_B > n_A ? n_B : n_A); j++) {
                int cost[3]; // DIOG UP SIDE
                if(A[j-1] == B[i-1] && A[j-1] != 0 && B[i-1] != 0) {
                    cost[0] = dp[i-1][j-1] + C;
                }
                else {
                    if(A[j-1] != 0 && B[i-1] != 0) {
                        cost[0] = dp[i-1][j-1] + 2 * C;
                    }
                    else {
                        cost[0] = dp[i-1][j-1] + C;
                    }
                }
                if(A[j-1] == 0) {
                    printf("end A\n");
                    cost[0] = dp[i][j-1] + (bt[i][j-1] == SIDE ? d : D + d) + C;
                }
                if(B[i-1] == 0) {
                    printf("end b\n");
                    cost[0] = dp[i-1][j] + (bt[i-1][j] == DOWN ? d : D + d) + C;
                }
                cost[1] = dp[i-1][j] + (bt[i-1][j] == DOWN ? d : D + d);
                cost[2] = dp[i][j-1] + (bt[i][j-1] == SIDE ? d : D + d);

                int index = 0;
                int min = cost[0];
                for(int k = 1; k < 3; k++) {
                    if(cost[k] < min) {
                        min = cost[k]; index = k;
                    }
                }
                dp[i][j] = min;
                if(index == 0) bt[i][j] = DIOG;
                else if(index == 1) bt[i][j] = DOWN;
                else bt[i][j] = SIDE;
                if(A[j-1] == 0) bt[i][j] = SIDE;
                if(B[i-1] == 0) bt[i][j] = DOWN;
            }
        }

        for(int i = 0; i <= (n_B > n_A ? n_B : n_A); i++) {
            for(int j = 0; j <= (n_B > n_A ? n_B : n_A); j++) {
                printf("%d ", dp[i][j]);
            }
            printf("\n");
        }
        printf("\n");
        printf("\n");
        for(int i = 0; i <= (n_B > n_A ? n_B : n_A); i++) {
            for(int j = 0; j <= (n_B > n_A ? n_B : n_A); j++) {
                printf("%c ", bt[i][j]);
            }
            printf("\n");
        }
        printf("%d\n", dp[(n_B > n_A ? n_B : n_A)][(n_B > n_A ? n_B : n_A)]);

    }
    return 0;
}
