# Use a Python runtime as base image
FROM python:3.8-slim

WORKDIR app

# Copia o arquivo main.py para dentro do contêiner
COPY . /app

# Instala o cron
RUN apt-get update && apt-get -y install cron

# Cria um diretório para logs do cron
RUN touch /var/log/cron.log

# Cria o arquivo de cronjob
RUN echo "*/1 * * * * python /app/main.py main.py --path_json_config /app/apps.json" > /etc/cron.d/cronjob

# Dá permissões de execução ao script do cron
RUN chmod 0644 /etc/cron.d/cronjob

# Comando para iniciar o cron e manter o contêiner em execução
CMD ["cron", "-f"]
