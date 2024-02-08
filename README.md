# Song Encoding and Reconstruction with Neural Networks

This project aims to explore the application of song encoding techniques into latent vectors for subsequent reconstruction. We will utilize the GTZAN dataset, consisting of 990 songs, each lasting 30 seconds and categorized into ten music genres. The main task is to design and train a neural network capable of transforming these songs into more compact latent vectors, with the goal of evaluating the quality of the reconstruction. Additionally, exploratory analysis of the latent vectors will be conducted to understand the relationships between songs in this new space.

## Overview

In the initial steps, we established the groundwork for the practical work by downloading the song files and setting the sampling rate. Subsequently, we introduced the MusicDataset class, designed to handle the loading and structuring of data from the GTZAN database. Within this class, we traversed genre directories, identified present classes (genres), and applied a spectrogram transformation to the data. Furthermore, we divided the dataset into training, validation, and test sets, ensuring reproducibility with a random seed and determining sizes for validation and test sets. We created dataloaders for training, validation, and test sets, specifying batch sizes and configuring options for efficient data loading.

For detailed instructions and results, please refer to the full report.

---------------------------------

# Codificación y Reconstrucción de Canciones con Redes Neuronales

Este proyecto tiene como objetivo explorar la aplicación de técnicas de codificación de canciones en vectores latentes para su posterior reconstrucción. Utilizaremos la base de datos GTZAN, que contiene 990 canciones, cada una con una duración de 30 segundos y clasificadas en diez géneros musicales. La tarea principal es diseñar y entrenar una red neuronal capaz de transformar estas canciones en vectores latentes más compactos, con el objetivo de evaluar la calidad de la reconstrucción. Además, se realizarán análisis exploratorios de los vectores latentes para comprender las relaciones entre las canciones en este nuevo espacio.

## Resumen

En los primeros pasos, establecimos las bases para el trabajo práctico descargando los archivos de las canciones y estableciendo la tasa de muestreo. Posteriormente, introdujimos la clase MusicDataset, diseñada para manejar la carga y estructuración de datos de la base de datos GTZAN. Dentro de esta clase, recorrimos los directorios de géneros, identificamos las clases presentes (géneros) y aplicamos una transformación de espectrograma a los datos. Además, dividimos el conjunto de datos en conjuntos de entrenamiento, validación y prueba, asegurando la reproducibilidad con una semilla aleatoria y determinando los tamaños de los conjuntos de validación y prueba. Creamos dataloaders para los conjuntos de entrenamiento, validación y prueba, especificando los tamaños de lote y configurando opciones para una carga eficiente de datos.

Para obtener instrucciones detalladas y resultados, consulte el informe completo.
