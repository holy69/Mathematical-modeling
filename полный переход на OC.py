import matplotlib.pyplot as plt

# Данные
years = [2024, 2025, 2026, 2027]
windows = [65.2, 45.0, 20.0, 0.0]
macos = [30.4, 25.0, 10.0, 0.0]
sber = [4.3, 30.0, 70.0, 100.0]

# Создание графика
plt.figure(figsize=(10, 6))

# Линии
plt.plot(years, windows, label='Windows', marker='o')
plt.plot(years, macos, label='macOS', marker='s')
plt.plot(years, sber, label='SberLinux OS', marker='D')

# Настройки
plt.title('План перехода на SberLinux OS')
plt.xlabel('Год')
plt.ylabel('Доля (%)')
plt.legend()
plt.grid(True)

plt.show()