+++
title = "Learning Spark: Lightning-Fast Data Analytics"
author = ["r_hasan"]
description = "Book Review - Build your pipelines with Apache Airflow"
date = 2024-01-05T00:00:00+00:00
draft = false
+++

> ******data engineers****** will learn how to use **Spark’s Structured APIs** to perform
> complex data exploration and analysis on both batch and streaming data; use **Spark
> SQL** for interactive queries; use Spark’s built-in and external **data sources** to read,
> refine, and write data in different file formats as part of their extract, transform, and
> load (ETL) tasks; and build reliable data lakes with Spark and the open source **Delta
> Lake table format**.
>
> for ******data scientists and machine learning engineers******, Spark’s **MLlib library** offers many
> common algorithms to build distributed machine learning models. This book covers
> how to build pipelines with MLlib, best practices for distributed machine learning, how to use Spark to scale single-node models, and how to manage and deploy these models using the open source library **MLflow**.


## Chapter 1: Introduction to Apache Spark: A Unified Analytics Engine {#chapter-1-introduction-to-apache-spark-a-unified-analytics-engine}

> 1.  A Unified Analytics Engine
> 2.  It's genesis, inspiration and adoption

**Keywords**: GFS, MapReduce, BigTable, data locality, cluster rack affinity

This chapter talks about the main components of the spark project and spark's distributed architecture.

The background goes like: Google at it's urgency to handle large volume of data had introduced the Google File System (GFS), MapReduce, BigTable. Taking inspiration from their published papers yahoo engineers came up with Hadoop File System and donated this to Apache. The shortcomings of MapReduce which are 1. hard to manage and administer with operational complexity 2. It's verbose API and lot of boilerplate setup code and 3. Intermediate computed results stored on the local disk affecting performance. To handle these engineers developed bespoke systems (Apache Hive, Apache Strom, Apache Impala, Apache Giraph, Apache Drill, Apache Malhout etc.). But all of them had their own learning curve with operational complexity. So Spark was introduced.

Apache Hadoop Framework: Hadoop Common, MapReduce, HDFS, and Apache Hadoop YARN.

> Simple things should be simple, complex things should be possible -- Alan Kay

Spark's design philosophy centers around four key characteristics:

1.  Speed

    Spark pursued this by

    -   Todays servers come cheap
    -   Spark builds it's query computations as DAG. The DAG schedular and query optimizer constructs effective computational graph
    -   Tungsten, physical execution engine, uses whole-stage code generation to generate compact code for execution.
2.  Ease of use

    provides a fundamental abstraction of a simple logical data structure called RDD. provides a set of transformation and actions which offers a simple programming model to build apps in familiar languages.
3.  Modularity

    Spark SQL, Spark Structured Streaming, Spark MLlib, and GraphX
4.  Extensibility

    Spark focuses on it's fast, parallel computation engine rather than on storage.

We use APIs to write spark application and spark converts this into a DAG that is executed by the core engine.

Spark's components:

-   **driver**: the orchestrator, orchestrates paraller operations on the cluster. Access the distributed components (cluster manager and spark executor) through a SparkSession.

    Key responsibilites:

    -   instantiating a SparkSession
    -   communicates with the cluster manager
    -   requests resoureces from the cluster manager for executors
    -   transforms all the spark operations into DAG computations, schedules them
    -   distributes their execution as tasks across the spark executors.
    -   communicates directly with the executors (after resoureces are allocated)
-   **SparkSession**:

    Not only did it subsume previous entry points to Spark like the SparkContext, SQLContext, HiveContext, SparkConf, and StreamingContext, but it also made working with Spark simpler and easier.

-   **Cluster Manager**:

    responsible for managing and allocationg resources. Currently supports standalone, yarn, mesos and kubernetes.

-   **Spark Executors**:

    runs on each worker node. In most deployment mode, only a single executor runs per node.

**Deployment Modes**: local, standalone, yarn(client), yarn(cluster), kubernetes.


