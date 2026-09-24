import streamlit as st
import psycopg2 

conn = psycopg2.connect(
    host = st.secrets["DB_HOST"],
    database = st.secrets["DB_NAME"],
    user = st.secrets["DB_USER"],
    password = st.secrets["DB_PASSWORD"],
    port = st.secrets["DB_PORT"]
)

cursor = conn.cursor()

st.title("Sistema de Cadastro")
st.write("Bem-vindo ao sistema!")

cursor.execute("SELECT Nome, email FROM cliente")
dados = cursor.fetchall()

for nome, email in dados:
    st.write(f"{nome} - {email}")