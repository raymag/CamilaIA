from rules import Machine as mc

Camila = mc('Camila')

while True:
      phrase = Camila.listen()
      answer = Camila.think(phrase)
      Camila.talk(answer)
      if answer == '--< Até mais!':
            break
      
      
      
