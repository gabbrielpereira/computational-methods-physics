#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int i = 0, j=0, k=0, n=0;
    double random;
    double t = 0.0;
    double dt = 0.01;
    double T = 150.0;
    int Nx = 10, Ny = 10;
    int N = Nx*Ny;
    double Lx = 10.0, Ly = 10.0;
    double dx = Lx/Nx, dy = Ly/Ny;
    double x[N] = {};
    double vx[N] = {};
    double Fx[N] = {};
    double ax[N] = {};
    double y[N] = {};
    double vy[N] = {};
    double Fy[N] = {};
    double ay[N] = {};
    double Ep[N] = {};
    double rx = 0.0;
    double ry = 0.0;
    double U = 0.0;
    double F = 0.0;
    double r = 0.0;
    double m = 1.0;

    for(i=0; i<Nx; i++){
        for(j=0;j<Ny; j++){
            n = Nx*j + i;
           random = (double)rand()/RAND_MAX - 0.5;
            x[n] =  -Lx/2 + (i+0.5)*dx + (random)*0.1*dx;
            random = (double)rand()/RAND_MAX - 0.5;
            y[n] =  -Ly/2 + (j+0.5)*dy + (random)*0.1*dy;

            printf("x = %lf      y = %lf      \n", x[n], y[n]);
        }
    }

    fflush(stdin);
    FILE *fp;
    fp = fopen("dmol_25N_r.txt","w+");
    if(fp==NULL){
      printf("Impossivel abrir arquivo");
      return 1;
    }

    while(t<T){
        fprintf(fp,"%f  ",t);
        for(i=0; i<N; i++){
        Ep[i] = 0;
        ax[i] = 0;
        ay[i] = 0;
        for(j=0;j<N ; j++){
            if (i!=j){
                rx = x[i] - x[j];
                ry = y[i] - y[j];
                if(rx > Lx/2){
                    rx -= Lx;
                }
                if(ry > Ly/2){
                    ry -= Ly;
                }
                if(rx < -Lx/2){
                    rx += Lx;
                }
                if(ry < -Ly/2){
                    ry += Ly;
                }
                r = rx*rx + ry*ry;
                F = 24*(2/(r*r*r*r*r*r) - 1/(r*r*r))/r;
                U = 4*(1/(r*r*r*r*r*r) - 1/(r*r*r));
                Ep[i] += U;
                ax[i] += (F*rx)/r;
                ay[i] += (F*ry)/r;
                }
                }
         }
         for(k=0;k<N;k++){
            vx[k] = vx[k] + ax[k]*dt;
            x[k] = x[k] + vx[k]*dt;
            if (x[k] > Lx/2){
                x[k] = x[k] - Lx;
            }
            if (x[k] < -Lx/2){
                x[k] = x[k] + Lx;
            }

            vy[k] = vy[k] + ay[k]*dt;
            y[k] = y[k] + vy[k]*dt;
            if (y[k] > Ly/2){
                y[k] = y[k] - Ly;
            }
            if (y[k] < -Ly/2){
                y[k] = y[k] + Ly;
            }


            //v2[k] = vx[k]*vx[k] + vy[k]*vy[k];

            fprintf(fp,"%f %f     ",x[k], y[k]);

            }
    fprintf(fp,"\n");
    t = t +dt;
    }
    fclose(fp);
    return 0;
}

