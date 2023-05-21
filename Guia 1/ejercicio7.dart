void main() {

  List<dynamic> lista = ['a', 2, 0, 'b', 8, 'c'];

  for (var numero in lista) {
    if(numero is int)
    print(numero);
  }

}