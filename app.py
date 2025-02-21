import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
import plotly.express as px


from librerias.sacarfechas import get_availability
from librerias.guardarSheets import grabarSheets
from librerias.agendarCita import anadirCita




st.set_page_config(page_title='Google Api',page_icon='🐴')

st.title('Formulario')

with st.form('form',clear_on_submit=True):
    nombre = st.text_input('Nombre')
    email = st.text_input('Email')
    telefono = st.text_input('Teléfono')
    fecha = st.date_input('Fecha')
    hora = st.time_input('Hora')
    hora_formato = datetime.combine(datetime.today(),hora)
    hora_fin = (hora_formato + timedelta(hours = 1))
    hora_fin = hora_fin.time()
    if st.form_submit_button('Enviar'):
        grabarSheets(nombre,email,telefono,str(fecha),str(hora),str(hora_fin))
        anadirCita(nombre,email,telefono,fecha,hora,hora_fin)


start_date = st.date_input("Fecha de inicio", value=pd.to_datetime("today"))
end_date = st.date_input("Fecha de fin", value=pd.to_datetime("today") + pd.DateOffset(days=5))

if st.button("Consultar disponibilidad"):
    availability = get_availability(str(start_date), str(end_date))

    date_list = []
    available_hours = []
    occupied_hours = []

    for date, slots in availability.items():
        date_list.append(date)
        available_hours.append(len(slots["available"]))
        occupied_hours.append(len(slots["occupied"]))

    df = pd.DataFrame({
        "Fecha": pd.to_datetime(date_list),
        "Horas Disponibles": available_hours,
        "Horas Ocupadas": occupied_hours
    })

    # 🔥 Gráfico de calor: Horas ocupadas por día
    fig = px.imshow(
        [[occupied_hours[i] if i < len(occupied_hours) else 0 for i in range(len(occupied_hours))]],
        labels=dict(x="Día", y="Horas Ocupadas"),
        x=[f"{d.day}/{d.month}" for d in df["Fecha"]],
        y=["Horas Ocupadas"],
        color_continuous_scale="Reds",
    )

    st.plotly_chart(fig, use_container_width=True)

    # 🕒 Mostrar lista de horarios disponibles y ocupados
    for date, slots in availability.items():
        st.subheader(f"📆 {date}")
        
        if slots["available"]:
            st.write("✅ **Horas disponibles:**")
            for slot in slots["available"]:
                st.write(f"🕒 {slot[0]} - {slot[1]}")

        if slots["occupied"]:
            st.write("❌ **Horas ocupadas:**")
            for slot in slots["occupied"]:
                st.write(f"🚫 {slot[0]} - {slot[1]}")