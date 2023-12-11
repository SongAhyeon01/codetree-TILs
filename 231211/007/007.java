import java.util.Scanner;

class Code {
    String a, b, c;

    public Code(String a, String b, String c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

}


public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        String a, b, c;
        a = sc.next();
        b = sc.next();
        c = sc.next();

        Code code1 = new Code(a, b, c);
        
        System.out.println("secret code : " + code1.a);
        System.out.println("meeting point : " + code1.b);
        System.out.println("time : " + code1.c);

    }
}