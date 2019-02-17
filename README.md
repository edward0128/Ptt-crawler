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

