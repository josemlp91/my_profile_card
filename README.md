# My Profile Card


### Estructura del proyecto 📂

El proyecto queda estructurado en los siguientes directorios:
Divido los directorios en tres **categorías**.

1. **Infra**, su propósito es preparar el entorno, instalar las dependencias y otras magias.
2. **UI / UX**, contiene el código para darle forma y color a la web, generalmente HTML, CSS.
3. **Content**, contiene artículos y publicaciones en markdown.
4. **Code**, contiene scripts en python para hacer pequeñas magias con Pelican y Python.

Y tendríamos los siguientes directorios:

- **.github** (infra) Aquí se definen las cosas referentes a la integración continua, (mejor no tocarlo mucho xD)
- **compose** (infra) Aquí se definen los manifiestos Docker, que preparan todo lo necesario para que funcione en tu localhost.
- **content** (content) Aquí se alojan los articulos y publicaciones en formato Markdown.
- **plugins** (code) Plugins de Pelican.
- **themes** (ui/ux) Código HTML y CSS que pone bonita la web.
- **output** (autogenerado) Aquí se guarda el código de la web compilado, se genera automáticamente, por lo tanto **no modifiques manualmente**.


### Localhost 👨🏼‍💻

Para arrancar este proyecto en local, independientemente del sistema operativo que uses, tienes dos alternativas


#### Docker 🐳

Para ello necesitas [Docker](https://www.docker.com/get-started) y [docker-compose](https://docs.docker.com/compose/install/).

```sh
docker-compose up --build
```

Accede con tu navegador a la url [localhost:8080](http://localhost:8080)

#### Python & Virtualenv 🐍

Debes tener instalado Python >= 3.6 y [virtualenv](https://virtualenv.pypa.io/en/latest/) y seguir los siguientes pasos:

1. Crear un virtualenv propio para este proyecto y activarlo

```bash
virtualenv venv
source ./venv/bin/activate
```

2. Instalar las dependencias Python necesarias

```bash
pip install -r requirements.txt
```

3. Iniciar el servidor web en local con el script o con make indicando de forma opcional el puerto deseado (por defecto 8000)

- Opción 1
```bash
./develop_server.sh start {PORT}
```

- Opción 2
```bash
 make devserver PORT={PORT}
```


## Despliegue y puesta en producción de la web 🚀

La web cuenta con un sistema de despliegue continuo, de forma que cada cambio (commit) en la rama ``main`` la web se compila y se sube a ``github pages``, usando [GitHub Pages Pelican Build Action](https://github.com/marketplace/actions/github-pages-pelican-build-action).

