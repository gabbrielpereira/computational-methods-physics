#include <stdio.h>
#include <math.h>

int main()
{
    double pi = 4*atan(1);
    int N = 3;
    float T = 5;
    double dt = 0.0001;
    double m[] = {1.0, 1.0, 0.00000035};
    //, 0.00001};
    //, 0.09532};
    double vx[N]= {0.0,0.0, 10.0};
    double x[]= {1.0, 1.5, 1.25};
    //, 0};
    //, 5.21};
    double Fx[N]= {};
    double ax[N]= {};
    double vy[N]= {0.0,0.0,0.0};
    //,0};
    double y[N]= {0,0,-1.0};
    //,2};
    double ay[N]= {};
    double Fy[N]= {};
    float R[N]= {};
    float v2[N]= {};
    float E[N]= {};
    float Ep[N]= {};
    float L[N]= {};
    float Rmax[N]= {};
    float Rmin[N]= {};
    float Rmed[N]= {};
    float omega[N]= {};
    float teta[N]= {};
    float Per[N]= {};
    float K[N]= {};
    float a[N]= {};
    float b[N]= {};
    float c[N]= {};
    double G = 4*pi*pi;
    float t = 0;
    float d = 0;
    float F = 0;
    float U = 0;
    float A = 0;
    double vxcm=0.0;
    double vycm=0.0;
    float Et = 0.0;
    float Lt = 0.0;
    int i=0, j=0, k=0;
    int resp = 0;
    float C = 300000000;
    float alfa = 0.001;

for(i=1; i<N; i++){
    vy[i] = sqrt((G)*m[0]/x[i]);
}

    fflush(stdin);
    FILE *fpx;
    FILE *fpy;
    fpx = fopen("bi_x.txt","w+");
    fpy = fopen("bi_y.txt","w+");
    //fprintf(fp,"Tempo\t\t\t Sol\t\t P1\t\t\t P2\t\t\t P3\t\t P4\t\t P5\n");

while (t<T){

        for(i=0; i<N; i++){
                    Ep[i] = 0;
                    ax[i] = 0;
                    ay[i] = 0;
            for(j=0;j<N ; j++){
                if (i!=j){
                    d = sqrt((x[i]-x[j])*(x[i]-x[j]) + (y[i] - y[j])*(y[i] - y[j]));
                    F = -((G*m[j]*m[i])/(d*d));
                    //F = -((G*m[j]*m[i])/(d*d))*(1.0+0.03/(d*d));
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
