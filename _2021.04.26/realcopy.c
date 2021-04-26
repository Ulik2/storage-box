#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h> // malloc이 포함된 라이브러리

int main(void)
{
    char *s = get_string("s: ");
    char *t = malloc(strlen(s) + 1); // malloc함수는 메모리를 할당함 => t라는 포인터에 s 문자길이 +1의 메모리 할당, 왜 +1? 널 종단문자도 포함해야지!!

    for (int i = 0, n = strlen(s) ; i < n +1 ; i++) // n = strlen(s)하고 i< n+1하는이유 : i<strlen(s)로 하게되면 계속 길이 확인해야되니까 비효율적 알고리즘임
                                                    // strlen(s)를 변수 n으로 박아놓으면 한번만 길이 확인하고 절댓값처럼 쓰이니까 번거로운 알고리즘이 아님
    {
        t[i] = s[i];
    }
    t[0] = toupper(t[0]);

    printf("s: %s\n", s);
    printf("t: %s\n", t);
}
