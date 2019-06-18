#include <cstdio>
#include <vector>
#include <queue>

using namespace std;

int main(void) {
    int n, k;
    int arr[101];
    vector<queue <int> > port;
    scanf("%d %d", &n, &k);
    for(int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    for(int i = 0; i < n; i++) {
        queue<int> temp;
        port.push_back(temp);
    }
    bool check = false;
    for(int i = n - 1; i >= 0; i--) {
        for(int j = 0; j < k; j++) {
            if(port[j].empty() || port[j].back() > arr[i]) {
                port[j].push(arr[i]);
                check = true;
                break;
            }
        }
        if(check == false) {
            printf("NO\n");
            return 0;
        }
        check = false;
    }
    printf("YES\n");
    return 0;
}
