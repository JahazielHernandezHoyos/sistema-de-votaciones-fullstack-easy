# 🗳️ Sistema de Votación 🗳️

Este es un sistema de votación web construido con FastAPI y SQLAlchemy ORM para el backend, y HTML, CSS y JavaScript (con Bootstrap) para el frontend. El sistema permite a los usuarios registrados crear, editar y eliminar votaciones, y a los usuarios no registrados votar en las votaciones existentes.

# 🚀 Instalación 🚀

Para instalar las dependencias, ejecute:

```bash
pip install -r requirements.txt
npm install 
```
# 💾 Configuración de la base de datos 💾

El sistema de votación utiliza una base de datos SQLite para almacenar la información de las votaciones y los usuarios registrados. Esta base de datos se configura automáticamente al iniciar la aplicación por primera vez y no es necesario realizar ninguna acción adicional por parte del usuario.
```
# 💻 Uso 💻

Para iniciar la aplicación, ejecute:

```bash
pyinstaller backend-fastapi.spec
```
Lo anterior hara un .exe del backend para luego ejecutar la aplicacion de escritorio la cual debe volverse a poner en la carpeta resources

Para iniciar la aplicación de escritorio, ejecute:

```bash
npm run start
```

Una vez que la aplicación esté en funcionamiento, abra un navegador y vaya a http://localhost:8000 para acceder a la página de inicio. Desde allí, puede crear una cuenta para empezar a crear votaciones y votar en ellas.

# Compilacion de la aplicacion de escritorio 📦

Para compilar la aplicacion de escritorio, ejecute:

```bash
npm run dist
```

Esto creara un .exe en la carpeta dist

# 🤝 Contribuciones 🤝

Las contribuciones son siempre bienvenidas. Siéntase libre de abrir un issue o enviar una pull request.

# 📝 Licencia 📝

Este proyecto está bajo la Licencia MIT. Consulte el archivo LICENSE para obtener más detalles.

En este archivo, se describe el sistema de votación y las tecnologías utilizadas. También se incluyen instrucciones para la instalación y el uso de la aplicación, así como información sobre cómo contribuir al proyecto y la licencia bajo la que se distribuye. Además, se incluye información sobre la configuración de la base de datos y el acceso a la aplicación.