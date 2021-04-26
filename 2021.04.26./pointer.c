#include <stdio.h>

int main(void)
{
    char *s = "EMMA"; // char *라는 자료형을 통해 s가 한 문자를 나타내는 포인터(표지판)임을 알 수 있음 이는 기존의 string과 같음
    printf("%p\n", s);
    printf("%p\n", &s[0]); // E의 주소
    printf("%p\n", &s[1]); // M의 주소
}
