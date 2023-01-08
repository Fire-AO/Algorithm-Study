#include <iostream>
using namespace std;
// 나와있는 피보나치 수열을 사용하면 시간 오류가 남
int dp[41]; // 마지막 인덱스까지 저장하기 위해

// 피보나치 수를 구하는 기본 함수를 활용하였다
// 이미 계산한 식은 넘어간다
int fibo(int n) {
	if (n == 0) {
		dp[0] = 0;
	}
	else if (n == 1) {
		dp[1] = 1;
	}
	else if (dp[n]== 0) {
		dp[n] = fibo(n - 1) + fibo(n - 2);
	}
	return dp[n];
}

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int T;
	cin >> T;

	fibo(40);

	int N;
	for (int i = 0; i < T; i++) {
		cin >> N;
		if (N == 0) {
			cout << "1 0" << '\n';
		}
		else {
			cout << dp[N - 1] << " " << dp[N] << '\n';
		}
	}
	return 0;
}