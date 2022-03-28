#Nombre: Jesús Bracamonte C.i:29795537

"""Dada una lista de las edades de una población que ha ido a vacunarse

vEdades = [2, 7, 58, 7, 45, 26, 10, 8, 56, 57, 97, 19, 11, 53, 3, 99,
, 62, 78, 29, 9, 37, 42, 56, 86, 28, 86, 95, 26, 49, 67, 21, 815, 67,
, 10, 58, 512, 24, 92, 89, 67, 53, 10, 9, 83, 1, 44, 10, 77, 98, 73, 57]
Elimine de la lista, todas las ocurrencias del entero 10 (3pts)
"""
tuple = ("Edades") 
print(tuple)

Edades = [2, 7, 58, 7, 45, 26, 10, 8, 56, 57, 97, 19, 11, 53, 3, 99, 62, 78, 29, 9, 37, 42, 56, 86, 28, 86, 95, 26, 49, 67, 21, 815, 67, 10, 58, 512, 24, 92, 89, 67, 53, 10, 9, 83, 1, 44, 10, 77, 98, 73, 57]

Edades.sort()
Edades.pop(8)
Edades.pop(8)
Edades.pop(8)
Edades.pop(8)
"""Las edades de 512 y 815 por logica la voy a eliminar porque no existe nadie con esa edad"""
Edades.remove(512)
Edades.remove(815)
print(Edades)

