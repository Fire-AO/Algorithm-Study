#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <stdio.h>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;

#define X first
#define Y second
#define MAX_ 101

int board[MAX_][MAX_];
int result = 0;
int vis[MAX_][MAX_]; //방문확인

int N, M;

int dx[4] = { 1,0,-1,0 };
int dy[4] = { 0,1,0,-1 };

void BFS(int x, int y) {
	vis[x][y] = 1;
	queue<pair<int, int>>Q;
	Q.push(pair<int, int>(x, y));
	//Q.push({ x,y });

	while (!Q.empty()) {
		//현재 원소 꺼내기
		pair<int, int> cur = Q.front();
		Q.pop();
		//주변 확인
		for (int dir = 0; dir < 4; dir++) {
			int nx = cur.X + dx[dir];
			int ny = cur.Y + dy[dir];
			if ((0 <= nx && nx < N) && (0 <= ny && ny < M)) { //범위 안에서
				if (vis[nx][ny] == -1 && board[nx][ny] == 1) { //이동 가능 하지만 방문 처리 안되었을 때 방문으로 변경
					vis[nx][ny] = vis[cur.X][cur.Y] + 1; // 거리로 저장하는 의미를 아직 잘 모르겠음
					result++;// 이러면 그냥 1인 곳을 다 도는 것... 아직 방법 안떠오름, result 필요없음
					Q.push(make_pair(nx, ny));
				}
			}
		}
	}
}

int main(void) {
	cin >> N >> M; // n개의 줄, m개의 정수
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%1d", &board[i][j]);
			vis[i][j] = -1; //모든 길 -1로 고정
		}
	}
	BFS(0, 0);
	cout << vis[N - 1][M - 1] << endl;
	return 0;
}