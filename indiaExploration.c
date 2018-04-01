#include<stdio.h>
#define MOD 1000000007
int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        unsigned long long int n, i = 0, sum = 1;
        scanf("%llu", &n);
        for(i = 1; i <= n; i++)
        {
            sum = sum << 1;
            sum = sum % MOD;
        }
        sum = sum - 2-2*n;      
        printf("%llu\n", sum % MOD); 
    }
    return 0;
}
