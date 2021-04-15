from tkinter import ttk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os
import csv
import time

pastaApp = os.path.dirname(__file__)
lista = {'Felipe': '24', 'Jose': '42', 'Maria': '22','Eduardo':'31'}


class bot_DP:
    def rodar_programa(self):
        self.ler_arquivo_csv()
        print("Arquivos SELECIONADOS com Sucesso!")


    def mp(self, milimetros):
        return milimetros/0.352777


    def ler_arquivo_csv(self):
        with open('livroVIAMAIS.csv', 'r', encoding='utf8') as entrada:
            ler = csv.reader(entrada, delimiter=',')
            next(ler)
            for linha in ler:
                self.NOME = linha[0]
                self.ctps = linha[1]
                self.CPF = linha[2]
                self.RUA = linha[3]
                self.QUADRA = linha[4]
                self.BAIRRO = linha[5]
                self.CIDADE = linha[6]
                time.sleep(1)
                self.GeneratePDF()
                
                valores = (self.NOME,self.ctps,  self.CPF, self.RUA, self.BAIRRO, self.CIDADE)
                print(valores)
                

    def GeneratePDF(self):
        try:
            nome_pdf = self.NOME
            pdf = canvas.Canvas(('{}.docx'.format(nome_pdf)), pagesize=A4)
            pdf.setFont("Helvetica-Oblique", 12)
            empresa = 'SADDI E SANTOS LTDA - ME'
            CNPJ = '10.416.300/0001-00'
            end_empresa = 'Rua T-39, Qd. 06, Lt. 09, nº 127'
            end_empresa2 = 'Setor Bueno, Goiânia - Goiás'
            texto = f'Por este instrumento particular aditivo ao Contrato de Trabalho, que entre si fazem a empresa {empresa}, pessoa jurídica de direito privado, inscrita no, CNPJ/MF {CNPJ} estabelecida na {end_empresa},{end_empresa2} neste ato denominada simplesmente Empregadora e o Sr.{self.NOME}, portador de {self.ctps}, inscrito no CPF  sob o nº {self.CPF}, residente e domiciliado, {self.RUA},{self.QUADRA}, {self.BAIRRO}, {self.CIDADE} doravante denominado de Empregado, mediante as seguintes condições, tendo em vista a Lei 12.619/2012.'

            texto2 = f'1ª. O empregado trabalha para a empregadora na função de VENDEDOR executando as tarefasinerentes a função e outras que forem determinadas pela empregadora, desde que compatíveis com as suas atribuições, nos termos do artigo 456, parágrafo único, da CLT.'

            texto3 = f'2ª. A partir da presente data, a empregadora adotará o sistema eletrônico AGHORA de controle de jornada, sendo que o início do trabalho dar-se-á através do acesso ao mencionado sistema através de Login e Senha pessoal intransferíveis;'

            texto4 = f'3ª. O empregado fica ciente que a empregadora poderá ainda adotar outros meios alternativosde controle de jornada além do sistema eletrônico AGHORA, cuja intenção é justamente parametrizar a real jornada desempenhada. '

            texto5 = f'4ª. Desde já o empregado se obriga a manter o sigilo do seu Login e Senha, sendo que será de sua responsabilidade o acesso de terceiros, podendo inclusive ser penalizado com advertência, suspensão ou até mesmo rescisão por justa causa em caso de descumprimento de tal regra;'

            texto6 = f'4ª Ficam mantidas as regras anteriores descritas no termo individual de banco de horas. E, por assim estarem de acordo, firmam o presente, em duas vias, uma das quais é entregue ao empregado.'

            texto7 = f'Goiânia, 11 de Março de 2021.'

            texto23 = f'{empresa} CNPJ nº {CNPJ}'
            texto24 = f'{self.NOME} CPF sob Nº {self.CPF}'


            pdf.stringWidth(texto, 'Helvetica-Oblique', 12)
            pdf.setTitle("TERMO ADITIVO DE CONTRATO DE TRABALHO")
            pdf.drawString(self.mp(40),self.mp(280),"TERMO ADITIVO DE CONTRATO DE TRABALHO")
            #01 PARAGRAFO
            pdf.drawString(self.mp(20),self.mp(270),texto)
     
            #02PARAGRAFO
            pdf.drawString(self.mp(9),self.mp(210),texto2)

            #03PARAGRAFO
            pdf.drawString(self.mp(9),self.mp(185),texto3)

            #04PARAGRAFO
            pdf.drawString(self.mp(8),self.mp(160),texto4)

            #05PARAGRAFO
            pdf.drawString(self.mp(9),self.mp(135),texto5)

            #06PARAGRAFO
            pdf.drawString(self.mp(9),self.mp(110),texto6)

            #FINAL 
            pdf.drawString(self.mp(9),self.mp(75),texto7)
            #RODAPE
            pdf.drawString(self.mp(40),self.mp(30),texto23)
            pdf.drawString(self.mp(40),self.mp(20),texto24)
            
            

            #pdf.drawString(100,100,texto)
            pdf.save()
        except:
            print('ERRO AO CRIAR PDF: {self.NOME}')


            



####TESTES
on = bot_DP()
on.rodar_programa()