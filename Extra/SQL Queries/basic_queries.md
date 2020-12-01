# SQL Commands

Basic commands to perform CRUD operations in mysql. This file contains commands for v4.0. For the structure and the related queries for 5.0, refer to the folder *5.0 structure*.

<br>

## Python Initialization

It is assumed that the database is already uploaded on the MySQL server and the XAMPP server is running. 

- Database for 4.0 -> `4.0/SETUP/mio_python.sql`
- Database for 5.0 -> `5.0/Extra/Database/nio_server.sql`

First install the required library by running:

    pip install mysql-connector-python

Use the following function as a general function for any SQL query. Its parameters are as follows:

1. database = if using 4.0, = *nio_python*. If 5.0 = *nio_server*
2. query = The SQL query that you want to execute
3. address = IP where the MySQL server is running which here is the localhost(*127.0.0.1*)
4. sqlite = Not required for connecting to MySQL so keep it *False*
5. arg = use it for queries such as `INSERT INTO battery_value (id,value) VALUES (?,?)`, keep `arg = [None, 72]` (any value that you want to specify)
6. returnVal = If the query is returning any values (SELECT queries), make it *True* else (DELETE, UDATE, INSERT) *False*

        def sql_query(database,query, address=None,sqlite=False,arg=None,returnVal=False):
            if sqlite:
                connection = sqlite3.connect(database)
            else:
                connection = mysql.connector.connect(
                    user = 'root',
                    password = '',
                    host = address,
                    database = database
                )
            cursor = connection.cursor()
            if returnVal == False:
                if arg is None:
                    cursor.execute(query)
                else:
                    cursor.execute(query,arg)
                connection.commit()
                cursor.close()
                connection.close()
                return None
            else:
                if arg is None:
                    cursor.execute(query)
                    records = cursor.fetchall()
                else:
                    records = cursor.execute(query,arg)
                connection.close()
                return records

<br>

## Database Structure of v4.0

Name : nio_python

Tables within:

       TABLE NAME      COLUMNS
    1. battery_value : [id, value]
    2. boat_position : [id, latitude, longitude]
    3. cbot_position : [id, latitude, longitude]
    4. home_position : [id, latitude, longitude]
    5. depth         : [id, value, time stamp]
    6. mission_upload: [id, input, time_stamp, status]
    7. pitch_value   : [id, value]
    8. yaw_value     : [id, value]

___Note___: All columns (id) have attribute primary key and are auto-incremented

<br>

## Getting value from table

### Getting all values within Table

__Query__   : `SELECT * FROM <table_name>` <br>
__Function__: Will select all entities from that _table_

    SELECT * FROM battery_value

### Getting all values of specified column in Table

__Query__   : `SELECT <specific_column> FROM <table_name>`<br>
__Function__: Returns all values of _specified-column_ from that _table_

    SELECT value FROM battery_value

### Getting all values of specifeid column with condition

__Query__   : `SELECT <specified_column> FROM <table_name> WHERE <condition>`<br>
__Function__: Returns all values of _specifed-column_ from _table_ which specifies the given _condition_. Condition can be multiple with AND/OR statements and follows operators [=,<,>,<=,>=]
__Note__    : replace _specifed-column_ with * to get that row instead of just value of the specifed column

    SELECT value FROM battery_value WHERE id < 5 AND value >= 36

### Getting all values in order

__Query__   : `SELECT <specified_column1> FROM <table_name> ORDER BY <specifed_column2> <type>` <br>
__Function__: Returns all values of the _specified-column1_ from _table_. The values are arranged in the order as governed by _specified-column2_ according to the <type>.
__Note__    : <type> By default, type would be increasing (i.e in order 1,2,3,4...). Reverse can be specified by using `DESC` (i.e 5,4,3...1).

    SELECT * FROM battery_value ORDER BY id DESC

### Limiting the response

__Query__   : `SELECT <specified_column1> FROM <table_name> LIMIT <limiting_nuber>` <br>
__Function__: Returns only a specifed _number_ of items (starting from the top of the returned list). Eg, if returned value is a list [1,2,3,4], by giving limiting number = 1, the query will return only [1].

    SELECT * FORM battery_value LIMIT 2

<br>

## Inseting values into Table

### Inserting one element

__Query__   : `INSERT INTO <table_name> (<all_columns_within_table>) VALUES (<specified_value_to_be_inserted>)` <br>
__Function__: Inserts the _specifed-values_ in the _table_.
__Note__    : If any row has a __auto incremnet__, do not give it a value. Instead leave it as `None` or don't mention it. <br>

    INSERT INTO battery_value(value) VALUES (44)
_id_ not mentioned as is a auto-incremented

### Inserting multiple rows

__Query__   : `INSERT INTO <table_name> (<all_columns_within_table>) VALUES (<values_inserted_for_row1>), (<values_inserted_for_row2>)` <br>
__Function__: Inserts multiple rows into the _table_.

    INSERT INTO mission_upload (input, time_stamp, status) VALUES ('text1', '10:30', 'RUNNING'), ('text2', '10:32', 'ABORTED')

<br>

## Updating values in Table

## Updating one value

__Query__   : `UPDATE <table_name> SET <column_name_to_update> = <specifed_value> WHERE <conditioned_column_name> = <value_of_condition_column>` <br>
__Function__: Will update the _specified-value_ of the _column-name-to-update_ which satisfes the condition, _conditioned-column_ and the _conditioned-value_ related to it.

    UPDATE mission_upload SET status = 'UPLOADED' WHERE status = 'ABORTED'

## Updating multiple values

__Query__   : `UPDATE <table_name> SET <col_name_1> = <update_col_1>, <col_name_2> = <update_col_2> WHERE <conditioned_col> = <conditioned_col_val>` <br>
__Function__: Updates more than one columns in the _table_ according to the specifed _condition_

    UPDATE mission_upload SET status = 'TESTING' WHERE status ! = 'TESTING'
    UPDATE mission_upload SET status = 'TEST RUN 2', time_stamp = '7:44' WHERE status = 'TESTING'

<br>

## Deleting values in Table

### Deleting all rows

__Query__   : `DELETE FROM <table_name>` <br>
__Function__: Will delete all the rows inside the _specifed-table_, thus emptying it.

    DELETE FROM mission_upload

### Deleting specifed rows

__Query__   : `DELETE FROM <table_name> WHERE <conditioned_col> = <conditioned_col_value>` <br>
__Function__: Will delete the row which specifies the input _condition_

    DELETE FROM mission_upload WHERE status = 'WRONG STATUS'

### Delete specifed rows with limit

__Query__   : `DELETE FROM <table_name> LIMIT <limiting_number>` <br>
__Function__: In the order that the table has been arranged, will start deleting rows from the top. <br>
__Note__    : It is better to use this with `ORDER BY`

    DELETE FROM mission_upload ORDER BY input LIMIT 2

### Delete statement with limit and conditions

__Query__   : `DELETE FROM <table_name> WHERE <conditioned_col> = <conditioned_col_val> LIMIT <limiting_number>` <br>
__Function__: Combination of delte statement with all parameters: limit, conditioned, order by

    DELETE FROM mission_upload WHERE status = 'ABORTED' ORDER BY time_stamp DESC LIMIT 2