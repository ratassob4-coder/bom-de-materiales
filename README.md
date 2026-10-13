# bom-de-materiales

## Bom mantenimiento

El archivo `Estructura_UT.html` pesa más de 25 MB y no se puede subir a GitHub.
Está disponible en Google Drive:

👉 [Estructura_UT.html (Google Drive)](https://drive.google.com/file/d/1oiqxZ04-XDNO6B3wz-FFrEtEZ2qCNsy7/view?usp=sharing)

## Visor web

Carpeta `visor/`: visor en línea del árbol de `Estructura_UT.xlsx` (ubicaciones técnicas → equipos → sub-equipos → materiales), con búsqueda por código, TAG o material, lista de materiales por nivel y casos "Para revisar".

- `visor/generar_datos.py` convierte la hoja `Estructura` en `visor/datos.json` (~4,5 MB).
- `visor/index.html` es el visor; necesita `datos.json` en la misma carpeta.

- `visor/BOM_Viacha.html` es un solo archivo (visor + datos) que se abre con doble clic, sin internet. Tiene **Modo edición**: cambiar filas, agregar o eliminar equipos y materiales, **Guardar HTML** (descarga una copia nueva con los cambios) y **Exportar Excel** (estructura completa + hoja de cambios).

Para regenerarlo después de cambiar el Excel: `python3 visor/generar_datos.py && python3 visor/construir_html.py`.
