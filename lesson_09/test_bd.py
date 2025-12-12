from sqlalchemy import create_engine, inspect, text


db_connection_string = "postgresql://postgres:1234@localhost:5432/postgres"
db = create_engine(db_connection_string)


def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[1] == 'users'


def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("""
        INSERT INTO subject("subject_title", "subject_id")
        VALUES (:title, :id)
    """)

    connection.execute(sql, {"title": "TOE", "id": "222"})
    transaction.commit()
    connection.close()


def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("""
    UPDATE subject
    SET subject_title = :subject_title
    WHERE subject_id = :id
""")
    connection.execute(sql, {"subject_title": 'New TOE', "id": 10})

    transaction.commit()
    connection.close()


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM subject WHERE subject_id = :id")
    connection.execute(sql, {"id": 10})

    transaction.commit()
    connection.close()
