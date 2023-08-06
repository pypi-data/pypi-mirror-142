# -*- coding: utf-8 -*-
# Package for easy working with files.
# File with class for files to professional working with files.
import os, codecs

class File: 
    def __init__(self, path: str, encoding: str = "utf-8", new: bool = False, binary: bool = False) -> None:
        self.__path = os.path.abspath(path)
        self.__binary = binary

        if not binary:
            encoding = encoding.replace("-", "_")
            codecs.lookup(encoding) # Check if python supports this encoding.
            self.__encoding = encoding

        if new:
            self.rewrite("")

        elif not os.path.isfile(path):
            raise FileNotFoundError("File doesn't exist!")


    def add(self, content: str) -> int:
        if self.__binary:
            if not isinstance(content, bytes):
                content = bytes(content)
            with open(self.__path, "ba") as file:
                return file.write(content)
        else:
            with open(self.__path, "ta", encoding = self.__encoding) as file:
                return file.write(content)

    def rewrite(self, content: str) -> int:
        if self.__binary:
            if not isinstance(content, bytes):
                content = bytes(content)
            with open(self.__path, "bw") as file:
                return file.write(content)
        else:
            with open(self.__path, "tw", encoding = self.__encoding) as file:
                return file.write(content)

    def replace(self, old: str, new: str, count: int = -1) -> None:
        content = self.read()
        changedContent = content.replace(__old = old, __new = new, __count = count)
        self.rewrite(changedContent)


    def read(self) -> str:
        if self.__binary:
            with open(self.__path, "br") as file:
                return str(file.read())
        else:
            with open(self.__path, "tr", encoding = self.__encoding) as file:
                return file.read()


    def rename(self, new_name: str) -> None:
        os.rename(self.__path, new_name)
        self.__path = os.path.join(self.getPathWithoutName(), new_name)

    def changeExtension(self, newExtension: str) -> None:
        if not newExtension.startswith("."):
            raise ValueError("Extension should starts with '.'")

        nameWithoutExtension = self.getNameWithoutExt()
        newName = nameWithoutExtension + newExtension

        self.rename(newName)


    def changeEncoding(self, newEncoding: str) -> None:
        codecs.lookup(newEncoding) # Check if python supports this encoding.
        self.__encoding = newEncoding

    def recode(self, newEncoding: str) -> None:
        codecs.lookup(newEncoding) # Check if python supports this encoding.

        content = self.read()

        self.__encoding = newEncoding

        self.rewrite(content)


    def getName(self) -> str:
        return os.path.basename(self.__path)

    def getNameWithoutExt(self) -> str:
        return os.path.splitext(self.getName())[0]

    def getExtension(self) -> str:
        return os.path.splitext(self.getName())[1]

    def getPath(self) -> str:
        return self.__path

    def getPathWithoutName(self) -> str:
        return os.path.split(self.__path)[0]

    def getEncoding(self) -> str:
        if self.__binary:
            raise Exception("Binary file doesn't have encoding.")
        return self.__encoding

    def getSize(self) -> int:
        return os.path.getsize(self.__path)

    def isBinary(self) -> bool:
        return self.__binary


    def remove(self) -> None:
        os.remove(self.__path)
        del self
        

    def readLine(self, number_of_line: int) -> str:
        return self.split("\n")[number_of_line]

    def split(self, key: str) -> list:
        content = self.read()
        return content.split(key)
    
    def rsplit(self, key: str) -> list:
        content = self.read()
        return content.rsplit(key)


    def __contains__(self, key) -> bool:
        content = self.read()
        return key in content


    def __eq__(self, __o) -> bool:
        if not isinstance(__o, File):
            raise TypeError("Can compare only File objects.")
        with open(self.__path, "r", encoding = self.getEncoding()) as file:
            thisFileContent = file.read()
        with open(__o.getPath(), "r", encoding = __o.getEncoding()) as file:
            anotherFileContent = file.read()
        return thisFileContent == anotherFileContent

    def __ne__(self, __o: object) -> bool:
        return not self == __o

    def __lt__(self, __o: object) -> bool:
        if not isinstance(__o, File):
            raise TypeError("Can compare only File objects.")
        size_1 = self.getSize()
        size_2 = __o.getSize()
        return size_1 < size_2

    def __gt__(self, __o: object) -> bool:
        if not isinstance(__o, File):
            raise TypeError("Can compare only File objects.")
        size_1 = self.getSize()
        size_2 = __o.getSize()
        return size_1 > size_2

    def __le__(self, __o: object) -> bool:
        if not isinstance(__o, File):
            raise TypeError("Can compare only File objects.")
        size_1 = self.getSize()
        size_2 = __o.getSize()
        return size_1 <= size_2

    def __ge__(self, __o: object) -> bool:
        if not isinstance(__o, File):
            raise TypeError("Can compare only File objects.")
        size_1 = self.getSize()
        size_2 = __o.getSize()
        return size_1 >= size_2

            
if __name__ == '__main__':
    raise Exception("Can't run as main program.")