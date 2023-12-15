import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        double arr[] = new double[8];

        for (int i=0; i<8; i++) {
            double s = sc.nextDouble();
            arr[i] = s;
        }

        double avg = Arrays.stream(arr).average().orElse(0);
        System.out.print(avg);

    }
}