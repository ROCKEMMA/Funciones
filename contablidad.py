# PRECIO NETO
# Es el precio sin iva, es quien refleja los impuestos

# Mi función
def precioNeto(iva,precio_bruto):
    resultado = precio_bruto / iva
    return resultado

# EJEMPLO
# Datos del producto botella de agua 600ml
producto = "botella de agua 600ml"
precio_bruto = 5
IVA = 1.12
precio_neto = precioNeto(IVA,precio_bruto)
print(f"producto: {producto} \nprodcuto bruto: Q{precio_bruto} precio neto: Q{precio_neto}")
