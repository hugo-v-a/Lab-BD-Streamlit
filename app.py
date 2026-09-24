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

cursor.execute("SELECT Nome, email FROM clientes")
dados = cursor.fetchall()

for nome, email in dados:
    st.write(f"{nome} - {email}")

nome = st.text_input("Nome")
email = st.text_input("Email")

if st.button("Cadastrar"):
    cursor.execute(
        "INSERT INTO clientes (nome, cpf, email) VALUES (%s,%s,%s)",
        (nome, "00000000000", email)
    )
    conn.commit()
    st.success("Cadastrado com sucesso!")