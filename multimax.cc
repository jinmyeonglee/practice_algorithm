#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int main(void) {
    int n;
    int arr[10001];
    int ans[6];
    scanf("%d", &n);

    for(int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    sort(arr, arr+n);

    ans[0] = (arr[n-1] * arr[n-2] * arr[n-3]);
    ans[1] = (arr[n-1] * arr[n-2]);
    ans[2] = (arr[0] * arr[1] * arr[2]);
    ans[3] = (arr[0] * arr[1]);
    ans[4] = arr[0] * arr[1] * arr[n-1];
    ans[5] = arr[0] * arr[n-2] * arr[n-1];


    printf("%d\n", *max_element(ans, ans + 6));

    return 0;
}
