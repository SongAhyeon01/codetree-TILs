import java.util.Scanner;


class Bomb{
    String code;
    char color;
    int second;

    public Bomb(String c, char r, int s){
        this.code = c;
        this.color = r;
        this.second = s;
    }
}


public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        String code;
        char color;
        int second;

        code = sc.next();
        color = sc.next().charAt(0);
        second = sc.nextInt();

        Bomb bomb = new Bomb(code, color, second);

        System.out.printf("code : %s\n", bomb.code);
        System.out.printf("color : %c\n", bomb.color);
        System.out.printf("second : %d\n", bomb.second);

    }
}