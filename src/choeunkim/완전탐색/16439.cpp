#define _CRT_NO_SECURE_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

#define MAX 31

int N; // 고리 회원의 수
int M; // 치킨 종류의 수
int prefer[MAX][MAX];
vector <int> chicken(3);
int answer = 0;

// 조합 계산이므로 30C3=4060 의 경우의 수
// 이 3개의 치킨을 N명 탐색해서 만족도가 최대가 되도록 해야한다
void combination(int count, int next) {
	if (count == 3) {
		int total = 0;
		for (int i = 1; i <= N; i++) {
			int max = 0;
			for (int chic : chicken) {
				if (max < prefer[i][chic]) {
					max = prefer[i][chic];
				}
			}
			total += max;
		}
		if (answer < total) {
			answer = total;
		}
		return;
	}
	for (int i = next; i <= M; i++) {
		chicken[count] = i;
		combination(count + 1, i + 1);
	}
	
}
int main() {
	cin >> N >> M;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= M; j++) {
			cin >> prefer[i][j];
		}
	}
	combination(0, 1);
	cout << answer << endl;
	return 0;
}