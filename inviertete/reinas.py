import random

# Función para generar un nuevo tablero 8x8
def generate_new_board():
    rows = 8
    columns = 8

    board = []

    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            board.append((i, j))

    return board

# Función para mostrar las reinas
def display(queens):
    rows = 8
    columns = 8

    message = ""

    # Generamos el mapa de 8x8
    for column in range(1, columns + 1):

        message += str(column) + " "

        # Creamos una fila con 8 espacios para cada columna
        for row in range(1, rows + 1):

            # Crear una nueva posición en las coordenadas actuales
            position = (row, column)

            # Si hay una reina en este punto mostramos el icono ♕, de lo contrario
            # dejamos el espacio vacío
            if position in queens:
                message += "♕ "
            else:
                message +=  "⃞ "

        message += "\n"

    print(message)


# El programa principal, aquí están los pasos para generar las 8 reinas
def run():
    queens_count = 8

    board_width = 8

    queens = []
    board = generate_new_board()

    # Definir una función para revisar que la posición esté disponible y
    # así eliminarla
    def remove_position(position):
        if position in board:
            board.remove(position)

    # Generar las 8 reinas
    for i in range(0, queens_count):
        # Escoger una fila y una columna de las disponibles
        queen = random.choice(board)

        # Inicializar las variables de los puntos que eliminaremos
        upper_right = queen
        upper_left = queen

        lower_right = queen
        lower_left = queen

        lower = queen
        upper = queen

        left = queen
        right = queen

        # Iterar en un rango 8 para eliminar los puntos
        for j in range(0, board_width):

            # Remover los puntos que interfieren con otras reinas
            remove_position(upper_right)
            remove_position(upper_left)

            remove_position(lower_right)
            remove_position(lower_left)

            remove_position(upper)
            remove_position(lower)

            remove_position(right)
            remove_position(left)

            # Asignar nuevos valores a las posiciones en las esquinas
            upper_right = (upper_right[0] - 1, upper_right[1] + 1)
            upper_left = (upper_left[0] - 1, upper_left[1] - 1)

            lower_right = (lower_right[0] + 1, lower_right[1] + 1)
            lower_left = (lower_left[0] + 1, lower_left[1] - 1)

            # Asignar nuevos valores a las posiciones arriba y abajo
            lower = (lower[0], lower[1] + 1)
            upper = (upper[0], upper[1] - 1)

            # Asignar nuevos valores a las posiciones a la derecha y a la izquierda
            right = (right[0] + 1, right[1])
            left = (left[0] - 1, left[1])

        # Agregar a la reina a la lista
        queens.append(queen)

    display(queens)

if __name__ == '__main__':
    '''
        Ejecutar el programa y si hay un error (la configuración del tablero no es correcta)
        entonces ejecutamos el programa de nuevo
    '''
    while True:
        try:
            run()
            break
        except:
            pass
