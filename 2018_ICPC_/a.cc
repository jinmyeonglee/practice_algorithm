#include<stdio.h>

#define ll long long int

ll pow(ll p, ll a){
    ll ans = 1;
    while(a){
        if(a%2)ans *=p;
        a/=2;
        p*=p;
    }
    return ans;
}

int main(void) {
    ll n;
    scanf("%lld",&n);
    ll cnt=1;
    for(ll i =2 ; i<=62 ; i++) {
        if(n >(i-1)+i*(pow(2,i)-1)){
            cnt++;
        }
        else
            break;

    }
    printf("%lld\n",cnt);
    return 0;
}
