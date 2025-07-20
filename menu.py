from extract import run_extraction
from transform import run_transformation
from disperse import run_dispersal

def main():
    while True:
        print("\n--- PIPELINE DE DATOS ---")
        print("1. Extracción (PostgreSQL ➜ Parquet)")
        print("2. Transformación (Validar esquema)")
        print("3. Dispersión (Dividir y cargar en DB)")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            run_extraction()
        elif opcion == "2":
            run_transformation()
        elif opcion == "3":
            run_dispersal()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
