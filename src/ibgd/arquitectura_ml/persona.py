import random
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Clase Persona con 15 atributos
class Persona:
    def __init__(self, 
                 id, 
                 nombre, 
                 edad, 
                 genero, 
                 peso, 
                 altura, 
                 ciudad, 
                 estado_civil, 
                 profesion, 
                 actividad_fisica, 
                 dieta, 
                 fumador, 
                 alcohol, 
                 presion_arterial, 
                 colesterol):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.peso = peso            # en kilogramos
        self.altura = altura        # en metros
        self.ciudad = ciudad
        self.estado_civil = estado_civil
        self.profesion = profesion
        self.actividad_fisica = actividad_fisica
        self.dieta = dieta
        self.fumador = fumador
        self.alcohol = alcohol
        self.presion_arterial = presion_arterial
        self.colesterol = colesterol

    def to_dict(self):
        return {
            'ID': self.id,
            'Nombre': self.nombre,
            'Edad': self.edad,
            'Genero': self.genero,
            'Peso (kg)': self.peso,
            'Altura (m)': self.altura,
            'Ciudad': self.ciudad,
            'Estado Civil': self.estado_civil,
            'Profesion': self.profesion,
            'Actividad Fisica': self.actividad_fisica,
            'Dieta': self.dieta,
            'Fumador': self.fumador,
            'Alcohol': self.alcohol,
            'Presion Arterial': self.presion_arterial,
            'Colesterol': self.colesterol
        }