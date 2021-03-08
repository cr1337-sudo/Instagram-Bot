El bot tiene incluido geckodriver.exe que es el webdriver correspondiente a mozilla firefox.

copyusers.py

Se pregunta la cantidad de usuarios que se quieren scrapear (copiar el nombre) y el usuario donde se van a copiar los nombres.
Logea, se va al perfil del usuario y da click en el botón de seguidores.
Copia el nombre de las personas que se le pidan.
Crea un documento de texto donde se anotan los nombres de los usuarios.

followusers.py

Ingresa el documento de texto creado por copyusers.py
Sigue a los primeros 50 usuarios de la lista. En un futuro hay que hacer que se eliminen esos 50 primeros usuarios de forma automatica.