### Distributed data and partitions {#distributed-data-and-partitions}

Though this is not always possible, each Spark executor is preferably allocated a task that requires it to read the partition closest to it in the network, observing data locality.

Partitioning allows for efficient parallelism. A distributed scheme of breaking up data into chunks or partitions allows Spark executors to process only data that is close to them, minimizing network bandwidth.


### The WH Questions {#the-wh-questions}

-   what is apache spark?
-   how all the components of Spark’s distributed architecture work together and communicate?
-   what deployment modes are available?


## Chapter 2: Downloading Apache Spark and Getting Started {#chapter-2-downloading-apache-spark-and-getting-started}

Spark computations are expressed as operations.
These operations are then converted into low-level RDD-based bytecode as tasks,
which are distributed to Spark’s executors for execution.

since Spark 2.x, RDDs are now consigned to low-level APIs

Every computation expressed in high-level Structured APIs is
decomposed into low-level optimized and generated RDD opera‐
tions and then converted into Scala bytecode for the executors’
JVMs. This generated RDD operation code is not accessible to
users, nor is it the same as the user-facing RDD APIs

**important terms**:

-   Applicaton
-   SparkSession
-   Job
-   Stage
-   Task

---

Often stages are delineated on the operator’s computation boundaries, where they dictate data transfer among Spark executors.

One example of an operator that dictates data transfer among Spark executors is the shuffle operation. Shuffle operations occur when data needs to be redistributed across the cluster, such as when performing a join or a group-by operation. Shuffle operations create new stages, where the tasks in the previous stage write their output to local disk and the tasks in the next stage read the data from the remote executors.

Another example of an operator that dictates data transfer among Spark executors is the broadcast operation. Broadcast operations occur when a small amount of data needs to be sent to all the executors, such as when performing a broadcast join or a broadcast variable. Broadcast operations create new stages, where the tasks in the previous stage send their output to the driver and the driver broadcasts the data to the tasks in the next stage.

---

As such, an executor with 16 cores can have 16 or more tasks working on 16 or more partitions in parallel, making the execution of Spark’s tasks exceedingly parallel!


### The WH Questions {#the-wh-questions}

-   how the code is transofrmed and executed as tasks across the spark executors?
-   What is SparkSession?

    An object that provides a point of entry to interact with underlying Spark functionality and allows programming Spark with its APIs.
-   What is Job?

    A parallel computation consisting of multiple tasks that gets spawned in response to a Spark action (e.g., save(), collect()).
-   what is Stage?

    Each job gets divided into smaller sets of tasks called stages that depend on each other.
-   What is a Task?

    A single unit of work or execution that will be sent to a Spark executor.


## Chapter 3: Apache Spark’s Structured APIs {#chapter-3-apache-spark-s-structured-apis}


## Chapter 4: Spark SQL and DataFrames: Introduction to Built-in Data Sources {#chapter-4-spark-sql-and-dataframes-introduction-to-built-in-data-sources}

This chapter is all about reading and writing files in different format.

Parquet is the default data source in Spark. (Parquet is also the default table open format for Delta Lake(Parquet is also the default table open format for Delta
Lake)


## Chapter 5: {#chapter-5}


## Chapter 6: {#chapter-6}


## Chapter 7: Optimizing and Tuning Spark Applications {#chapter-7-optimizing-and-tuning-spark-applications}


## Chapter 8: Structured Streaming {#chapter-8-structured-streaming}


## Chapter 9: Building Reliable Data Lakes with Apache Spark {#chapter-9-building-reliable-data-lakes-with-apache-spark}


## Chapter 10: Machine Learning with MLlib {#chapter-10-machine-learning-with-mllib}


## Chapter 11: Managing, Deploying, and Scaling Machine Learning Pipelines with Apache Spark {#chapter-11-managing-deploying-and-scaling-machine-learning-pipelines-with-apache-spark}


## Chapter 12: Epilogue: Apache Spark 3.0 {#chapter-12-epilogue-apache-spark-3-dot-0}
