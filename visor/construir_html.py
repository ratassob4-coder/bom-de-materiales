"""Arma un único archivo HTML (visor + datos) que se abre con doble clic, sin internet.

Uso: python3 visor/construir_html.py   (antes: python3 visor/generar_datos.py)
Genera visor/BOM_Viacha.html
"""
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
MARCA = '<script id="bom-data" type="application/json"></script>'


def main():
    with open(os.path.join(AQUI, "index.html"), encoding="utf-8") as f:
        pagina = f.read()
    with open(os.path.join(AQUI, "datos.json"), encoding="utf-8") as f:
        datos = f.read().replace("<", "\\u003c")
    assert MARCA in pagina
    pagina = pagina.replace(MARCA, MARCA.replace("></script>", ">" + datos + "</script>"))
    html = ('<!doctype html>\n<html lang="es">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            + pagina + "\n</html>\n")
    destino = os.path.join(AQUI, "BOM_Viacha.html")
    with open(destino, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"{destino} ({os.path.getsize(destino) / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
