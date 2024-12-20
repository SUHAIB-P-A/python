#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'extraLongFactorials' function below.
 *
 * The function accepts INTEGER n as parameter.
 */
#define MAX 1000
void extraLongFactorials(int n)
{
    int result[MAX];
    int resultsize = 1;
    result[0] = 1;
    for (int x = 2; x <= n; x++)
    {
        /* code */
        int carry = 0;
        for (int i = 0; i < resultsize; i++)
        {
            /* code */
            int product = (result[i] * x) + carry;
            result[i] = product % 10;
            carry = product / 10;
        }
        while (carry)
        {
            /* code */
            result[resultsize] = carry % 10;
            carry /= 10;
            resultsize++;
        }
    }

    for (int i = resultsize - 1; i >= 0; i--)
    {
        /* code */
        cout << result[i];
    }
}

int main()
{
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    extraLongFactorials(n);

    return 0;
}

string ltrim(const string &str)
{
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace))));

    return s;
}

string rtrim(const string &str)
{
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end());

    return s;
}
