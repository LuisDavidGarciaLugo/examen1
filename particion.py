


class Particion(object):

    def __init__(self, mem, parent=None):
        self.mem = mem
        self.top = None
        self.bottom = None
        self.process = None

        self.parent = parent


    def reservar(self, process):
        if self.process != None: return None
        if self.top == None and self.bottom == None and process.mem > self.mem/2: 
            self.process = process
            return self

        if self.top == None and process.mem <= self.mem/2: self.top = Particion(self.mem/2, self)
        if self.top != None: 
            result = self.top.reservar(process)
            if result != None: return result

        if self.bottom == None and process.mem <= self.mem/2: self.bottom = Particion(self.mem/2, self)
        if self.bottom != None:
            result = self.bottom.reservar(process)
            if result != None: return result

        return None


    def vacios(self):

        if self.process != None: return
        mem = str(self.mem/2)
        if self.top == None: print("espacio vacio de " + mem + " bloques")   
        else: self.top.vacios()
        if self.bottom == None: print("espacio vacio de " + mem + " bloques")
        else: self.bottom.vacios()


 
    def liberar(self):
        
        p = self.parent
        if p == None: return

        if p.top == self: p.top = None
        elif p.bottom == self: p.bottom = None

        if p.top == None and p.bottom == None: p.liberar()


    def __repr__(self):
        part = "-memoria: " + str(self.mem)
        if self.top != None: part += " -top" 
        if self.bottom != None:part += " -bottom" 
        if self.process != None:part += " -proceso: " + str(self.process)

        return part

    def __str__(self):
        part = "-memoria: " + str(self.mem)
        if self.top != None: part += " -top" 
        if self.bottom != None:part += " -bottom" 
        if self.process != None:part += " -proceso: " + str(self.process)





class Proceso(object):

    def __init__(self, name, mem):
        self.name = name
        self.mem = mem
        self.partition = None


    def __repr__(self):
        return "[name: {} memory: {}]".format(self.name, self.mem)

    def __str__(self):
        return "[name: {} memory: {}]".format(self.name, self.mem)


class SistemaPana(object): 
    
    names = {}

    def __init__(self, mem):
        self.particion = Particion(mem)

    def reservar(self, process):
        if process.mem > self.particion.mem: return False
        result = self.particion.reservar(process) 
        if result != None: 
            self.names[process.name] = process
            process.partition = result
            return True
        return False


    def liberar(self, name):
        try:
            process = self.names[name]
        except:
            return False
        
        self.names.pop(name)
        partition = process.partition

        partition.process = None
        partition.liberar()

    def mostrar(self):

        if self.particion.process != None:  print("no hay espacios vacios en memoria")
        else:
            print("espacios de memoria vacios:")
            if (self.particion.top == self.particion.bottom): print("espacio vacio de " + str(self.particion.mem) + " bloques")
            else: self.particion.vacios()

        if len(self.names.values()) == 0: print("\nno hay espacios de memoria ocupados")
        else:
            print("\nespacios de memoria ocupados:")
            for process in self.names.values():
                        print("{}: {} bloques (fragmentacion {})".format(process.name, process.mem, process.partition.mem - process.mem))



while True:
    mem = input("introduzca memoria a utilizar\n>")
    try:
        s = SistemaPana(int(mem))
        break
    except:
        print("dato invalido")


while True:

    command = input(">").strip().split(" ")
    l = len(command)

    if command[0] == "": continue

    if command[0] == "RESERVAR":

        if l < 3:
            print("Error: argumentos insuficientes para correr comando RESERVAR")
            continue
        elif l > 3:
            print("Error: argumento no reconocido " + command[2])
            continue

        if command[1] in s.names:
            print(command[1] + " ya tiene espacio reservado")
            continue

        try: mem =int(command[2])
        except: 
            print("cantidad de memoria debe ser un dato numerico")
            continue

        if s.reservar(Proceso(command[1], mem)): print("se ha reservado memoria para " + command[1])
        else: print("no hay espacio de memoria suficiente para " + command[1])

    elif command[0] == "LIBERAR":
        if l < 2:
            print("Error: argumentos insuficientes para correr comando LIBERAR")
            continue
        elif l > 2:
            print("Error: argumento no reconocido " + command[5])
            continue

        if command[1] not in s.names:
            print(command[1] + " no tiene espacio reservado")
            continue

        s.liberar(command[1])
        print("Se ha liberado " + command[1] +" de la memoria")
        


    elif command[0] == "MOSTRAR":
        s.mostrar()

    elif command[0] == "SALIR": exit()
    else: print("comando invalido")