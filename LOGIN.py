import mysql.connector
import customtkinter
from tkinter import PhotoImage, END, RIGHT, messagebox
from PIL import Image, ImageTk
import tkinter as tk
import DASHBOARD
import BANCODB

BANCODB.conectar_bd()

def pega_senha():
    usuario = entry1.get()
    senha = entry2.get()
    try:
        db = BANCODB.conectar_bd()
        if db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM usr_pass WHERE usuario = %s AND senha = %s", (usuario, senha))
            resultado = cursor.fetchone()
            if resultado:
                janela.destroy()
                DASHBOARD.abrir_nova_janela()
            else:
                messagebox.showerror("Erro", "Credenciais incorretas")
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao executar a consulta: {err}")
    finally:
        if db:
            db.close()
            
def cad():
    usuario = entry1.get()
    senha = entry2.get()
    try:
        db = BANCODB.conectar_bd()
        if db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO usr_pass (usuario, senha) VALUES (%s, %s)", (usuario, senha))
            db.commit()
            entry1.delete(0, END)
            entry2.delete(0, END)
            messagebox.showinfo("Sucesso", "Pronto para efetuar login") 
            
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao executar a inserção: {err}")
    finally:
        if db:
            db.close()

janela = customtkinter.CTk()
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

janela.geometry("700x400")
janela.geometry("+320+120")
janela.title("3DV5")
janela.iconbitmap("arts/favicon.ico")
janela.resizable(False, False)

# Carregar e redimensionar a imagem
tk_image = PhotoImage(file="arts/brain.png")
pil_image = Image.open("./arts/brain.png")
pil_image = pil_image.resize((pil_image.width // 4, pil_image.height // 4))
tk_image = ImageTk.PhotoImage(pil_image)

# Criação de widgets
label_img = customtkinter.CTkLabel(master=janela, text=None, image=tk_image)
label_img.pack(side="left", padx=(20, 10))

frame = customtkinter.CTkFrame(master=janela, width=350, height=396)
frame.pack(side=RIGHT)

label = customtkinter.CTkLabel(master=frame, text="LOGIN", font=("Roboto", 20, "bold"))
label.place(x=25, y=5)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Nome do usuario", width=300, font=("Roboto", 14))
entry1.place(x=25,y=105)

label1= customtkinter.CTkLabel(master=frame, text="Nome de usuario obrigatorio", text_color="green", font=("Roboto", 8, "bold"))
label1.place(x=25,y=135)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Senha do usuario", width=300, font=("Roboto", 14), show="*")
entry2.place(x=25,y=175)

label2= customtkinter.CTkLabel(master=frame, text="Senha do usuario obrigatorio", text_color="green", font=("Roboto", 8, "bold"))
label2.place(x=25,y=205)

butao = customtkinter.CTkButton(master=frame, text="LOGIN", command=pega_senha, width=300)
butao.place(x=25,y=285)

botao2 = customtkinter.CTkButton(master=frame, text="CADASTRAR", command=cad, width=300)
botao2.place(x=25,y=335)

janela.mainloop()
