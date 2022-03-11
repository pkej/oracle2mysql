# oracle2mysql
Create a migration from [oracle to mysql](https://dba.stackexchange.com/questions/114793/migrating-from-oracle-to-mysql-via-mysql-workbench-table-list-is-empty) using etlalchemy.

## Docker
- [x] ```DOCKER_BUILDKIT=1 docker build . --platform=linux/amd64```



## Installing
- [x] virtualenv -p /usr/bin/python2.7 venv
- [x] source venv/bin/activate
- [x] .gitignore
- [x] brew install pyenv
- [x] pyenv install pypy2.7-7.3.6
- [x] https://github.com/pyenv/pyenv#basic-github-checkout (from #2)
- [x] pip install [etlalchemy](https://github.com/seanharr11/etlalchemy)
- [x] [install_cx_oracle_mac](https://thelaziestprogrammer.com/sharrington/databases/oracle/install-cx_oracle-mac)
    - [x] [Instant Client Zip](https://download.oracle.com/otn_software/mac/instantclient/198000/instantclient-basic-macos.x64-19.8.0.0.0dbru.zip)
    - [x] [Instant Client SDK Zip](https://download.oracle.com/otn_software/mac/instantclient/198000/instantclient-sdk-macos.x64-19.8.0.0.0dbru.zip)
- [x] pip install cx_Oracle
- [ ] deactivate

## Ripped code, ideas and fixes from:
* https://github.com/CollinEstes/docker-node-oracle
* https://stackoverflow.com/questions/55823744/how-to-fix-cx-oracle-databaseerror-dpi-1047-cannot-locate-a-64-bit-oracle-cli
* https://vbaoverall.com/transfer-data-from-oracle-to-mysql-using-sqlalchemy-python/
* https://stackoverflow.com/questions/67908500/sql-alchemy-python-script-to-migrate-from-oracle-to-mysql
