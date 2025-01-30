import java.util.Scanner;

public class SpeedChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the vehicle's speed: ");
        int speed = scanner.nextInt();
        
        if (speed <= 30) {
            System.out.println("Very slow");
        } else if (speed <= 60) {
            System.out.println("Normal speed");
        } else if (speed <= 100) {
            System.out.println("Fast");
        } else {
            System.out.println("Too fast! Drive safely.");
        }
        
        scanner.close();
    }
}
