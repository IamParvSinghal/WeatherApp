#include <stdio.h>
#include <string.h>

int main() {
    int num_names;
    scanf("%d", &num_names);
    getchar(); 

    char name[20];
    for (int i = 0; i < num_names; i++) {
        fgets(name, sizeof(name), stdin);
        name[strcspn(name, "\n")] = 0;
        printf("Hello, %s!\n", name);
    }

    return 0;
}