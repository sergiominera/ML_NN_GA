# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 13:07:33 2019

@author: ng7d6b2
"""

#%% packages
import matplotlib.pyplot as plt
import numpy as np
#import functools
#import operator
#%% ejemplo elefante
img = plt.imread('elefante.png')
rows,cols,colors = img.shape # gives dimensions for RGB array
img_size = rows*cols*colors
img_1D_vector = img.reshape(img_size)
# you can recover the orginal image with:
img2 = img_1D_vector.reshape(rows,cols,colors)

#%% plot imagen
plt.imshow(img) # followed by 
plt.show() # to show the first image, then 
plt.imshow(img2) # followed by
plt.show() # to show you the second image.

#%% initial population
'''
Funcion para crear la poblacion inicial. Un grupo de 'cromosomas' (i.e. vectores random). 

Inputs:
input_len: numero de variables en el cromosoma
n_indiv: numero de cromosomas a crear. Numero de cromosomas (vectores) em la poblacion inicial
max_val: valor maximo esperado (eventualmente cambiar a un rango)
tipo: tipo de data que se espera (np.float, np.uint8, etc)

Regresa:
init_popul: Una matriz donde cada renglon es in cromosoma con valores aleatorios

'''
def initial_population(input_len, n_indiv, max_val, tipo):
     init_popul = np.empty(shape=(n_indiv, input_len), dtype=tipo)
     for indv_num in range(n_indiv):
         init_popul[indv_num, :] = np.random.random(input_len)*max_val
     return init_popul
#%% fitness
'''
Esta funcion es la que mide que tan apto es un cromosoma (individuo). Esta funcion depende de cada problema, aca se usa una de ejemplo para imagenes como prueba
''' 
def fitness_fun(target_chrom, indiv_chrom):
     quality = np.mean(np.abs(target_chrom-indiv_chrom))
     quality = np.sum(target_chrom) - quality
     return quality
#%% Population fitness calculation
'''
Funcion que calcula el fitness para todos los miembros de la poblacion (i.e. un loop). 
Esta funcion en particular usar un 'target', pero eso depende de la funcion de fitness, asi que se puede remover dependiendo del caso. 
'''
def cal_pop_fitness(target_chrom, pop):
     qualities = np.zeros(pop.shape[0])
     for indv_num in range(pop.shape[0]):
         qualities[indv_num] = fitness_fun(target_chrom, pop[indv_num, :])
     return qualities


#%% end



















































