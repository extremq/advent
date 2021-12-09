#include <stdio.h>
#include <stdlib.h>

// Keyboard colors.
#define KNRM "\x1B[0m"
#define KRED "\x1B[31m"
#define KGRN "\x1B[32m"
#define KYEL "\x1B[33m"

#define MAX_COMMAND_LENGTH 7

int main(void)
{
    FILE* fp;
    char* name = (char*) malloc(sizeof(char) * 256);
    
    // Read name of input file.
    printf("Input file:\n");
    scanf("%255[^\n]s", name);
    fp = fopen(name, "r");

    // Check if file exists.
    if(fp == NULL)
    {
        fprintf(stderr, KRED "Error: file '%s' doesn't exist.\n" KNRM, name);
        exit(EXIT_FAILURE);
    }
    free(name);

    // Init variables for reading.
    char* command = (char*) malloc(sizeof(char) * (MAX_COMMAND_LENGTH + 1));
    if(command == NULL)
    {
        fprintf(stderr, KRED "Error: can't allocate memory for reading file.\n" KNRM);
        exit(EXIT_FAILURE); 
    }
    int amount, depth = 0, horizontal = 0;

    while(fscanf(fp, "%7[a-z]s", command))
    {
        if(fscanf(fp, "%d", &amount) == EOF)
        {
            fprintf(stderr, KRED "Error: invalid input format." KNRM);
        }
        getc(fp);

        // Only look at the first character of the command.
        switch(*command)
        {
            case 'f':
                printf(KYEL "Horizontal position increased by %d units.\n" KNRM, amount);
                horizontal += amount;

                break;
            case 'd':
                printf(KGRN "Depth increased by %d units.\n" KNRM, amount);
                depth += amount;

                break;
            case 'u':
                printf(KRED "Depth decreased by %d units.\n" KNRM, amount);
                depth -= amount;
                
                break;
        }
    }

    printf("Answer: " KYEL "%d" KNRM "\n", horizontal * depth);
    free(command);
    fclose(fp);
    return 0;
}
