#include "headers.h"
int main(int args, char** argv) {
int x,i=3;
x=(++i,i++,i+10);
cout << x;
return 0;
}
