from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Function import *
from tkinter import *
import pyautogui as pg
import pandas as pd
import time
import os
from datetime import datetime
import openpyxl as xl
import pysnooper


class Instagram_bot ():
    def __init__(self):
        
        #Variaveis//////////////////
        self.color1 = '#121212' #Gray Fundo
        self.color2 = '#000000' #Black Destaque
        self.color3 = '#262626' #Light Gray Inputs
        self.color4 = '#ff254a' #Purple Detals
        self.color5 = '#ffca00' #Yellow 
        self.root_config = None
        
        self.window()
        
    def window(self):
        self.root = Tk()
        self.root.geometry(center(self.root,600,610))
        self.root.config(bg=self.color1)
        self.root.title('Followers Bot')
        self.root.iconbitmap('img\icon.ico')
        self.containers()
        self.itens_container1()
        self.itens_container2()
        self.root.mainloop()
    
    def containers(self):
        self.img_logo = PhotoImage(file=f'img\LOGO.png')
        self.img_btn_config = PhotoImage(file=r'img\btn_config.png')
        self. btn_config = Button(
            self.root,
            bg=self.color1,
            height=25,
            border=0,
            image=self.img_btn_config,
            activebackground=self.color1,
            command=self.window_config
        )
        self.lb_title = Label(
            self.root,
            image= self.img_logo,
            fg= self.color4,
            bg=self.color1
        )
        
        self.fr_container01 = Frame(
            self.root,
            width=310,
            height= 230,
            bg=self.color1
        )
        
        self.fr_container02 = Frame(
            self.root,
            width=550,
            height= 300,
            bg=self.color1
        )
        self. btn_config.pack(anchor=E, padx=10, pady=5)
        self.fr_container01.propagate(0)
        self.fr_container02.propagate(0)
        self.lb_title.pack()
        self.fr_container01.pack()
        self.fr_container02.pack()
        
    def itens_container1(self):
        
        #Variaveis para o Check_Button
        self.chkValue = BooleanVar() 
        self.chkValue.set(True)
        
        self.lb_usuario = Label(
            self.fr_container01,
            text="Telefone, nome de usuario ou email",
            bg=self.color1,
            fg=self.color3
        )
        
        self.en_usuario = Entry(
            self.fr_container01,
            bg=self.color3,
            width=35,
            font='15',
            fg='white',
            bd=0
        )
        
        self.lb_senha = Label(
            self.fr_container01,
            text="Senha",
            bg=self.color1,
            fg=self.color3
        )
         
        self.en_senha = Entry(
            self.fr_container01,
            bg=self.color3,
            width=35,
            font='15',
            show="*",
            fg='white',
            bd=0
        )
        
        self.lb_perfil_concorrente = Label(
            self.fr_container01,
            text="Perfil concorrente Ex: exemplo_perfil",
            bg=self.color1,
            fg=self.color3
        )
        
        self.en_perfil_concorrente = Entry(
            self.fr_container01,
            bg=self.color3,
            width=35,
            font='15',
            fg='white',
            bd=0
        )
        
        self.lb_qtd_user = Label(
            self.fr_container01,
            text="Quantidade de seguidores max 100",
            bg=self.color1,
            fg=self.color3
        )
        
        self.en_qtd_user = Entry(
            self.fr_container01,
            bg=self.color3,
            width=35,
            font='15',
            fg='white',
            bd=0
        )
        self.contaier_relembrar = Frame(
            self.fr_container01,
            bg=self.color1,
            width=35
        )
        self.lb_relembrar = Label(
            self.contaier_relembrar,
            text="Lembrar dados",
            bg=self.color1,
            fg=self.color3
        )
        self.ck_relembrar = Checkbutton(
            self.contaier_relembrar,
            bg=self.color1,
            bd=0,
            activebackground=self.color1,
            fg=self.color4,
            var = self.chkValue
        )
        
        self.btn_comecar = Button(
            self.fr_container01,
            bg=self.color4,
            fg='white',
            text="INICIAR",
            command=self.login,
            activebackground=self.color5,
            width=50
        )
        
        
        # Lendo o arquivo para 
        if os.path.exists('login.txt'):
            #Lendo o arquivo
            arquivo = open('login.txt','r')
            info_login = []
            for i in arquivo:
                i.replace('\n', '')
                info_login.append(i)
            arquivo.close()
            
            # Removendo dados antes de colocar novos
            self.en_usuario.delete(0, END)
            self.en_senha.delete(0, END)
            self.en_perfil_concorrente.delete(0, END)
            self.en_qtd_user.delete(0, END)
            
            # Colocando os valores salvos
            self.en_usuario.insert(0, info_login[0])
            self.en_senha.insert(0, info_login[1])
            self.en_perfil_concorrente.insert(0, info_login[2])
            self.en_qtd_user.insert(0, info_login[3])
            
        self.lb_usuario.pack(anchor=W)
        self.en_usuario.pack(anchor=W)
        self.lb_senha.pack(anchor=W)
        self.en_senha.pack(anchor=W)
        self.lb_perfil_concorrente.pack(anchor=W)
        self.en_perfil_concorrente.pack(anchor=W)
        self.lb_qtd_user.pack(anchor=W)
        self.en_qtd_user.pack(anchor=W)
        self.contaier_relembrar.pack(anchor=E)
        self.lb_relembrar.grid(row=0,column=0)
        self.ck_relembrar.grid(row=0, column=1)
        self.btn_comecar.pack(pady=5)
          
    def itens_container2(self):
        self.tempo_estimado = StringVar()
        self.tempo_estimado.set('Tempo estimado: ')
        self.lb_output = Label(
            self.fr_container02,
            text='Informações ao vivo:',
            bg=self.color1,
            fg=self.color3
        )
        self.tx_output = Text(
            self.fr_container02,
            bg=self.color3,
            width=550,
            height=15,
            fg= self.color5,
            bd=2
        )
        
        self.lb_tempo_estimado = Label(
            self.fr_container02,
            textvariable=self.tempo_estimado,
            bg=self.color1,
            fg=self.color3
        )
        
        self.lb_output.pack(anchor=W)
        self.tx_output.pack()
        self.lb_tempo_estimado.pack(anchor=W)
        
    def gerar_excel(self):
        data_atual = datetime.today().strftime('%d/%m/%Y')
        hora_atual = datetime.today().strftime('%H:%M')
        try:
            if os.path.exists(f'Followers.xlsx'):
                book = xl.load_workbook(f'Followers.xlsx')
                planilha = book['Sheet']
                planilha.append([str(data_atual),str(hora_atual),self.name_seg,'Seguindo',self.perfil_concorrente])
            
            else:
                #Criando e adicionado itens na planilha
                book = xl.Workbook()
                planilha = book['Sheet']
                planilha.append(['DATA','HORA','PESSOA','STATUS','PERFIL'])
                planilha.append([str(data_atual),str(hora_atual),self.name_seg,'Seguindo',self.perfil_concorrente])
            #Salvando arquivo
            book.save(f'Followers.xlsx')
        except PermissionError:
            pg.alert(f'A planilha Followers.xlsx pode estar aberta feche para continuar!')
            self.tx_output.insert(END, f'\nHOUVE ALGUM ERRO NO MOMENTO DE GRAVAR OS DADOS NO EXCEL\nCERTIFIQUE-SE QUE A PLANILHA "Followers.xlsx" ESTEJA FECHADA!\n')
            self.tx_output.insert(END, '-'*65)
            
        except:
            self.tx_output.insert(END, f'\nHOUVE ALGUM ERRO DESCONHECIDO NO MOMENTO DE GRAVAR OS DADOS NO EXCEL\n')
            self.tx_output.insert(END, '-'*65)
    
    def window_config(self):
        if self.root_config is None:
            self.root_config = Tk()
            self.root_config.protocol("WM_DELETE_WINDOW", self.fecha_jan)
            self.root_config.geometry(center(self.root_config, 500, 300))
            self.root_config.title('Configuration')
            self.root_config.resizable(False, False)
            self.root_config.iconbitmap('img\icon.ico')
            self.root_config.config(bg=self.color1)
            
            self.lb_btn_entrar = Label(
                self.root_config,
                text="Full XPath botão de entrar",
                bg=self.color1,
                fg=self.color3
            )
            
            self.en_btn_entrar = Entry(
                self.root_config,
                bg=self.color3,
                width=60,
                font='15',
                fg='white',
                bd=0
            )
            
            self.lb_name_seg = Label(
                self.root_config,
                text="Full XPath nome do seguidor",
                bg=self.color1,
                fg=self.color3
            )
            
            self.en_name_seg = Entry(
                self.root_config,
                bg=self.color3,
                width=60,
                font='15',
                fg='white',
                bd=0
            )
            
            self.lb_txt_btn_seguir = Label(
                self.root_config,
                text="Full XPath texto botão seguir",
                bg=self.color1,
                fg=self.color3
            )
            
            self.en_txt_btn_seguir = Entry(
                self.root_config,
                bg=self.color3,
                width=60,
                font='15',
                fg='white',
                bd=0
            )
            
            self.lb_btn_seguir = Label(
                self.root_config,
                text="Full XPath botão seguir",
                bg=self.color1,
                fg=self.color3
            )
            
            self.en_btn_seguir = Entry(
                self.root_config,
                bg=self.color3,
                width=60,
                font='15',
                fg='white',
                bd=0
            )
            
            self.lb_btn_deixar_seg = Label(
                self.root_config,
                text="Full XPath botão deixar de seguir",
                bg=self.color1,
                fg=self.color3
            )
            
            self.en_btn_deixar_seg = Entry(
                self.root_config,
                bg=self.color3,
                width=60,
                font='15',
                fg='white',
                bd=0
            )
            
            self.btn_save_config = Button(
                self.root_config,
                bg=self.color4,
                fg='white',
                text="SALVAR",
                command=self.salvar_informacoes_config,
                activebackground=self.color5
            )
            
            if os.path.exists('config.txt'):
                #Lendo o arquivo
                arquivo = open('config.txt','r')
                info_login = []
                for i in arquivo:
                    i.replace('\n', '')
                    info_login.append(i)
                arquivo.close()
                
                # Removendo dados antes de colocar novos
                self.en_btn_entrar.delete(0, END)
                self.en_name_seg.delete(0, END)
                self.en_txt_btn_seguir.delete(0, END)
                self.en_btn_deixar_seg.delete(0, END)
                
                # Colocando os valores salvos
                self.en_btn_entrar.insert(0, info_login[0])
                self.en_name_seg.insert(0, info_login[1])
                self.en_txt_btn_seguir.insert(0, info_login[2])
                self.en_btn_seguir.insert(0, info_login[3])
                self.en_btn_deixar_seg.insert(0, info_login[4])   
            
            #Colocando itens na jenela
            self.lb_btn_entrar.pack(anchor=W, padx=10,pady=3)
            self.en_btn_entrar.pack(anchor=W, padx=10)
            self.lb_name_seg.pack(anchor=W, padx=10,pady=3)
            self.en_name_seg.pack(anchor=W, padx=10)
            # self.lb_txt_btn_seguir.pack(anchor=W, padx=10,pady=3)
            # self.en_txt_btn_seguir.pack(anchor=W, padx=10)
            self.lb_btn_seguir.pack(anchor=W, padx=10,pady=3)
            self.en_btn_seguir.pack(anchor=W, padx=10)
            self.lb_btn_deixar_seg.pack(anchor=W, padx=10,pady=3)
            self.en_btn_deixar_seg.pack(anchor=W, padx=10)
            self.btn_save_config.pack(anchor=E, padx=10,pady=3)
            
        else:
            # Se já foi, basta colocá-la na frente
            self.root_config.lift()
            
    def fecha_jan(self):
        # Seta de novo em None para recriar quando abrir
        self.root_config.destroy()
        self.root_config = None   
        
    #@pysnooper.snoop()
    def login(self):
        #Validando campos
        if (self.en_usuario.get() == '')|(self.en_senha.get() == '')|(self.en_perfil_concorrente.get() == '')|(self.en_qtd_user.get() == ''):
            pg.alert('Existem campos obrigatórios vazios!')
        elif (self.en_usuario.get() == '\n')|(self.en_senha.get() == '\n')|(self.en_perfil_concorrente.get() == '\n')|(self.en_qtd_user.get() == '\n'):
            pg.alert('Existem campos obrigatórios vazios!')
        elif self.en_qtd_user.get().isnumeric() == False:
            pg.alert('O campo de quantidade de usuários só aceita números')
        elif int(self.en_qtd_user.get()) > 10000:
            pg.alert('O limite máximo é até 100 por vez')
            
        else:
            # Variaveis
            tempo_inicio = datetime.today().strftime('%H:%M')
            tempo = 0
            cont = 1
            i = 0
            tentativas = 0
            self.salvar_informacoes()
            self.calc_tempo_script()
            
            if os.path.exists('config.txt'):
                #Lendo o arquivo
                arquivo = open('config.txt','r')
                info_login = []
                isa = 0
                for linha in arquivo:
                    linha.rstrip('\n')
                    info_login.append(linha)
                    
                arquivo.close()
            
            self.driver = Chrome(executable_path='chromedriver.exe')
            self.usuario = self.en_usuario.get()
            self.senha = self.en_senha.get()
            self.perfil_concorrente = self.en_perfil_concorrente.get()
            self.qtd_seguidores = int(self.en_qtd_user.get())
            
            self.driver.get('https://www.instagram.com/')
            time.sleep(2)
            self.username = self.driver.find_element(By.NAME,'username').send_keys(self.usuario)
            self.password = self.driver.find_element(By.NAME,'password').send_keys(self.senha)
            time.sleep(2)
            try:
                self.btn_entrar = self.driver.find_element(By.XPATH, f''+info_login[0]).click()        
            except:
                pass
            time.sleep(15)
            self.driver.get(f'https://www.instagram.com/{self.perfil_concorrente}/followers/')
            time.sleep(20)
            
            self.tx_output.insert(END, '-'*65)
            while i <= self.qtd_seguidores:
                i = i+1
                tempo = tempo +1
                  
                
                self.name_seg = self.driver.find_element(By.XPATH, f''+info_login[1]).text
                
                self.txt_btn_seguir = self.driver.find_element(By.XPATH, f''+info_login[2]).text
                
                if str(self.txt_btn_seguir) != 'Seguindo':
                        self.tx_output.insert(END, f'\nPESSOA: {str(self.name_seg)}\n')
                        
                        try:
                            self.btn_seguir = self.driver.find_element(By.XPATH, f''+info_login[2]).click()
                            time.sleep(5)
                            self.txt_btn_seguir = self.driver.find_element(By.XPATH, f''+info_login[2]).text

                            if str(self.txt_btn_seguir) == 'Solicitado':
                                self.tx_output.insert(END, f'\nO perfil {self.name_seg} é privado, deixando de seguir...\n')
                                self.btn_seguir = self.driver.find_element(By.XPATH, f''+info_login[2]).click()  
                                time.sleep(10)
                                self.btn_deixar_seg = self.driver.find_element(By.XPATH, f''+info_login[4]).click()
                                
                                
                            elif str(self.txt_btn_seguir) == 'Seguindo':
                                self.tx_output.insert(END, f'\n{cont}° perfil seguido')
                                self.tx_output.insert(END, f'\nO perfil {self.name_seg} foi seguido com sucesso!\n')
                                cont = cont+1
                                self.gerar_excel()
                        except:
                            self.tx_output.insert(END, f'\nHouve algum problema ao localizar o botão de seguir vamos tentar novamente\n')
                            tentativas = tentativas+1
                            if tentativas > 10:
                                i = int(self.qtd_seguidores) + 1
                                self.tx_output.insert(END, f'\nPROBLEMA COM BOTÃO SEGUIR NÃO IDENTIFICADO\n')
                            
                elif str(self.txt_btn_seguir) == 'Seguindo':
                        self.tx_output.insert(END, f'\nO perfil {self.name_seg} já está sendo seguido!\n')
                        i=i-1
                self.tx_output.insert(END, '-'*65)
                if tempo == 10:
                        tempo = 0
                        time.sleep(300) 
                        self.tx_output.insert(END, '\nDANDO UMA PAUSA PARA INSTAGRAM NÃO GERAR BLOCK\n')
                        self.tx_output.insert(END, '-'*65)
                else:
                        time.sleep(2)  
                
                    
            tempo_fim = datetime.today().strftime('%H:%M')
            self.tx_output.insert(END, f'\nTEMPO INICIO: {tempo_inicio}\nTEMPO FINAL: {tempo_fim}')
    
    def salvar_informacoes(self):
        user = self.en_usuario.get().replace('\n','')
        senha = self.en_senha.get().replace('\n','')
        perfil_concorrente = self.en_perfil_concorrente.get().replace('\n','')
        qtd_user = self.en_qtd_user.get().replace('\n','')
        #Validar se o usuário deseja salvar as informações
        if self.chkValue.get() == True:
            #Sobrescreve o arquivo sempre que a checkbox estiver selecionada
            arquivo = open('login.txt','w')
            arquivo.write(f"{user}")
            arquivo.write(f"\n{senha}")
            arquivo.write(f"\n{perfil_concorrente}")
            arquivo.write(f"\n{qtd_user}")
        else:
            print('USUÁRIO DESEJOU NÃO SALVAR AS INFORMAÇÕES')
    
    def salvar_informacoes_config(self):
        btn_entrar = self.en_name_seg.get().replace('\n','')
        name_seg = self.en_name_seg.get().replace('\n','')
        txt_btn_seguir = self.en_txt_btn_seguir.get().replace('\n','')
        btn_seguir = self.en_btn_seguir.get().replace('\n','')
        btn_deixar_seg = self.en_btn_deixar_seg.get().replace('\n','')
        

        arquivo = open('config.txt','w')
        arquivo.write(f"{btn_entrar}")
        arquivo.write(f"\n{name_seg}")
        arquivo.write(f"\n{txt_btn_seguir}")
        arquivo.write(f"\n{btn_seguir}")
        arquivo.write(f"\n{btn_deixar_seg}")
        
    def calc_tempo_script(self):
        if int(self.en_qtd_user.get()) < 10:
            self.tempo_estimado.set('Tempo estimado: 10')
        elif int(self.en_qtd_user.get()) >= 10:
            self.tempo_estimado.set('Tempo estimado: 20')
            
Instagram_bot()