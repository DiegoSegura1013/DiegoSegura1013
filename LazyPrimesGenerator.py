def lazy_primes_generator():
    # Generador perezoso de números primos
    num = 2  # Comenzamos con el primer número primo
    while True:
        # Verificar si el número actual es primo
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num  # Si no se rompe el ciclo, num es primo
        num += 1  # Incrementar el número para verificar el siguiente

if __name__ == "__main__":
    # Solicitar al usuario la cantidad de números primos
    max_primes = int(input("¿Cuántos números primos deseas imprimir (máximo 100)? "))

    # Asegurarse de que el número no exceda 100
    if max_primes > 100:
        print("El número máximo permitido es 100. Se imprimirá 100 números primos.")
        max_primes = 100
    elif max_primes <= 0:
        print("Debes ingresar un número mayor a 0.")
        exit()  # Terminar el programa si el número es inválido

    primes_generator = lazy_primes_generator()
    prime_count = 0  # Contador para los números primos

    # Obtener un número primo a la vez hasta llegar al límite especificado
    while prime_count < max_primes:
        user_input = input("Presiona Enter para obtener el siguiente número primo o escribe 'salir' para terminar: ")
        if user_input.lower() == "salir":
            break
        next_prime = next(primes_generator)
        print(next_prime)
        prime_count += 1  # Incrementar el contador de primos

    print(f"Se han impreso {prime_count} números primos.")
