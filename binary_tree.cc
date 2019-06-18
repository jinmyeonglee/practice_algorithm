#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int ans[1048578];
int arr[2097155];

int merge(int s, int e, int total_max) {
    int index;
    int max = 0;

    for(int i = s; i <= e; i++) {
        if(ans[i] > max) {
            max = ans[i];
            index = i;
        }
    }
    int distance = total_max - max;
    for(int i = s; i <= e; i++) {
        ans[i] += distance;
    }

    return distance;
}

int main() {
    int h, total_max;
    int sum = 0;
    total_max = 0;
    scanf("%d", &h);
    int num = pow(2, h+1) - 2;

    for(int i = 2; i < num + 2; i++) {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }
    int limit = pow(2, h);
    for(int i = 0; i < limit; i++) {
        int temp = limit + i;
        while(temp > 1) {
            ans[i] += arr[temp];
            temp /= 2;
        }
    }
    for(int i = 0; i < limit; i++) {
        if(ans[i] > total_max) total_max = ans[i];
    }
    limit /= 2;
    for(int i = 1; i <= h; i++) {
        int s = 0;
        int e = limit - 1;
        for(int j = 0; j < pow(2, i); j++) {
            sum += merge(s, e, total_max);
            s += limit;
            e += limit;
        }
        limit /= 2;
    }
    printf("%d\n", sum);
    return 0;
}
