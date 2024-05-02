import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] array = new int[n];

        for (int i=0; i<n; i++){
            array[i] = sc.nextInt();
        }

        for (int i=0; i<n; i++){
            int now = array[i];
            for (int j=i; j>0; j--){
                if (now < array[j-1]){
                    array[j] = array[j-1];
                    array[j-1] = now;
                }
            }
        }

        for (int a : array){
            System.out.print(a + " ");
        }
        

    }
}