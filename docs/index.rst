.. Tamagochi documentation master file, created by
   sphinx-quickstart on Mon Feb 24 16:35:25 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentación Tamagotchi
========================
Trabajo Práctico para el nivel intermedio de la Diplomatura en Python de FRBA UTN e-learning.

Instalación
------------

Antes de ejecutar este trabajo, primero instalar las dependencias:

En virtualenv:
--------------
.. code-block:: console

   $ python -m venv .venv

   $ .venv\Scrips\activate

   (.venv) $ pip install -m requirements.txt

En Anaconda:
------------
.. code-block:: console

   $ conda create -n tamagochi python=3.11.10

   $ conda activate tamagochi

   (tamagochi) $ pip install -m requirements.txt

En virtualenvwrapper:
---------------------
.. code-block:: console

   $ mkvirtualenv tamagochi

   $ workon tamagochi

   (tamagochi) $ pip install -m requirements.txt

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   config
   main
   src
