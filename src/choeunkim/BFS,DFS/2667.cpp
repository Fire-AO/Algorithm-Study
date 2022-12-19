#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <stdio.h>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

#define X first
#define Y second
#define MAX_SIZE 25

int s; //지도 크기
int numHouse[MAX_SIZE*MAX_SIZE] = { 0, };
int number = 0;
int guide[MAX_SIZE][MAX_SIZE]; //지도
int house[MAX_SIZE][MAX_SIZE]; //집이 있는 곳
int dx[4] = { 1,0,-1,0 }; //행, 아래, 오른쪽, 위, 왼쪽 순서
int dy[4] = { 0,1,0,-1 }; //열

void BFS(int x, int y) {
	queue<pair<int, int>>Q; 
	house[x][y] = 1;
	Q.push(pair<int, int>(x, y));
	numHouse[number]++;
	while (!Q.empty()) {
		//현재 원소 꺼내기
		pair<int, int> cur = Q.front();
		Q.pop();
		//주변 확인
		for (int dir = 0; dir < 4; dir++) {
			int nx = cur.X + dx[dir];
			int ny = cur.Y + dy[dir];

			//지도를 벗어나지 않고
			if (0 <= nx && nx < s && 0 <= ny && ny < s) {
				//집이지만 방문하지 않았다면 방문으로 변환
				if (guide[nx][ny] == 1 && house[nx][ny]==0) {
					house[nx][ny] = 1;
					Q.push(pair<int, int>(nx, ny)); //큐에 추가
					numHouse[number]++; //단지의 가구수 추가
				}
			}
		}

	}

}
int main(void) {
	scanf("%d", &s); 
	for (int i = 0; i < s; i++) {
		for (int j = 0; j < s; j++) {
			scanf("%1d", &guide[i][j]);
		}
	}
	for (int i = 0; i < s; i++) {
		for (int j = 0; j < s; j++) {
			if (guide[i][j] == 1 && house[i][j] == 0) {
				number++;
				BFS(i, j); //BFS 탐색 -> 너비 우선 탐색
			}
		}
	}
	sort(numHouse + 1, numHouse + number + 1);
	printf("%d\n", number);
	for (int i = 1; i <= number; i++) {
		printf("%d\n", numHouse[i]);
	}
	return 0;
}
//#include <bits/stdc++.h> 헤더 인클루딩 타이핑 하지 않아도 됨, 용량 차이가 있음
//ios::sync_with_stdio(0); cpp의 iostream을 c의 stdio와 동기화, 실행 속도가 빨라짐


