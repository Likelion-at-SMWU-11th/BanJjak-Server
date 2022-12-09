#include <iostream>
using namespace std;
class CDummy
{
public:
    static int n;
    int m;
    CDummy() { n++; };
    ~CDummy() { n--; };
    static int getN() { return n; } // return n + m; -> 불가능, m 호출 불가
    int getM() { return m; }
};

int CDummy::n = 0;
int main()
{
    // CDummy::getM(); ->호출 불가
    CDummy::getN(); //호출 가능
    CDummy a;
    CDummy b[5];
    CDummy *c = new CDummy;
    cout << a.n << endl;
    delete c;
    cout << CDummy::n << endl;
    cout << sizeof(a) << endl;
    return 0;
}