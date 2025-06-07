import time

def cronometro(segundos):
    for i in range(segundos):
        print(f"Tempo: {i + 1}s")
        time.sleep(1)
    print("Tempo finalizado!")

cronometro(100) 
