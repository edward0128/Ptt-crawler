cat /sys/fs/cgroup/cpu/docker/cpu.shares

for i in {8000..8333};

do
    docker run -dit -m 25M -c 2  -p $i:80 nginx:latest
    echo "start $i"
done
