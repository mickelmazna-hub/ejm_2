import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Título del Dashboard
st.title("Dashboard de Repitencia Estudiantil")
st.write("Visualización de datos por facultad y nivel de repitencia.")

# --- TU CÓDIGO DE MATPLOTLIB ADAPTADO ---

# Etiquetas personalizadas del eje X
x_labels = ['Contabilidad', 'Ingeniería\nIndustrial', 'Ingeniería\nMecánica\nde Fluidos', 'Gestión\nTributaria', 'Derecho']
x = np.arange(len(x_labels))  # Posiciones de cada grupo

# Datos manuales por facultad
datos = [
    [504, 146, 25, 7],
    [286, 97, 15, 3],
    [209, 125, 32, 9],
    [256, 89, 21, 7],
    [267, 74, 24, 1]
]

# Colores: azul, naranja, verde, rojo
colores = ['blue', 'orange', 'green', 'red']
n_grupos = len(colores)
bar_width = 0.2 

# 1. Crear la figura explícitamente para Streamlit
fig = plt.figure(figsize=(11, 5))

for i in range(n_grupos):
    valores = [fila[i] for fila in datos]
    totales = [sum(fila) for fila in datos]
    # Evitar división por cero si totales es 0 (seguridad)
    porcentajes = [(v / t * 100) if t > 0 else 0 for v, t in zip(valores, totales)]

    posiciones = x + (i - (n_grupos - 1) / 2) * bar_width 
    barras = plt.bar(posiciones, valores, width=bar_width, color=colores[i])

    # Añadir texto del porcentaje
    for xi, yi, pct in zip(posiciones, valores, porcentajes):
        plt.text(xi + 0.01, yi + 6, f'{pct:.1f}%', ha='center', va='bottom', fontsize=9, color=colores[i])

# Personalización
plt.xticks(x, x_labels, rotation=0, ha='center')
plt.xlabel('Escuela Profesional', fontsize=14)
plt.ylabel('Estudiantes', fontsize=14)
plt.legend([f'{i+1}° Repitencia' for i in range(n_grupos)],
           loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, frameon=False)
plt.grid(axis='y', linestyle='--', alpha=0.4)

# Quitar bordes
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()

# 2. EN LUGAR DE plt.show(), USAMOS ESTO PARA STREAMLIT:
st.pyplot(fig)

# Opcional: Botón para descargar el PDF que generaba tu código
fig.savefig("1_Top5.pdf", bbox_inches='tight')
with open("1_Top5.pdf", "rb") as pdf_file:
    st.download_button(
        label="Descargar gráfico en PDF",
        data=pdf_file,
        file_name="grafico_repitencia.pdf",
        mime="application/pdf"
    )