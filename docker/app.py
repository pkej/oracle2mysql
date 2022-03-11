from etlalchemy import ETLAlchemySource, ETLAlchemyTarget

oracle_db_source = ETLAlchemySource("oracle+cx_oracle://username:password@hostname/SID")

mysql_db_target = ETLAlchemyTarget("mysql://username:password@hostname/db_name",
                                       drop_database=True)
mysql_db_target.addSource(oracle_db_source)
mysql_db_target.migrate()