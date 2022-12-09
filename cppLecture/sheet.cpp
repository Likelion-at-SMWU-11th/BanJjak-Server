#include <iostream>
#include <vector>

using namespace std;

vector<int> solution(int num, int total)
{
    vector<int> answer;

    if (!num % 2)
    {
        num + 1;
    }

    int k = total / num;
    int div = num / 2;
    int start = k - div;
    for (int i = 0; i < num; i++)
    {
        answer.push_back(start + i);
    }

    return answer;
}
