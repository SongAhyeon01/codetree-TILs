import java.util.Scanner;

class Product{
    String name;
    int code;

    public Product(String n, int c){
        this.name = n;
        this.code = c;
    }
}


public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        
        Product pro1 = new Product("codetree", 50);
        
        String name = sc.next();
        int code = sc.nextInt();

        Product pro2 = new Product(name, code);

        System.out.printf("product %d is %s\n", pro1.code, pro1.name);
        System.out.printf("product %d is %s\n", pro2.code, pro2.name);
    }
}