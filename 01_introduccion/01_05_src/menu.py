print('\n MENU \n======\n')

while True:
    print('Selecciona una opción:\n')
    print('1: Saludar')
    print('2: Sumar dos números')
    print('3: Salir\n')

    user_choice = input()

    if user_choice == '1':
        print('Hola, qué tal?')
    elif user_choice == '2':
        n1 = float(input('Introduce el primer número: '))
        n2 = float(input('Introduce el segundo número: '))
        print('El resultado de la suma es:', n1 + n2)
    elif user_choice == '3':
        print('Saliendo del programa!')
        break
    else:
        print('Opción no válida, vuelve a intentarlo.\n')

