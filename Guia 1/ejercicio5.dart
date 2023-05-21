import 'dart:math';

void main() {
  List<int> lista1 = generarNumerosAleatorios(7);
  List<int> lista2 = generarNumerosAleatorios(7);
  List<int> lista3 = generarNumerosAleatorios(7);
  print('Las listas generadas son:');
  print(lista1);
  print(lista2);
  print(lista3);

  double promedio1 = calcpromedio(lista1);
  double promedio2 = calcpromedio(lista2);
  double promedio3 = calcpromedio(lista3);

  
  List<String> listapromedio = [];
  listapromedio.add(promedio1.toStringAsFixed(2));
  listapromedio.add(promedio2.toStringAsFixed(2));
  listapromedio.add(promedio3.toStringAsFixed(2));
  print('Los promedio de cada lista son los siguientes respectivamente:');
  print(listapromedio);
}

List<int> generarNumerosAleatorios(int cantidad) {
  List<int> lista = [];
  Random random = Random();
  for (int i = 0; i < cantidad; i++) {
    int numeroAleatorios = random.nextInt(71) + 30;
    lista.add(numeroAleatorios);
  }
  return lista;
}

double calcpromedio(List<int> lista) {
  int suma = 0;
  for (int numero in lista) {
    suma += numero;
  }
  double promedio = suma / lista.length;
  return promedio;
}
