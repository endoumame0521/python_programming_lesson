"""
SQLAlchemyについて

SQLAlchemyとは
・リレーショナルデータベースとpythonがやり取りをする為のライブラリ
・直接SQL文を書かなくてもデータベース操作が可能
・クラスを作成する事でテーブルを作成できたりとオブジェクト指向でデーターベースを操作できる
・設定を変更するだけで、後にsqliteやmysqlやPostgreSQLといったリレーショナルDBを切り替える事が容易にできる
"""


import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

# 使用するデータベースを設定（今回はsqlite）
engine = sqlalchemy.create_engine('sqlite:///test_sqlite2.db', echo=True)
# engine = sqlalchemy.create_engine(
#     'mysql+pymysql:///test_mysql_database2', echo=True)

# SQLAlchemyのベースクラスを定義
Base = sqlalchemy.ext.declarative.declarative_base()


# SQLAlchemyのベースクラスを継承したPersonクラスを作成
class Person(Base):
    # テーブルの名前を定義
    __tablename__ = 'persons'
    # 各カラムを定義
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))


# 使用するデータベースの種類を設定(上で定義したengineを引数に渡す)
Base.metadata.create_all(engine)

# データベースにアクセスする為のセッションを作成
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

# personsテーブルにデータを投入
p1 = Person(name='Mike')
session.add(p1)
p2 = Person(name='Nancy')
session.add(p2)
p3 = Person(name='Jun')
session.add(p3)
session.commit()

# personsテーブルのデータを更新
p4 = session.query(Person).filter_by(name='Mike').first()
p4.name = 'Michel'
session.add(p4)
session.commit()

# personsテーブルのデータを更新
p5 = session.query(Person).filter_by(name='Nancy').first()
session.delete(p5)
session.commit()

# personsテーブルのデータを全て取得し、for文で一個づつ取り出し
persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)
