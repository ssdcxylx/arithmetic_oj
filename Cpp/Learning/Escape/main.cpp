/**
 * 分治算法
 */
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;

int main()
{
    float s,a,b,c,c0,c1,t1,t2,t3,t4;
    scanf("%f %f %f",&s,&a,&b);
    c0=0,c1=s;
    do
    {
        c=(c0+c1)/2.0;
        t3=c/b;
        t1=t3+(s-c)/a;
        t4=(c-t3*a)/(a+b);
        t2=t3+t4+((s-(t3+t4)*a)/b);
        if(t1<t2)
            c1=c;
        else
            c0=c;
    } while (fabs(t1-t2)>1e-4);
    printf("%4.2f", t1);
    return 0;
}