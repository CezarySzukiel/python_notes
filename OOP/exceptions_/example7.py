class Connection:
    def __init__(self):
        self.xid = 0

    def start_transaction(self):
        print("Starting transaction", self.xid)
        result = self.xid
        self.xid += 1
        return result

    @staticmethod
    def commit_transaction(xid):
        print("Committing transaction", xid)

    @staticmethod
    def rollback_transaction(xid):
        print("Rolling back transaction", xid)


class Transaction:
    def __init__(self, connection):
        self.connection = connection
        self.xid = connection.start_transaction()

    def commit(self):
        self.connection.commit_transaction(self.xid)

    def rollback(self):
        self.connection.rollback_transaction(self.xid)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.rollback()
        else:
            self.commit()
        return True


con = Connection()
with Transaction(con) as t:
    raise ZeroDivisionError("no many")
