from sqlalchemy import create_engine


class DatabaseLoader:
    def __init__(self, database_name) -> None:
        connection_url = "mysql+pymysql://root:root@127.0.0.1/" + database_name
        self.connection = create_engine(connection_url)

    def load_to_database(self, dataframe, table_name) -> None:
        dataframe.to_sql(
            table_name,
            self.connection.connect(),
            if_exists="append",
            index=False,
        )
