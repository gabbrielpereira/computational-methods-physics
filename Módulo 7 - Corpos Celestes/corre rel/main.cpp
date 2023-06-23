#include <stdio.h>
#include <math.h>

int main()
{
   double pi = 4*atan(1);
    int N = 6;
    float T = 2;
    float dt = 0.0001;
    float m[] = {99.86604, 0.00002, 0.00024 ,0.00030, 0.00003, 0.09532};
    //, 0.09532};
    float vx[]= {0,0,0,0,0,0};
    float x[]= {0, 0.38, 0.72, 1.00, 1.52, 5.21};
    //, 5.21};
    float Fx[] = {0,0,0,0,0,0};
    float ax[] = {0,0,0,0,0,0};
    float vy[] = {0,0,0,0,0,0};
    float y[] = {0,0,0,0,0,0};
    float ay[] = {0,0,0,0,0,0};
    float Fy[] = {0,0,0,0,0,0};
    float R[] = {0,0,0,0,0,0};
    float v2[] = {0,0,0,0,0,0};
    float E[] = {0,0,0,0,0,0};
    float Ep[] = {0,0,0,0,0,0};
    float L[] = {0,0,0,0,0,0};
    float Rmax[] = {0,0,0,0,0,0};
    float Rmin[] = {0,0,0,0,0,0};
    float Rmed[] = {0,0,0,0,0,0};
    float omega[] = {0,0,0,0,0,0};
    float teta[] = {0,0,0,0,0,0};
    float Per[] = {0,0,0,0,0,0};
    float K[] = {0,0,0,0,0,0};
    float a[] = {0,0,0,0,0,0};
    float b[] = {0,0,0,0,0,0};
    float c[] = {0,0,0,0,0,0};
    float G = 4*pi*pi;
    float t = 0;
    float d = 0;
    float F = 0;
    float U = 0;
    float A = 0;
    float Et = 0.0;
    float Lt = 0.0;
    int i=0, j=0, k=0;
    int resp = 0;
    float vxcm = 0.0;
    float vycm = 0.0;

for(i=1; i<N; i++){
    vy[i] = sqrt((G)*m[0]/x[i]);
}

    fflush(stdin);
    FILE *fpx;
    FILE *fpy;
    fpx = fopen("rel_x.txt","w+");
    fpy = fopen("rel_y.txt","w+");
    //fprintf(fp,"Tempo\t\t\t Sol\t\t P1\t\t\t P2\t\t\t P3\t\t P4\t\t P5\n");

while (t<T){

        for(i=0; i<N; i++){
                    Ep[i] = 0;
                    ax[i] = 0;
                    ay[i] = 0;
            for(j=0;j<N ; j++){
                if (i!=j){
                    d = sqrt((x[i]-x[j])*(x[i]-x[j]) + (y[i] - y[j])*(y[i] - y[j]));
                    //F = -((G*m[j]*m[i])/(d*d));
                    F = -((G*m[j]*m[i])/(d*d))*(1.0+0.001/(d*d));
                    U = - (G*m[j]*m[i])/d;
                    Ep[i] += U;
                    ax[i] += (F*(x[i] - x[j]))/(d*m[i]);
                    ay[i] += (F*(y[i] - y[j]))/(d*m[i]);
                }
            }
        }
        for(k=0; k<N ; k++){

            vx[k] = vx[k] + ax[k]*dt;
            x[k] = x[k] + vx[k]*dt;

            vy[k] = vy[k] + ay[k]*dt;
            y[k] = y[k] + vy[k]*dt;
            v2[k] = vx[k]*vx[k] + vy[k]*vy[k];

            E[k] = m[k]*v2[k]/2 + Ep[k];
            L[k] = x[k]*m[k]*vy[k] - y[k]*vx[k]*m[k];

            Et += E[k];
            Lt += L[k];

            }
            Et = 0.0;
            Lt = 0.0;
            vxcm = (vx[0]*m[0]+vx[1]*m[1]+vx[2]*m[2])/(m[0]+m[1]+m[2]);
            vycm = (vy[0]*m[0]+vy[1]*m[1]+vy[2]*m[2])/(m[0]+m[1]+m[2]);

    for(i=0;i<N;i++){
        fprintf(fpx,"%f ", x[i]-vxcm*t);
        fprintf(fpy,"%f ", y[i]-vycm*t);
        }
    fprintf(fpx,"\n ");
    fprintf(fpy,"\n ");
    t = t + dt;
    }
fclose(fpx);
fclose(fpy);
return 0;
}
