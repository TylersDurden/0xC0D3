#include <stdio.h>

int main(int argc, char *argv[]){
    char buffer [50];
    printf("[Buffer] = %p\n", &buffer);

    if(argc > 1)
        strcpy(buffer,argv[1]);
        printf("Data = %s\n", buffer);
    return 1;
}

