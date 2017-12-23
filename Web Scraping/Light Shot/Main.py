import BaixaImagem as BI
import Links as GL
import threading

TRABALHADORES = 20

def stop(self):
  self._is_running = False

def Worker():
    for x in range(100):
        url = GL.GeraLink()
        nome = ((url[0])[::-1])[4:]
        nome = (nome[:str(nome).find('/')])[::-1]
        BI.download(url[0], '{0}_{1}'.format(str(url[1]).replace('/','_'),nome))
    stop()

threads = []
for y in range(TRABALHADORES):
    t = threading.Thread(target=Worker)
    threads.append(t)
    t.start()
    print('Thread criada ' + y)
