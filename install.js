const { execSync } = require("child_process");
const os = require("os");
const fs = require("fs");

// Instalar Python y pip en el sistema operativo del usuario
if (os.platform() === "win32") {
  console.log("Instalando Python y pip...");
  execSync(`powershell.exe -Command "Start-Process 'python-3.9.4-amd64.exe' -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -Wait"`);
} else {
  console.log("Instalando Python y pip...");
  execSync("sudo apt-get update");
  execSync("sudo apt-get install -y python3 python3-pip");
}

// Instalar las dependencias del archivo requirements.txt en un virtual environment
console.log("Creando virtual environment...");
execSync("python3 -m venv venv");
console.log("Activando virtual environment...");
execSync(`${os.platform() === "win32" ? ".\\venv\\Scripts\\activate" : "source ./venv/bin/activate"}`);
console.log("Instalando dependencias...");
execSync("pip install -r requirements.txt");

// Escribir un archivo para indicar que la instalación se completó
console.log("Creando archivo de instalación completada...");
fs.writeFileSync("installation_complete.txt", "Installation completed successfully!");
