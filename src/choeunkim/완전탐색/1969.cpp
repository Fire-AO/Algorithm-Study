#define _CRT_NO_SECURE_WARNINGS
#include <iostream>
#include <algorithm>
using namespace std;

#define MAX 1001

int N; // DNA의 수
int M; // 문자열의 길이
string DNA[MAX];
int result=0;
string res;

int main() {
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> DNA[i];
	}

	for (int i = 0; i < M; i++) {
		int dnaCount[4] = { 0, };
		for (int j = 0; j < N; j++) {
			switch (DNA[j][i]) {
			case 'A':
				dnaCount[0]++;
				break;
			case 'C':
				dnaCount[1]++;
				break;
			case 'G':
				dnaCount[2]++;
				break;
			case'T':
				dnaCount[3]++;
				break;
			}
		}

		int max = 0;
		// 가장 많이 등장한 ACGT 값
		for (int k = 0; k < 4; k++) {
			if (max < dnaCount[k]) max = dnaCount[k];
		}
		// 열별로 계산 (for loop 안에 있음)
		result += (N - max);

		// 알파벳 순서로 비교 후 스트링에 저장
		if (dnaCount[0] == max) {
			res += 'A';
			continue;
		}
		if (dnaCount[1] == max) {
			res += 'C';
			continue;
		}
		if (dnaCount[2] == max) {
			res += 'G';
			continue;
		}
		if (dnaCount[3] == max) {
			res += 'T';
			continue;
		}

		
		
	}
	cout << res << endl;
	cout << result;
	
	return 0;
}
