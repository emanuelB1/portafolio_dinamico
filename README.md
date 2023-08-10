# Portafolio Personal
[Sitio Web Personal](https://emanuelbustos.com)
Este es mi portafolio personal. El portafolio está comentado y dockerizado para facilitar su despliegue en entornos de producción y desarrollo. Destaca por su dinamismo, ya que una vez desplegado, es totalmente actualizable desde el panel administrativo.

## Características

- Desarrollado en Python con el framework Django.
- Utiliza modelos para representar elementos como proyectos y contenido.
- Incorpora la lógica de un servicio de correo electrónico para mantenerme conectado.
- Comentado y estructurado para facilitar la comprensión y extensión del código.

## Despliegue

### Opciones de Despliegue 

El proyecto puede ser desplegado en dos entornos: producción o desarrollo. Asegúrate de elegir la configuración adecuada antes de continuar.

### Requisitos

- Docker solo en producción.
- Archivo `.env` en producción, configura las variables de entorno según tus necesidades.
- Python

### Pasos para el Despliegue

1. Clona este repositorio en tu máquina local.

2. Navega al directorio del proyecto: `cd nombre-de-tu-proyecto`

3. Crea y configure tu archivo `.env` con las variables de entorno necesarias.

4. Crea un Entorno Virtual e instala la bibliotecas: `python -venv venv` `pip install -r requirements.txt`

5. Despliega el proyecto en el entorno deseado (development o production): `python manage.py runserver --settings=config.settings.development`

6. Realiza las migraciones: `python manage.py makemigrations --settings=config.settings.development` `python manage.py migrate --settings=config.settings.development`

7. Crea un super usuario: `python manage.py createsuperuser --settings=config.settings.development`

8. Accede al panel administrativo en la URL http://localhost:8000/admin/ para comenzar a agregar contenido y proyectos.

### Contribuciones

- ¡Las contribuciones son bienvenidas! Si encuentras mejoras o correcciones, no dudes en hacer un pull request.

- Si tienes alguna pregunta o sugerencia, no dudes en contactarme a través de mi correo electrónico: contact@emanuelbustos.com

  Hecho con ❤️ por [emanuelB1](https://github.com/emanuelB1)



 
