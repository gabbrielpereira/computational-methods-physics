#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <windows.h>
#include <wincon.h>
#include <GLFW/glfw3.h>
#include "bitmap-font-opengl.h"

double ED=-1000;

static void error_callback(int error, const char* description){           //acusar eventuais impedimentos da janela ser aberta
      fprintf(stderr, "Error: %s\n", description);
}

static void key_callback(GLFWwindow* window, int key, int scancode, int action, int mods){        //listar respostas do programa a comandos no teclado
    if (key == GLFW_KEY_ESCAPE && action == GLFW_PRESS)
        glfwSetWindowShouldClose (window, GLFW_TRUE);
    if (key == GLFW_KEY_A && action == GLFW_PRESS)
        ED += 10;
    if (key == GLFW_KEY_D && action == GLFW_PRESS)
        ED -= 10;
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
    int i = 0, j=0;
    int random;
    int randomg;
    int cont = 0;
    double t = 0.0;
    double dt = 0.01;
    double T = 100.0;
    int Nx = 20, Ny = 20;
    int N = Nx*Ny;
    int S[Nx][Ny] = {};
    double Lx = 15.0, Ly = 15.0;
    double Ei=0,Ef=0,dE=0;
    int J=1, M=1;
    double B = 0;
    char name[128];
    int mcs=1;
    double w = 0;
    double Temp = 10;


 GLFWwindow* window;     //definir ponteiro janela

    if (!glfwInit())         // Initialize the library //
    return -1;

     window = glfwCreateWindow(800, 900, "Ising", NULL, NULL);     // Create a windowed mode window and its OpenGL context //
    if (!window){
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);
    glfwSetKeyCallback(window,key_callback);
    glfwSwapInterval(0.1); //tempo que leva pra cada iteração aparecer na tela em milisegundos
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f); //fundo preto

    glfwSetErrorCallback(error_callback);


    for(i=0; i<Nx; i++){
        for(j=0;j<Ny; j++){

//SPIN ALEATÓRIO
            random = rand()%2;
            if (random == 0)
            {
                random = -1;
            }
            S[i][j] =  random;
////SPIN IGUAL
//            S[i][j] =  1;
//            //printf("%d \n",S[i][j]);
        }
    }
    init();

while (!glfwWindowShouldClose(window)){

    //for(k=1;k<C;k++){
        glClear(GL_COLOR_BUFFER_BIT);
    i = rand()%Nx;
    j = rand()%Ny;

    if (i==0){
            if(j==0){
                Ei = -J*S[i][j]*(S[Nx-1][j] + S[i+1][j] + S[i][j+1] + S[i][Ny-1]) - B*S[i][j];
                S[i][j] = -S[i][j];
                Ef = -J*S[i][j]*(S[Nx-1][j] + S[i+1][j] + S[i][j+1] + S[i][Nx-1]) - B*S[i][j];
    }
            if (j==Ny-1){
                Ei = -J*S[i][j]*(S[Nx-1][j] + S[i+1][j] + S[i][0] + S[i][j-1]) - B*S[i][j];
                S[i][j] = -S[i][j];
                Ef = -J*S[i][j]*(S[Nx-1][j] + S[i+1][j] + S[i][0] + S[i][j-1]) - B*S[i][j];
    }
            else{
                Ei = -J*S[i][j]*(S[Nx-1][j] + S[i+1][j] + S[i][j+1] + S[i][j-1]) - B*S[i][j];
                S[i][j] = -S[i][j];
                Ef = -J*S[i][j]*(S[Nx-1][j] + S[i+1][j] + S[i][j+1] + S[i][j-1]) - B*S[i][j];
    }
    }
    if (j==0){
            if (i==Ny-1){
                Ei = -J*S[i][j]*(S[i-1][j] + S[0][j] + S[i][j+1] + S[i][Ny-1]) - B*S[i][j];
                S[i][j] = -S[i][j];
                Ef = -J*S[i][j]*(S[i-1][j] + S[0][j] + S[i][j+1] + S[i][Ny-1]) - B*S[i][j];
    }
            else{
                Ei = -J*S[i][j]*(S[i-1][j] + S[i+1][j] + S[i][j+1] + S[i][Ny-1]) - B*S[i][j];
                S[i][j] = -S[i][j];
                Ef = -J*S[i][j]*(S[i-1][j] + S[i+1][j] + S[i][j+1] + S[i][Ny-1]) - B*S[i][j];
    }
    }
    dE = Ef - Ei;
    if (dE <= 0){
        ED += - dE;
    }
    if (dE > 0){
        w = exp(-dE/Temp);
        random = (float)rand()/RAND_MAX;
        if (random < w){
            ED -= dE;
        }
        else{
            S[i][j] = -S[i][j];
        }
    }

//    printf("i=%d , j= %d, dE = %d  \n", i,j, dE);
//
 //printf("Ed = %f \n", ED);
    sprintf(name, "ED = %f", ED);
    writetext(name, -0.95, 0.85);
    sprintf(name, "Passos MC = %d", mcs);
    writetext(name, -0.95, 0.95);

    glPointSize(650/Nx);
        glBegin(GL_POINTS);
        glColor3d(1, 1, 0);

        for(i=1;i<Nx+1;i++){
            for(j=1;j<Ny+1;j++){
                if(S[i-1][j-1]==1){
                    glColor3d(1, 0, 0);
                }
                else{ //if(S[i-1][j-1]==-1){
                    glColor3d(0, 0, 1);
                }

                glVertex2f(2.0*((float)i/(Nx+1)) -1, 2.0*((float)j*0.9/(Ny+1)) -1);
        }
        }
        glEnd();
        glfwSwapBuffers(window);
        glfwPollEvents();
        mcs++;
}
    glfwDestroyWindow(window);
    glfwTerminate();

        return 0;
}
