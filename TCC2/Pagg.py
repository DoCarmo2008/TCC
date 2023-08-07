from tkinter import *
import customtkinter
import webbrowser
from Cadd import entf2_get
#region Funções da página


def Saldoo():
    from Cadd import entf2_get
    frm_pric = customtkinter.CTkFrame(pag, width=500, fg_color='#ebebec', bg_color='#ebebec', height=800).place(x = 250, y = 0)

    hi = customtkinter.CTkLabel(pag, text='Olá, ' + str(entf2_get.get()), text_color='black', bg_color='#ebebec', font=('Roboto Slab', 15)).place(x = 300, y = 20 )
    frm1 = customtkinter.CTkFrame(pag, bg_color='#ebebec', fg_color='white', border_width=0.6, border_color='black', corner_radius=30, width= 400, height=150).place(x = 280, y = 50)
    frm1_text = customtkinter.CTkLabel(pag, text='Saldo disponível', text_color='black', bg_color='white', font=('Roboto Slab', 10)).place(x = 310, y = 80 )
    saldi = 100.00
    frm1_text2 = customtkinter.CTkLabel(pag, text=saldi, text_color='black', bg_color='white', font=('Roboto Slab', 40)).place(x = 300, y = 100 )


    #Meu Cartão

    #region Função 1
    def Cardzin():
        card = customtkinter.CTkToplevel()
        card.geometry('350x350')
        card.resizable(False, False)
        card.iconbitmap('imgs\ctrlplaylogo.ico')
        customtkinter.set_appearance_mode('light')
        customtkinter.set_default_color_theme('dark-blue')
        card.title('Meu Cartâo')

        cardpic = PhotoImage(file='imgs\cart.png')
        cardpic = cardpic.subsample(3,3)
        cardpic_lab = customtkinter.CTkLabel(card, text='', image=cardpic).place(x = 0, y= 0)

    #endregion

    subbtn1 = customtkinter.CTkButton(pag, text='', width=400, height=45, bg_color='#ebebec', fg_color='lightgrey', border_color='black', border_width=0.6, corner_radius=10, command=Cardzin).place(x = 280, y = 250)
    subt1 = customtkinter.CTkLabel(pag, text='Meu Cartão', text_color='Black',bg_color='lightgrey', font=('Arial Black', 17)).place(x = 300, y = 257)
    setaind = PhotoImage(file='imgs\images-removebg-preview (1).png')
    setaind = setaind.subsample(7,7)
    setalab = customtkinter.CTkLabel(pag, text='', image=setaind, bg_color='lightgrey').place(x = 640, y = 256)

    #Código de barra

    subbtn2 = customtkinter.CTkButton(pag, text='', width=400, height=45, bg_color='#ebebec', fg_color='lightgrey', border_color='black', border_width=0.6, corner_radius=10, command=lambda: webbrowser.open('https://pageloot.com/pt/leitor-de-codigos-de-barra/')).place(x = 280, y = 320)
    subt2 = customtkinter.CTkLabel(pag, text='Código de barra', text_color='Black',bg_color='lightgrey', font=('Arial Black', 17)).place(x = 300, y = 327)
    setalab = customtkinter.CTkLabel(pag, text='', image=setaind, bg_color='lightgrey').place(x = 640, y = 326)

    #Recarregar celular
    #region Função 2
    def Qrcodee():
        from tkinter import messagebox
        asking = messagebox.askyesno('Aviso!', 'A página que você está preste a entrar, necessita de uso de um celular com leitor de QRCode.\n Deseja continuar?')
        if asking == True:
            cqr = customtkinter.CTkToplevel()
            cqr.geometry('160x160')
            cqr.resizable(False, False)
            cqr.iconbitmap('imgs\ctrlplaylogo.ico')
            customtkinter.set_appearance_mode('light')
            customtkinter.set_default_color_theme('dark-blue')
            cqr.title('Recarga de celular')

            cqrpic = PhotoImage(file='imgs\qrcode.png')
            cqrpic = cqrpic.subsample(1,1)
            cqrpic_lab = customtkinter.CTkLabel(cqr, text='', image=cqrpic).place(x = 0, y= 0)

    #endregion
    subbtn3 = customtkinter.CTkButton(pag, text='', width=400, height=45, bg_color='#ebebec', fg_color='lightgrey', border_color='black', border_width=0.6, corner_radius=10,command=Qrcodee).place(x = 280, y = 390)
    subt3 = customtkinter.CTkLabel(pag, text='Recarregar Celular', text_color='Black',bg_color='lightgrey', font=('Arial Black', 17)).place(x = 300, y = 397)
    setalab = customtkinter.CTkLabel(pag, text='', image=setaind, bg_color='lightgrey').place(x = 640, y = 396)

