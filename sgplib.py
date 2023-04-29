import zlib
class Package:
    def __init__(self):
        pass
    def encode(self,content,trytozip=True,zip_level=6):
        if trytozip:
            zipped=zlib.compress(content,zip_level)
            self.raw=content
            self.zipped=zipped
        else:
            self.raw=content
            self.zipped=content
        shouldzip=self.raw.__sizeof__() > self.zipped.__sizeof__()
        if shouldzip:
            data=self.zipped
        else:
            data=self.raw
        self.zipped=shouldzip
        self.data=bytes([int(shouldzip)])+data
        
        return self.data
    def decode(self,content):
        cont=list(content)
        zipped=bool(cont[0])
        string=bytes(cont[1:])
        self.zipped=zipped
        if zipped:
            inside=zlib.decompress(string)
        else:
            inside=string
        self.raw=inside
        return inside

