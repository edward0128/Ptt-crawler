for i in {8000..8333};

do
    echo $i
    curl 127.0.0.1:$i
done
