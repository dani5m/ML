# ML
Descripción:
En esta práctica desarrollaré un modelo que sea capaz de predecir el precio del dólar en euros con 6h de adelanto.

Conjunto de datos
Contaré con el siguiente conjunto de datos para entrenar mis modelo:

!wget "https://udcgal.sharepoint.com/:u:/s/GCEDAprendizajeAutomaticoII/EW-oyZUCNkBMvy80CvRjlnABDl5jxrGj1JyXG3C2vr2xAA?e=61EuOe&download=1" -O data.json

Enunciado del problema:

El problema consiste en predecir el valor del dólar 6h después del momento actual. La idea es hacer un modelo que te permita decidir cuándo comprar y cuándo vender dólares, para que puedas operar de la siguiente manera:

Si el modelo predice que el dólar bajará: vendo un dólar ahora y lo compro más barato dentro de 6h. La diferencia entre el precio de venta y el de compra es mi ganancia.
Si el modelo predice que el dólar subirá: compro un dólar ahora y lo vendo más caro dentro de 6h. La diferencia entre el precio de compra y el de venta es mi ganancia.

Elección del/los modelo/s:
Ajustaré a los datos de entrenamiento modelos con arquitecturas de tipo dense, LSTM y GRU, probando con ventanas de distintos tamaños.

Evaluación del rendimiento del/los modelo/s frente a baselines:
Compararé el rendimiento de mis modelos entre sí y con dos baselines sencillas:
Un modelo que prediga siempre el último valor de entrada recibido (6h antes del dato a predecir)
Un modelo que prediga la media de los valores de entrada recibidos

Con esta práctica buscaremos dar respuesta a las preguntas, ¿por cuántos céntimos de dólar falla cada modelo? ¿Cuánto puedo esperar ganar con mi modelo durante el periodo de test, haciendo las operaciones de 1$?
