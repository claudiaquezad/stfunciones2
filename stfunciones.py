import streamlit as st

st.title("Código")

tabs = st.tabs([
    "Saludo",
    "Suma",
    "Área del triángulo",
    "Calculadora de descuento",
    "Sumar una lista",
    "Funciones con valores predeterminados",
    "Números pares e impares",
    "Multiplicación con *args",
    "Información de persona con **kwargs",
    "Calculadora flexible"
])

with tabs[0]:
    def saludar(nombre):
        nombre = st.text_input(f"Ingresa tu nombre ({nombre})", value=nombre)
        return f"Hola {nombre}"

    resultado_saludo_1 = saludar("Usuario 1")
    resultado_saludo_2 = saludar("Usuario 2")
    resultado_saludo_3 = saludar("Usuario 3")

    st.text(resultado_saludo_1)
    st.text(resultado_saludo_2)
    st.text(resultado_saludo_3)


with tabs[1]:
    def suma(num1, num2):
        num1 = st.number_input("Ingrese el primer número", value=int(num1))
        num2 = st.number_input("Ingrese el segundo número", value=int(num2))
        resultado = num1 + num2
        return resultado

    resultado_suma = suma(0, 0)
    st.text(f"Resultado: {resultado_suma}")

with tabs[2]:
    def area_del_triangulo(base, altura):
        base = st.number_input("Ingrese la base", value=int(base))
        altura = st.number_input("Ingrese la altura", value=int(altura))
        area = (base * altura) / 2
        return area

    resultado_area = area_del_triangulo(0, 0)
    st.text(f"El área es: {resultado_area}")

with tabs[3]:
    def calcular_precio_final(p_original, porcentaje):
        p_original = st.number_input("Ingrese el precio original", value=int(p_original))
        porcentaje = st.slider("Elija porcentaje %:", min_value=0, max_value=100, value=10, step=1)

        desc = (p_original * porcentaje) / 100
        pr_con_desc = p_original - desc

        impuesto = st.slider("Impuesto %: ", min_value=0, max_value=100, value=16, step=1)
        im = (pr_con_desc * impuesto) / 100
        st.text(f"Cantidad descontada: {desc}")
        st.text(f"Impuesto: {im}")

        final = im + pr_con_desc
        return final

    resultado_descuento = calcular_precio_final(0, 0)
    st.text(f"Total: {resultado_descuento}")

with tabs[4]:
    def sumar_lista(numeros):
        lista = [int(num) for num in numeros if num.strip().isdigit()]
        return sum(lista)

    numeros_input = st.text_input("Ingrese los números de la lista separados por comas", value="")
    numeros = [num.strip() for num in numeros_input.split(',')]

    suma = sumar_lista(numeros)
    st.write(f"La suma de la lista es: {suma}")

with tabs[5]:
    def producto(nombre, cantidad=1, precio_por_unidad=10):
        total = cantidad * precio_por_unidad
        return f"Producto: {nombre}, Cantidad: {cantidad}, Precio por unidad: {precio_por_unidad}, Total a pagar: {total}"

    nombre = st.text_input("Ingrese el nombre del producto")
    cantidad = st.number_input("Ingrese la cantidad", min_value=1, value=1)
    precio_por_unidad = st.number_input("Ingrese el precio por unidad", min_value=1, value=10)

    resultado = producto(nombre, cantidad, precio_por_unidad)
    st.write(resultado)

with tabs[6]:
    def numeros_pares_e_impares(numeros):
        pares = []
        impares = []
        for num in numeros:
            if num % 2 == 0:
                pares.append(num)
            else:
                impares.append(num)
        return pares, impares

    numeros_input = st.text_input("Ingrese una lista de números separados por comas", value="")

    if numeros_input:
        numeros = [int(num.strip()) for num in numeros_input.split(',')]
        pares, impares = numeros_pares_e_impares(numeros)

        st.write(f"Números pares: {pares}")
        st.write(f"Números impares: {impares}")

with tabs[7]:
    def multiplicar_todos(*args):
        if not args:
            return 1
        resultado = 1
        for num in args:
            resultado *= num
        return resultado

    numeros_input = st.text_input("Ingrese los números separados por comas", value="")
    if numeros_input:
        numeros = [int(num.strip()) for num in numeros_input.split(',') if num.strip().isdigit()]
        resultado = multiplicar_todos(*numeros)
        st.write(f"El resultado de multiplicar todos los números es: {resultado}")
    else:
        resultado = multiplicar_todos()
        st.write(f"El resultado predeterminado es: {resultado}")

with tabs[8]:
    def informacion_personal(**kwargs):
        for clave, valor in kwargs.items():
            st.write(f"{clave}: {valor}")

    st.header("Ingrese su información personal")

    nombre = st.text_input("Nombre")
    edad = st.number_input("Edad", min_value=0, step=1)
    direccion = st.text_input("Dirección")
    telefono = st.text_input("Teléfono")
    email = st.text_input("Correo electrónico")

    if st.button("Mostrar información"):
        informacion_personal(
            Nombre=nombre,
            Edad=edad,
            Dirección=direccion,
            Teléfono=telefono,
            Correo_electrónico=email
        )

with tabs[9]:
    def calculadora_flexible(num1, num2, operacion="suma"):
        operaciones = {
            "suma": num1 + num2,
            "resta": num1 - num2,
            "multiplicación": num1 * num2,
            "división": num1 / num2 if num2 != 0 else "Error: División por cero"
        }
        return operaciones.get(operacion, "Operación no válida")

    st.header("Calculadora Flexible")

    num1 = st.number_input("Ingrese el primer número", value=0.0)
    num2 = st.number_input("Ingrese el segundo número", value=0.0)
    operacion = st.selectbox("Seleccione la operación", ["suma", "resta", "multiplicación", "división"])

    resultado = calculadora_flexible(num1, num2, operacion)
    st.write(f"El resultado de la {operacion} es: {resultado}")