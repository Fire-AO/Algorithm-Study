#include <iostream>
using namespace std;

#define MAX 100001

/* �������� ����ؾ��ϹǷ�
1. ������ �ƴҶ� (i-1�� ����), dp[i] ���� (�ڱ��ڽ�)
2. ������ �� (i-1�� ����), dp[i-1]+val[i} ���� (�� ���� ���ӵ� ���� �ڱ� �ڽ� ���� ���� �� Ŭ ��)*/
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