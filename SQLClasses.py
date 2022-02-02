from server.AppContainer import sqldb


class Player(DB.createModel):
    id = DB.createColumn(DB.createInteger(), pkey=True, nullable=False)