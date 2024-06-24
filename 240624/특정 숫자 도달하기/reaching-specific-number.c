#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.

    int arr[10];
    int sum = 0, cnt = 0;
    
    for (int i=0; i<10; i++){
        scanf("%d ", &arr[i]);
    }

    for (int i=0; i<10; i++){
        if (arr[i] >= 250){
            break;
        }

        sum += arr[i];
        cnt += 1;
    }

    double avg = (double)sum / cnt;
    printf("%d %0.1f", sum, avg);
   

    return 0;
}