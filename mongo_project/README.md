# 💾 Проект: Управление пользователями и подписками

## 📦 Установка и запуск

Установка зависимостей: pip install pymongo
Запуск MongoDB Shell: mongosh

## 📁 Структура проекта

    /project-root
    ├── db.py                 # Подключение к базе данных
    ├── user.py               # Класс User
    ├── service.py            # Работа с услугами
    ├── utils.py              # Утилиты: валидации, генерация пароля
    ├── data_init.py          # Первичное наполнение БД
    ├── test_user.py          # Пример тестирования
    └── README.md             # Этот файл

---

### 📂 Работа с базами данных

    show dbs                     // Показать все базы данных
    use mydb                     // Перейти в базу данных mydb
    use newdb                    // Создать новую базу данных newdb // чтобы ее увидеть, надо создать коллекцию
    db.createCollection('dc')    // Создать коллекцию
    db.dc.insertOne({"name": "N", "country": "USA"})    // Создать документ коллекции (можно сразу, без создания коллекции)
    db.dc.insertMany([{}, {}, {}])   // Создать много документов коллекции
    db.dc.find()                 // Посмотреть все документы коллекции
    db.dropDatabase()            // Удалить текущую базу данных

### 📁 Работа с коллекциями

    show collections             // Показать все коллекции
    db.users.find().pretty()     // Показать всех пользователей
    db.services.find()           // Показать все услуги
    db.users.deleteMany({})      // Удалить всех пользователей
    db.services.deleteMany({})   // Удалить все услуги

### ➕ Добавление документов вручную

    db.users.insertOne({
      name: "Алексей",
      login: "aleksei_01",
      password: "Password123",
      is_blocked: false,
      subscription_date: new Date(),
      subscription_mode: "free",
      services: []
    })

    db.services.insertOne({
      name: "Premium",
      type: 1,
      cost: 500,
      period_days: 30
    })

### ✏️ Обновление и удаление

    db.users.updateOne(
      { login: "aleksei_01" },
      { $set: { is_blocked: true } }
    )

    db.users.deleteOne({ login: "aleksei_01" })

### Сортировка данных

# По возрастанию (1) или убыванию (-1)
db.collection.find().sort({ поле: 1 })       # по возрастанию
db.collection.find().sort({ поле: -1 })      # по убыванию

# Сортировка по нескольким полям
db.collection.find().sort({ поле1: 1, поле2: -1 })

# Сортировка с ограничением количества
db.collection.find().sort({ поле: 1 }).limit(5)

# Сортировка с пропуском результатов
db.collection.find().sort({ поле: -1 }).skip(10).limit(5)


### Сортировка данных в MongoDB с условиями и параметрами

# Общий синтаксис:
db.collection.find(Условие).sort({ поле: 1 или -1 })

# Условия фильтрации:
# — равенство
{ "field": "value" }

# — больше, меньше и т.д.
{ "field": { $gt: значение } }     # больше
{ "field": { $lt: значение } }     # меньше
{ "field": { $gte: значение } }    # больше или равно
{ "field": { $lte: значение } }    # меньше или равно
{ "field": { $ne: значение } }     # не равно

# — логические операторы
{ $or: [ { поле1: значение }, { поле2: значение } ] }
{ $and: [ { поле1: значение1 }, { поле2: значение2 } ] }

---

## Основные методы обновления

- `updateOne(filter, update)` — обновить один документ, подходящий под фильтр  
- `updateMany(filter, update)` — обновить все документы, подходящие под фильтр  
- `replaceOne(filter, replacement)` — полностью заменить один документ

---

## Операторы обновления

| Оператор  | Описание                                                |
|-----------|---------------------------------------------------------|
| `$set`    | Устанавливает или обновляет значение поля                |
| `$unset`  | Удаляет поле из документа                                |
| `$inc`    | Увеличивает или уменьшает числовое значение поля         |
| `$push`   | Добавляет элемент в массив                               |
| `$pull`   | Удаляет элементы из массива по условию                  |
| `$addToSet` | Добавляет элемент в массив, если его там ещё нет       |
| `$rename` | Переименовывает поле                                     |

---

## 🔄 Резервное копирование и восстановление

### 📤 Экспорт данных в JSON

    // Экспорт коллекции users
    mongoexport --db=mydb --collection=users --out=users.json

    // Экспорт коллекции services
    mongoexport --db=mydb --collection=services --out=services.json

### 📥 Импорт данных из JSON

    // Импорт коллекции users
    mongoimport --db=mydb --collection=users --file=users.json --jsonArray

    // Импорт коллекции services
    mongoimport --db=mydb --collection=services --file=services.json --jsonArray

### 🗄 Полный бэкап базы данных

    mongodump --db=mydb --out=backup/

### ♻️ Восстановление из бэкапа

    mongorestore --db=mydb backup/mydb

---

## 🧪 Тестирование проекта

1. Инициализация базы:

    python data_init.py

2. Запуск тестов (например, создание пользователей и подключение услуг):

    python test_user.py

---

### 📌 Типы данных MongoDB

| Тип данных     | Описание                                          | Пример                                      |
|----------------|---------------------------------------------------|----------------------------------------------|
| `String`       | Строка                                            | `"name": "David Bowie"`                     |
| `NumberInt`    | Целое число (32-битное)                          | `"year": NumberInt(1977)`                   |
| `NumberLong`   | Целое число (64-битное)                          | `"views": NumberLong(1234567890)`           |
| `Double`       | Число с плавающей точкой                         | `"rating": 8.7`                              |
| `Boolean`      | Логическое значение                               | `"is_active": true`                         |
| `Date`         | Дата и время                                      | `"release_date": ISODate("1977-05-25")`     |
| `Array`        | Массив                                            | `"genres": ["rock", "glam", "pop"]`         |
| `Object`       | Вложенный объект                                  | `"label": { "name": "EMI", "country": "UK" }` |
| `ObjectId`     | Уникальный идентификатор MongoDB                 | `_id: ObjectId("64eabc...")`                |
| `Null`         | Отсутствие значения                               | `"middle_name": null`                       |
| `Binary`       | Двоичные данные                                   | `"file": BinData(0, "4a6f686e446f65")`       |
| `Timestamp`    | Временная метка (для системных нужд)             | `"ts": Timestamp()`                         |
| `Decimal128`   | Высокоточные десятичные числа                    | `"price": NumberDecimal("19.99")`           |
| `Regex`        | Регулярное выражение                              | `"login": { "$regex": "^admin" }`           |

