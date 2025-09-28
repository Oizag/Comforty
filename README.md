платформа интернет-магазина товаров для дома, построенная на Vue 3 и Django REST Framework.

![Vue.js](https://img.shields.io/badge/Vue.js-3.5.18-4FC08D?style=flat&logo=vue.js)
![Django](https://img.shields.io/badge/Django-5.2.6-092E20?style=flat&logo=django)
![TypeScript](https://img.shields.io/badge/TypeScript-5.8.0-3178C6?style=flat&logo=typescript)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.4.17-38B2AC?style=flat&logo=tailwind-css)

## 📁 Структура проекта

```
comforty/
├── backend/                 # Django REST API
│   ├── config/             # Настройки Django
│   │   ├── settings.py     # Конфигурация
│   │   ├── urls.py         # URL маршруты
│   │   └── wsgi.py         # WSGI конфигурация
│   ├── manage.py           # Django management script
│   ├── requirements.txt    # Python зависимости
│   └── .env                # Переменные окружения
├── frontend/               # Vue 3 приложение
│   ├── src/
│   │   ├── components/     # Vue компоненты
│   │   │   ├── common/     # Общие компоненты
│   │   │   ├── layout/     # Компоненты макета
│   │   │   └── product/    # Компоненты товаров
│   │   ├── views/          # Страницы приложения
│   │   ├── stores/         # Pinia stores
│   │   ├── services/       # API сервисы
│   │   ├── types/          # TypeScript типы
│   │   ├── router/         # Vue Router
│   │   └── assets/         # Статические ресурсы
│   ├── package.json        # Node.js зависимости
│   ├── vite.config.ts     # Vite конфигурация
│   └── tailwind.config.js # Tailwind CSS конфигурация
├── docker-compose.yml      # Docker конфигурация
├── .gitignore              # Git ignore правила
└── README.md               # Документация
```
