
class GrafoT(object):

    lados = {"LOCAL":[]}

    def nuevoNodo(self, n):
        if n not in self.lados: self.lados[n] = []


    def nuevoLado(self, a, b, dep = None):
        self.nuevoNodo(a)
        self.nuevoNodo(b)

        self.lados[a].append({"leng":b, "dep":dep})


class diagramaT(object):

    G = GrafoT()
    programas = {}


    def programa(self, nombre, leng):
        self.programas[nombre] = leng
        self.G.nuevoNodo(leng)

    def interprete(self, leng_base, leng):
        self.G.nuevoLado(leng, leng_base)

    def traductor(self, leng_base, leng_origen, leng_destino):
        self.G.nuevoLado(leng_origen, leng_destino, leng_base)
        self.G.nuevoNodo(leng_base)

    def correr(self, leng):

        Q = [leng] 

        while len(Q) > 0:
            u = Q.pop()
            if u == "LOCAL": return True

            for v in self.G.lados[u]:
                if v["dep"] == None or self.correr(v["dep"]): 
                    Q.append(v["leng"])

        return False



d = diagramaT()



while True:

    command = input(">").strip().split(" ")
    l = len(command)

    if command[0] == "": continue

    if command[0] == "DEFINIR":

        if l == 1:
            print("Error: no fue provisto <tipo>")
            continue

        if command[1] == "PROGRAMA":
            if l < 4:
                print("Error: argumentos insuficientes para definir programa")
                continue
            elif l > 4:
                print("Error: argumento no reconocido " + command[4])
                continue

            d.programa(command[2], command[3])
            print("Se definió el programa '{}', ejecutable en '{}'".format(command[2], command[3]))
            continue

        elif command[1] == "INTERPRETE":
            if l < 4:
                print("Error: argumentos insuficientes para definir interprete")
                continue
            elif l > 4:
                print("Error: argumento no reconocido " + command[4])
                continue

            d.interprete(command[2], command[3])
            print("Se definió un intérprete para '{}', escrito en '{}'".format(command[3], command[2]))
            continue
        elif command[1] == "TRADUCTOR":
            if l < 5:
                print("Error: argumentos insuficientes para definir traductor")
                continue
            elif l > 5:
                print("Error: argumento no reconocido " + command[5])
                continue

            d.traductor(command[2], command[3], command[4])
            print("Se definió un traductor de '{}' hacia '{}' escrito en '{}'".format(command[3], command[4], command[2]))
            continue
        
        else:
            print("Error: argumento <tipo> invalido")
            continue

    elif command[0] == "EJECUTABLE":
        if l < 2:
                print("Error: argumentos insuficientes para ecomando ejectutable")
                continue
        elif l > 2:
            print("Error: argumento no reconocido " + command[2])
            continue

        try: 
            leng = d.programas[command[1]]
        except: 
            print("Programa no econtrado")
            continue

        if d.correr(leng): print("Si, es posible ejecutar el programa '{}'".format(command[1]))
        else:  print("No es posible ejecutar el programa '{}'".format(command[1]))

    elif command[0] == "SALIR": exit()
    else: print("comando invalido")