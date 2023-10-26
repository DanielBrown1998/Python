class MyOpen:
    def __init__(self, caminho, modo):
        self.caminho = caminho
        self.modo = modo
        self._file = None

    def __enter__(self):
        print("abrindo ...")
        self._file = open(self.caminho, self.modo, encoding="utf-8")
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("fechando...")
        self._file.close()
        return True



with MyOpen("context.txt", "w") as file:
    for c in range(5):
        print(f"escrevendo na linha {c+1}...")
        file.write(f"linha {c+1}\n")


