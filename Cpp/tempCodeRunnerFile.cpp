#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#define MAX 100001
using namespace std;
int n, m;
int money[MAX];

bool judge_group(int mid)
{
    int sum = 0;
    int group = 1;
    for(int i=1; i<=n; i++)
    {
        if(sum+money[i]<=mid)
            sum += money[i];
        else
        {
            sum=money[i];
            group++;
        }
    }
    if(group > m)
        return false;
    else
        return true;
}

int main()
{
    scanf("%d %d", &n, &m);
    int money[MAX];
    int low=0, high=0;
    for(int i=1; i<=n; i++)
    {
        scanf("%d", &money[i]);
        high += money[i];
        if(low<money[i])
            low=money[i];
    }
    int mid = (low + high)/2;   
    while(low < high)
    {
        if(!judge_group(mid))
            low=mid+1;
        else
            high=mid-1;
        mid = (low + high)/2;
    }
    cout<<mid<<endl;
    return 0;
}