# {{cookiecutter.project_name}}
{{cookiecutter.short_description}}

## Ejecutar modo de desarrollo
- Instala las dependencias del proyecto ejecutando `pip install -r requirements.txt`
- Crea un fichero en la raíz del proyecto llamado `.env` con la variable `TELEGRAM_TOKEN`. Ejemplo:
```
TELEGRAM_TOKEN=MYTELEGRAMTOKEN
```
- Ejecuta el bot usando el comando `python3 src/{{cookiecutter.main_file}}`

## Comandos
`/start`: Muestra la información del bot

`/greetings`: Muestra un mensaje preguntando tu nombre y te lo devuelve con un saludo