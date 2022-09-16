import java.util.Scanner;

public class javaprincipal { 

	public static void main (String[] args) {
	
	Scanner sc = new Scanner(System.in);	
		
	Tipodedatos tp = new Tipodedatos (); 
	
	System.out.print ("ingrese el numero uno");
	
	int numeroUno = sc.nextInt();
	
	System.out.print (numeroUno);
	
	System.out.print ("ingrese el numero dos");
	
	int numeroDos = sc.nextInt();
	
	System.out.print (tp.SumarNumeros(numeroUno,numeroDos));
	
	System.out.print ("el resultado es:"+tp.SumarNumeros(numeroUno, numeroDos));
	
	}
	
}
