import java.util.Scanner;

public class TempChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter temperature in Celsius: ");
        double temperature = scanner.nextDouble();
        
        if (temperature > 30) {
            System.out.println("It’s hot.");
        } else if (temperature >= 15) {
            System.out.println("It’s warm.");
        } else {
            System.out.println("It’s cold.");
        }
        
        scanner.close();
    }
}
