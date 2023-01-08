#include <iostream>
#include <vector>
using namespace std;

//아래처럼 해결하면 메모리 초과
/*int n, k;
int coin[100];
int dp[1000000 + 1];*/

//dp[금액]=해당금액이 만들어질 경우의 수
//탐색중인 동전의 가치보다 크거나 같고 k 보다 작거나 같은 금액이 만들어지는 경우의 수 갱신
//금액-탐색중인 동전의 가치를 만들 수 있는 경우의 수를 dp[금액]에 더한다
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