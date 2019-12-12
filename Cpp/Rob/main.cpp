/**
 * 分治算法
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

void run(int Q)
{
    int start=1;
    int end=21;
    int ans=22;
    int mid;
    int t;
    while(start<=end)
    {
        mid=(end-start)/2+start;
        int t=solve(mid);
        if(t==Q&&mid<ans)
            ans=mid;
        if(t>Q)
            end=mid-1;
        else if(t<Q)
            start=mid+1;    
        else
            end=mid-1; 
    }
    if(ans!=22)
        printf("%d\n", ans);
    else
        printf("No solution\n");
}

int main()
{
    int Q,i;
    scanf("%d", &Q);
    run(Q);

    return 0;
}