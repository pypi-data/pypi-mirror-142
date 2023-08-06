import codecs
import platform
def check_address(address,range=1,address_get="auto",slash_add=False):#range only can use by Windows
    global slash
    if address_get == "auto":
        if platform.system() == "Windows":
            slash="\\"
            _slash = slash*(2**(int(range)-1))
        else:
            slash="/"
            _slash = slash
    elif address_get == "\\":
        slash = address_get
        _slash = slash*(2**(int(range)-1))
    else:
        slash = address_get
        _slash = slash
    add = address.split(slash)[0]
    for i in address.split(slash)[1:len(address.split(slash))]:
        if i != "":
            add = add + _slash + i
    if slash_add:
        add = add + _slash
    return add
class open_normal:
    class basic:
        def __init__(self,address,mode,encode="utf-8",address_get="auto",range=1):
            self.address = check_address(address,range,address_get)
            self.mode = mode
            self.encode = encode
            if "b" not in mode:
                self.o = codecs.open(self.address,self.mode,encoding=self.encode)
            else:
                self.o = codecs.open(self.address,self.mode)
        def __str__(self):
            return self.o
        def refresh(self):
            return self.o.read()
        def write(self,thing):
            self.o.write(thing)
            return thing
        def clear(self):
            with codecs.open(self.address,"w") as o:
                o.write("")
            return None
    def __init__(self,address,mode,encode="utf-8",address_get="auto",range=1):
        if type(mode) == type("str") and mode in ["a","ab","w","wb","r","rb"]:
            self.basic = open_normal.basic(address,mode+"+",encode,address_get,range)
        elif type(mode) == type("str") and mode in ["a+","ab+","w+","wb+","r+","rb+"]:
            self.basic = open_normal.basic(address,mode,encode,address_get,range)
    def read(self):
        return self.basic.refresh()
    def write(self,thing):
        self.basic.write(thing)
        return self.basic.refresh()
    def clear():
        self.basic.clear()
class open_simple:
    def __init__(self,address,encoding="utf-8",address_get="auto",range=1):
        self.address = check_address(address,range,address_get)
        self.encoding = encoding
    def write(self,thing):
        with open(self.address,"w",encoding=self.encoding) as o:
            o.write(thing)
    def add(self,thing):
        with open(self.address,"a",encoding=self.encoding) as o:
            o.write(thing)
    def clear(self):
        with open(self.address,"w") as o:
            o.write("")
    def read(self):
        with open(self.address,"r",encoding=self.encoding) as o:
            return o.read()
    def write_in_binary(self,thing):
        with open(self.address,"wb") as o:
            o.write(thing)
    def add_in_binary(self,thing):
        with open(self.address,"ab") as o:
            o.write(thing)
    def read_in_binary(self):
        with open(self.address,"rb") as o:
            return o.read()
