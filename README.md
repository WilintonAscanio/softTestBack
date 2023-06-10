### Soft Test Back

A continuación se detalla como inicializar el proyecto :

# Características
Django, Djangorestframework

# Instalación
1. Clona el repositorio : 
git clone https://github.com/WilintonAscanio/softTestBack

2. Accede al directorio del proyecto : 
cd soft_back

3. Crea un entorno virtual e instala las dependencias: 
python -m venv venv
source venv/bin/activate (Linux/Mac) o venv\Scripts\activate (Windows)
pip install -r requirements.txt

4. Dentro de la carpeta soft_users accede al archivo settings.py y en donde dice DATABASES descomentar el código y agregar las credenciales necesarias.
5. Realiza las migraciones de la base de datos
: python manage.py migrate

6. Corre el servidor : #
python manage.py runserver

  