def Transfere():
    frm_pric = customtkinter.CTkFrame(pag, width=500, fg_color='#ebebec', bg_color='#ebebec', height=800).place(x = 250, y = 0)

    #Depositante
    hi = customtkinter.CTkLabel(pag, text='Depositante', text_color='black', bg_color='#ebebec', font=('Roboto Slab', 15)).place(x = 300, y = 20 )
    frm1 = customtkinter.CTkFrame(pag, bg_color='#ebebec', fg_color='orange', border_width=0.6, border_color='black', corner_radius=30, width= 400, height=150).place(x = 280, y = 50)

    entt1_text = customtkinter.CTkLabel(pag, text='*Nome Completo (Confirmação)', text_color='darkgreen', bg_color='orange', font=('Roboto Slab', 10)).place(x = 295, y = 65 )

    entt1_get = customtkinter.StringVar(value = '')
    entt1 = customtkinter.CTkEntry(pag, placeholder_text='Nome Completo (Confirmação)', placeholder_text_color='grey',bg_color='orange', width=250, textvariable=entt1_get ).place(x = 290, y = 90)
    entt1_get.get()

    entt2_text = customtkinter.CTkLabel(pag, text='*Quantia que deseja depositar', text_color='darkgreen', bg_color='orange', font=('Roboto Slab', 10)).place(x = 295, y = 115 )

    entt2_get = customtkinter.StringVar(value = '')
    entt2 = customtkinter.CTkEntry(pag, placeholder_text='Quantia que deseja depositar', placeholder_text_color='grey',bg_color='orange', width=250, textvariable=entt2_get).place(x = 290, y = 140)
    entt2_get.get()

    #Recebinte
    hi2 = customtkinter.CTkLabel(pag, text='Recebinte', text_color='black', bg_color='#ebebec', font=('Roboto Slab', 15)).place(x = 300, y = 220 )
    frm2 = customtkinter.CTkFrame(pag, bg_color='#ebebec', fg_color='#1184b7', border_width=0.6, border_color='black', corner_radius=30, width= 400, height=150).place(x = 280, y = 250)

    entt3_text = customtkinter.CTkLabel(pag, text='*Nome Completo (Recebinte)', text_color='white', bg_color='#1184b7', font=('Roboto Slab', 10)).place(x = 295, y = 265 )

    entt3_get = customtkinter.StringVar(value = '')
    entt3 = customtkinter.CTkEntry(pag, placeholder_text='Nome Completo (Recebinte)', placeholder_text_color='grey',bg_color='#1184b7', width=250, textvariable=entt3_get).place(x = 290, y = 290)
    entt3_get.get()

    entt4_text = customtkinter.CTkLabel(pag, text='*Número da conta (Recebinte)', text_color='white', bg_color='#1184b7', font=('Roboto Slab', 10)).place(x = 295, y = 324 )

    entt4_get = customtkinter.StringVar(value = '')
    entt4 = customtkinter.CTkEntry(pag, placeholder_text='Número da conta (Recebinte)', placeholder_text_color='grey',bg_color='#1184b7', width=250, textvariable=entt4_get).place(x = 290, y = 350)
    entt4_get.get()


    def Comprovante():
        
        comp = customtkinter.CTkToplevel()
        comp.geometry('300x450')
        comp.resizable(False, False)
        comp.iconbitmap('imgs\ctrlplaylogo.ico')
        customtkinter.set_appearance_mode('light')
        customtkinter.set_default_color_theme('dark-blue')
        comp.title('Comprovante de transferência')



        comp_frm = customtkinter.CTkFrame(comp, fg_color='#f6f0ab', width=300, height=450).place(x= 0, y =0)
        comp_lab = customtkinter.CTkLabel(comp, text='Comprovante Fiscal \n\n -------------------------------------------------', text_color='black',bg_color='#f6f0ab', font=('Roboto Slab', 13)).place(x = 45, y = 30)

        comp_lab2 = customtkinter.CTkLabel(comp, text='Dados do depositante: \n\nNome: '+ str(entt1_get.get()) + '\nValor depositado: R$' + str(entt2_get.get()) + '\n\n\nDados do recebinte: \n\nNome: ' + str(entt3_get.get()) + '\nNúmero da conta: ' + str(entt4_get.get()) + '\n\n -------------------------------------------------\n\n Data: 02/08/2023', bg_color='#f6f0ab', font=('Roboto Slab', 14)).place(x = 30, y = 90)

    def Conferir():
            try:
                float(entt2_get.get())
            except ValueError:
                from tkinter import messagebox
                messagebox.showerror('Error!', 'Digite o valor da transferência corretamente, tente novamente!')
            else:
                try:
                    int(entt4_get.get())
                except ValueError:
                    from tkinter import messagebox
                    messagebox.showerror('Error!', 'Digite o número da conta corretamente, tente novamente!')

                else:
                    Comprovante()

         


        
    transbtn = customtkinter.CTkButton(pag, text='Transferir', text_color='blue', fg_color='orange', command=Conferir).place(x = 420, y = 430)

