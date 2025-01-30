import java.util.Scanner;

public class DiscountCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the total purchase amount: ");
        double amount = scanner.nextDouble();
        double finalPrice;
        
        if (amount > 1000) {
            finalPrice = amount * 0.8;
        } else if (amount >= 500) {
            finalPrice = amount * 0.9;
        } else {
            finalPrice = amount;
        }
        
        System.out.println("Final price after discount: $" + finalPrice);
        
        scanner.close();
    }
}
