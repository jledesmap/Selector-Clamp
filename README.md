# Selector-Clamp

# Table of Contents
   * [Qué es esto?](#Qué-es-esto)
   * [Requisitos software](#requisitos-software)
   * [Documentation](#documentation)
   * [How to use](#how-to-use)
   * [Path Planning](#path-planning)
      * [Dynamic Window Approach](#dynamic-window-approach)
      * [Grid based search](#grid-based-search)
         * [Dijkstra algorithm](#dijkstra-algorithm)
   * [Use-case](#use-case)
   * [Contribution](#contribution)
   * [Citing](#citing)
   * [Support](#support)
   * [Authors](#authors)

# Qué es esto?

Nuestro grupo ha desarrollado el proyecto llamado Selector Clamp. Este consiste en un brazo mecánico que cuenta con 4 grados de libertad para realizar sus movimientos de búsqueda de objetos y una cámara con la cual poder detectar su entorno.

El usuario a través de una aplicación móvil podrá seleccionar los detalles de la búsqueda. La aplicación permitirá hacer búsquedas de forma y/o color de los objetos. A más a más, hay la opción de hacer varias fotografías vía smartphone, a continuación, el usuario seleccionará aquellas imágenes que mejor describan la forma del objeto que desea que el brazo busque. Entre la comunicación del usuario y Selector Clamp tendremos un servidor donde se almacenarán las órdenes dadas por el usuario.

# Requisitos software

Python 3.7.x:

- numpy

- pirebase

- cv2

Unity:

- using Firebase;
- using Firebase.Database;
- using Firebase.Unity.Editor;

Android Studio

Lenguajes de programación usados: Python3, C#, Java.

# Documentation

This README only shows some examples of this project. 

If you are interested in other examples or mathematical backgrounds of each algorithm, 

You can check the full documentation online: [https://pythonrobotics.readthedocs.io/](https://pythonrobotics.readthedocs.io/)

All animation gifs are stored here: [AtsushiSakai/PythonRoboticsGifs: Animation gifs of PythonRobotics](https://github.com/AtsushiSakai/PythonRoboticsGifs)

# How to use

1. Clone this repo.

> git clone https://github.com/AtsushiSakai/PythonRobotics.git


2. Install the required libraries. You can use environment.yml with conda command.

> conda env create -f environment.yml


3. Execute python script in each directory.

4. Add star to this repo if you like it :smiley:. 


# Path Planning

## Dynamic Window Approach

This is a 2D navigation sample code with Dynamic Window Approach.

- [The Dynamic Window Approach to Collision Avoidance](https://www.ri.cmu.edu/pub_files/pub1/fox_dieter_1997_1/fox_dieter_1997_1.pdf)

![2](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/PathPlanning/DynamicWindowApproach/animation.gif)


## Grid based search

### Dijkstra algorithm

This is a 2D grid based shortest path planning with Dijkstra's algorithm.

![PythonRobotics/figure_1.png at master · AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/PathPlanning/Dijkstra/animation.gif)

In the animation, cyan points are searched nodes.

# Use-case

If this project helps your robotics project, please let me know with creating an issue.

Your robot's video, which is using PythonRobotics, is very welcome!!

This is a list of other user's comment and references:[users\_comments](https://github.com/AtsushiSakai/PythonRobotics/blob/master/users_comments.md)

# Contribution

Any contribution is welcome!!

If your PR is merged multiple times, I will add your account to the author list.

# Citing

If you use this project's code for your academic work, we encourage you to cite [our papers](https://arxiv.org/abs/1808.10703) 

If you use this project's code in industry, we'd love to hear from you as well; feel free to reach out to the developers directly.

# Support

If you or your company would like to support this project, please consider:

- [Sponsor @AtsushiSakai on GitHub Sponsors](https://github.com/sponsors/AtsushiSakai)

- [Become a backer or sponsor on Patreon](https://www.patreon.com/myenigma)

- [One-time donation via PayPal](https://www.paypal.me/myenigmapay/)

# Authors

- [Javi Ledesma Pardo](https://github.com/jledesmap)

- [Pol Magre Moya](https://github.com/polmm96)

- [Ridouan Elbachiri](https://github.com/)

- [Irene González Fernández](https://github.com/)
