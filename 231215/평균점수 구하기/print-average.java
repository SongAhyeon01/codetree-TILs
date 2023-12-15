import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        float arr[] = new float[8];

        for (int i=0; i<8; i++) {
            float s = sc.nextFloat();
            arr[i] = s;
        }

        float sum = 0;
        for (int i=0; i<8; i++) {
            sum += arr[i];
        }
        
        float avg = sum / 8;
        System.out.print(String.format("%.1f", avg));

    }
}