/**
 * 数学方法
 */
#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;


int solve(int n)
{
    int ans=0;
    while(n>0)
    {
        ans+=n/5;
        n=n/5;
    }
    return ans;
}

int run(int Q)
{
    int N=4*Q/5*5;
    while(solve(N)<=Q)
    {
        if(solve(N)==Q)
            return N;
        N=N+5;
    }
    return -1;
}

int main()
{
    int Q;
    scanf("%d", &Q);
    int ans=run(Q);
    if(ans!=-1)
        printf("%d\n", ans);
    else
        printf("No Solution\n");
    return 0;
}