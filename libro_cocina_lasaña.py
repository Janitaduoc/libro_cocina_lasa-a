
EXPECTED_BAKE_TIME = 40
#se define la constante
def bake_time_remaining(tiempo_real):
    valor_a_retornar = EXPECTED_BAKE_TIME - tiempo_real
    return valor_a_retornar    
#tiempo de horneado restante, ya definimos la variable EXPECT_BAKE_TIME
#Que equivale a 40 minutos , y debemos saber cuanto nos falta por hornear
# donde la variable tiempo_real equivale al valor en minutos de cuanto ya lleva en el horno
#entonces a el tiempo total le restamos lo que ya lleva en el horno 
#para saber cuanto es lo que nos falta por hornear

def preparation_time_in_minutes(number_of_layers):
    minutos_en_preparar = (number_of_layers * 2)
    return minutos_en_preparar
#cantidad de tiempo segun las capas agregadas que seria el argumento de la funcion
#damos valor a una variable que almacene dicho calculo
#el calculo es number_of_layer * 2 que es los minutos que demoras en preparar cada capa


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    total_de_minutos = (number_of_layers*2 ) +  elapsed_bake_time
    return total_de_minutos
#tiempo total de preparacion  y coccion 
# en nuestra funcion el argumento es los numeros de capas + el tiempo ya transcurrido
# y creamos una variable que almacene el total del tiempo de preparacion
# donde hacemo la suma entre ambos y devolvemos el resultado         