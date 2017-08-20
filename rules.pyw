#===================================
#======== Codado por C.Magno ========
#===================================
import json as js
import random as r
import webbrowser as wb
neo = {}
file = ''
m = open('links.json', 'r')
lLinks = js.load(m) #Variável que armazena os endereços da função abra
m.close()


class Machine():
      def __init__(self, name):
            self.name = name #Recebe o nome da IA
            self.history = [""] #Armazena a conversa
            m = open('known.json', 'r')
            self.known = js.load(m) #Recebe os nomes de usuários conhecidos
            m.close()
            memory = open('asks.json', 'r')
            self.phrases = js.load(memory) #Variável vital que recebe uma biblioteca de frases
            memory.close()

      def listen(self): #Função que recebe as frases e respostas do usuário
            phrase = input('===>>>    ').lower()
            phrase.strip()
            phrase.replace('é', 'eh')
            phrase.replace('você', 'voce')
            return phrase

      def takeName(self, phrase): #Serve apenas para capturar o nome do usuário
            if 'me chamo' in phrase:
                  name = phrase.split('chamo')
                  name = name[1]
            else:
                  name = phrase
            return name

      def answerName(self, name):
            if name in self.known:
                  return 'Bem vindo de volta' #Caso o usuário seja conhecido
            self.known.append(name)
            m = open('known.json', 'w')
            js.dump(self.known, m)
            m.close()
            return '--< Prazer em  te conhecer' #Caso contrário

      def learn(self): #Permite à IA aprender após receber a string 'Ouça'
            key = input('--< Quando você dizer?  ').lower()
            keyword = input('--< Quê devo responder-lhe? ').lower()
            m = open('asks.json', 'w')
            self.phrases[key] = keyword
            js.dump(self.phrases, m)
            m.close()

      def learnNow(self, phrase): #A forma mais eficiênte de aprendizado da IA
            key = phrase
            keyword = input('--< Como eu deveria te responder? ').lower()
            m = open('asks.json', 'w') #As frases são armazenadas no arquivo padrão
            self.phrases[key] = keyword
            js.dump(self.phrases, m)
            m.close()

      def think(self, phrase): #Função que processa as strings do usuário e encontra uma resposta
            global neo
            global file
            if phrase in self.phrases:
                  return '--< ' + self.phrases[phrase]
            if self.history[-1] == '--< Como se chama?':
                  name = self.takeName(phrase)
                  phrase = self.answerName(name)
                  return phrase
            if 'hey' in phrase or 'iae' in phrase or 'eae' in phrase or 'oie' in phrase:
                  print('--< Olá! Me chamo ' + self.name)
                  return '--< Como se chama?'
            if 'if: ' in  phrase: #Serve para o cálculo de Indicativo de Fuso
                  x = phrase.split('if: ')
                  x = x[1]
                  x = x.split(' ')
                  side = x[1]
                  numb = x[0]
                  IF = int(numb)/15
                  if int(numb)%15 > 7.30:
                        IF += 1
                  if side == 'w':
                        IF = IF*(-1)
                  return '--< ' + str(int(IF))
            if 'if = ' in  phrase: #Também calcula o Indicativo de Fuso
                  x = phrase.split('if = ')
                  x = x[1]
                  x = x.split(' ')
                  side = x[1]
                  numb = x[0]
                  IF = int(numb)/15
                  if int(numb)%15 > 7.30:
                        IF += 1
                  if side == 'w':
                        IF = IF*(-1)
                  return '--< ' + str(int(IF))
            if phrase == 'dh': #Calculo da diferença horária entre dois pontos
                  IFa = int(input('--< Indicativo do ponto A: '))
                  IFb = int(input('--< Indicativo do ponto B: '))
                  DH = IFb - IFa
                  return 'DH = ' + str(DH)
            if phrase == 'hb': #Calculo da hora em um ponto B por um ponto A
                  DH = int(input('--< Diferença Horária: '))
                  hour = int(input('--< Hora em A (Horas apenas) : '))
                  minHour = int(input('--< Hora em A (Minutos apenas) : '))
                  flight = int(input('--< Duração total da viajem (Apenas Horas): '))
                  minFlight = int(input('--< Duração (Minutos apenas) : '))
                  hour += flight
                  minHour += minFlight
                  hour += int(minHour/60)
                  minHour -= int(minHour/60)*60
                  Hb = hour + DH
                  if Hb > 24:
                        Hb -= 24
                        return '--< ' + str(Hb) + ' e ' + str(minHour) + ' minutos do dia seguinte. '
                  elif Hb < 0:
                        Hb = 24 - (Hb*(-1))
                        return '--< ' + str(Hb) + ' e ' + str(minHour) + ' minutos do dia anterior. '
                  return '--< ' + str(Hb) + ' e ' + str(minHour) + ' minutos do mesmo dia. '
                  
            elif 'ouça' in phrase: #Isto chamará a função que permite à IA aprender novas frases
                 self.learn()
                 return '--< Certo!'
            elif 'crie' in phrase: #Informa a IA para criar um novo arquivo .json
                  phrase = phrase.split('crie ')
                  file = phrase[1]
                  m = open(file+'.json', 'a')
                  m.close()
                  neo = {}
                  return '--< Arquivo criado. '
            elif 'record' in phrase: #Salva novos valores em um dicionário em um arquivo .json
                  x = phrase.split('record ')
                  file = x[1]
                  q = input('--< Record... What? ').lower()
                  qx = input('--< Whith what value? ').lower()
                  neo[q] = qx
                  m = open(file+'.json', 'w')
                  js.dump(neo, m)
                  m.close()
                  return 'Done! '
            elif 'read' in phrase: #Permite a IA ler dado valor nos arquivos .json
                  x = phrase.split('read ')
                  x = x[1]
                  q = input('--< Which book? ').lower()
                  m = open(q+'.json', 'r')
                  text = js.load(m)
                  m.close()
                  if x in text:
                        return text[x]
                  else:
                        return '-- < There is not of it'
            elif 'de =' in phrase: #Ainda em beta... Informa a distribuição eletrônica de algum elemento químico
                  element = phrase.split('de = ')[1]
                  if element == 'h':
                        return '1s¹'
                  elif element == 'he':
                        return '1s²'
                  return '--< não reconheço este elemento...'
            elif 'abra =' in phrase: #Informa a IA para abrir determinado site
                  site = phrase.split('abra = ')[1]
                  if site in lLinks:
                        wb.open(lLinks[site])
                        return '--< Feito.'
                  else:
                        print('--< Não reconheço este endereço') #Caso ela não reconhecer o site, ela pedirá o endereço
                        place = input('--< Informe o Link: ')
                        lLinks[site] = place
                        m = open('links.json', 'w')
                        js.dump(lLinks, m)
                        m.close()
                        return '--< Pronto.'
            elif 'tchau' in phrase or 'flw' in phrase:
                  return '--< Até mais!'
            self.learnNow(phrase)
            return '--< Ah.. Legal.'

      def talk(self, answer): #Função que executa o print, das respostas encontradas
            print(answer)
            self.history.append(answer)
