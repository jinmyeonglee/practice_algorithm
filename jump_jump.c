#include <stdio.h>

int n;
int nums[1001];
int dp[1001];
int dfs(int p) {
  int min = 1000000;
  if(dp[p] != 1000001) {
    return dp[p];
  }
  for(int i = p - 1; i <= p - nums[p]; i++) {
    if(i >= 0 && i < n) {
      dp[p] = 0;
      int temp = dfs(i);
      if(min > temp) min = temp;
    }
  }
  dp[p] = min + 1;
  return min + 1;
}

int main(void) {
  int ans;
  scanf("%d", &n);

  for(int i = 0; i < n; i++) {
    scanf("%d", &nums[i]);
    dp[i] = 1000001;
  }


  ans = dfs(n - 1);
  for(int i = 0; i < n; i++) {
    printf("%d ", dp[i]);
  }
  printf("%d\n", ans);
  return 0;
}
