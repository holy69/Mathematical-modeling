import matplotlib.pyplot as plt

# Данные
years = [2024, 2025]
attacks = [970, 0]

# Настройка графика
plt.figure(figsize=(8, 6))
plt.bar(years, attacks, color=['#ff6b6b', '#4ecdc4'], edgecolor='black')
plt.title("DDoS-атаки через уязвимости ПО до и после SberOS", fontsize=14, pad=20)
plt.xlabel("Год", fontsize=12)
plt.ylabel("Количество атак", fontsize=12)
plt.xticks(years, ["До перехода", "После перехода"])
plt.grid(axis='y', linestyle='--')

# Аннотации
for i, value in enumerate(attacks):
    plt.text(i, value + 20, str(value), ha='center', va='bottom', fontsize=12)

plt.show()