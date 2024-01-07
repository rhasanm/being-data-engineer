# being-data-engineer

## Languages
```sh
sdk install scala 2.12.18 # for spark 3.5.0
```

## Tools
```sh
cd tools
wget https://dlcdn.apache.org/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz
tar xzvf spark-3.5.0-bin-hadoop3.tgz
cd spark-3.5.0-bin-hadoop3
echo 'export PATH=$PATH:'"$(pwd)"/bin >> ~/.zshrc
echo 'export SPARK_SHELL='"$(pwd)" >> ~/.zshrc
```

