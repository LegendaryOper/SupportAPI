# SupportAPI
Приложение “Support”.

Технические требования:
Никакого фронта/темплейтов, только Backend API, стремимся к REST архитектуре.
Технологии:
Django + Django Rest Framework, JWT авторизация, PostgreSQL, Docker (Docker-compose), PyTests (для тестов, лучше пару написать, просто чтобы понимать что это и зачем, и как с этим работать), Celery и Redis в качестве брокера сообщений. 
Для код стайла: 
flake8(можно и другие либы юзать, если у вас с ними есть опыт, только поставьте ограничение длины строки на 120 символов), isort(для импортов).=

Описание бизнес задачи:
Базово:
Служба саппорта:
1) Пользователь пишет тикет и отправляет.
2) Саппорт видит решенные, нерешенные и замороженные тикеты (все по факту), может отвечать на них.
3) Пользователь может просмотреть ответ саппорта, и добавить новое сообщение( саппорт ответить на него).
4) Саппорт может изменять статусы тикетов.

Дополнительно:
Рассылка уведомлений об изменении статуса на почту
