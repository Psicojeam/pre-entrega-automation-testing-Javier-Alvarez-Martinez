

Testeo Automatizado del Sitio [saucedemo](https://www.saucedemo.com/)

Este proyecto tiene como objetivo realizar pruebas automatizadas sobre el sitio saucedemo.com en un entorno de práctica diseñado para testear aplicaciones web. Las pruebas buscan verificar el funcionamiento correcto de las funcionalidades principales del sitio: el inicio de sesión, la visualización de productos y la gestión del carrito de compras.


                             Propósito del Proyecto

El propósito principal es validar que las funcionalidades clave del sitio funcionen correctamente desde la perspectiva del usuario. Las pruebas cubren:

Inicio de sesión (login) con credenciales válidas e inválidas.

Visualización y selección de productos.

Operaciones básicas del carrito de compras (agregar y quitar productos).

Estas pruebas automatizadas permiten simular flujos de uso reales, detectar errores y asegurar una experiencia de usuario estable.



                             Tecnologías Utilizadas


Python – Como lenguaje principal.

Pytest – Framework de pruebas.

Selenium – Herramienta para automatización de navegadores.

WebDriver – Permite la conexión con el navegador (se uilizó puntualmente ChromeDriver, pero pueden usarse otros modelos según el explorador)

Git y GitHub - para control de versiones


                            Instalación de Dependencias


Asegúrarme de tener Python 3.7+ instalado.

Crear el repositorio o descargar el código fuente.

Desde la terminal, instalar las dependencias ejecutando:

pip install 

Se debe incluir:

pytest
selenium
pytest-html

Descargar automaticamente el WebDriver correspondiente a mi navegador (por ejemplo, ChromeDriver) y asegúrar de que esté incluido en el PATH del sistema.



                            Ejecución de las Pruebas

Para ejecutar todas las pruebas, utilizce el siguiente comando desde la raíz del proyecto:

pytest -v --html=reporte.html


-v: Modo verbose (muestra más detalles).

--html=reporte.html: Genera un reporte HTML con los resultados de la ejecución.

También puedes ejecutar pruebas específicas:

pytest tests/test_login.py



                            Pruebas Incluidas

test_login.py: Pruebas de inicio de sesión (válido e inválido).

test_productos.py: Verifica que los productos se visualicen correctamente.

test_carrito.py: Pruebas para agregar y eliminar productos del carrito.

Reportes y Evidencias
Reporte HTML

Al ejecutar las pruebas con el parámetro --html=reporte.html, se genera automáticamente un reporte detallado en formato HTML que incluye:

Casos de prueba ejecutados.

Estado (éxito o fallo).

Mensajes de error en caso de fallos.

Tiempos de ejecución por prueba.

Este archivo se guardo en la raíz del proyecto.



                            Evidencias Adicionales

Capturas de pantalla automáticas: En caso de fallo, el sistema toma una captura de pantalla del navegador para ayudar en el análisis del error. Estas imágenes se guardan en una carpeta específica (/screenshots).

Este proyecto permite automatizar pruebas básicas pero esenciales de saucedemo.com, asegurando que el flujo de usuario más importante esté siempre funcionando correctamente. Además, los reportes y evidencias facilitan el análisis posterior de fallos y comportamientos inesperados.

