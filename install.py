import os
import urllib.request
import zipfile

# Descarga Python 3.9.5 para Windows de la página oficial de Python.
url = "https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe"
filename = "python-3.9.5-amd64.exe"
urllib.request.urlretrieve(url, filename)

# Ejecuta el instalador de Python.
os.system(filename)

# Crea un entorno virtual de Python llamado "votations".
os.system("python -m venv votations")

# Activa el entorno virtual de Python.
activate_script = os.path.join("votations", "Scripts", "activate")
os.system(activate_script)

# Instala las dependencias del archivo requirements.txt.
os.system("pip install -r requirements.txt")

# Desactiva el entorno virtual de Python.
# os.system("deactivate")
