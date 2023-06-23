#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    double pi = 4*atan(1);
    int i = 0, j=0, k=0, n=0;
    double t = 0.0;
    double ta, te;
    double T = 200;
    double dt = 0.01;
    double r[3] = {-0.5, 1.0 ,0}; //POSIÇÃO DO ÁTOMO
    double v[3] = {1,0,1}; //VELOCIDADE DO ÁTOMO
    int N = 1;        //GROUND STATE
    double pa;
    double pr;    //PROB DE ABSORÇÃO E PMC
    double gamma = 0.5;
    double St;
    double Wt;
    double ka = 0.2;
    double ks = 0.1;
    //double ks[3]={};
    double B;
    double pe = gamma;
    int cont;
    double px,py,pz;
    double R;
    double Ei,Ef,dE;
    double ri[3];
    double rf[3];
    double vi[3];
    double vf[3];

    fflush(stdin);
    FILE *fpr;
    FILE *fpv;
    fpr = fopen("AMO_rmeu.txt","w+");
    fpv = fopen("AMO_vmeu.txt","w+");

     while (t<T){

        fprintf(fpr,"%f\t %f\t %f\t \n", r[0],r[1], r[2]);
        fprintf(fpv,"%f\t %f\t %f\t \n", v[0],v[1], v[2]);

        R = sqrt(r[0]*r[0]+r[1]*r[1]+r[2]*r[2]);
        pa = exp(-1/(R*R))*dt; //prob de absorção

        //printf("pa = %f \n", pa);
        pr = (float)rand()/RAND_MAX;
        if(pr<pa){
            for(i=0;i<3;i++){
                r[i] = r[i] + v[i]*dt;  //incremento na posição
            }
        }
        if(pr>pa){
            for(i=0;i<3;i++){ //velocidade inicial
                    vi[i] = v[i];
                    ri[i] = r[i];
               }
            Ei = (vi[0]*vi[0] + vi[1]*vi[1] + vi[2]*vi[2]) + (ri[0]*ri[0]+ri[1]*ri[1]+ri[2]*ri[2]); //energial inicial

            R = sqrt(ri[0]*ri[0]+ri[1]*ri[1]+ri[2]*ri[2]);

            px = sqrt(ri[0]*ri[0])/R;
            py = sqrt(ri[1]*ri[1])/R;
            pz = sqrt(ri[2]*ri[2])/R;


            pr = (float)rand()/RAND_MAX;   //sorteio do feixe de absorção
            if(pr>=0 & pr < px){      //absorve x+
                if(ri[0]<0){
                   vf[0] = vi[0] + ka;
                   vf[1] = vi[1];
                   vf[2] = vi[2];
                    }
                if(ri[0]>0){
                   vf[0] = vi[0] - ka;
                   vf[1] = vi[1];
                   vf[2] = vi[2];
                    }
            }
            if(pr>= px & pr < px+py){      //absorve x-
                if(ri[1]<0){
                   vf[0] = vi[0] + ka;
                   vf[1] = vi[1];
                   vf[2] = vi[2];
                }
                if(ri[1]>0){
                   vf[0] = vi[0] - ka;
                   vf[1] = vi[1];
                   vf[2] = vi[2];
                }
            }
            if(pr>= px+py & pr <= 1){      //absorve z+
                if(r[2]<0){
                   vf[2] = vi[2] + ka;
                   vf[0] = vi[0];
                   vf[1] = vi[1];
                }
                if(r[2]>0){
                   vf[2] = vi[2] - ka;
                   vf[0] = vi[0];
                   vf[1] = vi[1];
                }
            }
            for(i=0;i<3;i++){
                    rf[i] = ri[i] + vf[i]*dt;  //incremento na posição
               }
            Ef = (vf[0]*vf[0] + vf[1]*vf[1] + vf[2]*vf[2]) + (rf[0]*rf[0]+rf[1]*rf[1]+rf[2]*rf[2]); //energial final

            dE = Ef - Ei;

            if (dE>0){
                for(i=0;i<3;i++){ //descarta alteração
                    v[i] = vi[i];
                    r[i] = ri[i];
               }
            }
            if (dE<0){
                for(i=0;i<3;i++){ //assume alteração
                    v[i] = vf[i];
                    r[i] = rf[i];
               }
            }
        }
        t = t+dt;
        cont++;

        pr = (float)rand()/RAND_MAX;

        if (pr<pe){
            for(i=0;i<3;i++){
                r[i] = r[i] + v[i]*dt;  //incremento na posição
           }
        }
        if(pr>pe){
        for(i=0;i<3;i++){ //velocidade inicial
                vi[i] = v[i];
                ri[i] = r[i];
           }
        Ei = (vi[0]*vi[0] + vi[1]*vi[1] + vi[2]*vi[2]) + (ri[0]*ri[0]+ri[1]*ri[1]+ri[2]*ri[2]); //energial inicial

//        for(i=0;i<3;i++){
//            ks[i] = (2*((float)rand()/RAND_MAX) - 1.0); //sorteio do vetor de onda de emissão
//            vf[i] = vi[i] + ks[i]/10.0;
//        }
        pr = rand()&6; //sorteio do vetor de onda de emissão

        //printf("ks = %f \t", ks[i]);
        if (pr == 0){
        if(vf[0]<0){
            vf[0] = vi[0] + ks;
            vf[1] = vi[1];
            vf[2] = vf[2];
            }
        if (vf[0]>0){
            vf[0] = vi[0] - ks;
            vf[1] = vi[1];
            vf[2] = vf[2];
        }
        }
        if (pr == 1){
        if(vf[1]<0){
            vf[1] = vi[1] + ks;
            vf[0] = vi[0];
            vf[2] = vf[2];
            }
        if (vf[1]>0){
            vf[1] = vi[1] - ks;
            vf[0] = vi[0];
            vf[2] = vf[2];
        }
        }
        if (pr == 2){
        if(vf[2]<0){
            vf[2] = vi[2] + ks;
            vf[1] = vi[1];
            vf[0] = vf[0];
            }
        if (vf[2]>0){
            vf[2] = vi[2] - ks;
            vf[1] = vi[1];
            vf[0] = vf[0];
        }
        }
        if (pr == 3){
        if(vf[0]>0){
            vf[0] = vi[0] + ks;
            vf[1] = vi[1];
            vf[2] = vf[2];
            }
        if (vf[0]<0){
            vf[0] = vi[0] - ks;
            vf[1] = vi[1];
            vf[2] = vf[2];
        }
        }
        if (pr == 4){
        if(vf[1]>0){
            vf[1] = vi[1] + ks;
            vf[0] = vi[0];
            vf[2] = vf[2];
            }
        if (vf[1]<0){
            vf[1] = vi[1] - ks;
            vf[0] = vi[0];
            vf[2] = vf[2];
        }
        }
        if (pr == 5){
        if(vf[2]>0){
            vf[2] = vi[2] + ks;
            vf[1] = vi[1];
            vf[0] = vf[0];
            }
        if (vf[2]<0){
            vf[2] = vi[2] - ks;
            vf[1] = vi[1];
            vf[0] = vf[0];
        }
        }
        for(i=0;i<3;i++){
                    rf[i] = ri[i] + vf[i]*dt;  //incremento na posição
               }

        Ef = (vf[0]*vf[0] + vf[1]*vf[1] + vf[2]*vf[2]) + (rf[0]*rf[0]+rf[1]*rf[1]+rf[2]*rf[2]); //energial final

        dE = Ef - Ei;

        if (dE>0){
            for(i=0;i<3;i++){ //descarta alteração
                v[i] = vi[i];
                r[i] = ri[i];
           }
        }
        if (dE<0){
            for(i=0;i<3;i++){ //assume alteração
                v[i] = vf[i];
                r[i] = rf[i];
           }
        }
        }
        t = t + dt;
        cont++;
    }

    fclose(fpr);
    fclose(fpv);
    return 0;
}


            //printf("\n");
       // if (cont%200 == 0){

      //  }
//        printf("Wt = %f \t", Wt);
//        printf("ta = %f\t", ta);
//        printf("te = %f \t", te);
//        printf("t = %f\n",t);
   // cont++;
