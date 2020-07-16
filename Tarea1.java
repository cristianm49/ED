

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Tarea1 {

    public static void main(String[] args) throws IOException {
        BufferedReader tc = new BufferedReader(new InputStreamReader(System.in));

        String op;

        while (true) {
            System.out.println("Ingresar estudiante op.1");
            System.out.println("Salir otro numero");
            op = tc.readLine();
            if (!op.equals("1")) {
                break;
            }

            System.out.println("Ingrese Nombre");
            String nombre = tc.readLine();

            System.out.println("Ingrese Materia");
            String materia = tc.readLine();

            System.out.println("Ingrese la dimension");
            int dimension = Integer.parseInt(tc.readLine());
            int[][][] notas = new int[dimension][dimension][dimension];

            double sumaNotas = 0;
            int mes = 1;

            System.out.println("Notas mes " + mes);
            for (int i = 0; i < dimension; i++) {
                for (int j = 0; j < dimension; j++) {

                    for (int k = 0; k < dimension; k++) {
                        System.out.println("Ingrese la nota");
                        notas[i][j][k] = Integer.parseInt(tc.readLine());
                        sumaNotas += notas[i][j][k];
                    }

                    if (mes < 12) {
                        mes++;

                        System.out.println("Notas mes " + mes);
                    }
                }

            }
            System.out.println("El promedio del estudiante" + nombre + " materia " + materia + " es: " + (sumaNotas / (dimension * dimension * dimension)));

        }

    }
}
