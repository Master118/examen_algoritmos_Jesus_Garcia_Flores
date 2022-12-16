# examen_algoritmos_Jesus_Garcia_Flores
Examen de postulacion


Problema 1: Un cliente requiere utilizar sendgrid para envíos de email, pero otro cliente
requiere enviarlos por mandril. Se quiere evitar el uso de IF, y realizar un diseño en donde
podamos utilizar más servicios en caso de que un cliente requiera alguno en específico ¿Qué
patrón de diseño utilizarías y por qué?

Opción 1: Strategy
Usaria la Strategy porque tengo dos clases similares que sólo se diferencien en utilizar sendgrid o mandril
que seria la diferencia de ejecucion. 
Ademas el patrón Strategy me permite extraer en clases separadas, la cual se podra implementar la misma interfaz. 
por lo que el  objeto original delega la ejecución a uno de esos objetos, en lugar de implementar 
todas las variantes del algoritmo.

Lo magino como  que tienes que llegar al trabajo. 
Puedes tomar el metrobús, pedir un uber o ir en metro. Éstas serian mis  estrategias de transporte. 
y Puedo elegir una de las estrategias, dependiendo de factores como el presupuesto o los límites de tiempo.


Opción 2: Factory Method
Opción 3: Adapter


Problema 2: Explica en tus propias palabras la diferencia entre Factory Method y Abstract
Factory. Y proporciona un caso de uso.


Aunque ambas son patrones de diseño creacional tienen las siguientes diferencias

La diferencia principal entre ambos es que Abstract Factory trata con familias de productos, mientras que el Factory Method  se preocupa por un único producto.

Factory Method es un patrón de clase, mientras que Abstract Factory es un patrón de objeto.


Caso de uso Abstract Factory

Un ejemplo lo veo en una torteria Para crear tortas disponemos de un método abstracto en la clase Torteria que será implementada por cada subclase de Torteria.
Concretamente se creará una subclase de Torteria por cada zona, por ejemplo la Pizzería de Ixtapalapa sería TorteriaIxta y la de Neza TorteriaNeza que implementarán el método con los ingredientes de sus zonas.

Las tortas son diferentes según las zonas. No es igual la torta de Ixtapalapa que la torta de Neza.Igualmente, aunque usarán los mismos 
ingredientes (milanesa, queso...) no los obtendrán del mismo lugar, cada zona los comprará donde lo tenga más cerca. Así pues podemos crear un método creador de Torta.

Y asi utilizamos la factoría abstracta (no las concretas de cada zona, como podría ser IngredientesIxta o IngredientesNeza). 
Torta podrá obtener los ingredientes de la factoría independientemente de donde sea. 
Sería fácil crear nuevas factorías y añadirlas al sistema para crear tortas con estos nuevos ingredientes.

Caso de uso Factory Method
Se me ocurre una tienda en la que puedes realizar pagos de diferente manera, en dinero o por pago por tarjeta, 
pero es posible que en un futuro se pueda pagar de más formas.

--------------------------------------------------------------------------------------

El ejercicio 1 lo puede descargar y verificar en un navegador.


--------------------------------------------------------------------------------------
Para el ejercicio 2 lo puede descargar y ejecutar por medio de CMD CON \Python\ejercicio2>python ejercicio2.py
