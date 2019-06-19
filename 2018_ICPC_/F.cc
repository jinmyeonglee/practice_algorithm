#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long int lld;
int arr[5003];
vector<pair<int ,pair<int, int> > >v;
int w,n;
bool chk(int i,int j){
    if(v[i].second.first==v[j].second.first) return false;
    if(v[i].second.first==v[j].second.second)return false;
    if(v[i].second.second==v[j].second.first)return false;
    if(v[i].second.second==v[j].second.second)return false;
    return true;
}
int main(){
    scanf("%d %d",&w,&n);
    for(int i = 0;i <n;i++){
        scanf("%d",&arr[i]);
    }
    sort(arr,arr+n);
    for(int i = 0;i<n;i++){
        for(int j = i+1;j<n;j++){
            v.push_back(make_pair(arr[i]+arr[j],make_pair(i,j)));
        }
    }

    sort(v.begin(),v.end());
    int st = 0, en = v.size()-1,flag = 0;
    while(st<en){
        if(v[st].first+v[en].first<w)st++;
        else if(v[st].first+v[en].first>w)en--;
        else if(v[st].first+v[en].first==w){
            int l = v[st].first, r = v[en].first;
            //printf("%d %d\n",l,r);
            int i,j;
            for(i = st;v[i].first==l;i++){
                for(j = en;v[j].first==r;j--){
                    if(chk(i,j)){
                        flag = 1;
                        break;
                    }
                }
                if(flag)break;
            }
            if(flag)break;
            st = i; en = j;
            flag = 0;
        }
    }
    if(flag) printf("YES\n");
    else printf("NO\n");
    return 0;
}
