#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
class Number {
    private:
        string n;
        int k;
        // int getNum();
        
    public:
        Number(int n);
        void changeNum(int k);   
        string getN();
        void setNum(string n);
        void setNum(int n);
        int getNum();
};

class Converter {
    public:
        static string reverse(string str);
};

string Converter::reverse(string str) {
    string ret = "";
    for (int i = str.length() - 1; i >= 0; i--) {
        ret += str[i];
    }
    return ret;
}

Number::Number(int n) {
    this->k = 10;
    setNum(n);
}

void Number::setNum(int n) {
    this->n = "";
    for (int m = n; m > 0; m = m / 10) {
        this->n = (char)('0' + (m % 10)) + this->n;
    }
}


void Number::setNum(string n) {
    this->n = n;
}


int Number::getNum() {
    int i = 1;
    int num = 0;
    for (int m = n.length() - 1; m >= 0; m--) {
        num += (n[m] - '0') * i;
        i = i * k;
    }
    return num;
}

void Number::changeNum(int k) {
    int dec = getNum();
    this->k = k;
    this->n = "";

    for (int m = dec; m > 0; m = m / k) {
        this->n = (char)('0' + (m % k)) + this->n;
    }
}

string Number::getN() {
    return n;
}


int main() {

    Number mynum(125);
    cout << mynum.getN() << endl;
    
    mynum.changeNum(3);
    cout << mynum.getN() << endl;

    mynum.setNum(Converter::reverse(mynum.getN()));
    // cout << Converter::reverse(mynum.getN()) << endl;       // static은 굳이 object가 필요 없어서 :: 사용
    cout << mynum.getN() << endl;

    mynum.changeNum(10);

    cout << mynum.getN() << endl;
    // mynum.changeNum(10);

    cout << mynum.getNum() << endl;
   
    return 0;

}