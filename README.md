# bom-de-materiales

## Bom mantenimiento

El archivo `Estructura_UT.html` pesa más de 25 MB y no se puede subir a GitHub.
Está disponible en Google Drive:

👉 [Estructura_UT.html (Google Drive)](https://drive.google.com/file/d/1oiqxZ04-XDNO6B3wz-FFrEtEZ2qCNsy7/view?usp=sharing)

## Visor web

Carpeta `visor/`: visor en línea del árbol de `Estructura_UT.xlsx` (ubicaciones técnicas → equipos → sub-equipos → materiales), con búsqueda por código, TAG o material, lista de materiales por nivel y casos "Para revisar".

- `visor/generar_datos.py` convierte la hoja `Estructura` en `visor/datos.json` (~4,5 MB).
- `visor/index.html` es el visor; necesita `datos.json` en la misma carpeta.

Para actualizarlo después de cambiar el Excel: `python3 visor/generar_datos.py`.
