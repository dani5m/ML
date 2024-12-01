# ML
Descripción
En esta práctica deberás desarrollar un modelo que sea capaz de predecir el precio del dólar en euros con 6h de adelanto.

Conjunto de datos
Contarás con el siguiente conjunto de datos para entrenar tu modelo (puedes utilizar este código para cargarlo en Colab):

!wget "https://udcgal.sharepoint.com/:u:/s/GCEDAprendizajeAutomaticoII/EW-oyZUCNkBMvy80CvRjlnABDl5jxrGj1JyXG3C2vr2xAA?e=61EuOe&download=1" -O data.json
Enunciado del problema
El problema consiste en predecir el valor del dólar 6h después del momento actual. La idea es hacer un modelo que te permita decidir cuándo comprar y cuándo vender dólares, para que puedas operar de la siguiente manera:

Si el modelo predice que el dólar bajará: vendo un dólar ahora y lo compro más barato dentro de 6h. La diferencia entre el precio de venta y el de compra es mi ganancia.
Si el modelo predice que el dólar subirá: compro un dólar ahora y lo vendo más caro dentro de 6h. La diferencia entre el precio de compra y el de venta es mi ganancia.
Puedes suministrarle al modelo los datos de entrada que estimes para cada predicción, siempre respetando que ninguno esté a menos de 6h del que intentas predecir.

Debes respetar las siguientes restricciones:

No se deben utilizar datos posteriores a 31/08/2022 23:59:59 para entrenamiento. Los datos desde 01/09/2022 00:00:00 en adelante se podrán utilizar como conjunto de test.
La predicción se deberá hacer a 6h vista, es decir, se deberá predecir el valor de salida 6 horas después del dato más reciente que se le proporcione al modelo. Se deberán predecir dos valores distintos:
Valor de la variable "precio fin"
Valor binario que indicará si "precio fin" 6h después será mayor o menor que en el dato más reciente proporcionado a la entrada.
Desarrollo
A la hora de calificar se tendrán en cuenta los siguientes apartados:

Carga y examen de los datos
Carga los datos con Pandas y haz un examen preliminar de los mismos. Descarta aquellos que sean erróneos.
Haz la partición entre conjunto de entrenamiento y conjunto de test.
Preprocesado
Representa las variables en un formato que facilite el aprendizaje. Para ello estandariza aquellas que lo necesiten y transforma las fechas a un formato adecuado.
Transforma los conjuntos de entrenamiento y test a NumPy.
Utiliza la función sliding_window del Lab9 para ventanear la serie temporal para obtener un lote de muchos pares (vector de entrada, etiqueta) para entrenamiento y otro lote para test.
Haz que el tamaño de ventana sea configurable para poder probar varias alternativas
Revisa la continuidad temporal de la serie para que las ventanas representen siempre el mismo periodo de tiempo. Descarta las ventanas incorrectas.
Elección del/los modelo/s
Ajusta a los datos de entrenamiento modelos con arquitecturas de tipo dense, LSTM y GRU, probando con ventanas de distintos tamaños.
Evaluación del rendimiento del/los modelo/s frente a baselines
Compara el rendimiento de tus modelos frente entre sí y con dos baselines sencillas (diseña dos baselines similares para el problema binario):
Un modelo que prediga siempre el último valor de entrada recibido (6h antes del dato a predecir)
Un modelo que prediga la media de los valores de entrada recibidos
Identifica sesgos en tu modelo. Para ello, analiza las distribuciones de entrenamiento y test y las predicciones/errores de entrenamiento/test. Si identificas algún problema, adapta tu pipeline para intentar solventarlo.
Busca dar respuesta a las preguntas, ¿por cuántos céntimos de dólar falla cada modelo? ¿Cuánto puedo esperar ganar con mi modelo durante el periodo de test, haciendo las operaciones de 1$?
