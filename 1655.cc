#include <cstdio>
#include <vector>
#include <queue>

using namespace std;

priority_queue< int, vector<int>, greater<int> > minh;
priority_queue< int, vector<int>, less<int> > maxh;
int n_max = 0;
int n_min = 0;

int main(void) {
    int median;
    int N;
    scanf("%d", &N);
    scanf("%d", &median);
    printf("%d\n", median);
    maxh.push(median);
    n_max++;

    for(int i = 0; i < N - 1; i++) {
        int num;
        scanf("%d", &num);
        if(num <= median) {
            maxh.push(num);
            n_max++;
        }
        else {
            minh.push(num);
            n_min++;
        }
        if(n_max > n_min + 1) {
            int temp = maxh.top();
            maxh.pop();
            minh.push(temp);
            median = maxh.top();
            n_max--;
            n_min++;
        }
        else if(n_min > n_max) {
            median = minh.top();
            minh.pop();
            maxh.push(median);
            n_max++;
            n_min--;
        }
        printf("%d\n", median);
    }

    return 0;
}