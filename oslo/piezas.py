from oslo.tablero import Tablero

class Pieza:
    def __init__(self, color, posicion):
        self.color = color
        self.posicion = posicion

    def mover(self, nueva_posicion):
        self.posicion = nueva_posicion

    def movimientos_posibles(self, tablero):
        pass

    def __str__(self):
        return f"Pieza de color {self.color} en la posición {self.posicion}"
    

class Peon(Pieza):

    def __init__(self, color, posicion):
        super().__init__(color, posicion)

    def mover(self, nueva_posicion):
        super().mover(nueva_posicion)
    
    def movimientos_posibles(self, tablero):
        movimientos = []
        if self.color == "blanco":
            # Movimiento normal
            if tablero[self.posicion[0]][self.posicion[1] + 1] is None:
                movimientos.append((self.posicion[0], self.posicion[1] + 1))
            # Movimiento inicial
            if self.posicion[1] == 1 and tablero[self.posicion[0]][self.posicion[1] + 2] is None:
                movimientos.append((self.posicion[0], self.posicion[1] + 2))
            # Movimientos de comer
            if self.posicion[0] > 0 and tablero[self.posicion[0] - 1][self.posicion[1] + 1] is not None and tablero[self.posicion[0] - 1][self.posicion[1] + 1].color != self.color:
                movimientos.append((self.posicion[0] - 1, self.posicion[1] + 1))
            if self.posicion[0] < 7 and tablero[self.posicion[0] + 1][self.posicion[1] + 1] is not None and tablero[self.posicion[0] + 1][self.posicion[1] + 1].color != self.color:
                movimientos.append((self.posicion[0] + 1, self.posicion[1] + 1))
        else:
            # Movimiento normal
            if tablero[self.posicion[0]][self.posicion[1] - 1] is None:
                movimientos.append((self.posicion[0], self.posicion[1] - 1))
            # Movimiento inicial
            if self.posicion[1] == 6 and tablero[self.posicion[0]][self.posicion[1] - 2] is None:
                movimientos.append((self.posicion[0], self.posicion[1] - 2))
            # Movimientos de comer
            if self.posicion[0] > 0 and tablero[self.posicion[0] - 1][self.posicion[1] - 1] is not None and tablero[self.posicion[0] - 1][self.posicion[1] - 1].color != self.color:
                movimientos.append((self.posicion[0] - 1, self.posicion[1] - 1))
            if self.posicion[0] < 7 and tablero[self.posicion[0] + 1][self.posicion[1] - 1] is not None and tablero[self.posicion[0] + 1][self.posicion[1] - 1].color != self.color:
                movimientos.append((self.posicion[0] + 1, self.posicion[1] - 1))
        return movimientos

    def __str__(self):
        return f"Peón de color {self.color} en la posición {self.posicion}"
    
        
class Torre(Pieza):
    def __init__(self, color, posicion):
        super().__init__(color, posicion)

    def mover(self, nueva_posicion):
        super().mover(nueva_posicion)
    
    def movimientos_posibles(self, tablero):
        movimientos = []
        # Movimiento hacia adelante
        for i in range(1, 8):
            if self.posicion[0] + i < 8:
                if tablero[self.posicion[0] + i][self.posicion[1]] is None:
                    movimientos.append((self.posicion[0] + i, self.posicion[1]))
                else:
                    if tablero[self.posicion[0] + i][self.posicion[1]].color != self.color:
                        movimientos.append((self.posicion[0] + i, self.posicion[1]))
                    break
        # Movimiento hacia atrás
        for i in range(1, 8):
            if self.posicion[0] - i >= 0:
                if tablero[self.posicion[0] - i][self.posicion[1]] is None:
                    movimientos.append((self.posicion[0] - i, self.posicion[1]))
                else:
                    if tablero[self.posicion[0] - i][self.posicion[1]].color != self.color:
                        movimientos.append((self.posicion[0] - i, self.posicion[1]))
                    break
        # Movimiento hacia la derecha
        for i in range(1, 8):
            if self.posicion[1] + i < 8:
                if tablero[self.posicion[0]][self.posicion[1] + i] is None:
                    movimientos.append((self.posicion[0], self.posicion[1] + i))
                else:
                    if tablero[self.posicion[0]][self.posicion[1] + i].color != self.color:
                        movimientos.append((self.posicion[0], self.posicion[1] + i))
                    break
        # Movimiento hacia la izquierda
        for i in range(1, 8):
            if self.posicion[1] - i >= 0:
                if tablero[self.posicion[0]][self.posicion[1] - i] is None:
                    movimientos.append((self.posicion[0], self.posicion[1] - i))
                else:
                    if tablero[self.posicion[0]][self.posicion[1] - i].color != self.color:
                        movimientos.append((self.posicion[0], self.posicion[1] - i))
                    break
        return movimientos

    def __str__(self):
        return f"Torre de color {self.color} en la posición {self.posicion}"


