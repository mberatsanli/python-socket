import socket
import time

class mbsSocket:

    ip = "0.0.0.0"
    port = 5656
    data_size = 1024
    soc = ""

    def __init__(self, ip=None, port=None, data_size=None):
        if ip: self.ip = ip
        if port: self.port = port
        if data_size: self.data_size = data_size
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    # Socket baglantisini saglar
    def baglan(self):
        self.soc.connect((self.ip, self.port))
        return True
    
    # Socket baglantisini kapatir
    def kapat(self):
        self.soc.close()
        return True

    # Veri yollama tur="send/sendall"
    def veriYolla(self, veri, tur="send", oku=False):
        if veri:
            if tur == "sendall":
                self.soc.sendall(veri)
            else:
                self.soc.send(veri)
        
            if oku: 
                return self.soc.recv(self.data_size)

            return True
        else:
            return False

    # Veri yollayip responselama
    def veriOku(self, data_size=None):
        if data_size is None:
            data_size = self.data_size
        return self.soc.recv(data_size)

    # Baglanti testi
    def test(self):
        return self.veriYolla("Merhaba", oku=True)

mbs = mbsSocket("0.0.0.0", 7800)
mbs.baglan()

time.sleep(1)
while True:
    w = raw_input("Gonder: ")
    print(mbs.veriYolla(w, oku=True))

#mbs.kapat()