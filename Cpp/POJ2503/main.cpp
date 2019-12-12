#define LOCAL 1

#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstring>
#include <cmath>
#define MAX 100001
using namespace std;
typedef struct
{
    char e[11];
    char g[11];
} Node;
Node dic[100001];
char str[21];
int pos;

bool cmp(Node a, Node b)
{
    return strcmp(a.g, b.g) < 0;
}

int BinSearch(char *s)
{
    int low = 0, high = pos - 1;
    int mid, t;
    while (low <= high)
    {
        mid = (low + high) / 2;
        t = strcmp(dic[mid].g, s);
        if (t == 0)
            return mid;
        else if (t > 0)
            high = mid - 1;
        else
            low = mid + 1;
    }
    return -1;
}

int main()
{
#ifdef LOCAL
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
#endif
    pos = 0;
    char z;
    while (scanf("%s%c", dic[pos].e, &z) != EOF)
    {
        if (z == '\n')
        {
            strcpy(str, dic[pos].e);
            break;
        }
        scanf("%s", dic[pos++].g);
    }
    ///排序
    sort(dic, dic + pos, cmp);
    int index = BinSearch(str);
    if (index >= 0)
        printf("%s\n", dic[index].e);
    else
        puts("eh");
    while (scanf("%s", str) != EOF)
    {
        index = BinSearch(str);
        if (index >= 0)
            printf("%s\n", dic[index].e);
        else
            puts("eh");
    }
    return 0;
}
