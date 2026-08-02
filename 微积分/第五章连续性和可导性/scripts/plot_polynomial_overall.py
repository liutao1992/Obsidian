import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 输出目录
output_dir = Path(__file__).resolve().parent.parent / 'imgs'
output_dir.mkdir(parents=True, exist_ok=True)

# 函数 y = 3x^2 + 5x - 7
x = np.linspace(-3, 3, 400)
y = 3*x**2 + 5*x - 7

fig, ax = plt.subplots(figsize=(7, 5), dpi=150)
ax.plot(x, y, color='#1f77b4', linewidth=2.5, label=r'$y = 3x^2 + 5x - 7$')

# 标出一个示例点，比如 x=2
x0 = 2
y0 = 3*x0**2 + 5*x0 - 7
ax.plot(x0, y0, 'o', color='#d62728', markersize=8, zorder=5)
ax.annotate(r'$(2, 15)$', xy=(x0, y0), xytext=(0.5, 18),
            fontsize=11, color='#d62728',
            arrowprops=dict(arrowstyle='->', color='#d62728'))

ax.set_title(r'最终我们研究的确实是这一条整体曲线', fontsize=15)
ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('y', fontsize=11)
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig(output_dir / 'polynomial_overall.png', bbox_inches='tight')
print(f'已保存配图：{output_dir / "polynomial_overall.png"}')
