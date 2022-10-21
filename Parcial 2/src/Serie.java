public class Serie implements Entregable{
 
 //Constantes
 
 private final static int NUM_TEMPORADAS_DEF=3;
 
 public final static int MAYOR=1;
 
 public final static int MENOR=-1;
 
 public final static int IGUAL=0;
 
 //Atributos
 
 private String titulo;
 
 private int numeroTemporadas;
 
 private boolean entregado;
 
 private String genero;
 
 private String creador;
 
 //Métodos publicos
 
 public String getTitulo() {
 return titulo;
 }
 
 public void setTitulo(String titulo) {
 this.titulo = titulo;
 }
 
 public int getnumeroTemporadas() {
 return numeroTemporadas;
 }
 
 public void setnumeroTemporadas(int numeroTemporadas) {
 this.numeroTemporadas = numeroTemporadas;
 }
 
 public String getGenero() {
 return genero;
 }
 
 public void setGenero(String genero) {
 this.genero = genero;
 }
 
 public String getcreador() {
 return creador;
 }
 
 public void setcreador(String creador) {
 this.creador = creador;
 }
 
 public void entregar() {
 entregado=true;
 }
 
 public void devolver() {
 entregado=false;
 }
 
 public boolean isEntregado() {
 if(entregado){
 return true;
 }
 
 return false;
 }
 
 public int compareTo(Object a) {
 int estado=MENOR;
 
 //Hacemos un casting de objetos para usar el metodo get
 
 Serie ref=(Serie)a;
 if (numeroTemporadas>ref.getnumeroTemporadas()){
 estado=MAYOR;
 }else if(numeroTemporadas==ref.getnumeroTemporadas()){
 estado=IGUAL;
 }
 
 return estado;
 }
 
 public String toString(){
 return "Informacion de la Serie: \n" +
 "\tTitulo: "+titulo+"\n" +
 "\tNumero de temporadas: "+numeroTemporadas+"\n" +
 "\tGenero: "+genero+"\n" +
 "\tCreador: "+creador;
 }
 
 public boolean equals(Serie a){
 if (titulo.equalsIgnoreCase(a.getTitulo()) && 
creador.equalsIgnoreCase(a.getcreador())){
 return true;
 }
 
 return false;
 }
 
 //Constructor
 
 public Serie(){
 this("",NUM_TEMPORADAS_DEF, "", "");
 }
 
 public Serie(String titulo, String creador){
 this(titulo,NUM_TEMPORADAS_DEF, "", creador);
 }
 
 public Serie(String titulo, int numeroTemporadas, String genero, String creador){
 this.titulo=titulo;
 this.numeroTemporadas=numeroTemporadas;
 this.genero=genero;
 this.creador=creador;
 this.entregado=false;
 }
 
}