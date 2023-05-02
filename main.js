const { app, BrowserWindow } = require('electron');
const { spawn } = require('child_process');
const fs = require('fs');
const os = require('os');

function runPythonScriptDev() {
  //ejecutar server fastapi
  const child = spawn('resources/backend-fastapi.exe');
  child.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });
  child.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });
  child.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
  });
}

function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
    },
  });
  win.maximize();
  win.loadFile('frontend/index.html');
}

function startApp() {
  //ejecutar server fastapi
  runPythonScriptDev();
  app.whenReady().then(createWindow);
}

startApp();
