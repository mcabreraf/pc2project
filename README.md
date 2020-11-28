# Pc2project - MYSQL, Jupyter notebook and Dash Server with Docker

Project created as a solution for the final assignment stablished by the teacher. 
This is a docker-compose build that creates a mysql server, jupyter server and dash server, each in a different container but all of them connected using a network.

Be aware of the following recommendations:

1. When building the project (using docker-compose up), it may take a while before starting due to the use of the many images, which, some of them, are heavy.
2. The dash server will probably restart the service at least three or more times. This is because this container is connected to the database and as a result, the database needs to initialize first. But docker starts all the services at the same time, giving the services that depends on database no to much time to connect with mysql. For this reason, the dash server will restart at least three times trying to reconnect with the database but at the end it will do it.
3. It was not necessary to implement a bind mount for all the files. This is because the database and dash server have their own Dockerfile which will use the other files as they fit. So, there was not really a reason for using a bind volume for just one volume (the one from the jupyter).
4. The Jupyter service needs a token when accesing to it. This token is automatically created by the server and can be located in the console of the container or by typing the command 'jupyter notebook list' in the CLI of the container.

And that's it! Enjoy!
