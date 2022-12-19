#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <queue>
using namespace std;

#define MAX_ 100
#define X first
#define Y second

//단순하게 연결된 것을 찾는 문제이므로 DFS와 BFS 모두 사용 가능.
//컴퓨터끼리 연결이 된다면 양방향으로 연결된 것
//1,2 이 연결 됐다면 2,1도 연결해줘야 함

int board[MAX_][MAX_];
int vis[MAX_];
int result = -1; //1번 컴퓨터 제외  

void DFS(int n, int com) {
	vis[com] = 1; //감염 확인
	result++;
	for (int i = 1; i < n+1 ; i++) {
		if (vis[i] == 1) { // 이미 감염 확인 시
			continue;
		}
		if (board[com][i] == 0) { //연결 안됐을 때는 넘김
			continue;
		}
		DFS(n, i); //컴퓨터 개수는 똑같음, 감염된 컴퓨터가 변경
	}
} 

int main(void) {
	int n;
	int con;
	int a, b;
	scanf("%d", &n);
	scanf("%d", &con);
	for (int i = 0; i < con; i++) {
		scanf("%d %d", &a, &b);
		board[a][b] = 1; // 연결
		board[b][a] = 1;
	}
	DFS(n, 1);
	cout << result << endl;
	return 0;
}

