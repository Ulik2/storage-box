#include <cs50.h>
#include <stdio.h>

void draw(int h);

int main(void)
{
    int height; // do while은 하나의 루프 안에서기 때문에 선언이 되지 않아 height가, 그래서 하기 전에 height가 뭔지 선언을 해줘야 while에서 컴퓨터가 뭔지 알지

    do
    {
        height = get_int("Height: "); //위에서 height가 int임을 선언 해줘서 여기서 int적으면 오류나네?..
    }
    while(height < 1);

    draw(height);
}

void draw(int h)
{
    if (h == 0)
    {
        return;
    }

    draw(h-1); //재귀의 사용 : draw라는 함수를 draw로 정의(내 코딩노트 참조)

    for (int i = 0 ; i < h ; i++)
    {
        printf("#");
    }
    printf("\n");
}