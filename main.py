from colorama import init, Fore, Style
import os

from alumno_a.funciones import mostrar_menu, ver_tareas, añadir_tarea
from alumno_b.funciones import marcar_completada, eliminar_tarea, despedida

FICHERO_TAREAS = "tareas.txt"


def main():
    # Inicializa colorama para Windows/Linux
    init(autoreset=True)

    # Creamos el fichero vacío si no existe
    if not os.path.exists(FICHERO_TAREAS):
        with open(FICHERO_TAREAS, "w") as f:
            pass

    # Bucle principal
    while True:
        try:
            # Llamamos al menú
            opcion = mostrar_menu()

            # Decidimos según opción
            if opcion == 1:
                print(Fore.BLUE + "\n--- VER TAREAS ---")
                ver_tareas(FICHERO_TAREAS)

            elif opcion == 2:
                print(Fore.MAGENTA + "\n--- AÑADIR TAREA ---")
                añadir_tarea(FICHERO_TAREAS)

            elif opcion == 3:
                marcar_completada(FICHERO_TAREAS)

            elif opcion == 4:
                eliminar_tarea(FICHERO_TAREAS)

            elif opcion == 5:
                despedida()
                break

            else:
                print(Fore.RED + "Opción incorrecta. Elige entre 1 y 5.")

            print("\n")

        except ValueError:
            print(Fore.RED + "Error: Debes introducir un número.")
        except KeyboardInterrupt:
            # Por si se pulsa Ctrl+C :3
            print(Fore.RED + "\n¡Hasta luego!")
            break


if __name__ == "__main__":
    main()
