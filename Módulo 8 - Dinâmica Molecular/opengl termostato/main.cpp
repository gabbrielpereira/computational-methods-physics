#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <random>
#include <windows.h>
#include <wincon.h>
#include <GLFW/glfw3.h>
#include "bitmap-font-opengl.h"


static void error_callback(int error, const char* description){           //acusar eventuais impedimentos da janela ser aberta
      fprintf(stderr, "Error: %s\n", description);
}

static void key_callback(GLFWwindow* window, int key, int scancode, int action, int mods){        //listar respostas do programa a comandos no teclado
    if (key == GLFW_KEY_ESCAPE && action == GLFW_PRESS)
        glfwSetWindowShouldClose (window, GLFW_TRUE);
}

void writetext(char *name, float xat, float yat)
{
    GLfloat white[3] = { 1.0, 1.0, 1.0 };
    int i, j;
    char teststring[33];

    glColor3fv(white);

    glRasterPos2f(xat, yat);
    printString(name);
    glFlush ();
}

int main()
{
    int i = 0, j=0, k=0, n=0;
    double random;
    double randomg;
    int cont = 0;
    double t = 0.0;
    double dt = 0.01;
    double T = 100.0;
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
    double v2[N] = {};
    double xcm = 0.0;
    double ycm = 0.0;
    double vxcm = 0.0;
    double vycm = 0.0;
    double rx = 0.0;
    double ry = 0.0;
    double U = 0.0;
    double F = 0.0;
    double r = 0.0;
    double freq = 90.0;
    double m = 1.0;
    double somv2 = 0.0;
    double kbT = 0.0;
    double kbTo = 0.0;
    char name[128];
    std::default_random_engine generator;
    std::normal_distribution<double> distribution(0, sqrt(kbTo));

         GLFWwindow* window;     //definir ponteiro janela

    if (!glfwInit())         // Initialize the library //
    return -1;

     window = glfwCreateWindow(600, 600, "Dinamica Molecular", NULL, NULL);     // Create a windowed mode window and its OpenGL context //
    if (!window){
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);
    glfwSetKeyCallback(window,key_callback);
    glfwSwapInterval(1.0); //tempo que leva pra cada iteração aparecer na tela em milisegundos
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f); //fundo preto

    glfwSetErrorCallback(error_callback);


    for(i=0; i<Nx; i++){
        for(j=0;j<Ny; j++){
            n = Nx*j + i;
            random = (double)rand()/RAND_MAX - 0.5;
            x[n] =  -Lx/2 + (i+0.5)*dx + (random)*0.1*dx;
//            xcm += x[n];
//            vxcm += vx[n];
            random = (double)rand()/RAND_MAX - 0.5;
            y[n] =  -Ly/2 + (j+0.5)*dy + (random)*0.1*dy;
//            ycm += y[n];
//            vycm += vy[n];

            //printf("x = %lf      y = %lf      \n", x[n], y[n]);
        }
    }

//    xcm = xcm/N;
//    ycm = ycm/N;
//    vxcm = vxcm/N;
//    vycm = vycm/N;




    fflush(stdin);
    FILE *fp;
    fp = fopen("100N_kbTo_0.txt","w+");
    if(fp==NULL){
      printf("Impossivel abrir arquivo");
      return 1;
    }
    init();
     while (!glfwWindowShouldClose(window)){
    //for(k=1;k<C;k++){
        glClear(GL_COLOR_BUFFER_BIT);
        //fprintf(fp,"%f  ",t);
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
                ax[i] += (F*rx)/m*r;
                ay[i] += (F*ry)/m*r;
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

            random = (double)rand()/RAND_MAX;
            if (random < freq*dt){
                    randomg = distribution(generator);
                    vx[k] = randomg;
                    randomg = distribution(generator);
                    vy[k] = randomg;
            }

            v2[k] = vx[k]*vx[k] + vy[k]*vy[k];
            somv2 += m*v2[k];

            }
            kbT = somv2/(2*(N-1));

            somv2 = 0.0;

    sprintf(name, "N = %d", N);
    writetext(name, -0.95, 0.95);
    sprintf(name, "Tempo = %f", t);
    writetext(name, -0.95, 0.85);
    sprintf(name, "T = %f", kbT);
    writetext(name, -0.95, 0.75);
//    sprintf(name, "To = %f", kbTo);
//    writetext(name, -0.95, 0.75);
    fprintf(fp, "%f\t%f\t%f\n", t,kbT, kbTo);

    glPointSize(5);
        glBegin(GL_POINTS);
        glColor3d(1, 0, 0);

        for(i=0;i<(N);i++){

            //for(j=1;j<(N-1);j++)
//                if(grupo[i][j]==1){
//                    glColor3d(1, 0, 0);
//                }
//                if(grupo[i][j]==2){
//                    glColor3d(0, 1, 0);
//                }
//                if(grupo[i][j]==3){
//                    glColor3d(0, 0, 1);
//                }
                glVertex2f((float)x[i]*1.2/Lx,((float)y[i]*1.2/Ly));
        }
         glEnd();
        glfwSwapBuffers(window);
        glfwPollEvents();
        t = t +dt;
   }
    glfwDestroyWindow(window);
    glfwTerminate();
    fclose(fp);
    return 0;
}
