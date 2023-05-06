from claseViajeroFrecuente3 import ViajeroFrecuente

if __name__ == '__main__':
 def __eq__(self, otro):
        if isinstance(otro, int):
            return self.millas_acumuladas == otro
        elif isinstance(otro, ViajeroFrecuente):
            return self.millas_acumuladas == otro.millas_acumuladas
        else:
            return False
        
        
 def __add__(self, valor):
        if isinstance(valor, int):
            return ViajeroFrecuente(self.num_viajero, self.doc_viajero, self.nombre, self.apellido, self.millas_acumuladas + valor)
        else:
            return None
    
 def __sub__(self, valor):
        if isinstance(valor, int):
            return ViajeroFrecuente(self.num_viajero, self.doc_viajero, self.nombre, self.apellido, self.millas_acumuladas - valor)
        else:
            return None