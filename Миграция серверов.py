# Импорт необходимых библиотек
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------
# ГРАФИК 1: Динамика миграции серверов
# ---------------------------

# Данные для графика (гипотетические)
years = [2022, 2023, 2024]              # Годы миграции
servers = [10000, 25000, 43000]          # Количество перенесенных серверов

# Настройка стиля графиков
sns.set_style("whitegrid")               # Сетка на белом фоне
plt.figure(figsize=(10, 5))              # Размер графика

# Создание линейного графика
plt.plot(
    years,
    servers,
    marker='o',                          # Маркеры в виде кругов
    markersize=10,                       # Размер маркеров
    linewidth=3,                         # Толщина линии
    color='#1f77b4'                      # Синий цвет линии
)

# Настройка заголовка и подписей
plt.title("Динамика миграции серверов Сбербанка на SberLinux OS", pad=20)
plt.xlabel("Год", labelpad=15)
plt.ylabel("Кол-во серверов", labelpad=15)

# Настройка осей
plt.xticks(years)                        # Метки на оси X
plt.ylim(0, 50000)                       # Пределы оси Y

# Добавление аннотаций значений
for x, y in zip(years, servers):
    plt.text(
        x, y + 1500,                     # Позиция текста
        f'{y//1000}K',                   # Формат вывода (в тысячах)
        ha='center',                     # Горизонтальное выравнивание
        va='bottom',                     # Вертикальное выравнивание
        fontsize=12
    )

plt.tight_layout()  # Автоматическая настройка отступов

# ---------------------------
# ГРАФИК 2: Ключевые особенности ОС
# ---------------------------
plt.figure(figsize=(8, 8))               # Новое окно для графика

# Данные для круговой диаграммы
features = ['Безопасность', 'Локализация', 'Совместимость']
sizes = [45, 35, 20]                     # Процентное соотношение
colors = ['#ff6b6b', '#4ecdc4', '#45b7d1']  # Цвета сегментов

# Создание круговой диаграммы
plt.pie(
    sizes,
    labels=features,
    autopct='%1.1f%%',                   # Формат вывода процентов
    startangle=90,                       # Начальный угол
    colors=colors,                       # Цвета сегментов
    wedgeprops={'linewidth': 1, 'edgecolor': 'white'},  # Границы сегментов
    textprops={'fontsize': 12}           # Размер шрифта
)

plt.title("Распределение ключевых функций SberLinux OS", pad=25)

# ---------------------------
# ГРАФИК 3: Сертификации безопасности
# ---------------------------
plt.figure(figsize=(10, 5))              # Новое окно для графика

# Данные для столбчатой диаграммы
certifications = {
    'ФСТЭК УД1+': 5,     # Уровень доверия
    'ГОСТ Р 57580': 4,   # Стандарт шифрования
    'PCI DSS': 3         # Стандарт платежных систем
}

# Настройка позиций столбцов
x_pos = range(len(certifications))

# Создание столбчатой диаграммы
plt.bar(
    x_pos,
    certifications.values(),
    color='#4ecdc4',                     # Цвет столбцов
    edgecolor='black',                   # Границы столбцов
    linewidth=1
)

# Настройка осей и подписей
plt.xticks(x_pos, certifications.keys()) # Метки категорий
plt.ylabel('Уровень соответствия', labelpad=15)
plt.title('Сертификации безопасности SberLinux OS', pad=20)
plt.ylim(0, 6)                           # Пределы оси Y

# Добавление значений над столбцами
for i, value in enumerate(certifications.values()):
    plt.text(
        i,
        value + 0.2,
        str(value),
        ha='center',
        va='bottom',
        fontsize=12
    )

# Отображение всех графиков
plt.show()