import customtkinter
from PIL import Image
import webbrowser
import teste

def abrir_nova_janela():
    janela2 = customtkinter.CTk()
    janela2.geometry("1080x600")
    janela2.geometry("+200+70")
    janela2.title("3DV5")
    janela2.iconbitmap("arts/favicon.ico")
    janela2.resizable(False, False)
    Frame_principal = customtkinter.CTkFrame(master=janela2, width=1080, height=600, fg_color=("#808080"))
    Frame_principal.pack()
    Frame_lateral = customtkinter.CTkFrame(master=janela2, width=90, height=600, fg_color=("#363636"))
    Frame_lateral.place(x=0, y=0)
    Frame_SEC = customtkinter.CTkFrame(master=janela2, width=990, height=600, fg_color=("#00FF7F"), corner_radius=0)
    Frame_SEC.place(x=90, y=0)


    #BOTAO INSTAGRAM
    inst_image = customtkinter.CTkImage(light_image=Image.open('arts/instagram.png'),
	dark_image=Image.open('arts/instagram.png'),
	size=(43,43)) # Width x Height
    def instbut():
        url = "https://www.instagram.com/eduardo_v.silva/"
        webbrowser.open(url)  
    inst_botao = customtkinter.CTkButton(Frame_lateral, text="", image=inst_image, command=instbut, width=60,fg_color=("#363636") ,hover=True)
    inst_botao.place(x=15, y=13)

    # FUNDO
    ttt2 = customtkinter.CTkImage(light_image=Image.open('arts/arlog.jpg'),
	dark_image=Image.open('arts/arlog.jpg'),
	size=(990,600))
    tttL = customtkinter.CTkLabel(Frame_SEC, image=ttt2, text="")
    tttL.grid(row=0, column=0, padx=(0), pady=(0))

    #BOTAO TESTE
    testi_img = customtkinter.CTkImage(light_image=Image.open('arts/mao.png'),
	dark_image=Image.open('arts/mao.png'),
	size=(43,43)) # Width x Height 
    testi = customtkinter.CTkButton(Frame_lateral, text="", image=testi_img, command=teste.tst, width=60,fg_color=("#363636") ,hover=True)
    testi.place(x=15, y=90)
    

    janela2.mainloop()

