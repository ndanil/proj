import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Rings(SqlAlchemyBase):
    __tablename__ = 'rings'
    days = ['Пн','Вт','Ср','Чт','Пт','Сб']
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    starttime = sqlalchemy.Column(sqlalchemy.Integer)
    endtime = sqlalchemy.Column(sqlalchemy.Integer)
    dayofweek = sqlalchemy.Column(sqlalchemy.Integer)
    timetable = orm.relation('TimeTables', back_populates='rings')

    def time_to_str(self,t):
        return f'{t//60//10}{t//60%10}:{t%60//10}{t%60%10}'

    def __str__(self):
        return f'{self.days[self.dayofweek-1]} {}-{}'