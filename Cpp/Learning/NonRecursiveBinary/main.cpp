/**
 * 非递归算法
 */
#include <iostream>
#include <cstdlib>
#define MAXN 10001
using namespace std;
int key, top, bot, mid, n, a[MAXN];

void half()
{
    top=1;
    bot=n;
    while(top<=bot){
       mid=(bot+top)/2;
       if(key==a[mid])
       {
           cout<<mid<<endl;
           exit(0);
       }
       else if(key<a[mid])
       {
           bot=mid-1;
       }
       else
       top=mid+1;
       cout<<-1<<endl;
    }
    cout<<-1<<endl;
}

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    cin>>n;
    for(int i=1;i<=n;++i)
        cin>>a[i];
    cin>>key;
    if(key<a[1]||key>a[n])
        cout<<-1<<endl;
    else
        half();
    return 0;
}
