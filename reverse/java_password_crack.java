import java.util.*;

class password_crack {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the password: ");
        String flag = "EHS{FAKE_FLAG}";
        String password_input = scan.next();

        if (flag.equals(password_input)) {
            System.out.println("Correct!! you found the flag!");
        } else {
            System.out.println("Wrong password!");
        }

    }
}