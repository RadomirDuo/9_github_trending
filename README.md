# Github тренды

Скрипт `github_trending.py` при выполнении возвращает тренды github'а за последнюю неделю:

- название репозитория;
- описание репозитория;
- количество звёзд;
- количество задач;
- ссылка на репозиторий;

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```
python github_trending.py

Введите количество репозиториев для показа: 10

Название: preact-cli
Описание: Your next Preact PWA starts in 30 seconds.
Количество звёзд: 1008
Количество задач: 26
Ссылка: https://github.com/developit/preact-cli

Название: wannakey
Описание: Wannacry in-memory key recovery
Количество звёзд: 884
Количество задач: 1
Ссылка: https://github.com/aguinet/wannakey

Название: whats-new-in-swift-4
Описание: An Xcode playground showing off the new features in Swift 4.0.
Количество звёзд: 800
Количество задач: 1
Ссылка: https://github.com/ole/whats-new-in-swift-4

...
```

# Ограничения

Приложение будет работать корректно до превышения лимита запросов 
(На момент создания скрипта, ограничения не более 60 запросов в час)

# Цель проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
