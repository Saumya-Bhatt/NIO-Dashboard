# SQL Queries

<br>

## Selecting the Instance to the given Instance Key

    SELECT id FROM auvinstances WHERE AUV_Key = 'TestKey'

<br>

## Getting the value from the table

    SELECT Uploaded_File, Time_Stamp
    FROM missionfile
    INNER JOIN auvinstances ON auvinstances.ID = missionfile.Instance_missionFile_ID
    WHERE auvinstances.AUV_Key = '123'
    ORDER BY missionfile.ID DESC

<br>

## Storing the value in the table: (Instace_Cordi... value comes from top most query)

First get ID of the instance to which to add

    SELECT id FROM auvinstance WHERE AUV_Key = 'TestKey'

Now store the value pertaining to that ID

    INSERT INTO coordinates (ID, Latitude, Longitude, Instance_Cordi_ID) VALUES (Null, '42.42', '42.42', 1)

<br>

## Updating values in the table

First get ID that instance in the table. Will give the latest stored data to that instance

    SELECT missionfile.ID
    FROM missionfile
    INNER JOIN auvinstances ON auvinstances.ID = missionfile.Instance_missionFile_ID
    WHERE auvinstances.AUV_Key = '123'
    ORDER BY missionfile.ID DESC LIMIT 1

Now update that value:

    UPDATE missionfile
    SET Uploaded_File = 'Updated_file', Time_Stamp = '44:44'
    WHERE ID = 1;

<br>

## Creating an instance

    INSERT INTO auvinstance (ID, AUV_Name, AUV_Key) VALUES (Null, 'FinalName','Admin123')

## Deleting an instance
Deleting an instance will delete all values related to it.

    DELETE FROM auvinstances WHERE AUV_Key = '987'