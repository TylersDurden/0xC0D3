#include <stdio.h>

int main(int argc, char *argv[]){
    char buffer [50];

    if(argc == 1)
        strcpy(buffer, *argv[1]);
        printf("%p\n", &buffer);
    return 0;
}