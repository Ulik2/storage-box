#include <cs50.h>
#include <stdio.h>

float average(int length, int array[]);

int main(void) //실행쪽이 맨 위로 오는게 good
{
    int n = get_int("Scores: "); //과목 수를 사용자한테 받음

    int scores[n]; //그 갯수만큼의 배열을 지정
    for(int i = 0 ; i < n ; i++) // 그래서 과목의 갯수, n 번만큼 과목의 점수를 물어봄
    {
        scores[i] = get_int("Score %i: ", i+1);
    }

    printf("Average: %.1f", average(n, scores));
}


float average(int length, int array[]) // 평균구하는 함수 average는 '배열의 길이'와 '배열'을 값으로 받음
{
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += array[i];
    }
    return (float) sum / (float) length;
}

