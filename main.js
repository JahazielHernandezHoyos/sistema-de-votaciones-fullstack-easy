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

  win.maximize(); // Para maximizar la ventana
  win.loadFile('frontend/index.html');
  // win.webContents.openDevTools(); // Para abrir la consola de desarrollador

  // Run the python script
  const python = spawn('python', [path.join(__dirname, 'backend', 'main.py')]);
  python.stdout.on('data', (data) => {
    console.log(data.toString());
  }
  );
}

app.whenReady().then(createWindow);
