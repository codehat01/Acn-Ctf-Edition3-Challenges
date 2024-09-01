#include <stdio.h>
#include <string.h>

void function(int i)
{
    char arr[] = {65 ,67 ,78 ,95,67 ,84 ,70 ,123 ,72 ,109 ,72 ,116 ,104 ,101 ,95 ,117 ,72 ,116 ,104 ,72 ,95 ,82 ,72 ,97 ,125 };
    char arr2[29]; 
    int c =1;   
    printf("f(%d)\n", i);
    if (i == 19) {
      
        for (int j = 0; j < sizeof(arr); j++) {
            arr2[j] = arr[j] * c; 
            printf("%c\n",arr2[i]);
        }
        arr2[sizeof(arr)] = '\0';
      
      
          
      }
}

int main()
{
    int i;
    for (i = 1; i < 9; i++) {
        function(i);
    }

    return 0;
}
