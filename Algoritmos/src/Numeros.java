import java.util.Scanner;

public class Numeros {
    public static Scanner scanner;
    public static Integer numero;
    public static void main(String[] args) throws Exception {
        scanner = new Scanner(System.in);
        
        System.out.println("Escriba un número: ");
        numero = scanner.nextInt();

        do {
            System.out.println(numero);
            numero -= 2;
        } while (numero >= 0);
    }
}
