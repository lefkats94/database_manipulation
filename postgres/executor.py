from psycopg2 import sql
from connector import ConnectionManager

class ExecuteQuery:

    @staticmethod
    def get(table_name, columns=None, filter=None, order=None):

        # Select all columns if none are provided
        fields = sql.SQL("*") if columns is None else sql.SQL(", ").join(map(sql.Identifier, columns))

        query = sql.SQL("SELECT {fields} FROM {table}").format(fields=fields, table=sql.Identifier(table_name))

        if filter is not None:
            query += sql.SQL(" WHERE {}").format(sql.SQL(filter))

        if order is not None:
            query += sql.SQL(" ORDER BY {}").format(sql.Identifier(order))

        with self.connection.cursor() as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]

        return pd.DataFrame(data, columns=column_names)