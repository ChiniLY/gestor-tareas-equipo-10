from colorama import Fore, Style

def mostrar_menu():
    print(Fore.BLACK + "=== GESTOR DE TAREAS ===")
    print(Fore.BLUE + "1. Ver tareas")
    print(Fore.MAGENTA + "2. Añadir tarea")
    print(Fore.GREEN + "3. Marcar tarea como completada")
    print(Fore.YELLOW + "4. Eliminar tarea")
    print(Fore.RED + "5. Salir")

    opcion=int(input(Style.RESET_ALL + "Elige opción: "))

    return opcion

def ver_tareas(fichero):
    """Muestra todas las tareas numeradas."""
    # TODO: Implementar
    pass

def añadir_tarea(fichero):
    """Añade una nueva tarea al fichero."""
    # TODO: Implementar
    pass