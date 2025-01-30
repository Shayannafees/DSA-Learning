import java.util.Scanner;

public class NumberSignAndParityCheck {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter an integer: ");
        int number = scanner.nextInt();
        
        if (number > 0) {
            System.out.print("Positive ");
        } else if (number < 0) {
            System.out.print("Negative ");
        } else {
            System.out.println("Zero");
            scanner.close();
            return;
        }
        
        if (number % 2 == 0) {
            System.out.println("even number.");
        } else {
            System.out.println("odd number.");
        }
        
        scanner.close();
    }
}
