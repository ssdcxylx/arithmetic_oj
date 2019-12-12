// 递归二分算法
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#define Max 1001
using namespace std;
int a[Max],key;

int search(int bot, int top)
{
    int mid;
    if(top >= bot)
    {
        mid=(top+bot)/2;
        if(key==a[mid])
        {
            cout<<mid<<endl;
            return 0;
        }
        else if(key < a[mid])
            search(bot, mid-1);
        else
            search(mid+1, top);
    }
    else
    {
        printf("-1\n");
        return 0;
    }
}


int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int n;
    cin>>n;
    for(int i=1; i<=n; ++i)
        cin>>a[i];
    cin>>key;
    search(1, n);
    return 0;
}
