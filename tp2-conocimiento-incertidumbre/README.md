## Trabajo Práctico 2 - Conocimiento e Incertidumbre

### Problema: Busca Minas

#### Enunciado

El objetivo de este trabajo es implementar un agente que resuelva el problema del juego Busca Minas. El problema consiste en encontrar todas las minas en un tablero de NxN casilleros. Para ello se cuenta con un tablero que indica la cantidad de minas que hay en cada fila y columna, y se puede utilizar la información de los casilleros que ya fueron descubiertos.

#### Resolución del problema

Se utiliza la clase Sentence para representar sentencias lógicas. Cada sentencia lógica en esta representación tiene dos partes: un conjunto de cells en el tablero que están involucrados en la sentencia y un número count, que representa el recuento de cuántas de esas celdas son minas.

Se utiliza la clase Minesweeper para representar el estado del juego. El estado del juego contiene un conjunto de mines, que son las celdas que son minas, y un conjunto de moves_made, que son las celdas que ya se descubrieron.

Se utiliza la clase MinesweeperAI para representar el agente.

#### Ejecución

:warning: _Para ejecutar el agente se debe tener instalado Python 3.10 o superior._

:warning: _Para ejecutar el agente se debe tener instalado Pygame 2.0.1 o superior._

Para ejecutar el agente se debe ejecutar el siguiente comando:

```bash
python3 runner.py
```

#### Ejemplos

![capture-win.png](assets%2Fimages%2Fcapture-win.png)

![capture-lose.png](assets%2Fimages%2Fcapture-lose.png)

#### Conclusiones

Se puede observar que el agente resuelve el problema de forma óptima, ya que encuentra todas las minas en el menor tiempo posible.