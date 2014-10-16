#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#define base (10000)
#define SIZE (1000100)

using namespace std;
typedef long long LL;

LL a;
LL b;
int x[20000];
int y[20000];
int z[20000];
vector<pair<LL,LL> > ans;

void Multiply(int *o,int *p,int *q) {
	z[0] = p[0] + q[0];
	memset(z, 0, sizeof(int)*(z[0]+10));
	for(int i=1; i<=p[0]; i++) {
		for(int j=1; j<=q[0]; j++) {
			z[i+j-1] += p[i]*q[j];
		}
	}
	for(int i=1; i<=z[0]; i++) {
		if(z[i]>=10) {
			z[i+1] += z[i] / base;
			z[i] %= base;
		}
	}
	while(z[0]>1 && z[z[0]]==0) --z[0];
	memcpy(o, z, sizeof(z));
}

void Solve1() {
	LL tmp = a;
	while(tmp) {
		x[++x[0]] = tmp % base;
		tmp /= base;
	}
	y[++y[0]] = 1;
	for(int i=1; i<=b; i++) {
		Multiply(y,y,x);
	}
	printf("%d",y[y[0]]);
	for(int i=y[0]-1; i>=1; i--) printf("%04d",y[i]);
	putchar('\n');
}

/*void Solve2() {
	LL tmp = a;
	for(LL i=2; i*i<=a; i++) {
		if(tmp%i==0) {
			LL cnt(0);
			while(tmp%i==0) {
				tmp /= i;
				cnt++;
			}
			cnt *= b;
			ans.push_back(make_pair(i,cnt));
			if(tmp==1) break;
		}
	}
	if(tmp!=1) ans.push_back(make_pair(tmp,b));
	for(int i=0; i<ans.size(); i++) {
		if(i!=0) putchar('*');
		printf("%lld",ans[i].first);
		if(ans[i].second!=1) printf("^%lld",ans[i].second);
	}
	putchar('\n');
}*/

int main() {

	scanf("%lld %lld",&a,&b);
	Solve1();


	return 0;
}
