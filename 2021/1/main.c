#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Keyboard colors
#define KNRM "\x1B[0m"
#define KRED "\x1B[31m"
#define KGRN "\x1B[32m"
#define KYEL "\x1B[33m"

long stringToNumber(char* str, unsigned int len);

long stringToNumber(char* str, unsigned int len)
{
    if(len < 1)
    {
        fprintf(stderr, "Error: Invalid string to number conversion.\n");
        exit(EXIT_FAILURE);
    }

    long number = 0;

    // Check the first character for minus sign.
    _Bool isPositive = *str == '-' ? false : true;
    unsigned int start = *str == '-' ? 1 : 0;

    int digit;
    for(; start < len; ++start)
    {
        digit = *(str + start) - '0';
        if(digit < 0 || digit > 9)
        {
            fprintf(stderr, "Error: Tried converting a letter to a digit.\n");
            exit(EXIT_FAILURE);
        }
        
        number *= 10;
        number += digit;
    }

    number = isPositive ? number : number * -1;

    return number;
}

int main(void)
{
    FILE* fp;
    char* line = NULL;
    size_t len = 0;
    ssize_t read;

    char* name = (char*) malloc(sizeof(char) * 256);
    
    printf("Input file:\n");
    scanf("%s", name);

    fp = fopen(name, "r");
    free(name);

    if (fp == NULL)
    {
        fprintf(stderr, "Error: file doesn't exist.\n");
        exit(EXIT_FAILURE);
    }

    long number, prevNumber;
    _Bool isFirst = true;
    long larger = 0;
    
    // Read line by line.
    while((read = getline(&line, &len, fp)) != -1)
    {
        prevNumber = number;
        number = stringToNumber(line, (unsigned int) read - 1);

        printf("%ld", number);
        
        if(isFirst)
        {
            isFirst = false;
            printf(" - " KYEL "First number" KNRM "\n");
        }
        else if(number > prevNumber)
        {
            ++larger;
            printf(" - " KGRN "Increased" KNRM "\n");
        }
        else {
            printf(" - " KRED "Decreased" KNRM "\n");
        }
    }
    
    fclose(fp);
    if(line)
    {
        free(line);
    }

    printf("Larger measurements: " KYEL "%ld" KNRM "\n", larger); 
    return 0;
}
