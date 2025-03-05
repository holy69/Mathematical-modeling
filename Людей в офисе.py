import matplotlib.pyplot as plt
import seaborn as sns

# Данные
labels = ['Windows', 'macOS', 'SberLinux OS']
sizes = [15000, 7000, 1000]
colors = ['#2D6AE2', '#A3A3A3', '#4BCA49']  # Синий, серый, зелёный (бренд Сбера)

# Настройка стиля
sns.set_style("whitegrid")
plt.rcParams.update({
    'font.size': 12,
    'axes.titlesize': 16,
    'axes.titleweight': 'bold',
    'axes.titlepad': 20
})

# 1. Улучшенная круговая диаграмма
fig, ax = plt.subplots(figsize=(12, 10))
wedges, texts, autotexts = ax.pie(
    sizes,
    colors=colors,
    startangle=90,
    explode=(0.03, 0.03, 0.1),  # Выделение SberLinux
    shadow=True,
    pctdistance=0.85,
    autopct=lambda p: f'{p:.1f}%\n({int(round(p*sum(sizes)/100))})',
    textprops={'fontsize': 12, 'color': 'black'}
)

# Настройка легенды
legend_labels = [f'{l} ({s} чел.)' for l, s in zip(labels, sizes)]
plt.legend(
    wedges,
    legend_labels,
    title="Операционные системы:",
    loc="upper left",
    bbox_to_anchor=(0.9, 0.8, 0.3, 0.2),
    frameon=True
)

# Центральная подпись
centre_circle = plt.Circle((0,0), 0.6, fc='white')
ax.add_artist(centre_circle)
ax.text(0, 0, f'Всего сотрудников:\n{sum(sizes):,}',
        ha='center', va='center', fontsize=14, fontweight='bold')

plt.title('Распределение операционных систем\nсреди сотрудников Сбербанка (офис на Кутузовском)',
          fontsize=16, pad=25)
plt.tight_layout()
plt.show()

# 2. Улучшенная столбчатая диаграмма
plt.figure(figsize=(14, 8))
ax = sns.barplot(x=labels, y=sizes, palette=colors, edgecolor='black', linewidth=2)

# Кастомизация графика
plt.title('Количество сотрудников по операционным системам', fontsize=16, pad=20)
plt.ylabel('Число сотрудников', fontsize=14, labelpad=15)
plt.xlabel('Операционная система', fontsize=14, labelpad=15)
plt.ylim(0, 16000)

# Аннотации и сетка
for p in ax.patches:
    ax.annotate(
        f'{p.get_height():,}\n({p.get_height()/sum(sizes):.1%})',
        (p.get_x() + p.get_width() / 2., p.get_height()),
        ha='center',
        va='center',
        xytext=(0, 9),
        textcoords='offset points',
        fontsize=12
    )

ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)
sns.despine(left=True)

# Добавление подсказки
plt.text(
    0.5, -0.15,
    '*Данные на 2024 год. Всего в офисе работает 23,000 сотрудников',
    transform=ax.transAxes,
    ha='center',
    fontsize=10,
    color='gray'
)

plt.tight_layout()
plt.show()