import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int arr[] = new int[10];

        for (int i=0; i<10; i++) {
            int tk = sc.nextInt();
            if (tk == 0) {
                break;
            }
            arr[9-i] = tk;
        }

        for (int i=0; i<10; i++) {
            if (arr[i] != 0) {
                System.out.printf("%d ", arr[i]);
            }
        }
    }
}