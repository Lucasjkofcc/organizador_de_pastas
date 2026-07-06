import os
import shutil

home = "/home/lucas/Downloads/"
categorias = {
    "Imagens": [".png", ".jpg", ".jpeg"],
    "Vídeos": [".mp4", ".mov"],
    "Programas": [".py", ".c", ".cpp"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Músicas": [".mp3", ".wav"],
    "Isos": [".iso"],
    "Compactados": [".zip", ".rar", ".tar", ".gz", ".zst"],
    "Executáveis": [".exe", ".msi"],
    "Pastas (Ou executaveis....)": [""],
    "Instalação": [".deb", ".rpm"],
    "urls": [".url", ".html"]
}
os.chdir(home)
pasta_downloads = os.listdir()
print(os.listdir())
for pasta in categorias:
    if not os.path.exists(pasta):
        os.mkdir(pasta)
        #os.mkdir("Outros")
# organiza eu acho
for pasta, extensoes in categorias.items():
    for arquivo in pasta_downloads:
        nome, extensao = os.path.splitext(arquivo)
        if extensao in extensoes:
            if arquivo == "Pastas":
                pass
            if arquivo in categorias:
                pass
            else:
                shutil.move(arquivo, os.path.join(pasta, arquivo))
                print(f"{arquivo} -> {pasta}")
       # elif extensao not in extensoes:
            #shutil.move(arquivo, os.path.join("Outros", arquivo))