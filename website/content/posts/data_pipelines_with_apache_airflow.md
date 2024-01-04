+++
title = "Data Pipelines with Apache Airflow"
author = ["r_hasan"]
description = "Book Review - Build your pipelines with Apache Airflow"
date = 2024-01-02T00:00:00+00:00
draft = false
+++

## Insights {#insights}

-   Airflow requires all tasks upstream of a given task to complete successfully before that the task itself can be executed


## Chapter 3 {#chapter-3}


### Best Practices for designing tasks {#best-practices-for-designing-tasks}

The two of the most important properties of proper Airflow tasks are atomicity and idempotency.

-   atomicity:

    > either all occurs or nothing occurs

    Suppose we have a dag whose purpose is to parse a file and store the processed data to another file/database table. This has another responsibility to send a success follow up email when all the tasks are completed. A sample code example can be
    ```python
    def send_email():
        # email sending logic

    def parse_process_email():
        # do something with the file
        parse()

        process()

        # send email
        send_email()

    final_task = PythonOperator(
        python_callable=parse_process_email,
        dag=dag
    )
    ```
    Now when the send email program fails, this marks the final task failed. Whereas we could declare a seperate task for email sending so that the final task result would not get affected when failed.
    ```python
    def send_email():
        # email sending logic

    def parse_process():
        parse()

        process()

    final_task = PythonOperator(
          python_callable=parse_process_email,
          dag=dag
    )

    email_sending_task = PythonOperator(
        python_callable=send_emai,
        dag=dag
    )

    final_task >> email_sending_task

    ```
    This can help us when debugging the dag. It will be more visible which part of the program is really affecting the result.

-   Idempotency:

    > If calling the same task multiple times with the same inputs has no additional effect.

    For example, If we had stored the processed data in a file, where each successful iteration we append the processed data to the file, then if the same input file was given then there will be duplicate data inserted. Where as if we created a new file with a pattern i.e kpi_2024_01_02, then when the same inputs file was given then the previous pattern file will be override with the processed data.


## Chapter 5: Defining dependencies between tasks {#chapter-5-defining-dependencies-between-tasks}


### Basic dependencies {#basic-dependencies}


#### linear dependencies {#linear-dependencies}


#### fan out/in dependencies {#fan-out-in-dependencies}


### Branching {#branching}


#### branching within tasks {#branching-within-tasks}


#### branching within the DAG {#branching-within-the-dag}


### Conditional Tasks {#conditional-tasks}


#### condition withing tasks {#condition-withing-tasks}


#### making tasks conditional {#making-tasks-conditional}


#### using built-in operators {#using-built-in-operators}


### Trigger Rules {#trigger-rules}


### Sharing Data between tasks {#sharing-data-between-tasks}


## Chapter 9: Testing {#chapter-9-testing}

-   Types of testing:
    -   acceptance
    -   integration
    -   unit

From the above this book covers the integration and unit testing, and pytest as testing framework.
