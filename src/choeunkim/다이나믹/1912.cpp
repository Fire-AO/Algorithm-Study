#include <iostream>
using namespace std;

#define MAX 100001

/* 연속합을 고려해야하므로
1. 연속이 아닐때 (i-1을 선택), dp[i] 선택 (자기자신)
2. 연속일 때 (i-1을 선택), dp[i-1]+val[i} 선택 (그 전의 연속된 값에 자기 자신 더한 것이 더 클 때)*/
int val[MAX];
int dp[MAX] = { 0, };

int main() {
	int N;
	cin >> N;
	
	for (int i = 0; i < N; i++) {
		cin >> val[i];
		dp[i] = val[i];
	}
	int MSum = dp[0];

	for (int i = 1; i < N; i++) {
		dp[i] = max(dp[i], dp[i - 1] + val[i]);
		if (dp[i] > MSum) {
			MSum = dp[i];
		}
	}
	cout << MSum << endl;
	return 0;
}