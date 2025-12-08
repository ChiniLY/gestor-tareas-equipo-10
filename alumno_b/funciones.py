from colorama import Fore, Style
import os


def marcar_completada(fichero):
    """Marca una tarea como completada."""
    print(Fore.CYAN + "\n--- COMPLETAR TAREA ---" + Style.RESET_ALL)

    # Comprobar si existe el fichero
    if not os.path.exists(fichero):
        print(Fore.RED + "No se encuentra el fichero de tareas." + Style.RESET_ALL)
        return

    try:
        # Leemos el fichero
        with open(fichero, "r", encoding="utf-8") as f:
            lineas = f.readlines()

        if not lineas:
            print(Fore.YELLOW + "No hay tareas en la lista." + Style.RESET_ALL)
            return

        # Mostramos las tareas
        print("Selecciona la tarea a completar:")
        for i, linea in enumerate(lineas):
            if "|" in linea:
                datos = linea.strip().split("|")
                estado_visual = "[✓]" if datos[0] == "1" else "[ ]"
                color = Fore.GREEN if datos[0] == "1" else Fore.YELLOW

                print(f"{color}{i+1}. {estado_visual} {datos[1]}{Style.RESET_ALL}")

        # Pedimos al usuario que elija una tarea
        try:
            opcion = int(input(Style.RESET_ALL + "\nNúmero de tarea: ")) - 1

            if 0 <= opcion < len(lineas):
                partes = lineas[opcion].strip().split("|")

                if partes[0] == "1":
                    print(
                        Fore.YELLOW
                        + "¡Esa tarea ya estaba completada!"
                        + Style.RESET_ALL
                    )
                else:
                    lineas[opcion] = f"1|{partes[1]}\n"

                    # Sobrescribimos el fichero con el cambio
                    with open(fichero, "w", encoding="utf-8") as f:
                        f.writelines(lineas)
                    print(
                        Fore.GREEN
                        + "✓ Tarea marcada como completada correctamente."
                        + Style.RESET_ALL
                    )
            else:
                print(Fore.RED + "Número inválido." + Style.RESET_ALL)

        except ValueError:
            print(Fore.RED + "Por favor, introduce un número válido." + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"Error inesperado: {e}" + Style.RESET_ALL)


def eliminar_tarea(fichero):
    """Elimina una tarea del fichero."""
    # TODO: Implementar
    pass


def despedida():
    """Muestra mensaje de despedida."""
    # TODO: Implementar
    pass
