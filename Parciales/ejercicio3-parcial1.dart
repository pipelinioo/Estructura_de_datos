import 'dart:io';
import 'dart:math';

void main() {
  List<int> lista1= [];//listas 
  List<int> lista2= [];
  List<int> lista3= [];

  Random random =Random();

  for (int i =0; i <10; i++) {
    int elementos = random.nextInt(11) + 10;
    lista1.add(elementos);
  }

  for (int i= 0; i< 10;i++) {
    int elementos = random.nextInt(11) + 10;
    lista2.add(elementos);
  }

  print("Ingresa 5 elementos para la tercera lista:");
  for (int i= 0; i<5;i++) {
    int elemento = int.parse(stdin.readLineSync()!); //en mi caso nunca paro al querer ingresar los 5 elementos:(
    lista3.add(elemento);
  }

  List<int> listaConcatenada = [];
  listaConcatenada.addAll(lista1);
  listaConcatenada.addAll(lista2);
  listaConcatenada.addAll(lista3);

  print('Lista 1: $lista1');
  print('Lista 2: $lista2');
  print('Lista 3: $lista3');
  print('Lista concatenada: $listaConcatenada');
}
