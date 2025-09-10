# Proyecto-Agente-Reactivo
Este proyecto es una simulación en Python de un robot (agente) que se mueve en un grid evitando obstáculos de manera reactiva.

El agente no planifica rutas ni conoce la ubicación de un objetivo: simplemente observa su entorno inmediato y decide moverse según reglas simples como:

Si no hay obstáculo al frente → avanza.
Si hay obstáculo → gira y busca otra dirección libre.

Esta simulación sirve como base para entender los agentes inteligentes y la diferencia entre reactivos y deliberativos.

Funciones:

Representación gráfica sencilla del grid.
Obstáculos colocados aleatoriamente en el entorno.
Un agente que se mueve evitando colisiones.

## Requisitos
Tener instalado [Python] en su versión 3.13.17 
Tener instalado [Visual Studio Code]
Pip (este ya debería venir incluido en la instalación de Python)

## Instalación
Para empezar a usar este documento, necesitarás clonar el repositorio a tu sistema de archivos. Todas las instrucciones están escritas para usuarios de Windows solamente.

Entra a la carpeta en la que quieras tener el proyecto usando el Explorador de Archivos; por ejemplo en tu carpeta de `Documentos\Proyectos` o algo por el estilo.

Haz clic derecho sobre algún espacio en blanco dentro del Explorador y selecciona la opción `Abrir en Terminal`. Si no aparece, puede ser que diga `Abrir en Símbolo del Sistema`, `Abrir en PowerShell` `Abrir en CMD` o algo por el estilo. Si no aparece ninguna de estas opciones, prueba manteniendo la tecla `Shift` pulsada en tu teclado mientras haces clic derecho.

Una vez abierta la terminal, ingresa el siguiente comando:

```bash
git clone https://github.com/Alejandro-Guerra/Inteligencia-Artificial-U1.git
```

Es posible que te aparezca una ventana pidiendo que ingreses tu nombre de usuario o correo electrónico que tienes en GitHub y la contraseña de tu cuenta. Ingrésalas para poder continuar.

Una vez clonado el repositorio, podrás acceder a la carpeta usando.

```bash
cd Proyecto-Int-Art
```

## Ejecución

Para ejecutar el proyecto exitente dos metodos: 

El Primer metodo, bastaría con poner el siguiente comando en la consola desde visual studio:

```bash
python AgenteReactivo.py
```
El segundo metodo, lo encontraras en la carpeta dist, es un archivo ejecutable que solo haciendo doble clic podras entrar, no necesitas tener nada instalado en tu computadora para visualizarlo.

Proyecto-Int-Art           # Carpeta principal
 ├─ AgenteReactivo.py      # Código fuente
 ├─ README.md              # Este archivo
 ├─ dist/                  # Contiene el ejecutable
 │   └─ AgenteReactivo.exe # Archivo Ejecutable 


## Links
[Python]: https://www.python.org/downloads/
[Visual Studio Code]: https://code.visualstudio.com/
