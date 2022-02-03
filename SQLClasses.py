from AppContainer import sqldb


class Player(sqldb.Model):
    id = sqldb.Column(sqldb.Integer(), primary_key=True, nullable=False)