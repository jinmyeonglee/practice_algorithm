#include <stdio.h>
#include <string.h>

int Map[501][501];
int dp[501][501];
int dx[] = {1, 0, 0, -1};
int dy[] = {0, 1, -1, 0};
int n;

int dfs(int y, int x) {
  int max = 0;
  if(dp[y][x] != -1) {
    return dp[y][x];
  }

  for(int i = 0; i < 4; i++) {
    int ny = y + dy[i];
    int nx = x + dx[i];
    if(ny >= 0 && ny < n && nx >= 0 && nx < n && Map[y][x] < Map[ny][nx]) {
      dp[y][x] = 0;
      int temp = dfs(ny, nx);
      if(temp > max) max = temp;
    }
  }
  dp[y][x] = max + 1;
  return max + 1;
}

int main(void) {
  int max = 0;
  scanf("%d", &n);

  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      dp[i][j] = -1;
      scanf("%d", &Map[i][j]);
    }
  }

  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      dfs(i, j);
    }
  }

  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      if(max < dp[i][j]) max = dp[i][j];
    }
  }

  printf("%d\n", max);

  return 0;
}
