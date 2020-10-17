
# Tarea3CriptografiaySeguridadEnRedes

Introducción.

Se Utilizo la librería de crypto tanto en python como javascript para analizar la interoperabilidad entre estas, ademas de interactur con los diferentes formatos de bits.

Desarrollo.

Para comenzar se decidió utilizar hash256 para encriptar el mensaje en python, para esto fue necesario importar la siguiente librería.
*import hashlib 


hash256 pedía trabajar los string en formato UTF-8 para esto se utilizó la función encode('utf-8'), con hashSha256.hexdigest() transformamos el hash a hexadecimal en formato string, este dato fue enviado a la página index de forma oculta.

Lo siguiente fue utilizar Tampermonkey, con esta extensión a través de importaciones simples se podría trabajar con código javascript de forma sincrónica.
Las librerías mas importantes fueron las siguientes.
Main
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/crypto-js.min.js
Inicializador
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/x64-core.min.js
Encriptar y desencriptar formato hexadecimal 
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/enc-hex.min.js
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/format-hex.min.js
Consola
// @grant       GM_log


encryptHex(string) retorna un valor de 256 bits en formato crc32.
Posteriormente se planeaba ejecutar AES para resolver este algoritmo, aun que también se estaba analizando la forma de hacerlo matricialmente , utilizando los bits.
No fue posible hallar una forma eficiente de desencriptar CRC32.

No se logró por terminar de aplicar el algoritmo AES de forma correcta debido al tiempo.

Conclusión

Es fundamental saber de la lógica de los algoritmos para su posterior ejecución y análisis. Tiempo de codificación para ver el funcionamiento de esta librería de forma correcta y creatividad para lograr desencriptar de la forma más óptima a través de cifradores ya estandarizados que podrían alivianar la carga en gran medida. La compatibilidad entre ambos lenguajes no presentó problemas, siendo eficiente.
