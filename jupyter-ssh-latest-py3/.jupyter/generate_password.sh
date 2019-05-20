#! /bin/bash

encode_password=$(python /root/.jupyter/password_generate.py $1)

echo "{\"NotebookApp\": {\"password\": \"$encode_password\"}}" > /root/.jupyter/jupyter_notebook_config.json
