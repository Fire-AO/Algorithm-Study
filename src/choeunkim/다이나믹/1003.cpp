#include <iostream>
using namespace std;
// �����ִ� �Ǻ���ġ ������ ����ϸ� �ð� ������ ��
int dp[41]; // ������ �ε������� �����ϱ� ����

// �Ǻ���ġ ���� ���ϴ� �⺻ �Լ��� Ȱ���Ͽ���
// �̹� ����� ���� �Ѿ��
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