import streamlit as st
# --------DISEÑO DE LA PÁGINA----------
st.title("Mi contador de propinas")
st.write("Introduce los datos de la cuenta para poder calcularlos automaticamente")
#----cajas de entrada web-------
cuenta= st.number_input("¿Cuánto costo la comida? (€):", min_value=0.0, step=1.0)
porcentaje= st.number_input("¿Qué porcentaje de propina deseas dejar? (%):", min_value=0, max_value=100, step=1)
amigos= st.number_input("¿Entre cuántas personas se divide la cuenta?:", min_value=1, step=1)
#---------paso de calculos---------
dinero_propina= cuenta*(porcentaje/100)
total_Absoluto= cuenta+dinero_propina
pago_individual= total_Absoluto/amigos
#------mostrar en la web-------
st.write("-RESULTADOS-")
st.metric(label="Dinero de propina total", value=f"{round(dinero_propina, 2)}€")
st.metric(label="Total con propina incluida", value=f"{round(total_Absoluto, 2)}€")
st.metric(label="Cada persona debe de pagar", value=f"{round(pago_individual, 2)}€")