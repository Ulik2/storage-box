#include <stdio.h>

void swap(int *a, int *b);

int main(void)
{
    int x = 1;
    int y = 2;

    printf("x is %i, y is %i\n", x, y);
    swap(&x,&y); //스왑이 포인터로 되있으니까 주소를 알려줘야지
    printf("x is %i, y is %i\n", x, y);
}

void swap(int *a, int *b) // 두 변수의 값을 바꿔주면 복사되어 저장된 a와 b 둘만 바뀌고 x y는 그대로니까 x의 주소와 b의 주소를 바꿔준다.
{
    int tmp = *a; // a가 가리키고있는 곳의 값을 tmp에 할당한다
    *a = *b; // b가 가리키고있는 곳의 값을 a가 가리키고있는 곳에 할당한다 (즉, x에 2를 할당한다)
    *b = tmp; // b가 가리키고 있는곳(y)에 tmp의 값을 할당한다 (즉, y에 1을 할당)
}