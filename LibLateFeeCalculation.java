import java.util.Scanner;

public class LibLateFeeCalculation {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of days the book is overdue: ");
        int daysOverdue = scanner.nextInt();
        int fee;
        
        if (daysOverdue <= 5) {
            fee = daysOverdue * 1;
        } else if (daysOverdue <= 10) {
            fee = 5 + (daysOverdue - 5) * 2;
        } else {
            fee = 5 + 10 + (daysOverdue - 10) * 5;
        }
        
        System.out.println("Total late fee: $" + fee);
        
        scanner.close();
    }
}
