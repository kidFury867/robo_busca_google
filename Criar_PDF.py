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
        with open('x-livroVIAMAIS.csv', 'r', encoding='utf8') as entrada:
            ler = csv.reader(entrada, delimiter=',')
            for linha in ler:
                self.NOME = linha[0]
                self.ctps = linha[1]
                self.CPF = linha[2]
                self.RUA = linha[3]
                self.QUADRA = linha[4]
                self.BAIRRO = linha[5]
                self.CIDADE = linha[6]
                #time.sleep(1)
                self.GeneratePDF()
                
                valores = (self.NOME,self.ctps,  self.CPF, self.RUA, self.BAIRRO, self.CIDADE)
                print(valores)
                

    def GeneratePDF(self):
        try:
            nome_pdf = self.NOME
            pdf = canvas.Canvas(('{}.pdf'.format(nome_pdf)), pagesize=A4)
            pdf.setFont("Helvetica-Oblique", 12)
            empresa = 'SADDI E SANTOS LTDA - ME'
            CNPJ = 'SADDI E SANTOS LTDA - ME'
            end_empresa = 'Rua T-39, Qd. 06, Lt. 09, nº 127,SALA 5, '
            end_empresa2 = 'Setor Bueno, Goiânia - Goiás'
            texto = f' Por este instrumento particular aditivo ao Contrato de Trabalho, que entre si fazem a '
            texto01 = f'empresa {empresa}, pessoa jurídica de direito privado, '
            texto02 = f'inscrita no CNPJ/MF {CNPJ} estabelecida na {end_empresa} '
            texto022 = f'{end_empresa2} neste ato denominada simplesmente Empregadora e '
            texto03 = f'o Sr.{self.NOME}, portador de {self.ctps}, '
            texto04 = f'inscrito no CPF  sob o nº {self.CPF}, residente e domiciliado, '
            texto05 = f'{self.RUA},{self.QUADRA}, {self.BAIRRO},{self.CIDADE}, '
            texto06 = f'  doravante denominado de Empregado, mediante as seguintes condições,'
            texto066 = f' tendo em vista a Lei 12.619/2012.'

            texto07 = f'1ª. O empregado trabalha para a empregadora na função de VENDEDOR executando as tarefas'
            texto08 = f'inerentes a função e outras que forem determinadas pela empregadora, desde que compatíveis'
            texto09 = f'com as suas atribuições, nos termos do artigo 456, parágrafo único, da CLT.'
            texto10 = f'2ª. A partir da presente data, a empregadora adotará o sistema eletrônico AGHORA de controle '
            texto11 = f'de jornada, sendo que o início do trabalho dar-se-á através do acesso ao mencionado sistema'
            texto12 = f'através de Login e Senha pessoal intransferíveis;'
            texto13 = f'3ª. O empregado fica ciente que a empregadora poderá ainda adotar outros meios alternativos'
            texto14 = f'de controle de jornada além do sistema eletrônico AGHORA, cuja intenção é justamente '
            texto15 = f'parametrizar a real jornada desempenhada.'
            texto16 = f'4ª. Desde já o empregado se obriga a manter o sigilo do seu Login e Senha, sendo que será de sua'
            texto17 = f'responsabilidade o acesso de terceiros, podendo inclusive ser penalizado com advertência,'
            texto18 = f'suspensão ou até mesmo rescisão por justa causa em caso de descumprimento de tal regra;'
            texto19 = f'4ª Ficam mantidas as regras anteriores descritas no termo individual de banco de horas.'
            texto20 = f'E, por assim estarem de acordo, firmam o presente, em duas vias, uma das quais '  
            texto21 = f'é entregue ao empregado.'
            texto22 = f'Goiânia, 01 de Abril de 2021.'
            texto23 = f'{empresa} CNPJ nº {CNPJ}'
            texto24 = f'{self.NOME}'
            texto25 = f'CPF sob Nº {self.CPF}'

            pdf.stringWidth(texto, 'Helvetica-Oblique', 12)
            pdf.setTitle("TERMO ADITIVO DE CONTRATO DE TRABALHO")
            pdf.drawCentredString(self.mp(100),self.mp(280),"TERMO ADITIVO DE CONTRATO DE TRABALHO")
            #01 PARAGRAFO
            pdf.drawCentredString(self.mp(105),self.mp(270),texto)
            pdf.drawCentredString(self.mp(105),self.mp(265),texto01)
            pdf.drawCentredString(self.mp(105),self.mp(260),texto02)
            pdf.drawCentredString(self.mp(105),self.mp(255),texto022)
            pdf.drawCentredString(self.mp(105),self.mp(250),texto03)
            pdf.drawCentredString(self.mp(105),self.mp(245),texto04)
            pdf.drawCentredString(self.mp(105),self.mp(240),texto05)
            pdf.drawCentredString(self.mp(105),self.mp(235),texto06)
            pdf.drawCentredString(self.mp(105),self.mp(230),texto066)
            #02PARAGRAFO
            pdf.drawString(self.mp(9),self.mp(210),texto07)
            pdf.drawString(self.mp(12),self.mp(205),texto08)
            pdf.drawString(self.mp(12),self.mp(200),texto09)
            #03PARAGRAFO
            pdf.drawString(self.mp(9),self.mp(185),texto10)
            pdf.drawString(self.mp(12),self.mp(180),texto11)
            pdf.drawString(self.mp(12),self.mp(175),texto12)
            #04PARAGRAFO
            pdf.drawString(self.mp(8),self.mp(160),texto13)
            pdf.drawString(self.mp(12),self.mp(155),texto14)
            pdf.drawString(self.mp(12),self.mp(150),texto15)
            #05PARAGRAFO
            pdf.drawString(self.mp(9),self.mp(135),texto16)
            pdf.drawString(self.mp(12),self.mp(130),texto17)
            pdf.drawString(self.mp(12),self.mp(125),texto18)
            #06PARAGRAFO
            pdf.drawString(self.mp(9),self.mp(110),texto19)
            pdf.drawString(self.mp(12),self.mp(105),texto20)
            pdf.drawString(self.mp(12),self.mp(100),texto21)
            #FINAL 
            pdf.drawString(self.mp(9),self.mp(75),texto22)
            #RODAPE
            linha = ("-")*100
            pdf.drawCentredString(self.mp(100),self.mp(40),texto23)
            pdf.drawCentredString(self.mp(100),self.mp(23),linha)
            pdf.drawCentredString(self.mp(100),self.mp(20),texto24)
            pdf.drawCentredString(self.mp(100),self.mp(15),texto25)
            
            

            #pdf.drawString(100,100,texto)
            pdf.save()
        except:
            print('ERRO AO CRIAR PDF: {self.NOME}')


            



####TESTES
on = bot_DP()
on.rodar_programa()