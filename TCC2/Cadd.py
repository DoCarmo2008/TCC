from tkinter import *
import customtkinter


############ FUNÇÕES ##############
def Logr():
    cad.destroy()
    import Logg

def PagInic():
    try:
        int(entf4_get.get())
    except ValueError:
        from tkinter import messagebox
        messagebox.showerror('Erro!', 'A senha deve conter apenas números!\nTente novamente!')
    else:
        cad.destroy()
        import Logg


####### CONFIGURAÇÕES DE TELA #######
cad = customtkinter.CTkToplevel()
cad.geometry('720x480')
cad.resizable(False, False)
cad.iconbitmap('imgs\ctrlplaylogo.ico')
customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('dark-blue')
cad.title('Cadastrar')

########### FRAME ##############
framm = customtkinter.CTkFrame(cad, width=400, height=500, fg_color='lightgrey').place(x = 10, y = 10)
frame_la = customtkinter.CTkLabel(cad, text='CADASTRAR', text_color='orange', bg_color='lightgrey',font=('IMPACT', 36)).place(x = 120, y = 20)


#region WIDGETS DO FRAME
entf1_get = customtkinter.StringVar(value = '')
entf1_la1 = customtkinter.CTkLabel(cad, text='*Digite seu nome completo (Obrigatório)', text_color='green', bg_color='lightgrey').place(x = 30, y = 80)
entf1 = customtkinter.CTkEntry(cad, placeholder_text='Nome Completo', placeholder_text_color='grey', width=250, textvariable=entf1_get).place(x = 30, y = 100)
entf1_get.get()

entf2_get = customtkinter.StringVar(value = '')
entf1_la1 = customtkinter.CTkLabel(cad, text='*Digite seu nome de usuário(Obrigatório)', text_color='green', bg_color='lightgrey').place(x = 30, y = 140)
entf2 = customtkinter.CTkEntry(cad, placeholder_text='Nome de usuário', placeholder_text_color='grey', width=250, textvariable=entf2_get).place(x = 30, y = 160)
e2 = entf2_get.get()

entf3_get = customtkinter.StringVar(value = '')
entf1_la1 = customtkinter.CTkLabel(cad, text='*Digite seu e-mail(Obrigatório)', text_color='green', bg_color='lightgrey').place(x = 30, y = 200)
entf3 = customtkinter.CTkEntry(cad, placeholder_text='Digite seu e-mail', placeholder_text_color='grey', width=250, textvariable=entf3_get).place(x = 30, y = 220)
e3 = entf3_get.get()

entf4_get = customtkinter.StringVar(value = '')
entf1_la1 = customtkinter.CTkLabel(cad, text='*Crie uma senha(Obrigatório, apenas números)', text_color='green', bg_color='lightgrey').place(x = 30, y = 260)
entf4 = customtkinter.CTkEntry(cad, placeholder_text='Crie uma senha', placeholder_text_color='grey', width=250, textvariable=entf4_get).place(x = 30, y = 280)
e4 = entf4_get.get()


rdsex_variavel = customtkinter.IntVar(value = 0)
rdsex = customtkinter.CTkRadioButton(cad, text='Masculino', bg_color='lightgrey', variable=rdsex_variavel,value=1).place(x = 130, y = 320)
rdsex1 = customtkinter.CTkRadioButton(cad, text='Feminino', bg_color='lightgrey', variable=rdsex_variavel,value=2).place(x = 30, y = 320)
#endregion


######### IMAGEM #############
imf = PhotoImage(file = 'imagens\ctrlplay.png')
imf = imf.subsample(2,2)
imfl = customtkinter.CTkLabel(cad, text='', image=imf).place(x = 430, y = 70)

######### BOTÃO CADASTRO ###########

butt = customtkinter.CTkButton(cad, text='Cadastrar', text_color='white', corner_radius=10, height=40, command=PagInic).place(x = 490, y = 360)

btnlab = customtkinter.CTkLabel(cad, text='ou', text_color='darkorange', font=('Roboto Slab', 14)).place(x = 550, y = 400 )
btn2 = customtkinter.CTkButton(cad, text='LOGIN', fg_color='orange', text_color='darkblue', width=140, height=30,  command=Logr).place(x = 490, y= 430)


