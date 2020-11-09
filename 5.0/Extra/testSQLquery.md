# SQL Queries

<br>

## Selecting the Instance to the given Instance Key

    SELECT id FROM auvinstance WHERE AUV_Key = 'TestKey'

<br>

## Getting the value from the table

    SELECT Latitude, Longitude
    FROM coordinates
    INNER JOIN auvinstance ON auvinstance.ID = coordinates.Instance_Cordi_ID
    WHERE auvinstance.AUV_Key = 'TestKey'
    ORDER BY coordinates.ID DESC LIMIT 1

<br>

## Storing the value in the table: (Instace_Cordi... value comes from top most query)

First get ID of the instance to which to add

    SELECT id FROM auvinstance WHERE AUV_Key = 'TestKey'

Now store the value pertaining to that ID

    INSERT INTO coordinates (ID, Latitude, Longitude, Instance_Cordi_ID) VALUES (Null, '42.42', '42.42', 1)

<br>

## Updating values in the table

First get ID that instance in the table. Will give the latest stored data to that instance

    SELECT coordinates.ID
    FROM coordinates
    INNER JOIN auvinstance ON auvinstance.ID = coordinates.Instance_Cordi_ID
    WHERE auvinstance.AUV_Key = 'TestKey'
    ORDER BY coordinates.ID DESC LIMIT 1

Now update that value:

    UPDATE coordinates
    SET Latitude = '77.77', Longitude = '44.44'
    WHERE ID = 6;

<br>

## Creating an instance

    INSERT INTO auvinstance (ID, AUV_Name, AUV_Key) VALUES (Null, 'FinalName','Admin123')

Deleting an instance will delete all values related to it. To delete an instance:

    DELETE FROM auvinstance WHERE AUV_Key = 'admin123'