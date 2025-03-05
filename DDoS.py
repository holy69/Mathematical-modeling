import matplotlib.pyplot as plt
import numpy as np

# ---------------------------
# ГРАФИК 1: Снижение DDoS-атак после перехода на SberOS
# ---------------------------
plt.figure(figsize=(10, 6))

(до и после внедрения SberOS)
categories = ['Атаки через уязвимости ядра', 'Амплификация DNS', 'SSDP-флуд', 'Слабые TLS-конфигурации']
before = [38, 25, 22, 15]  # % атак до
after = [8, 12, 5, 3]       # % атак после

x = np.arange(len(categories))
width = 0.35

plt.bar(x - width/2, before, width, label='До внедрения SberOS', color='#ff6b6b')
plt.bar(x + width/2, after, width, label='После внедрения SberOS', color='#4ecdc4')

plt.title('Снижение DDoS-атак за счёт устранения уязвимостей', fontsize=14)
plt.xticks(x, categories, rotation=15)
plt.ylabel('Доля атак, %', fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='--')

# ---------------------------
# ГРАФИК 2: Эффективность защиты
# ---------------------------
plt.figure(figsize=(8, 6))

# Данные для радиарной диаграммы
labels = ['Устранение уязвимостей', 'Фильтрация трафика', 'Лимит запросов', 'Шифрование', 'Изоляция сервисов']
values = [85, 70, 90, 95, 80]  

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
values += values[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.fill(angles, values, color='#1f77b4', alpha=0.25)
ax.plot(angles, values, color='#1f77b4', marker='o')
ax.set_theta_offset(np.pi/2)
ax.set_theta_direction(-1)
plt.xticks(angles[:-1], labels)
plt.yticks([20, 40, 60, 80, 100], color='grey', size=10)
plt.title('Эффективность SberOS против DDoS-векторов', pad=30)
plt.show()
