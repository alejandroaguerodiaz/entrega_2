if __name__ == "__main__":
    print("Este modulo no posee ejecucion principal")





def valor(datos):
    breakpoint()
    """Recibe la estructura de datos del equipo y devuelve una tupla con el nombre del jugador asociado a su valor"""
    # Un lambda para calcular el valor de cada jugador a traves de 3 elementos
    valor = lambda tabla: (tabla[0] * 1.5) + (tabla[1] * 1.25) + tabla[2]
    # retorna un mapeado de "jugador":[][][]
    valor_de_cada_jugador = map(valor, datos.values())
    print(list(valor_de_cada_jugador))
    return dict(zip(datos.keys(), valor_de_cada_jugador))

def promedio_goles(datos):
    """Recibe la estructura de datos del equipo y devuelve el promedio de goles por partido del equipo"""
    goles_totales = sum(gol[0] for gol in datos.values())
    return (goles_totales / 25)

#que venga una variable con la cantidad de goles

def top_scorer(top):
    """Dado los goles, devuelve el promedio teniendo en cuenta que sean 25 partidos"""
    return top/25

def nombres():
    """Retorna la cadena de nombres de los jugadores"""
    return """ Agustin, Yanina, Andrés, Ariadna, Bautista, CAROLINA, 
            CESAR, David, Diego, Dolores, DYLAN, ELIANA, Emanuel, Fabián, Noelia, 
            Francsica', FEDERICO, Fernanda, GONZALO, Nancy """

def goles(): 
    """Retorna los goles del equipo"""
    return [0, 10, 4, 0, 5, 14, 0, 0, 7, 2, 1, 1, 1, 5, 6, 1, 1, 2, 0, 11]

def goles_e():
    """Retorna los goles evitados del equipo"""
    return [0, 2, 0, 0, 5, 2, 0, 0, 1, 2, 0, 5, 5, 0, 1, 0, 2, 3, 0, 0]

def asistencias():
    """Retorna las asistencias del equipo"""
    return [0, 5, 1, 0, 5, 2, 0, 0, 1, 2, 1, 5, 5, 0, 1, 0, 2, 3, 1, 0]
