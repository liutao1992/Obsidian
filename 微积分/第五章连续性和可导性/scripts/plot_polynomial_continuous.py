import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 输出目录
output_dir = Path(__file__).resolve().parent.parent / 'imgs'
output_dir.mkdir(parents=True, exist_ok=True)

x = np.linspace(-3, 3, 400)

# 图1：x² 的图像（连续抛物线）
fig, ax = plt.subplots(figsize=(6, 4.5), dpi=150)
ax.plot(x, x**2, color='#1f77b4', linewidth=2.5, label=r'$y = x^2$')
ax.set_title(r'$y = x^2$ 是一条连续曲线', fontsize=14)
ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('y', fontsize=11)
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper center')
plt.tight_layout()
plt.savefig(output_dir / 'x2_curve.png', bbox_inches='tight')
plt.close()

# 图2：x² 与 3x² 叠加，展示纵向拉伸
fig, ax = plt.subplots(figsize=(6, 4.5), dpi=150)
ax.plot(x, x**2, color='#1f77b4', linewidth=2, label=r'$y = x^2$', linestyle='--')
ax.plot(x, 3*x**2, color='#ff7f0e', linewidth=2.5, label=r'$y = 3x^2$')
ax.set_title(r'$y=3x^2$ 是 $y=x^2$ 纵向拉高 3 倍', fontsize=14)
ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('y', fontsize=11)
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper center')
plt.tight_layout()
plt.savefig(output_dir / 'x2_stretch.png', bbox_inches='tight')
plt.close()

# 图3：y=x 与 y=5x 比较
fig, ax = plt.subplots(figsize=(6, 4.5), dpi=150)
ax.plot(x, x, color='#2ca02c', linewidth=2, label=r'$y = x$')
ax.plot(x, 5*x, color='#d62728', linewidth=2.5, label=r'$y = 5x$')
ax.set_title(r'$y=5x$ 是 $y=x$ 斜率变大 5 倍', fontsize=14)
ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('y', fontsize=11)
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig(output_dir / 'linear_compare.png', bbox_inches='tight')
plt.close()

# 图4：y = -7 水平线
fig, ax = plt.subplots(figsize=(6, 4.5), dpi=150)
ax.plot(x, np.full_like(x, -7), color='#9467bd', linewidth=2.5, label=r'$y = -7$')
ax.set_title(r'$y = -7$ 是一条水平线', fontsize=14)
ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('y', fontsize=11)
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper right')
plt.tight_layout()
plt.savefig(output_dir / 'constant_line.png', bbox_inches='tight')
plt.close()

# 图5：多项式叠加：3x² + 5x - 7
fig, ax = plt.subplots(figsize=(8, 5), dpi=150)
ax.plot(x, 3*x**2, color='#1f77b4', linewidth=1.8, linestyle='--', alpha=0.7, label=r'$y=3x^2$')
ax.plot(x, 5*x, color='#2ca02c', linewidth=1.8, linestyle='--', alpha=0.7, label=r'$y=5x$')
ax.plot(x, np.full_like(x, -7), color='#d62728', linewidth=1.8, linestyle='--', alpha=0.7, label=r'$y=-7$')
ax.plot(x, 3*x**2 + 5*x - 7, color='#ff7f0e', linewidth=2.8, label=r'$y=3x^2+5x-7$')
ax.set_title(r'三个连续函数相加，结果仍然连续', fontsize=14)
ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('y', fontsize=11)
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper center', ncol=2)
plt.tight_layout()
plt.savefig(output_dir / 'polynomial_superposition.png', bbox_inches='tight')
plt.close()

print(f'已保存 5 张配图到：{output_dir}')
