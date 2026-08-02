import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 数据
x = np.linspace(-3, 3, 400)
y1 = x ** 2
y2 = 3 * x ** 2

# 创建图像：左右两个子图
fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), dpi=150)

# 左图：x^2
axes[0].plot(x, y1, color='#1f77b4', linewidth=2, label=r'$y = x^2$')
axes[0].set_title(r'$y = x^2$ 的图像', fontsize=13)
axes[0].set_xlabel('x', fontsize=11)
axes[0].set_ylabel('y', fontsize=11)
axes[0].set_xlim(-3, 3)
axes[0].set_ylim(0, 27)
axes[0].axhline(0, color='gray', linewidth=0.5)
axes[0].axvline(0, color='gray', linewidth=0.5)
axes[0].grid(True, linestyle='--', alpha=0.5)
axes[0].legend(loc='upper center')

# 右图：3x^2
axes[1].plot(x, y2, color='#ff7f0e', linewidth=2, label=r'$y = 3x^2$')
axes[1].set_title(r'$y = 3x^2$ 的图像', fontsize=13)
axes[1].set_xlabel('x', fontsize=11)
axes[1].set_ylabel('y', fontsize=11)
axes[1].set_xlim(-3, 3)
axes[1].set_ylim(0, 27)
axes[1].axhline(0, color='gray', linewidth=0.5)
axes[1].axvline(0, color='gray', linewidth=0.5)
axes[1].grid(True, linestyle='--', alpha=0.5)
axes[1].legend(loc='upper center')

plt.tight_layout()

# 保存到 imgs 目录
output_path = Path(__file__).resolve().parent.parent / 'imgs' / 'x2_vs_3x2.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, bbox_inches='tight')
print(f'已保存配图：{output_path}')
