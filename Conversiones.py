import tkinter as tk
from tkinter import messagebox

def vali(val):
    try:
        return float(val)
    except:
        messagebox.showerror("Error", "Ese número no es válido.")
        return None

def convertir_longitud(tipo, entrada, resultado):
    val = vali(entrada.get())
    if val is None:
        return

    if tipo == "metro_kilometro":
        res = val / 1000
        resultado.config(text=f"{val} m = {res} km")
    elif tipo == "pulgada_metro":
        res = val * 0.0254
        resultado.config(text=f"{val} pulgadas = {res} m")

def convertir_masa(tipo, entrada, resultado):
    val = vali(entrada.get())
    if val is None:
        return

    if tipo == "kilogramo_gramo":
        res = val * 1000
        resultado.config(text=f"{val} kg = {res} g")
    elif tipo == "libra_kilogramo":
        res = val * 0.453592
        resultado.config(text=f"{val} lb = {res} kg")

def convertir_tiempo(tipo, entrada, resultado):
    val = vali(entrada.get())
    if val is None:
        return

    if tipo == "segundo_minuto":
        res = val / 60
        resultado.config(text=f"{val} s = {res} min")
    elif tipo == "hora_dia":
        res = val / 24
        resultado.config(text=f"{val} h = {res} días")

def abrir_formulario(titulo, opciones, funcion_conversion):
    vent = tk.Toplevel()
    vent.title(titulo)
    vent.geometry("350x300")
    vent.configure(bg="#ffeaf2")

    tk.Label(vent, text="Tipo de conversión:", bg="#ffeaf2", font=("Arial", 10, "bold")).pack(pady=10)

    selec = tk.StringVar()
    selec.set(opciones[0][1])

    for texto, valor in opciones:
        tk.Radiobutton(vent, text=texto, variable=selec, value=valor, bg="#ffeaf2").pack()

    tk.Label(vent, text="Valor:", bg="#ffeaf2").pack(pady=5)
    entr = tk.Entry(vent)
    entr.pack()

    result = tk.Label(vent, text="", bg="#ffeaf2", font=("Arial", 10))
    result.pack(pady=10)

    def hacer_conversion():
        tipo = selec.get()
        funcion_conversion(tipo, entr, result)

    tk.Button(vent, text="Convertir", command=hacer_conversion, bg="#f8c8dc", fg="black").pack(pady=10)

princ = tk.Tk()
princ.title("Menú de Conversiones")
princ.geometry("300x300")
princ.configure(bg="#fff0f5")

tk.Label(princ, text="Selecciona una conversión:", bg="#fff0f5", font=("Arial", 11, "bold")).pack(pady=20)

tk.Button(princ, text="Longitud", width=20, bg="#ffc1cc", fg="black", command=lambda: abrir_formulario(
    "Conversión de Longitud",
    [("Metros a Kilómetros", "metro_kilometro"), ("Pulgadas a Metros", "pulgada_metro")],
    convertir_longitud)).pack(pady=10)

tk.Button(princ, text="Masa", width=20, bg="#ffb6c1", fg="black", command=lambda: abrir_formulario(
    "Conversión de Masa",
    [("Kilogramos a Gramos", "kilogramo_gramo"), ("Libras a Kilogramos", "libra_kilogramo")],
    convertir_masa)).pack(pady=10)

tk.Button(princ, text="Tiempo", width=20, bg="#f4a6b7", fg="black", command=lambda: abrir_formulario(
    "Conversión de Tiempo",
    [("Segundos a Minutos", "segundo_minuto"), ("Horas a Días", "hora_dia")],
    convertir_tiempo)).pack(pady=10)

princ.mainloop()
