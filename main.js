const { app, BrowserWindow } = require('electron');
const { spawn } = require('child_process');
const path = require('path');

function createWindow () {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
    },
  });

  win.loadFile('frontend/index.html');
  win.webContents.openDevTools();

  // Ruta del directorio donde se encuentra el script de instalación.
  const installScriptPath = path.join(__dirname, 'install.py');

  // Ejecuta el script de instalación.
  const installProcess = spawn('python3', [installScriptPath]);

  installProcess.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });

  installProcess.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  installProcess.on('close', (code) => {
    if (code === 0) {
      console.log('La instalación se ha completado con éxito.');
      // Cuando la instalación se completa, activa el entorno virtual y levanta el backend.
      const activateProcess = spawn('cmd.exe', ['/c', 'venv\\Scripts\\activate.bat'], {
        cwd: path.join(__dirname, 'votations')
      });

      activateProcess.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
      });

      activateProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
      });

      activateProcess.on('close', (code) => {
        if (code === 0) {
          console.log('El entorno virtual se ha activado con éxito.');
          // Cuando el entorno virtual se activa, levanta el backend.
          const backendProcess = spawn('python', ['backend/main.py'], {
            cwd: path.join(__dirname, 'votations')
          });

          backendProcess.stdout.on('data', (data) => {
            console.log(`stdout: ${data}`);
          });

          backendProcess.stderr.on('data', (data) => {
            console.error(`stderr: ${data}`);
          });
        } else {
          console.error(`El proceso de activación del entorno virtual se ha cerrado con el código de salida ${code}`);
        }
      });
    } else {
      console.error(`El proceso de instalación se ha cerrado con el código de salida ${code}`);
    }
  });
}

app.whenReady().then(createWindow);
