#include<iostream>
#include<ctime>
#include<set>

using namespace std;

void main() {

    int start = clock();
    long long n = 60085147514309;
    long long c = 2;
    set <int> list_simple;
    
    while (n > 1)
    {
        if (n % c != 0)
        {
            if (c > 2)
            {
                c += 2;
            }
            else
            {
                c = 3;
            }
            
        }
        else 
        {
            n = n / c;
            list_simple.insert(c);
        }
        
    }

    set <int> :: iterator it = list_simple.begin();
    for (int i = 1; it != list_simple.end(); i++, it++) {
        cout << *it << " ";
    }

    int t = (clock() - start);
    cout << "\n" << t << "\n";
	system("pause");
}