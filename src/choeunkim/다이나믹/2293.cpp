#include <iostream>
#include <vector>
using namespace std;

//�Ʒ�ó�� �ذ��ϸ� �޸� �ʰ�
/*int n, k;
int coin[100];
int dp[1000000 + 1];*/

//dp[�ݾ�]=�ش�ݾ��� ������� ����� ��
//Ž������ ������ ��ġ���� ũ�ų� ���� k ���� �۰ų� ���� �ݾ��� ��������� ����� �� ����
//�ݾ�-Ž������ ������ ��ġ�� ���� �� �ִ� ����� ���� dp[�ݾ�]�� ���Ѵ�
int main() {
	ios_base::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);

	int n, k;
	cin >> n >> k;
	vector<int> coin(n + 1);
	vector<int> dp(k + 1, 0);
	for (int i = 0; i < n; i++) {
		cin >> coin[i];
	}

	dp[0] = 1;
	for (int i = 0; i < n; i++) {
		for (int j = coin[i]; j <= k; j++) {
			dp[j] += dp[j - coin[i]];
		}
	}
	cout << dp[k] << endl;
	return 0;
}