class Caballo(Pieza):
    def __init__(self, color, posicion):
        super().__init__(color, posicion)

    def mover(self, nueva_posicion):
        super().mover(nueva_posicion)
    
    def movimientos_posibles(self, tablero):

        movimientos = []
        # Posibles movimientos del caballo
        posibles_movimientos = [
            (self.posicion[0] + 1, self.posicion[1] + 2),
            (self.posicion[0] + 1, self.posicion[1] - 2),
            (self.posicion[0] - 1, self.posicion[1] + 2),
            (self.posicion[0] - 1, self.posicion[1] - 2),
            (self.posicion[0] + 2, self.posicion[1] + 1),
            (self.posicion[0] + 2, self.posicion[1] - 1),
            (self.posicion[0] - 2, self.posicion[1] + 1),
            (self.posicion[0] - 2, self.posicion[1] - 1)
        ]
        
        for mov in posibles_movimientos:
            if 0 <= mov[0] < 8 and 0 <= mov[1] < 8:  # Verifica si está dentro de los límites del tablero
                if tablero[mov[0]][mov[1]] is None or tablero[mov[0]][mov[1]].color != self.color: # Verifica si la posición está vacía o contiene una pieza enemiga
                    movimientos.append(mov)
                
        return movimientos

    def __str__(self):
        return f"Caballo de color {self.color} en la posición {self.posicion}"


class Alfil(Pieza):
    def __init__(self, color, posicion):
        super().__init__(color, posicion)

    def mover(self, nueva_posicion):
        super().mover(nueva_posicion)

    def movimientos_posibles(self, tablero):
        movimientos = []
        # Movimiento hacia la derecha y hacia arriba
        for i in range(1, 8):
            if self.posicion[0] + i < 8 and self.posicion[1] + i < 8:
                if tablero[self.posicion[0] + i][self.posicion[1] + i] is None:
                    movimientos.append((self.posicion[0] + i, self.posicion[1] + i))
                else:
                    if tablero[self.posicion[0] + i][self.posicion[1] + i].color != self.color:
                        movimientos.append((self.posicion[0] + i, self.posicion[1] + i))
                    break
        # Movimiento hacia la derecha y hacia abajo
        for i in range(1, 8):
            if self.posicion[0] + i < 8 and self.posicion[1] - i >= 0:
                if tablero[self.posicion[0] + i][self.posicion[1] - i] is None:
                    movimientos.append((self.posicion[0] + i, self.posicion[1] - i))
                else:
                    if tablero[self.posicion[0] + i][self.posicion[1] - i].color != self.color:
                        movimientos.append((self.posicion[0] + i, self.posicion[1] - i))
                    break
        # Movimiento hacia la izquierda y hacia arriba
        for i in range(1, 8):
            if self.posicion[0] - i >= 0 and self.posicion[1] + i < 8:
                if tablero[self.posicion[0] - i][self.posicion[1] + i] is None:
                    movimientos.append((self.posicion[0] - i, self.posicion[1] + i))
                else:
                    if tablero[self.posicion[0] - i][self.posicion[1] + i].color != self.color:
                        movimientos.append((self.posicion[0] - i, self.posicion[1] + i))
                    break
        # Movimiento hacia la izquierda y hacia abajo
        for i in range(1, 8):
            if self.posicion[0] - i >= 0 and self.posicion[1] - i >= 0:
                if tablero[self.posicion[0] - i][self.posicion[1] - i] is None:
                    movimientos.append((self.posicion[0] - i, self.posicion[1] - i))
                else:
                    if tablero[self.posicion[0] - i][self.posicion[1] - i].color != self.color:
                        movimientos.append((self.posicion[0] - i, self.posicion[1] - i))
                    break
        return movimientos

    def __str__(self):
        return f"Alfil de color {self.color} en la posición {self.posicion}"


class Reina(Pieza):
    def __init__(self, color, posicion):
        super().__init__(color, posicion)

    def mover(self, nueva_posicion):
        super().mover(nueva_posicion)
    
    def movimientos_posibles(self, tablero):
        movimientos = []
        # Movimientos de la torre
        for mov in Torre(self.color, self.posicion).movimientos_posibles(tablero):
            movimientos.append(mov)
        # Movimientos del alfil
        for mov in Alfil(self.color, self.posicion).movimientos_posibles(tablero):
            movimientos.append(mov)
        return movimientos

    def __str__(self):
        return f"Reina de color {self.color} en la posición {self.posicion}"


class Rey(Pieza):
    def __init__(self, color, posicion):
        super().__init__(color, posicion)
        self.movida = False

    def mover(self, nueva_posicion):
        super().mover(nueva_posicion)
    
    def movimientos_posibles(self, tablero):
        movimientos = []
        # Posibles movimientos del rey
        posibles_movimientos = [
            (self.posicion[0] + 1, self.posicion[1] + 1),
            (self.posicion[0] + 1, self.posicion[1]),
            (self.posicion[0] + 1, self.posicion[1] - 1),
            (self.posicion[0], self.posicion[1] + 1),
            (self.posicion[0], self.posicion[1] - 1),
            (self.posicion[0] - 1, self.posicion[1] + 1),
            (self.posicion[0] - 1, self.posicion[1]),
            (self.posicion[0] - 1, self.posicion[1] - 1)
        ]

        # Obtener las piezas negras del tablero
        piezas_negras = tablero.obtener_piezas_enemigas(self.color)

        # Sacar los movimientos de todas las piezas
        movimientos_piezas = []
        for pieza in piezas_negras:
            movimientos_piezas += pieza.movimientos_posibles(tablero)
        
        # Filtrar los movimientos que no están en los movimientos de las piezas
        for mov in posibles_movimientos:
            if 0 <= mov[0] < 8 and 0 <= mov[1] < 8:
                if mov not in movimientos_piezas and (tablero[mov[0]][mov[1]] is None or tablero[mov[0]][mov[1]].color != self.color):
                    movimientos.append(mov)

        return movimientos

    def __str__(self):
        return f"Rey de color {self.color} en la posición {self.posicion}"