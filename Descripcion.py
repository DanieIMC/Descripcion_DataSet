# Descripcion del Dataset
# 1. Numero de variables o columnas: 17.
# 2. Variables clave:
#    - Demograficas y fisicas:
#        - Age: Edad del individuo.
#        - Gender: Genero del individuo (Masculino/Femenino).
#        - Height: Altura (en metros).
#        - Weight: Peso (en kilogramos).
#    - Habitos alimenticios:
#        - CALC: Frecuencia de consumo de alcohol (No, A veces, Frecuentemente).
#        - FAVC: Consumo frecuente de alimentos altos en calorías (Si/No).
#        - NCP: Numero de comidas principales al dia.
#        - FCVC: Frecuencia de consumo de vegetales (en una escala del 1 al 3).
#        - CH2O: Consumo diario de agua (en litros).
#    - Estilo de vida y actividad fisica:
#        - SCC: Seguimiento de calorias (Si/No).
#        - SMOKE: Habito de fumar (Si/No).
#        - FAF: Frecuencia de actividad fisica (dias a la semana).
#        - TUE: Tiempo de uso de dispositivos electrónicos al dia (en horas).
#        - CAEC: Frecuencia de consumo de alimentos entre comidas (No, A veces, Frecuentemente).
#        - MTRANS: Medio de transporte utilizado (por ejemplo, Transporte público, Caminata).
#    - Historia medica:
#        - family_history_with_overweight: Historia familiar de sobrepeso (Si/No).
#    - Clasificacion del peso:
#        - NObeyesdad: Clasificación del estado de obesidad (por ejemplo, Peso normal, Sobrepeso, Obesidad).

# En el dataset, la clase o variable objetivo es la columna:
# 
# NObeyesdad
#
# Esta columna clasifica el estado de obesidad de cada individuo y contiene valores categoricos como:
# - Normal_Weight: Peso normal.
# - Overweight_Level_I: Sobrepeso nivel I.
# - Overweight_Level_II: Sobrepeso nivel II.
# - Obesity_Type_I: Obesidad tipo I.
# - Obesity_Type_II: Obesidad tipo II.
# - Obesity_Type_III: Obesidad tipo III.
# - Insufficient_Weight: Peso insuficiente.
#
# Esta variable se utiliza como la clase porque representa el resultado que queremos predecir o analizar 
# basándonos en las demás variables (atributos).

# Objetivo de Investigacion
# El objetivo de investigacion basado en este dataset es el siguiente:
# - Identificar los factores determinantes que contribuyen a los diferentes niveles de obesidad
#   en una poblacion.
#     - Analizar cómo los habitos alimenticios, actividad fisica y factores geneticos (historia familiar)
#       estan relacionados con los diferentes niveles de obesidad.
#     - Desarrollar modelos predictivos para clasificar a los individuos segun su nivel de obesidad 
#       basandose en las variables disponibles.
#     - Evaluar la influencia relativa de cada factor (por ejemplo, consumo de calorias, actividad fisica, 
#       habito de fumar) en la clasificacion del peso.
