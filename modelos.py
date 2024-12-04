#aquí cominza el proyecto#
# #Una vez realizada la carga y examinación de datos, vamos a empezar ya con el preprocesado
#Empezamos representando los datos en un formato que sea más fácil de trabajar

##PARA NORMALIZAR USO LA API DE SKLEARN, DE ESTA API USO LA CLASE MinMaxScaler LA CUAL USA EL MIN Y EL MAX DE CADA COLUMNA
##QUE QUIERA NORMALIZAR, ESTA CLASE CUENTA CON DIFERENTES MÉTODOS COMO FIT, TRANFORM O EL PROPIO FIT_TRANSFORM
###DSP PODRÍA USAR STANDARD SCALER , PERO OPTÉ POR NORMALIZAR MEDIANTE MINIMO Y MÁXIMO
columnas_a_normalizar = ['volumen', 'volumen en cuotas', 'volumen de dolares', 'volumen de euros', 'numero de compras']

scaler = MinMaxScaler()

df[columnas_a_normalizar] = scaler.fit_transform(df[columnas_a_normalizar])

df.head()
# df.info()