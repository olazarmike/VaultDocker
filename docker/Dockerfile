# Imagen de ubuntu
FROM ubuntu

#Actualizar los paquetes de ubuntu
RUN apt -qq update

#Crear el virtual environment
RUN apt install python3-pip -y

#Para definir una variable del sistema q tenga la direccion en la que se ejecuta el servidor
RUN export VAULT_ADDR='http://localhost:8200/'

#Ejecutar main
COPY main.py /main.py

#Actualizar pip
RUN pip install --upgrade pip

#Instalar las dependencias
RUN python3 -m pip install hvac

CMD ["python3", "main.py"]