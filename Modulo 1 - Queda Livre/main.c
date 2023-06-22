#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main()
{
    float y=100, t=0, v=0, g=9.8, e=0, dt=0.001;
    float vmeio = 0, ymeio=0, ameio=0;
    int resp=0;
    int b = 2;
    float a = -(1-v*v);

    printf("Método: 1(EulerCromer) , 2 (EulerRichardson), 3 (Solucao Exata)\n");
    scanf("%d", &resp);

    if(resp==1){
    fflush(stdin);
    FILE *fp;
    fp = fopen("vterminal_eulercromer_b2_0.001.txt","w+");
    if(fp==NULL){
      printf("Impossivel abrir arquivo");
      return 1;
    }
    while(t<20){

        v = v + a*dt;
        y = y + v*dt;
        e = 0.5*v*v + y;
        a = -(1-v*v);
        t = t+dt;

        //printf("%f",v);
        //printf("\n");

        fprintf(fp,"%f\t\t",t);
        fprintf(fp,"%f\t\t",y);
        fprintf(fp,"%f\t\t",v);
        fprintf(fp,"%f\n",e);

    }

    fclose(fp);
    }
    if(resp==2) {
    fflush(stdin);
        FILE *fp;
    fp = fopen("vterminal_eulerichardson_b2_0.001.txt","w+");
    if(fp==NULL){
      printf("Impossivel abrir arquivo");
      return 1;
    }

    while(t<20){


        vmeio = v + (a*dt)/2;
        ymeio = y + (v*dt)/2;
        ameio = -(1-vmeio*vmeio);


        v = v + ameio*dt;
        y = y + vmeio*dt;
        a = -(1-v*v);

        e = 0.5*v*v + y;

        t = t+dt;

        //printf("%f",v);
        //printf("\n");

        fprintf(fp,"%f\t\t",t);
        fprintf(fp,"%f\t\t",y);
        fprintf(fp,"%f\t\t",v);
        fprintf(fp,"%f\n",e);
    }

        fclose(fp);
    }
    else{
    fflush(stdin);
            FILE *fp;
    fp = fopen("vexata_b2_0.001.txt","w+");
    if(fp==NULL){
      printf("Impossivel abrir arquivo");
      return 1;
    }

        while(t<20){

            v = tanh(t);
            t = t+dt;

            fprintf(fp,"%f\t\t",t);
            fprintf(fp,"%f\n",v);
        }

       fclose(fp);
    }


    return 0;
}
