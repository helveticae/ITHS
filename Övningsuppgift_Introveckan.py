Question = ["Vad har du studerat/jobbat med/gjort tidigare?", "Varför valde du denna utbildning?", "Hur kan vi skapa de bästa förutsättningarna för att du ska lyckas med dina studier?", "Något annat du vill berätta för din utbildningsledare?"]
Answer = ["Journalistik, Grafisk design, Digital Marknadsföring.", "automatisering och statistik. Vill lära mig programmering.", "bidra med god stämning och god kompetens!", "Allt gott!", "Övningsuppgift Introveckan", "William Akilles Lindstedt"]

def hd(i):
  a = len(str(i))
  t = (f" {i} ")
  print("-" * a + t + "-" * a, "\n")

hd(Answer[4])
s = 0
for i in Question:
  if s == 1:
    p = " Intresse för"
  elif s == 2:
    p = " Ni kan"
  else:
    p = ''
  print (f"Fråga {s+1}: {i} \n -{p} {Answer[s]}\n")
  s = s + 1
  if s >= 4:
    break
  else:
    continue
print(f"/{Answer[5]}")