# Guía y Reglas de Modificación de Estilos (Moodle)

Este documento sirve como recordatorio y conjunto de instrucciones para futuras modificaciones de código en los archivos CSS/SCSS y HTML de este proyecto.

## 1. Respetar el orden y las secciones existentes
- **No añadir código al final del archivo de forma indiscriminada.** 
- Antes de agregar nuevas reglas CSS para un elemento, se debe buscar en el archivo si ya existe una sección dedicada a ese componente (por ejemplo, accesibilidad, header, footer, etc.).
- Si el elemento ya tiene estilos previos definidos, cualquier nuevo ajuste o sobreescritura debe añadirse en esa misma línea o sección para mantener la coherencia y facilitar la lectura del código.

## 2. Buscar antes de escribir
- Usar las herramientas de búsqueda (grep, ctrl+f, etc.) para rastrear la clase, ID o etiqueta antes de hacer una modificación.
- Si se trata de un elemento de un plugin (como `local-accessibility-buttoncontainer`), es muy probable que ya se haya estilizado antes para adaptarlo al tema general.

## 3. Manejo de HTML Adicional
- Cualquier inyección en el `html_adicional_conjunto.html` debe seguir la estructura semántica de lo que ya está construido.
- Evitar duplicar scripts o contenedores si ya existe una lógica que hace algo similar (por ejemplo, los observadores del DOM).

## 4. Impacto global vs local
- Al realizar ajustes que pretenden arreglar una página específica (como el login), siempre aislar las reglas CSS usando el selector único de esa página (ej. `body.path-login`).
- Evitar cambios en el layout base (`body`, `.row`, `.container`) que puedan repercutir en los cursos o el dashboard, a menos que sea estrictamente necesario.

## 5. Lógica de Tematización de Aulas (Colores)
El diseño de la plataforma maneja dos tipos de entornos principales que determinan la paleta de colores a utilizar:
- **Aulas Normales (Módulos):** Existen 16 submódulos/módulos regulares. El tema asigna dinámicamente un color acorde al número del módulo mediante clases en el `body` (como `.M1-tema`, `.M5-tema`, etc.) y el uso de variables CSS exclusivas para cada uno (por ejemplo, `--pl-m{n}-primario`).
- **Aula de Capacitación:** Este entorno es diferente e independiente. Tiene su propia identidad gráfica y paleta de colores, gobernada por la clase `.capacitacion-tema` y sus variables propias (`--cap-color-1`, etc.).

Cualquier cambio estructural o visual debe considerar siempre a qué tipo de aula afecta y respetar las variables de color predefinidas para no romper la dinámica visual.

---
*Nota: Mantener este archivo presente al interactuar con asistentes de IA o nuevos desarrolladores para asegurar que el código no se desordene y crezca de forma estructurada.*
