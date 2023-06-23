#include <stdio.h>
#include <math.h>
#include <windows.h>
#include <wincon.h>
#include <GLFW/glfw3.h>

static void error_callback(int error, const char* description){           //acusar eventuais impedimentos da janela ser aberta
      fprintf(stderr, "Error: %s\n", description);
}

static void key_callback(GLFWwindow* window, int key, int scancode, int action, int mods){        //listar respostas do programa a comandos no teclado
    if (key == GLFW_KEY_ESCAPE && action == GLFW_PRESS)
        glfwSetWindowShouldClose (window, GLFW_TRUE);
}


int main()
{
    double pi = 4*atan(1);
    int N = 3;
    float T = 2;
    float dt = 0.0001;
    float m[] = {1.0, 1.0, 1.0};
    //, 0.00001};
    //, 0.09532};
    float vx[N]= {0.0,0.0, 10.0};
    float x[]= {0.0, 1.0, 0.5};
    //, 0};
    //, 5.21};
    float Fx[N]= {};
    float ax[N]= {};
    float vy[N]= {0.0,0.0,0.0};
    //,0};
    float y[N]= {0,0,-1.0};
    //,2};
    float ay[N]= {};
    float Fy[N]= {};
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
    float G = 4*pi*pi;
    float t = 0;
    float d = 0;
    float F = 0;
    float U = 0;
    float A = 0;
    float vxcm=0.0;
    float vycm=0.0;
    float Et = 0.0;
    float Lt = 0.0;
    int i=0, j=0, k=0;
    int resp = 0;
    float C = 300000000;
    float alfa = 0.001;

 GLFWwindow* window;     //definir ponteiro janela

    if (!glfwInit())         // Initialize the library //
    return -1;

     window = glfwCreateWindow(600, 600, "Spatial Chaos", NULL, NULL);     // Create a windowed mode window and its OpenGL context //
    if (!window){
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);
    glfwSetKeyCallback(window,key_callback);
    glfwSwapInterval(0.0001); //tempo que leva pra cada iteração aparecer na tela em milisegundos
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f); //fundo preto

    glfwSetErrorCallback(error_callback);


for(i=1; i<N; i++){
    vx[i] = sqrt((G)*m[i]);

}

    fflush(stdin);
    FILE *fpE;
    FILE *fpL;
    fpE = fopen("5p_E.txt","w+");
    fpL = fopen("5p_L.txt","w+");
    //fprintf(fp,"Tempo\t\t\t Sol\t\t P1\t\t\t P2\t\t\t P3\t\t P4\t\t P5\n");

while (!glfwWindowShouldClose(window)){
    //for(k=1;k<C;k++){
        glClear(GL_COLOR_BUFFER_BIT);

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

    glPointSize(10);
    //glDrawArrays(GL_LINE_LOOP, 0, N);
        glBegin(GL_POINTS);
        //glColor3d(0, 0, 1);

        for(i=0;i<(N);i++){
            if (i==0 ){
            glColor3d(1, 0, 0);
            }
             if (i==1 ){
            glColor3d(0, 1, 0);
            }
             if (i==2 ){
            glColor3d(0, 0, 1);
            }
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
                glVertex2f((float)(x[i]-vxcm*t)/3,((float)(y[i]-vycm*t)/3));
        }
         glEnd();
        glfwSwapBuffers(window);
        glfwPollEvents();
        t = t + dt;
    }
    glfwDestroyWindow(window);
    glfwTerminate();
//for (i=1;i<N;i++){
//
//        printf("Planeta %i     Periodo: %f     Raio medio: %f      ", i, Per[i], Rmed[i]);
//
//        K[i] = (Per[i]*Per[i])/(Rmed[i]*Rmed[i]*Rmed[i]);
//        printf("k: %f      ", K[i]);
//printf("\n");

//for (i=1;i<N;i++){
//    printf("%f  %f",Per[i], Rmed[i]);
//    printf("\n");
//}
    return 0;
}
