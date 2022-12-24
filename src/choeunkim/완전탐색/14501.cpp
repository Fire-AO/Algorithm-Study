#define _CRT_NO_SECURE_WARNINGS
#include <iostream>
#include <algorithm>
using namespace std;

#define MAX 16

int N; // 퇴사일
int consult[MAX] = { 0, }; // 걸리는 상담일수
int money[MAX] = { 0, }; // 상담 후 받는 돈
int total_money = 0; // 돈의 총합

void solve(int day, int cost) { // 날짜와 총액
	if (day >= N + 1) {
		total_money = max(total_money, cost);
		return;
	}
	if (day + consult[day] <= N + 1) { // 그날 상담 후 상담하는데 걸리는 시간만큼 추가한 경우
		solve(day + consult[day], cost + money[day]);
	}
	if (day + 1 <= N + 1) { // 그날 상담 안하고 다음날로 넘어간 경우
		solve(day + 1, cost);
	}
}
int main() {
	cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> consult[i] >> money[i];
	}
	solve(1,0);
	cout << total_money << endl;
	return 0;

}
