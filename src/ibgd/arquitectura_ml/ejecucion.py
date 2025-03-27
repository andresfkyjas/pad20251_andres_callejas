
from persona import Persona
from obecidad import ObesityEvaluator
import random
import pandas as pd
def main():
    print("=== Evaluación de Obesidad utilizando IMC ===")
    
    evaluator = ObesityEvaluator()
    print("\nGenerando datos dummy y entrenando modelo...")
    #data_dummy = evaluator.generar_datos_dummy(n_samples=200)
    #evaluator.entrenar_modelo(data_dummy)
    

    #evaluator.guardar_modelo('modelo_obesidad.pkl')
    

    personas = []
    nombres = ['Ana', 'Luis', 'Carlos', 'María', 'Pedro', 'Sofía', 'Juan', 'Laura', 'Diego', 'Elena']
    generos = ['F', 'M']
    ciudades = ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
    estados_civiles = ['Soltero', 'Casado', 'Divorciado']
    profesiones = ['Ingeniero', 'Médico', 'Abogado', 'Profesor', 'Arquitecto']
    actividades = ['Alta', 'Media', 'Baja']
    dietas = ['Equilibrada', 'No equilibrada']
    fumadores = [True, False]
    alcohol_opciones = [True, False]
    presion = ['Normal', 'Alta']
    colesterol_opciones = ['Normal', 'Alto']
    
    n_personas = 10
    for i in range(1, n_personas+1):
        persona = Persona(
            id = i,
            nombre = random.choice(nombres),
            edad = random.randint(18, 70),
            genero = random.choice(generos),
            peso = round(random.uniform(40, 120), 1),
            altura = round(random.uniform(1.5, 2.0), 2),
            ciudad = random.choice(ciudades),
            estado_civil = random.choice(estados_civiles),
            profesion = random.choice(profesiones),
            actividad_fisica = random.choice(actividades),
            dieta = random.choice(dietas),
            fumador = random.choice(fumadores),
            alcohol = random.choice(alcohol_opciones),
            presion_arterial = random.choice(presion),
            colesterol = random.choice(colesterol_opciones)
        )
        personas.append(persona)
    
    df_personas = pd.DataFrame([p.to_dict() for p in personas])
    

    def calcular_nivel(peso, altura):
        imc = peso / (altura ** 2)
        if imc < 18.5:
            return "Bajo peso"
        elif imc < 25:
            return "Normal"
        elif imc < 30:
            return "Sobrepeso"
        else:
            return "Obeso"
    

    df_personas['NivelObesidad'] = df_personas.apply(lambda row: calcular_nivel(row['Peso (kg)'], row['Altura (m)']), axis=1)
    df_personas['EsObeso'] = df_personas['NivelObesidad'].apply(lambda x: True if x == "Obeso" else False)
    
    print("\nDataFrame de Personas con nivel de obesidad:")
    print(df_personas[['ID', 'Nombre', 'Peso (kg)', 'Altura (m)', 'NivelObesidad', 'EsObeso']])
    
    # Ejemplo de predicción para una persona específica
    evaluator.cargar_modelo('modelo_obesidad.pkl')
    test_peso = 85
    test_altura = 1.75
    nivel_predicho, imc_calculado = evaluator.predecir(test_peso, test_altura)
    print(f"\nPara una persona con {test_peso} kg y {test_altura} m:")
    print(f"Nivel de obesidad predicho: {nivel_predicho}")
    print(f"IMC calculado: {imc_calculado:.2f}")

if __name__ == '__main__':
    main()