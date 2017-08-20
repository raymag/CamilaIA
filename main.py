from rules import Machine as mc

Camila = mc('Camila') 

while True: #Este é o Loop Básico da IA
      phrase = Camila.listen() #Fará a requisição de uma string do usuário
      answer = Camila.think(phrase)#A IA verificará a melhor resposta ao usuário
      Camila.talk(answer)#E por fim, informará tal resposta ao usuário
      if answer == '--< Até mais!':
            break
      
      
      
