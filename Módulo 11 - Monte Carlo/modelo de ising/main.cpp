#include <stdio.h>
#include <math.h>
#include <stdlib.h>


int main()
{
    int i = 0, j=0, k=0, n=0;
    int random;
    int randomg;
    int cont = 0;
    double t = 0.0;
    double dt = 0.01;
    double T = 100.0;
    int Nx = 30, Ny = 30;
    int N = Nx*Ny;
    int S[Nx][Ny] = {};
    double Lx = 10.0, Ly = 10.0;
    int Ei=0,Ef=0,dE=0, ED=0;
    int J=1, B=1, M=1;
    int proxv = 0, antv = 0;

    for(i=0; i<Nx; i++){
        for(j=0;j<Ny; j++){
            random = rand()%2;
            if (random == 0){
                random = -1;
            }
            S[i][j] =  random;
            //printf("%d \n",S[i][j]);
        }
    }
while(t<T){
    i = rand()%Nx;
    j = rand()%Ny;
    if (i==0 || j==0){

        S[i-1][j] = S[Nx-1][j];
        S[i][j-1] = S[i][Ny-1];
    }
    if (i==Nx-1 || j==Ny-1){

        S[i+1][j] = S[0][j];
        S[i][j+1] = S[i][0];
    }
    Ei = -J*S[i][j]*(S[i-1][j] + S[i+1][j] + S[i][j+1] + S[i][j-1]) - B*S[i][j];
    S[i][j] = -S[i][j];
    Ef = -J*S[i][j]*(S[i-1][j] + S[i+1][j] + S[i][j+1] + S[i][j-1]) - B*S[i][j];
    dE = Ef - Ei;
    if (dE <= 0){
        ED += - dE;
    }
    else{
        if (ED > dE){
            ED -= dE;
        }
        else{
            S[i][j] = -S[i][j];
        }
    }
//    printf("i=%d , j= %d, dE = %d  \n", i,j, dE);
//
    printf("Ed = %d \n", ED);
    t = t + dt;
}

        return 0;
}