def Saqq():
    frm_pric = customtkinter.CTkFrame(pag, width=500, fg_color='#ebebec', bg_color='#ebebec', height=800).place(x = 250, y = 0)

    frm1 = customtkinter.CTkFrame(pag, bg_color='#ebebec', fg_color='#a8cef6', border_width=0.6, border_color='black', corner_radius=30, width= 400, height=400).place(x = 280, y = 50)

    saqimg = PhotoImage(file='imgs\pngtree-cartoon-hand-drawn-customer-service-voice-communication-illustration-png-image_2162274-removebg-preview.png')
    saqimg = saqimg.subsample(6,6)
    saqlabe = customtkinter.CTkLabel(pag, text='', bg_color='#a8cef6',image=saqimg).place(x=440, y = 70)

    llabb = customtkinter.CTkLabel(pag, text='CTRL BANK(TEL): \n\(31) 3582-8726', text_color='black',bg_color='#a8cef6', font=('Arial black', 15)).place(x = 410, y = 160)

    llabb2 = customtkinter.CTkLabel(pag, text='Nos envie uma mensagem', text_color='black',bg_color='#a8cef6', font=('Arial black', 15)).place(x = 376, y = 220)

    llabb2_entt = customtkinter.CTkEntry(pag, width=250, height= 190, placeholder_text='Envie sua mensagem').place(x = 355, y = 250)

    def Mensag():
        from tkinter import messagebox
        messagebox.showinfo('Mensagem | SAQ', 'Mensagem enviada com sucesso! Nossos atendentes irão entrar em contato, o mais breve possível!')
        Saqq()

    llabb2_entt_btn = customtkinter.CTkButton(pag, height=20,text='Enviar',command=Mensag ,corner_radius=70).place(x = 410, y = 455)
#endregion

#region Configurações da janela
pag = customtkinter.CTkToplevel()
pag.geometry('720x480')
pag.resizable(False, False)
pag.iconbitmap('imgs\ctrlplaylogo.ico')
customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('dark-blue')
pag.title('Página principal')
#endregion

#region FRAME LATERAL
frame_lat = customtkinter.CTkFrame(pag, fg_color='#6666FF', width=250, height=800).place(x = 0, y = 0)
frm_lat_lab = customtkinter.CTkLabel(pag, text='CTRL BANK', bg_color='#6666FF',text_color='white', font=('IMPACT', 25)).place( x = 100, y = 50)

frm_img = PhotoImage(file = 'imagens\ctrlplay.png')
frm_img = frm_img.subsample(8,8)
frm_img_lab = customtkinter.CTkLabel(pag, text='', image=frm_img, bg_color='#6666FF').place(x = 30, y = 25)

btnsald = customtkinter.CTkButton(pag, text='Saldo', width=250, height=50, text_color='white', fg_color='#6666FF', bg_color='#6666FF', font=('Roboto Slab', 20), command=Saldoo).place(x = 0, y = 120)

btntrans = customtkinter.CTkButton(pag, text='Transferência', width=250, height=50, text_color='white', fg_color='#6666FF', bg_color='#6666FF', font=('Roboto Slab', 20), command=Transfere).place(x = 0, y = 170)

btnsaq = customtkinter.CTkButton(pag, text='SAQ', width=250, height=50, text_color='white', fg_color='#6666FF', bg_color='#6666FF', font=('Roboto Slab', 20), command=Saqq).place(x = 0, y = 220)


def LogOutt():
    pag.destroy()
    import Logg

btnlt = customtkinter.CTkButton(pag, text='< Log Out', text_color='white', bg_color='#6666FF', fg_color='#6666FF', font=('Roboto Slab', 10),command=LogOutt).place(x = 0, y = 430 )


#Imagens
frml_img1 = PhotoImage(file='imgs\download-removebg-preview (2).png')
frml_img1 = frml_img1.subsample(6,6)
frml_lab1 = customtkinter.CTkLabel(pag,  text='', image=frml_img1, bg_color='#6666FF').place(x = 50, y = 125 )

frml_img2 = PhotoImage(file='imgs\download-removebg-preview (1).png')
frml_img2 = frml_img2.subsample(6,6)
frml_lab2 = customtkinter.CTkLabel(pag,  text='', image=frml_img2, bg_color='#6666FF').place(x = 25, y = 175 )

