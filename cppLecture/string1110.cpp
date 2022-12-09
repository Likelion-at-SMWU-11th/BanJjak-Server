#include <iostream>
#include <string>

using namespace std;

class MyString {
protected:
    char *pstr; //char 포인터
    void initPstr();
public:
    MyString();
    ~MyString();
    int length();
    //char* getPstr(); -> operator overroading
    void setString(const char* t);
    friend ostream& operator<<(ostream &a, const MyString &b); //ouptut stream
};

class FiveString : public MyString{ //문제를 풀기 위한 별도의 class -> 상속 받기
public:
    FiveString();
    bool solve();
};

FiveString::FiveString(){
    cout<<"FiveString::FiveString()"<<endl;
}

bool FiveString::solve(){
    // int len = string::length();
    // if(len == 4 || len == 6){
    //     for(int i = 0; i < len-1 ; i++){
    //         if((*this)[i] < '0' || (*this)[i] > '9')
    //             return false;
    //     }
    // }
    // else 
    //     return false;
    // return true;
}

MyString::MyString(){
    cout<<"MyString::MyString()"<<endl;
    pstr = NULL;
    initPstr();
}

MyString::~MyString(){
    cout<<"MyString::~MyString()"<<endl;
    if(pstr != NULL)
        delete [] pstr; //메모리 전체 삭제
}

void MyString::initPstr(){
    pstr = new char[10]; //길이가 8이하인 문자열
}

int MyString::length(){
    int i;
    for(i = 0; i < 10; i++){
        if(pstr[i] == '\0')
            break;
    }
    return i;
}

// char* MyString::getPstr(){
//     return pstr;
// }

void MyString::setString(const char* t){
    for(int i = 0; i < 10; i++){
        pstr[i] = t[i]; //한글자씩 복사
        if(t[i] == '\0')
            break;
    }
}

ostream& operator<<(ostream &a, const MyString &b){ 
    //member가 아님 -> MyString:: 없음
    a << b.pstr;
    return a;
}

int main(){
    FiveString my;
    //cout << my.length() << " : " << my << " : " << my.solve()<< endl;
    return 0;
}