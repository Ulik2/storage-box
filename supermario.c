#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Size:");
    }
    while(n<1); // -> n이 1보다 작다면 계속해라!!질문을(do-while)

    for (int i = 0 ; i < n ; i++) // 이중루프로 총 2단계를 설정(n번만큼 반복)
    {
        for (int j = 0 ; j < n ; j++) //1단계(n번만큼의 #을 쓴다)
        {
            printf("#");
        }
        printf("\n"); //2단계(줄을 바꾸고 다시 - n번 채워야하니까)
    }
}
