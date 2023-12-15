import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> v = new ArrayList<>();

        int n = sc.nextInt();
        for (int i=0; i<n; i++) {
            String co = sc.next();

            if (co.equals("push_back")) {
                int data = sc.nextInt();
                v.add(data);
            }
            else if (co.equals("pop_back")) {
                v.remove(v.size()-1);

            }
            else if (co.equals("size")) {
                System.out.println(v.size());
            }
            else {
                int idx = sc.nextInt();
                System.out.println(v.get(idx-1));
            }

        }

    }
}