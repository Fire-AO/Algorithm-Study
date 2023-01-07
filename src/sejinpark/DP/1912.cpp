#include "bits/stdc++.h"
using namespace std;
/**
 * DP가 어떻게 접근하냐에 따라서 난이도가 훅훅 왔다갔다 하는 것 같다.
 * D[i]=i번째 항을 마지막으로 사용하는 수열의 합 중 최댓값을 구하는 것으로 접근했다.
 */
int n;
int a[100005];
int d[100005];
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;
    for (int i = 1; i <= n; i++) cin >> a[i];
    d[1] = a[1];
    /**
     * k-1번째 항을 마지막으로 하는 수열의 합 중 최댓값이 0보다 크면 그 수열에 a[k]를 붙이게 했고
     * 0보다 작으면 a[k-1]을 쓰지 않고 a[k]민으로 수열을 만들게 했다.
     */
    for(int i = 2; i <= n; i++) d[i] = max(d[i-1], 0) + a[i];
    cout << *max_element(d+1, d+n+1); // max_element(d+1,d+n+1)은 d[1] to d[n]중에 최댓값의 주소를 반환하는 함수.
}