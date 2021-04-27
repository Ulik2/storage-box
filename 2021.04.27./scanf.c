#include <stdio.h>

int main(void)
{
    int x;
    printf("x: ");
    scanf("%i", &x); // scanf는 사용자에게 입력받은 값을 특정 주소에 할당함, 여기서는 변수 x의 주소에 할당해서 x가 입력값을 가지게함 (!get_int의 원리)
    printf("x: %i\n", x);
}