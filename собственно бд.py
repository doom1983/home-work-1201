import sqlite3
from typing import List, Dict


# Создаем подключение к базе данных SQLite
conn = sqlite3.connect('composites.db')
cursor = conn.cursor()

# Создаем таблицу для хранения записей из Excel
create_table_query = '''
CREATE TABLE IF NOT EXISTS compositions (
    number INTEGER PRIMARY KEY AUTOINCREMENT,
    num TEXT,
    title TEXT,
    authors TEXT,
    references TEXT,
    year TEXT,
    abstract TEXT,
    keywords TEXT,
    publication_type TEXT,
    source TEXT,
    organization TEXT,
    note TEXT
)
'''
cursor.execute(create_table_query)

# Функция для вставки записи в базу данных
def insert_record(record: Dict[str, str]):
    columns = ', '.join(record.keys())
    placeholders = ':' + ', :'.join(record.keys())
    query = f'INSERT INTO compositions ({columns}) VALUES ({placeholders});'
    cursor.execute(query, record)
    conn.commit()

# Список записей из файла Excel
records = [
    {
        'num': '1',
        'title': 'Влияние различных полимеров и технологических добавок на свойства древесно-полимерных композитов',
        'authors': 'Сафин Р. Г., Фахрутдинов Р. Р.',
        # Остальные поля...
    },
    # Продолжайте добавлять остальные записи аналогичным образом
]

# Вставляем каждую запись в базу данных
for record in records:
    insert_record(record)

# Закрываем соединение с базой данных
conn.close()