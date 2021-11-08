from konsoli_io import KonsoliIO

class Laskin:
    def __init__(self, io):
        self._io = io

    def suorita(self):
        while True:
            luku1 = int(self._io.lue("Luku 1:"))

            if luku1 == -9999:
                return

            luku2 = int(self._io.lue("Luku 2:"))

            if luku2 == -9999:
                return

            vastaus = self._laske_summa(luku1, luku2)

            self._io.kirjoita(f"Summa: {vastaus}")

    def _laske_summa(self, luku1, luku2):
        return luku1 + luku2

def main():
    io = KonsoliIO()
    laskin = Laskin(io)

    laskin.suorita()

# Pelkkä main()-metodi tuntui aiheuttavan virheen.
# Kelpaakohan tämä kuitenkin ratkaisusta?
if __name__ ==  "__main__":
    main()