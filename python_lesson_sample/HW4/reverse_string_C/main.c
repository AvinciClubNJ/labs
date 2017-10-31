#include <stdio.h>
#include <string.h>

void reverseMe(char *strIn)
{
    int len = strlen(strIn);
    int i;
    char tempChar;

    for (i = 0; i < (len/2); i++) {
        tempChar = strIn[len - 1 - i] ;
        strIn[len - 1 -i] = strIn[i];
        strIn[i] = tempChar;
    }
    strIn[len] = '\0';
}

int main()
{
    char strToReverse[80] = "Please reverse me!";

    printf("After reverseMe: %s\n", strToReverse);

    reverseMe(strToReverse);

    printf("After reverseMe: %s\n", strToReverse);

    return 0;
}
