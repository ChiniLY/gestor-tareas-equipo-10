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
    
    with open(fichero,"r",encoding="utf-8") as txt:

        contenido=txt.readlines()
        count=1
        ##Comprobar si hay tareas que hacer
        if len(contenido)==0:
            print(Fore.GREEN + "No tienes ninguna tarea que hacer :)")
        else:
            for linea in contenido:
            
                if "0" in linea:
                    pendiente=linea.strip().split("|")
                    print(f"{count}. " + Fore.YELLOW + f"[ ] {pendiente[1]} " + Style.RESET_ALL,)
                elif "1" in linea:
                    completado=linea.strip().split("|")
                    print(f"{count}. " + Fore.GREEN+ f"[✓] {completado[1].strip()} " + Style.RESET_ALL)

                count+=1

def añadir_tarea(fichero):
    tarea=input("Indica la nueva tarea: ")

    with open(fichero,"w") as txt:
        txt.write(f"0|{tarea}\n")
        print(Fore.GREEN+ "Tarea añadida correctamente")