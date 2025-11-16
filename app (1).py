import streamlit as st
import pandas as pd
import statsmodels.api as sm
from scipy.stats import chi2_contingency
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Análisis Estadístico – UCBAdmissions (Chi Cuadrado)")
st.subheader("Estudiante: Jhostin Agámez – Nº53")

# Cargar dataset
df_raw = sm.datasets.get_rdataset("UCBAdmissions", "datasets").data
df = df_raw.copy()

st.write("### Datos originales")
st.dataframe(df)

# Tabla de contingencia Sexo vs Admisión
tabla = pd.pivot_table(df, values="Freq", index="Gender", columns="Admit", aggfunc="sum")

st.write("### Tabla de contingencia")
st.dataframe(tabla)

# Chi cuadrado
chi2, p, dof, expected = chi2_contingency(tabla)

st.write("### Resultados de la prueba Chi²")
st.write(f"**Chi²:** {chi2:.4f}")
st.write(f"**p-valor:** {p:.4f}")
st.write(f"**Grados de libertad:** {dof}")
st.write("**Frecuencias esperadas:**")
st.write(expected)

# Interpretación automática
st.write("### Interpretación")
if p < 0.05:
    st.success("Existe evidencia estadística para afirmar que hay asociación entre el género y la admisión en la universidad.")
else:
    st.info("No existe evidencia estadística suficiente para afirmar una asociación entre género y admisión.")

# Gráfico
st.write("### Visualización")
fig, ax = plt.subplots()
sns.barplot(data=df, x="Gender", y="Freq", hue="Admit", ax=ax)
st.pyplot(fig)
