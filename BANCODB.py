import mysql.connector
from tkinter import messagebox

def conectar_bd():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="EDU",
            password="1234",
            database="login_teste"
        )
        return db
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {err}")
        return None