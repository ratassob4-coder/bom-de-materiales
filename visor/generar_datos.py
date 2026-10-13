"""Convierte Estructura_UT.xlsx (hoja Estructura) en datos compactos para el visor web.

Uso: python3 visor/generar_datos.py
Genera visor/datos.json
"""
import json
import os
import openpyxl

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGEN = os.path.join(RAIZ, "Estructura_UT.xlsx")
DESTINO = os.path.join(RAIZ, "visor", "datos.json")

NIVELES = ["Planta", "Proceso", "Ubicación", "Línea", "Función", "Equipo",
           "Sub-equipo", "Sub-sub-equipo", "Material"]
RANGO = {"Planta": 0, "Proceso": 1, "Ubicación": 1, "Línea": 2, "Función": 3,
         "Equipo": 4, "Sub-equipo": 5, "Sub-sub-equipo": 6, "Material": 9}
FUENTES = ["VCH", "TAX", "Lista", "Repuesto", "IH08"]
TIPOS = ["", "REPUESTOS", "SUMINISTROS"]


def num(v):
    if v in (None, ""):
        return 0
    try:
        f = float(v)
    except (TypeError, ValueError):
        return 0
    return int(f) if f == int(f) else round(f, 3)


def txt(v):
    return "" if v is None else str(v).strip()


def main():
    wb = openpyxl.load_workbook(ORIGEN, read_only=True)
    ws = wb["Estructura"]
    filas = ws.iter_rows(values_only=True)
    next(filas)

    materiales = []      # [codigo, nombre, tipo, stock]
    idx_mat = {}
    nodos = []           # ver formato en visor
    pila = []            # (rango, profundidad)

    for r in filas:
        nivel = txt(r[0])
        if nivel not in RANGO:
            continue
        rango = RANGO[nivel]
        while pila and pila[-1][0] >= rango:
            pila.pop()
        prof = pila[-1][1] + 1 if pila else 0
        if nivel != "Material":
            pila.append((rango, prof))

        flags = 0
        for i, _ in enumerate(FUENTES):
            if txt(r[5 + i]):
                flags |= 1 << i
        revisar = 1 if txt(r[15]).upper().startswith("S") else 0
        tipo = txt(r[14])
        if tipo not in TIPOS:
            TIPOS.append(tipo)

        if nivel == "Material":
            codigo = txt(r[1])
            if codigo not in idx_mat:
                idx_mat[codigo] = len(materiales)
                materiales.append([codigo, txt(r[2]), TIPOS.index(tipo), num(r[13])])
            # [nivel, prof, idxMaterial, flags, cantTAX, consVCH, consIW13, revisar, obs]
            fila = [NIVELES.index(nivel), prof, idx_mat[codigo], flags,
                    num(r[10]), num(r[11]), num(r[12]), revisar, txt(r[16])]
        else:
            # [nivel, prof, codigo, nombre, tag, contenido, flags, revisar, obs]
            fila = [NIVELES.index(nivel), prof, txt(r[1]), txt(r[2]), txt(r[3]),
                    txt(r[4]), flags, revisar, txt(r[16])]
        while fila and fila[-1] in ("", 0) and len(fila) > 4:
            fila.pop()
        nodos.append(fila)

    datos = {"niveles": NIVELES, "fuentes": FUENTES, "tipos": TIPOS,
             "materiales": materiales, "nodos": nodos}
    with open(DESTINO, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, separators=(",", ":"))
    print(f"{len(nodos)} filas, {len(materiales)} materiales distintos -> {DESTINO}")


if __name__ == "__main__":
    main()
