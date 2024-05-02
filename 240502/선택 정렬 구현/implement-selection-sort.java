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
            for (int j=i+1; j<n; j++) {
                if (array[j] < array[i]){
                    int tmp = array[i];
                    array[i] = array[j];
                    array[j] = tmp;
                }
            }
            
        }
        for (int a : array){
            System.out.print(a + " ");
        }

    }
}