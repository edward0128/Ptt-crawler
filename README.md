# Ptt-crawler

使用 dokcer 進行環境建置

```
安裝 docker 
ap-get install docker

建置系統 jupyter

 cd jupyter
 docker build -t jupyter:v1 .

啟動 docker -p 設定 Port 號

docker run -dit -p 8888:8888 -p 22:9527 jupyter:v1

`````
執行系統後，會出現以下訊息

root@XXXX:/home/gemini/jupyter# docker run -it -p 8888:8888 -p 9527:22 jupyter:v1
 * Starting OpenBSD Secure Shell server sshd                                                                                                              [ OK ]
[I 08:20:46.877 NotebookApp] Writing notebook server cookie secret to /home/jovyan/.local/share/jupyter/runtime/notebook_cookie_secret
[I 08:20:47.301 NotebookApp] JupyterLab extension loaded from /opt/conda/lib/python3.6/site-packages/jupyterlab
[I 08:20:47.301 NotebookApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
[I 08:20:47.307 NotebookApp] Serving notebooks from local directory: /home/jovyan
[I 08:20:47.307 NotebookApp] The Jupyter Notebook is running at:
[I 08:20:47.307 NotebookApp] http://(1f6fd0c7670f or 127.0.0.1):8888/?token=141deac21ecb4f436a115303b95079c53f2080ed2c483e29
[I 08:20:47.307 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 08:20:47.308 NotebookApp]

    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://(1f6fd0c7670f or 127.0.0.1):8888/?token=141deac21ecb4f436a115303b95079c53f2080ed2c483e29
[I 08:21:25.486 NotebookApp] 302 GET / (192.168.54.34) 2.00ms
[I 08:21:25.510 NotebookApp] 302 GET /tree? (192.168.54.34) 1.36ms
[I 08:21:48.025 NotebookApp] 302 POST /login?next=%2Ftree%3F (192.168.54.34) 4.43ms
```
```
   使用瀏覽器連結到 jupyter
   http://10.18.188.80:8888/?token=141deac21ecb4f436a115303b95079c53f2080ed2c483e29
   
   環境建置完成，如果測試完成，可以使用 docker run -dit 將此服務跑在後端
   

```



