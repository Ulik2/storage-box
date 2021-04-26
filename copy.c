#include <cs50.h>
#include <ctype.h>
#include <stdio.h>

int main(void)
{
    char *s = get_string("s: ");
    char *t = s; // s가 가리키고 있는 주소가 t가 가리키고 있는 메모리상의 주소와 동일함(둘은 같은 곳을 포인터로써 수행중)

    t[0] = toupper(t[0]); // 둘은 같은곳을 가리키고 있으니까 t의 첫글자가 대문자가되면 s의 첫글자도 당연히 대문자가 되겠지?

    printf("s: %s\n", s); // 그래서 t만 대문자로 해줬음에도 s를 프린트해도 대문자로 나오는거임
    printf("s: %s\n", t);
}