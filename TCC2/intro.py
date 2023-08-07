import customtkinter
from tkinter import *



#region  ############## FUNÇÕES ###############
def Cade():
    introo.destroy()
    import Cadd

def Loga():
    introo.destroy()
    import Logg
#endregion


#region ########### PÁGINA INTRODUTÓRIA #############
######### Configurações da página #########
introo = customtkinter.CTk()
introo.geometry('720x480')
introo.title('Ctrl Bank')
introo.iconbitmap('imagens\ctrlplay.ico')
customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('dark-blue')
introo.resizable(False, False)


######### IMAGEM #########
imagm = PhotoImage(file = 'imagens\ctrlplay.png')
imagm = imagm.subsample(2,2)
labeil = customtkinter.CTkLabel(introo, image = imagm, text='')
labeil.place(x=10, y = 70)


######### FRAME #########
princ = customtkinter.CTkFrame(introo,width = 400, height = 400, corner_radius=30, fg_color='lightgrey')
princ.place(x = 270, y = 50)


    ######### TEXTO #########
inic = customtkinter.CTkLabel(princ, text = 'Bem-vindo(a) ao Ctrl Bank', font =('IMPACT', 20), text_color='darkblue').place(x=90, y = 50)

inicio = customtkinter.CTkLabel(princ, text = 'Para acessar o app, entre em sua conta ou crie uma!', font =('Calibri', 12), text_color='darkorange').place(x=60, y = 86)


######### BOTÕES #########
btn1 = customtkinter.CTkButton(princ, text='Login', text_color='white', font=('Cambria',15), corner_radius=20, width=300, height=50, command=Loga).place(x=50, y = 160)

pqn = customtkinter.CTkLabel(princ, text = 'OU', font =('Calibri', 12), text_color='darkorange').place(x=195, y = 215)

btn2 = customtkinter.CTkButton(princ, text='Cadastrar', text_color='white', font=('Cambria',15), corner_radius=20, width=300, height=50, border_color='blue', command=Cade).place(x=50, y = 250)

checkz = customtkinter.CTkCheckBox(princ, text = 'Aceito o termos de privadade e declaro que estou de acordo com as regras', text_color='black', font=('Roboto', 10), corner_radius=50).place(x = 20, y = 320)

 #endregion






introo.mainloop()