#include <stdio.h>
#include <math.h>
#include <stdlib.h>
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
    double pi = 4*atan(1);
    int i = 0, j=0, k=0, n=0;
    double t = 0.0;
    double ta, te;
    double T = 100;
    double dt = 0.001;
    double r[3] = {2,2,2}; //POSIÇÃO DO ÁTOMO
    double v[3] = {1,1,1}; //VELOCIDADE DO ÁTOMO
    int N = 1;        //GROUND STATE
    double pa, pr;    //PROB DE ABSORÇÃO E PMC
    double gamma = 10.0;
    double St;
    double Wt;
    double fi;
    double cos0;
    double ka = 0.01;
    double ks[3]={};
    double B;

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
    glfwSwapInterval(2.0); //tempo que leva pra cada iteração aparecer na tela em milisegundos
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f); //fundo preto
    glRotatef(40,1.0,1.0,0.0);

    glfwSetErrorCallback(error_callback);

    init();
     while (!glfwWindowShouldClose(window)){
        B = sqrt(r[2]*r[2] + (r[0]*r[0])/4 + (r[1]*r[1])/4);
        Wt = gamma/(B*B);
        pr = (float)rand()/RAND_MAX;
        ta = - log(pr)/Wt; //calculo do tempo de absorção
        for(i=0;i<3;i++){
            r[i] = r[i] + v[i]*ta;  //incremento na posição
           }
        pr = rand()%6;   //sorteio do feixe de absorção
        if(pr==0){      //absorve x+
           v[0] = v[0] + ka;
        }
        if(pr==1){      //absorve x-
           v[0] = v[0] - ka;
        }
        if(pr==2){      //absorve y+
           v[1] = v[1] + ka;
        }
        if(pr==3){      //absorve y+
           v[1] = v[1] - ka;
        }
        if(pr==4){      //absorve z+
           v[2] = v[2] + ka;
        }
        if(pr==5){      //absorve z-
           v[2] = v[2] - ka;
        }
        pr = (float)rand()/RAND_MAX;
        te = -log(pr)/gamma; //calculo do tempo de emissão
        for(i=0;i<3;i++){
            r[i] = r[i] + v[i]*te;  //incremento na posição
           }
        for(i=0;i<3;i++){
            ks[i] = (2*((float)rand()/RAND_MAX) - 1.0)/100.0; //sorteio do vetor de onda de emissão
            v[i] = v[i] - ks[i];
           }

        glPointSize(5);
        glBegin(GL_POINTS);
        glColor3d(1, 0, 0);

        glVertex3f((float)r[0]/6,(float)r[1]/6, (float)r[2]/6 );

        glEnd();
        glfwSwapBuffers(window);
        glfwPollEvents();
    }
    glfwDestroyWindow(window);
    glfwTerminate();

    return 0;
}
