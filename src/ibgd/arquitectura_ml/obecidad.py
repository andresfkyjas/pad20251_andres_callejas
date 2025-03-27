import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

class ObesityEvaluator:
    def __init__(self):
        self.model = None
        self.niveles_dict = {0: "Bajo peso", 1: "Normal", 2: "Sobrepeso", 3: "Obeso"}
    
    @staticmethod
    def calcular_nivel_imc(peso, altura):
        imc = peso / (altura ** 2)
        if imc < 18.5:
            return 0
        elif imc < 25:
            return 1
        elif imc < 30:
            return 2
        else:
            return 3
    
    def generar_datos_dummy(self, n_samples=200, random_seed=42):
        np.random.seed(random_seed)
        pesos = np.random.uniform(40, 120, n_samples)
        alturas = np.random.uniform(1.5, 2.0, n_samples)
        niveles = np.array([self.calcular_nivel_imc(p, a) for p, a in zip(pesos, alturas)])
        data = pd.DataFrame({
            'Peso (kg)': pesos,
            'Altura (m)': alturas,
            'Nivel': niveles
        })
        return data
    
    def entrenar_modelo(self, data, test_size=0.2, random_seed=42):
        X = data[['Peso (kg)', 'Altura (m)']]
        y = data['Nivel']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_seed)
        self.model = DecisionTreeClassifier(random_state=random_seed)
        self.model.fit(X_train, y_train)
        score = self.model.score(X_test, y_test)
        print(f"Precisión del modelo: {score*100:.2f}%")
        return score
    
    def guardar_modelo(self, filename='modelo_obesidad.pkl'):
        if self.model is None:
            print("No hay un modelo entrenado para guardar.")
        else:
            joblib.dump(self.model, filename)
            print(f"Modelo guardado en '{filename}'")
    
    def cargar_modelo(self, filename='modelo_obesidad.pkl'):
        self.model = joblib.load(filename)
        print(f"Modelo cargado desde '{filename}'")
    
    def predecir(self, peso, altura):
        if self.model is None:
            print("El modelo no está cargado o entrenado.")
            return None
        nueva_muestra = np.array([[peso, altura]])
        pred = self.model.predict(nueva_muestra)[0]
        nivel = self.niveles_dict[pred]
        imc = peso / (altura ** 2)
        return nivel, imc
    
    def visualizar_distribucion(self, data):
        plt.hist(data['Nivel'], bins=np.arange(-0.5, 4.5, 1), edgecolor='black')
        plt.xticks([0, 1, 2, 3], ['Bajo peso', 'Normal', 'Sobrepeso', 'Obeso'])
        plt.xlabel("Nivel de obesidad")
        plt.ylabel("Cantidad de muestras")
        plt.title("Distribución de niveles de obesidad")
        plt.show()