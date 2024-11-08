from oslo.piezas import Peon, Torre, Caballo, Alfil, Reina, Rey

class Tablero:

    def __init__(self):
        self.piezas_blancas = []
        self.piezas_negras = []
        self.crear_piezas()
        self.turno = "blanco"
    
    def crear_piezas(self):
        for i in range(8):
            self.piezas_blancas.append(Peon(i, 1, "blanco"))
            self.piezas_negras.append(Peon(i, 6, "negro"))
        
        self.piezas_blancas.append(Torre(0, 0, "blanco"))
        self.piezas_blancas.append(Torre(7, 0, "blanco"))
        self.piezas_negras.append(Torre(0, 7, "negro"))
        self.piezas_negras.append(Torre(7, 7, "negro"))

        self.piezas_blancas.append(Caballo(1, 0, "blanco"))
        self.piezas_blancas.append(Caballo(6, 0, "blanco"))
        self.piezas_negras.append(Caballo(1, 7, "negro"))
        self.piezas_negras.append(Caballo(6, 7, "negro"))

        self.piezas_blancas.append(Alfil(2, 0, "blanco"))
        self.piezas_blancas.append(Alfil(5, 0, "blanco"))
        self.piezas_negras.append(Alfil(2, 7, "negro"))
        self.piezas_negras.append(Alfil(5, 7, "negro"))

        self.piezas_blancas.append(Reina(3, 0, "blanco"))
        self.piezas_negras.append(Reina(3, 7, "negro"))

        self.piezas_blancas.append(Rey(4, 0, "blanco"))
        self.piezas_negras.append(Rey(4, 7, "negro"))

    def movimientos_posibles(self, pieza):
        return pieza.movimientos_posibles(self)
    
    def aplicar_movimiento(self, movimiento, pieza):
        x_destino, y_destino = movimiento
        pieza_a_eliminar = None

        # Verificar si hay una pieza en la posición de destino
        for p in (self.piezas_blancas if self.turno == "negro" else self.piezas_negras):
            if p.x == x_destino and p.y == y_destino:
                pieza_a_eliminar = p
            break

        # Eliminar la pieza si existe
        if pieza_a_eliminar:
            if self.turno == "blanco":
                self.piezas_negras.remove(pieza_a_eliminar)
            else:
                self.piezas_blancas.remove(pieza_a_eliminar)

        # Mover la pieza a la nueva posición
        pieza.mover(movimiento)
    
    def obtener_piezas_enemigas(self, color):
        if color == "blanco":
            return self.piezas_negras
        else:
            return self.piezas_blancas

    def jaque_mate(self):

        rey = None

        if self.turno == "blanco":
            for pieza in self.piezas_negras:
                if isinstance(pieza, Rey):
                    rey = pieza
            
            for pieza in self.piezas_blancas:
                if rey and rey.posicion in pieza.movimientos_posibles(self):
                    if not rey.movimientos_posibles(self):
                        return True
            return False
        else:
            for pieza in self.piezas_blancas:
                if isinstance(pieza, Rey):
                    rey = pieza
            
            for pieza in self.piezas_negras:
                if rey and rey.posicion in pieza.movimientos_posibles(self):
                    if not rey.movimientos_posibles(self):
                        return True
            return False
        
    def cambiar_turno(self):
        self.turno = "blanco" if self.turno == "negro" else "negro"

