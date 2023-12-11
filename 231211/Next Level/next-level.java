import java.util.Scanner;

class User {
    String id;
    int level;

    public User(String id, int level) {
        this.id = id;
        this.level = level;
    }
}

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        String name;
        int level;

        name = sc.next();
        level = sc.nextInt();

        User user1 = new User("codetree", 10);
        User user2 = new User(name, level);

        System.out.println("user " + user1.id + " lv " + user1.level);
        System.out.println("user " + user2.id + " lv " + user2.level);
    }
}