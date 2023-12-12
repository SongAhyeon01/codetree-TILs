import java.util.Scanner;

class Loc{
    String name;
    String addr;
    String city;

    public Loc(String n, String a, String c){
        this.name = n;
        this.addr = a;
        this.city = c;
    }


}

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int n;
        n = sc.nextInt();

        Loc[] locs = new Loc[n];
        for (int i=0; i<n; i++) {
            String name = sc.next();
            String addr = sc.next();
            String city = sc.next();
            locs[i] = new Loc(name, addr, city);
        }

        int last_idx = 0;
        for (int i=0; i<n; i++) {
            String now = locs[i].name;
            if (now.compareTo(locs[last_idx].name) > 0) {
                last_idx = i;
            }
        }

        System.out.printf("name %s\n", locs[last_idx].name);
        System.out.printf("addr %s\n", locs[last_idx].addr);
        System.out.printf("city %s\n", locs[last_idx].city);

    }
}