frml_img3 = PhotoImage(file='imgs\download-removebg-preview.png')
frml_img3 = frml_img3.subsample(6,6)
frml_lab3 = customtkinter.CTkLabel(pag,  text='', image=frml_img3, bg_color='#6666FF').place(x = 55, y = 228 )

#endregion

#region FRAME PRINCIPAL
frm_pric = customtkinter.CTkFrame(pag, width=500, fg_color='#ebebec', bg_color='#ebebec', height=800).place(x = 250, y = 0)

hi = customtkinter.CTkLabel(pag, text='Olá, '+ str(entf2_get.get()), text_color='black', bg_color='#ebebec', font=('Roboto Slab', 15)).place(x = 300, y = 20 )
frm1 = customtkinter.CTkFrame(pag, bg_color='#ebebec', fg_color='white', border_width=0.6, border_color='black', corner_radius=30, width= 400, height=150).place(x = 280, y = 50)
frm1_text = customtkinter.CTkLabel(pag, text='Saldo disponível', text_color='black', bg_color='white', font=('Roboto Slab', 10)).place(x = 310, y = 80 )
saldi = 100.00
frm1_text2 = customtkinter.CTkLabel(pag, text=saldi, text_color='black', bg_color='white', font=('Roboto Slab', 40)).place(x = 300, y = 100 )



#Meu Cartão

#region Função 1
def Cardzin():
    card = customtkinter.CTkToplevel()
    card.geometry('350x350')
    card.resizable(False, False)
    card.iconbitmap('imgs\ctrlplaylogo.ico')
    customtkinter.set_appearance_mode('light')
    customtkinter.set_default_color_theme('dark-blue')
    card.title('Meu Cartâo')

    cardpic = PhotoImage(file='imgs\cart.png')
    cardpic = cardpic.subsample(3,3)
    cardpic_lab = customtkinter.CTkLabel(card, text='', image=cardpic).place(x = 0, y= 0)

#endregion

subbtn1 = customtkinter.CTkButton(pag, text='', width=400, height=45, bg_color='#ebebec', fg_color='lightgrey', border_color='black', border_width=0.6, corner_radius=10, command=Cardzin).place(x = 280, y = 250)
subt1 = customtkinter.CTkLabel(pag, text='Meu Cartão', text_color='Black',bg_color='lightgrey', font=('Arial Black', 17)).place(x = 300, y = 257)
setaind = PhotoImage(file='imgs\images-removebg-preview (1).png')
setaind = setaind.subsample(7,7)
setalab = customtkinter.CTkLabel(pag, text='', image=setaind, bg_color='lightgrey').place(x = 640, y = 256)

#Código de barra

subbtn2 = customtkinter.CTkButton(pag, text='', width=400, height=45, bg_color='#ebebec', fg_color='lightgrey', border_color='black', border_width=0.6, corner_radius=10, command=lambda: webbrowser.open('https://pageloot.com/pt/leitor-de-codigos-de-barra/')).place(x = 280, y = 320)
subt2 = customtkinter.CTkLabel(pag, text='Código de barra', text_color='Black',bg_color='lightgrey', font=('Arial Black', 17)).place(x = 300, y = 327)
setalab = customtkinter.CTkLabel(pag, text='', image=setaind, bg_color='lightgrey').place(x = 640, y = 326)

#Recarregar celular
#region Função 2
def Qrcodee():
    from tkinter import messagebox
    asking = messagebox.askyesno('Aviso!', 'A página que você está preste a entrar, necessita de uso de um celular com leitor de QRCode.\n Deseja continuar?')
    if asking == True:
        cqr = customtkinter.CTkToplevel()
        cqr.geometry('160x160')
        cqr.resizable(False, False)
        cqr.iconbitmap('imgs\ctrlplaylogo.ico')
        customtkinter.set_appearance_mode('light')
        customtkinter.set_default_color_theme('dark-blue')
        cqr.title('Recarga de celular')

        cqrpic = PhotoImage(file='imgs\qrcode.png')
        cqrpic = cqrpic.subsample(1,1)
        cqrpic_lab = customtkinter.CTkLabel(cqr, text='', image=cqrpic).place(x = 0, y= 0)

#endregion
subbtn3 = customtkinter.CTkButton(pag, text='', width=400, height=45, bg_color='#ebebec', fg_color='lightgrey', border_color='black', border_width=0.6, corner_radius=10,command=Qrcodee).place(x = 280, y = 390)
subt3 = customtkinter.CTkLabel(pag, text='Recarregar Celular', text_color='Black',bg_color='lightgrey', font=('Arial Black', 17)).place(x = 300, y = 397)
setalab = customtkinter.CTkLabel(pag, text='', image=setaind, bg_color='lightgrey').place(x = 640, y = 396)

#endregion
