Start
To Run this flask application in a docker container

First Create an image by running this command
"docker build -t myflask ."

Next Start the container by running this command
"docker run -d -p 5000:5000 myflask"

Once you got your container id copy it and run this command to deploy the flask application
"docker exec <container_id> python main.py"

End
