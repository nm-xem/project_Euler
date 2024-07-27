#include<iostream>
#include<ctime>

using namespace std;

void main() {
    int start = clock();

    int sum_num = 0;

    for (int i = 1; i < 1000000000; i++) {
        if (((i % 3) == 0) || ((i % 5) == 0)){
            sum_num += i;
        }
    }
    cout << sum_num << "\n";
    int t = (clock() - start);
    cout << t << "\n";
	system("pause");
}