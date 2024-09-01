# Productor perezoso (1):
def read_huge_transaction_file(filename):
    with open(filename, "r") as file:
        for line in file:
            data = line.strip()
            yield data  # Entregar solo una línea

# Consumidor perezoso:
def lazy_transactions_processor(filename, num_transactions):
    # Crear objeto generador perezoso llamado a (1)
    transaction_gen = read_huge_transaction_file(filename)
    for _ in range(num_transactions):
        try:
            transaction = next(transaction_gen)
            print(transaction)
        except StopIteration:
            print("No hay más transacciones para leer")
            break

if __name__ == "__main__":
    file_name = input("Ingrese nombre de archivo de transacciones: ")
    n = int(input("Ingrese el número de transacciones: "))
    lazy_transactions_processor(file_name, n)

