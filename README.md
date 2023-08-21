pipenv install;
pipenv run start
pipenv run init;
pipenv run migrate;
pipenv run upgrade;

####

Estan junto los dos proyectos de api de star wars y el de autenticacion, las apis de star wars no estan conectadas al fron solo la de autenticarse, las apis se pueden testear con postman, para correr elproyecto de autenticacion hay que arrancar el back y a la vez abrir el front por separado con npm run dev - el front consume la ruta del back en el localhost puerto 3000
