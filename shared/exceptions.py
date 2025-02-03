class ConnectionExceptions:
    @staticmethod
    def handle_connection_error(e):
        print(f"Database connection error: {e}")
        return None, None

    @staticmethod
    def handle_closing_error(e):
        print(f"Error while closing the database connection: {e}")

    @staticmethod
    def handle_unexpected_error(e, action=""):
        print(f"Unexpected error while {action}: {e}")