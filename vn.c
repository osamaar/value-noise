#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define SZ (512+1)

static int** y;
static int** z;

static void save(const char* filename) {
    FILE* fp=fopen(filename,"w");
    for(int i=0; i<SZ; i++){
        for(int j=0; j<SZ; j++){
            fprintf(fp, "%d ", z[i][j]);
        }
        fprintf(fp, "\n");
    }
    fclose(fp);
}

static void del2d(int** arr) {
    for(int i=0; i<SZ; i++)
        free(*(arr+i));
    free(arr);
}

static inline void binterp(int i0, int j0, int t) {
    for(int i=i0; i<=i0+t; i++)
    for(int j=j0; j<=j0+t; j++) {
        int a=t*t;
        int b=y[  i0][  j0]*(t-j+j0)*(t-i+i0);
        int c=y[  i0][t+j0]*(  j-j0)*(t-i+i0);
        int d=y[t+i0][  j0]*(t-j+j0)*(  i-i0);
        int e=y[t+i0][t+j0]*(  j-j0)*(  i-i0);
        y[i][j]=(b+c+d+e)/a;
    }
}

static void octave(int a, int t) {
    for(int i=0; i<SZ-1; i+=t)
    for(int j=0; j<SZ-1; j+=t) {
        y[i  ][j  ]=rand()%a-a/2;
        y[i  ][j+t]=rand()%a-a/2;
        y[i+t][j  ]=rand()%a-a/2;
        y[i+t][j+t]=rand()%a-a/2;
    }
    for(int i=0; i<SZ-1; i+=t)
    for(int j=0; j<SZ-1; j+=t)
        binterp(i,j,t);
    for(int i=0; i<SZ; i++)
    for(int j=0; j<SZ; j++)
        z[i][j]+=y[i][j];
}

static int** new2d(void) {
    int** arr=(int**)malloc(SZ*sizeof(int*));
    for(int i=0; i<SZ; i++)
        *(arr+i)=(int*)malloc(SZ*sizeof(int));
    for(int i=0; i<SZ; i++)
    for(int j=0; j<SZ; j++)
        arr[i][j]=0;
    return arr;
}

static void generate(void) {
    srand(time(NULL));
    y=new2d();
    z=new2d();
    for(int a=1,t=2; t<=(SZ-1)/4; a*=2,t*=2)
        octave(a,t);
    del2d(y);
    save("land.dat");
    del2d(z);
}

int main(void) {
    generate();
    return 0;
}
