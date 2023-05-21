import 'dart:math';
void main() {
  List<int> a=[4,3,2,2,1];
  List<int> b=[-3,2,8,0,1];

  List<int> resultado = [];

  for (int i=0; i<a.length; i++) { 
    resultado.add(a[i]*b[i]);
  }

  Random random = Random();

  for(int i=0; i<5; i++) { 
    resultado.add(-random.nextInt(5));
  }

  resultado.sort((a,b)=> b.compareTo(a));

  print(resultado);
}
