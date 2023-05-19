import 'dart:io';
import 'dart:math';

void main() {
  // primera lista
  List<int> lista1 = [14, 2, 5, 3, 9];

  // segunda list
  List<int> lista2 = [];
  print('Ingresa 5 números enteros para la segunda lista:');
  for (int i = 0; i < 5; i++) {
    int numero = int.parse(stdin.readLineSync()!);
    lista2.add(numero);
  }
  
}

