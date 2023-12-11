import java.util.Scanner;

class Person {
    String name = "";
    int score = 0;

    public Person(String n, int s){
        this.name = n;
        this.score = s;
    }
}



public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        Person[] persons = new Person[5];


        for (int i=0; i<5; i++) {
            String name = sc.next();
            int score = sc.nextInt();
            persons[i] = new Person(name, score);
        }


        int min_idx = 0;
        for (int i=0; i<5; i++) {
            int now = persons[i].score;
            if (now < persons[min_idx].score) {
                min_idx = i;
            }
        }

        System.out.printf("%s %d\n", persons[min_idx].name, persons[min_idx].score);

    }
}