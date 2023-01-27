from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime, BigInteger, create_engine, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    tg_id = Column(BigInteger, nullable=False)
    city = Column(String(20))
    connection_date = Column(DateTime, default=datetime.now(), nullable=False)
    reports = relationship('WeatherReport', backref='report', lazy=True, cascade='all, delete-orphan')

    def __repr__(self) -> str:
        return self.tg_id


class WeatherReport(Base):
    __tablename__ = 'weather_reports'
    id = Column(Integer, primary_key=True)
    owner = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(DateTime, default=datetime.now, nullable=False)
    temp = Column(Integer, nullable=False)
    feels_like = Column(Integer, nullable=False)
    wind_speed = Column(Integer, nullable=False)
    pressure_mm = Column(Integer, nullable=False)
    city = Column(String, nullable=False)

    def __repr__(self):
        return self.city


engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

### ONE TO MANY
# session.add(User(tg_id='98217369', city='Kostroma'))
# user1 = session.query(User).filter_by(tg_id='98217369').first()
 
# session.add(WeatherReport(temp=-30, owner=user1.id, feels_like=-35, wind_speed=5, pressure_mm=760, city='Anadyr'))
# report1 = session.query(WeatherReport).filter_by(id=2).first()
# user1.reports.append(report1)

# session.commit()


#session.add(WeatherReport(temp=-10, feels_like=-15, wind_speed=5, pressure_mm=768, city='Moscow'))
# session.add(Book(title='Jorney to the center of Earth', author='Jul Vern'))
#user1 = session.query(User).filter_by(tg_id='98217369').first()
#report1 = session.query(WeatherReport).filter_by(id=1).first()
#user1.reports.append(report1)


# session.add(User(name='user2'))
# session.add(Reviews(text='Замечатьльный роман о приключениях Робинзона', book_id=1, user_id=1)) # Отзыв о книге 1 от пользователя 1
# session.add(Reviews(text='Замечатьльный роман о путешествии к центру земли', book_id=2, user_id=2)) # Отзыв о книге 2 от пользователя 2
# session.add(Reviews(text='Мне не понравилось', book_id=1, user_id=2)) # Отзыв о книге 1 от пользователя 2
# session.commit()

# stmt = select(Book).where(Book.title == 'Robinson Cruzo')
# for book in session.scalars(stmt):
#     print(book.reviews[1].text)

### MANY TO MANY
# book1 = session.query(Book).filter_by(title='Robinson Cruzo').first()
# book2 = session.query(Book).filter_by(title='Jorney to the center of Earth').first()
# user1 = session.query(User).filter_by(name='user1').first()
# user2 = session.query(User).filter_by(name='user2').first()
# book1.readers.append(user1)
# book1.readers.append(user2)
# book2.readers.append(user1)
# book2.readers.append(user2)
# session.commit()

###ONE TO ONE
# book1 = session.query(Book).filter_by(title='Robinson Cruzo').first()
# film1 = Film(name='Невероятные приключения Робинзона', producer='Квентин Тарантино', book_id=book1.id)
# film2 = Film(name='Не правильный фильм', producer='Не Квентин Тарантино', book_id=book1.id)
# session.add(film1)
# session.add(film2)
# session.commit()


