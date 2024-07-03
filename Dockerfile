# Use uma imagem base oficial do Python
FROM python:3.12

# Defina o diretório de trabalho no contêiner
WORKDIR /usr/src/app

# Copie os arquivos de requisitos do seu projeto
COPY requirements.txt ./

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código do projeto
COPY . .

# Expor a porta que o servidor Django está usando
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "meu_projeto.wsgi:application"]
