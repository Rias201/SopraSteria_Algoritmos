import java.util.Scanner;

public class Salario {

    public static Double sueldo;
    public static Scanner scanner;
    public static Double tarifa;
    public static Integer horasTrabajadas;
    public static Integer horasExtras;
    public static Double precioHorasExtras;
    public static void main(String[] args) throws Exception {
        scanner = new Scanner(System.in);
        
        System.out.println("Cuál es la tarifa del trabajador?");
        tarifa = scanner.nextDouble();
        
        System.out.println("Horas trabajadas por el trabajador?");
        horasTrabajadas = scanner.nextInt();

        if (horasTrabajadas > 40) {
            horasExtras = horasTrabajadas - 40;
            precioHorasExtras = horasExtras * (tarifa*1.5);
            sueldo = 40*tarifa + precioHorasExtras;
        } else {
            sueldo = horasTrabajadas*tarifa;
        }

        System.out.println("El sueldo del trabajador es de " + sueldo);
    }
}
