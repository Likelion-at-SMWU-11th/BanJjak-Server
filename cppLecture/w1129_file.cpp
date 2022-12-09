#include <vector>
#include <iostream>
#include <fstream>

using namespace std;

class Reading
{
    int hour;
    double temperature;

public:
    Reading(int, double);
};

int main()
{
    vector<Reading> temps;
    ifstream ist{"sample.txt"};
    int hour;
    double temperature;
    while (ist >> hour >> temperature) //읽을 수 있을 때까지 파일 읽기
    {
        if (hour < 0 || 23 < hour)
            cout << "hour out od range";
        cout << hour << ", " << temperature << endl;
        temps.push_back(Reading{hour, temperature}); //저장
    }

    return 0;
}