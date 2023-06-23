#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    double pi = 4*atan(1);
    int i = 0, j=0, k=0, n=0;
    double t = 0.0;
    double ta, te;
    double T = 2000;
    double dt = 0.01;
    double r[3] = {0.5,0.5,0.5}; //POSIÇÃO DO ÁTOMO
    double v[3] = {1,1,0}; //VELOCIDADE DO ÁTOMO
    int N = 1;        //GROUND STATE
    double pa, pr;    //PROB DE ABSORÇÃO E PMC
    double gamma = 100000.0;
    double St;
    double Wt;
    double ka = 0.0001;
    double ks[3]={};
    double B;
    double pe = gamma*dt;
    int cont;
    double px,py,pz;
    double R;

    fflush(stdin);
    FILE *fpr;
    FILE *fpv;
    fpr = fopen("AMO_rml.txt","w+");
    fpv = fopen("AMO_vml.txt","w+");

     while (t<T){
        pa = sqrt(r[0]*r[0]+r[1]*r[1]+r[2]*r[2])*dt;
                printf("pa = %f \n", pa);
        pr = (float)rand()/RAND_MAX;
        while (pr>pa){
            for(i=0;i<3;i++){
                r[i] = r[i] + v[i]*dt;  //incremento na posição
                t = t+dt;
                pr = (float)rand()/RAND_MAX;
           }
        }
        R = sqrt(r[0]*r[0]+r[1]*r[1]+r[2]*r[2]);
        px = sqrt(r[0]*r[0])/R;
        py = sqrt(r[1]*r[1])/R;
        pz = sqrt(r[2]*r[2])/R;
        pr = (float)rand()/RAND_MAX;   //sorteio do feixe de absorção
        if(pr>=0 & pr < px/2){      //absorve x+
           v[0] = v[0] + ka;
        }
        if(pr>= px/2 & pr < px){      //absorve x-
           v[0] = v[0] - ka;
        }
        if(pr>= px & pr < py/2){      //absorve y+
           v[1] = v[1] + ka;
        }
        if(pr>= py/2 & pr < py){      //absorve y+
           v[1] = v[1] - ka;
        }
        if(pr>= py & pr < pz/2){      //absorve z+
           v[2] = v[2] + ka;
        }
        if(pr>= pz/2 & pr <= 1){      //absorve z-
           v[2] = v[2] - ka;
        }
        for(i=0;i<3;i++){
                r[i] = r[i] + v[i]*dt;  //incremento na posição
                t = t+dt;
           }
        pr = (float)rand()/RAND_MAX;
        while (pr>pe){
            for(i=0;i<3;i++){
                r[i] = r[i] + v[i]*dt;  //incremento na posição
                t = t+dt;
                pr = (float)rand()/RAND_MAX;
           }
        }
        for(i=0;i<3;i++){
            ks[i] = (2*((float)rand()/RAND_MAX) - 1.0); //sorteio do vetor de onda de emissão
            //printf("ks = %f \t", ks[i]);
            v[i] = v[i] - ks[i]/1000;
           }
            //printf("\n");
        if (cont%200 == 0){
        fprintf(fpr,"%f\t %f\t %f\t \n", r[0],r[1], r[2]);
        fprintf(fpv,"%f\t %f\t %f\t \n", v[0],v[1], v[2]);
        }
//        printf("Wt = %f \t", Wt);
//        printf("ta = %f\t", ta);
//        printf("te = %f \t", te);
//        printf("t = %f\n",t);
    cont++;
    }

    fclose(fpr);
    fclose(fpv);
    return 0;
}
