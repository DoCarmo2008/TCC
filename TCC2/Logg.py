from tkinter import *
import customtkinter
from Cadd import entf2_get
from Cadd import entf4_get

#region Functions
####### BOTÃO DE VOLTAR #########
def Cadas():
  janl.destroy()
  import Cadd
    
def Logar():
  try:
    int(senha_get.get())
  except ValueError:
    from tkinter import messagebox
    messagebox.showerror('Erro!', 'A senha só pode ser digitada em números\nTente novamente')
  

  if int(senha_get.get()) != int(entf4_get.get()):
    from tkinter import messagebox
    messagebox.showerror('Erro!', 'A senha não corresponde com a cadastrada\nTente novamente')
  elif str(usuario_get.get()) != str(entf2_get.get()):
    from tkinter import messagebox
    messagebox.showerror('Erro!', 'Nome de usuário não corresponde com a cadastrada\nTente novamente')
  else:
    janl.destroy()
    import Pagg


#endregion
  
######### JANELA #########
    
janl = customtkinter.CTkToplevel()
janl.geometry('720x480')
janl.title('Login - Ctrl Bank')
janl.iconbitmap('imagens\ctrlplay.ico')
customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('dark-blue')
janl.resizable(False, False)
    
    

######### FRAME #########
fram1 = customtkinter.CTkFrame(janl, width = 370, height = 460, corner_radius=30, fg_color='lightgrey')
fram1.pack(side=RIGHT)

######### IMAGEM #########
imag = PhotoImage(file = 'imagens\ctrlplay.png')
imag = imag.subsample(2,2)
labei = customtkinter.CTkLabel(janl, image = imag, text='')
labei.place(x=50, y = 100)

######### WIDGETS #########
inicio = customtkinter.CTkLabel(fram1, text = 'LOGIN', text_color='darkorange',font=('IMPACT',40)).place(x=140, y = 40)

usuario_get = customtkinter.StringVar(value='')
usuario = customtkinter.CTkEntry(fram1, placeholder_text='Digite seu nome de usuário', placeholder_text_color='darkgray', width = 250, textvariable=usuario_get)
usuario.place(x=50,y=130)
usuario_get.get()

usuariotxt = customtkinter.CTkLabel(fram1, text = '*Opção obrigatória', text_color='darkblue',font=('Roboto',10))
usuariotxt.place(x=50,y=160)

senha_get = customtkinter.StringVar(value = '')
senha = customtkinter.CTkEntry(fram1, placeholder_text='Digite sua senha (apenas números)', placeholder_text_color='gray', width = 250, show = '*', textvariable=senha_get)
senha.place(x=50,y=200)
senha_get.get()

usuariotxtt = customtkinter.CTkLabel(fram1, text = '*Opção obrigatória', text_color='darkblue',font=('Roboto',10))
usuariotxtt.place(x=50,y=230)

check = customtkinter.CTkCheckBox(fram1, text = 'Lembrar de mim', corner_radius=10).place(x=50, y = 270)

btn = customtkinter.CTkButton(fram1, text = 'LOGIN', text_color='white', command=Logar).place(x=100, y= 320)

btnlab = customtkinter.CTkLabel(fram1, text='ou', text_color='darkorange', font=('Roboto Slab', 14)).place(x = 160, y = 350 )
btn2 = customtkinter.CTkButton(fram1, text='CADASTRE-SE', fg_color='orange', text_color='darkblue', width=140, height=30,  command=Cadas).place(x = 100, y= 385)