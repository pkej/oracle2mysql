# oracle2mysql
Create a migration from [oracle to mysql](https://dba.stackexchange.com/questions/114793/migrating-from-oracle-to-mysql-via-mysql-workbench-table-list-is-empty) using etlalchemy.

## Run
Download instantclient-basic-linux.x64-12.2.0.1.0.zip and instantclient-sdk-linux.x64-12.2.0.1.0 from [Oracle](https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html) and place them in the "oracle/linux" folder.

Open the app.py file in your edior and add your own configuration for oracle and mysql.

```DOCKER_BUILDKIT=1 docker build . --platform=linux/amd64 --tag etlalchemy:latest``` 
to build the docker image

Run the image in Docker Desktop.

Open a shell into the image and run the command:
```apt-get install -y mariadb-server```

fill in the root password, doesn't matter what, we're not using it (or perhaps you are?)

```python /app/app.py```


## Ripped code, ideas and fixes from:
* https://github.com/seanharr11/etlalchemy
* https://github.com/CollinEstes/docker-node-oracle
* https://stackoverflow.com/questions/55823744/how-to-fix-cx-oracle-databaseerror-dpi-1047-cannot-locate-a-64-bit-oracle-cli
* https://vbaoverall.com/transfer-data-from-oracle-to-mysql-using-sqlalchemy-python/
* https://stackoverflow.com/questions/67908500/sql-alchemy-python-script-to-migrate-from-oracle-to-mysql
