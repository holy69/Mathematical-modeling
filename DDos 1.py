import matplotlib.pyplot as plt


years = [2024, 2025]
attacks = [970, int(970 * 0.6)]  # 970 → 582 (снижение на 40%)

# Настройка графика
plt.figure(figsize=(10, 6))
plt.bar(years, attacks,
        color=['#ff6b6b', '#4ecdc4'],
        edgecolor='black',
        width=0.6)

# Заголовок и подписи
plt.title("Снижение DDoS-атак на 40% после перехода на SberOS",
          fontsize=14, pad=20)
plt.xlabel("Год", fontsize=12)
plt.ylabel("Количество атак", fontsize=12)
plt.xticks(years, ["До перехода\n(2024)", "После перехода\n(2025)"], fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Аннотации с процентами
for i, value in enumerate(attacks):
    plt.text(
        x = years[i],
        y = value + 30,
        s = f"{value}\n(-{40 if i==1 else 0}%)",
        ha = 'center',
        va = 'bottom',
        fontsize=12,
        linespacing=1.5
    )

plt.ylim(0, 1050)
plt.tight_layout()
plt.show()
