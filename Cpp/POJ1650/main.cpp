/**
 * 追赶法
 */
#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;


void run(double A, int L, int flag)
{
    
    double d=1,n=1;
    double ans_n,ans_d;
    double error=L;
    while(n<=L)
    {
        if(n/d>A)
        {
            if(n/d-A<error)
            {
                error=n/d-A;
                ans_n=n,ans_d=d;
            }
            d++;
        }
        else
        {
            if(A-n/d<error)
            {
                error=A-n/d;
                ans_n=n,ans_d=d;
            }
            n++;
        }
    }
    if(flag)
        printf("%0.f %0.f", ans_d, ans_n);
    else
        printf("%0.f %0.f", ans_n, ans_d);
}

int main()
{
    double A;
    int L;
    int flag=0;
    scanf("%lf %d", &A, &L);
    if(A<1)
    {
        A=1/A;
        flag=1;
    }
    run(A,L,flag);
    return 0;
}