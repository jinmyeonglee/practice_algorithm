#include <cstdio>
#include <utility>
#include <vector>
#include <set>

using namespace std;

int main(void) {
    int m, n;
    unsigned int matrix[1001][1001];
    int sum = 0;
    set<pair<int, int> > points;

    scanf("%d %d", &m, &n);

    for(int i = 0; i < m; i++) {
        unsigned int max = 0;
        int x, y;
        for(int j = 0; j < n; j++) {
            scanf("%d", &matrix[i][j]);
            if(matrix[i][j] > max) {
                max = matrix[i][j];
                y = i; x = j;
            }
            sum += matrix[i][j];
        }
        points.insert(pair<int, int>(y, x));
    }
    for(int j = 0; j < n; j++) {
        unsigned int max = 0;
        int x, y;
        for(int i = 0; i < m; i++) {
            if(matrix[i][j] > max) {
                max = matrix[i][j];
                y = i; x = j;
            }
        }
        points.insert(pair<int, int>(y, x));
    }
    for(auto i : points) {
        sum -= matrix[i.first][i.second];
    }

    printf("%d\n", sum);
    return 0;
}
