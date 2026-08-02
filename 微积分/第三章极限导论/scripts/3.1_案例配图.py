#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3.1 极限与定义关系 案例配图

案例1：f(x) = (x²-4)/(x-2)，x ≠ 2 → 化简后 f(x) = x + 2
案例2：分段函数，x ≠ 2 时 f(x) = x + 2，x = 2 时 f(x) = 0
"""

import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Hiragino Sans GB', 'Arial Unicode MS', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# ========== 案例1：f(2)无定义，但极限存在 ==========
fig, ax = plt.subplots(figsize=(10, 6))

x = np.linspace(0, 4, 400)
# f(x) = (x²-4)/(x-2) = x + 2，但 x=2 处挖空
y = (x**2 - 4) / (x - 2)
# 在 x=2 处制造一个洞
mask = np.abs(x - 2) > 0.08
ax.plot(x[mask], y[mask], 'b-', linewidth=2.5)
# x=2 处的空心点
ax.scatter([2], [4], color='white', s=150, zorder=6, edgecolors='red', linewidths=3)
ax.scatter([2], [4], color='red', s=120, zorder=7, facecolors='none', edgecolors='red', linewidths=2)

# 标注
ax.axvline(x=2, color='gray', linestyle=':', alpha=0.6)
ax.axhline(y=4, color='green', linestyle=':', alpha=0.4)
ax.annotate(r'$\lim_{x \to 2} f(x) = 4$', xy=(2.05, 4), xytext=(2.5, 4.5),
            fontsize=13, color='green', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='green', lw=1.5))
ax.annotate(r'$f(2)$ 无定义', xy=(2.1, 2.5), xytext=(2.5, 2.8),
            fontsize=12, color='red',
            arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
ax.text(0.5, 4.8, r'$f(x) = \frac{x^2 - 4}{x - 2} = x + 2 \ (x \neq 2)$', fontsize=11, color='blue')

ax.set_xlim(0, 4)
ax.set_ylim(0, 6)
ax.set_xlabel(r'$x$', fontsize=14)
ax.set_ylabel(r'$f(x)$', fontsize=14)
ax.set_title(r'案例1：$f(2)$ 无定义，但极限存在', fontsize=15, fontweight='bold')
ax.grid(True, alpha=0.3)

# 公式标注放在左上角空白区域
ax.text(0.15, 0.92, r'$f(x) = \frac{x^2 - 4}{x - 2} = x + 2 \ (x \neq 2)$',
        fontsize=11, color='blue', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('../imgs/3.1_案例1_无定义但极限存在.png', dpi=150, bbox_inches='tight')
plt.close()

print("案例1 生成完成：f(2)无定义，但极限存在")

# ========== 案例2：f(2)有定义，但极限值 ≠ 函数值 ==========
fig, ax = plt.subplots(figsize=(10, 6))

# x ≠ 2 时，f(x) = x + 2
x1 = np.linspace(0, 1.97, 100)
y1 = x1 + 2
x2 = np.linspace(2.03, 4, 100)
y2 = x2 + 2

ax.plot(x1, y1, 'b-', linewidth=2.5)
ax.plot(x2, y2, 'b-', linewidth=2.5)

# x = 2 处的函数值 f(2) = 0
ax.scatter([2], [0], color='blue', s=150, zorder=5, edgecolors='blue', linewidths=2)

# x=2 处的空心点（极限值 4）
ax.scatter([2], [4], color='white', s=150, zorder=6, edgecolors='red', linewidths=3)
ax.scatter([2], [4], color='red', s=120, zorder=7, facecolors='none', edgecolors='red', linewidths=2)

# 标注
ax.axvline(x=2, color='gray', linestyle=':', alpha=0.6)
ax.axhline(y=4, color='green', linestyle=':', alpha=0.4)
ax.annotate(r'$\lim_{x \to 2} f(x) = 4$', xy=(2.05, 4), xytext=(2.5, 4.5),
            fontsize=13, color='green', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='green', lw=1.5))
ax.annotate(r'$f(2) = 0$', xy=(2.05, 0), xytext=(2.5, 0.3),
            fontsize=13, color='blue', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))

ax.set_xlim(0, 4)
ax.set_ylim(-1, 6)
ax.set_xlabel(r'$x$', fontsize=14)
ax.set_ylabel(r'$f(x)$', fontsize=14)
ax.set_title(r'案例2：$f(2)$ 有定义，但极限值 $\neq$ 函数值', fontsize=15, fontweight='bold')
ax.grid(True, alpha=0.3)

# 公式标注放在左上角空白区域（使用相对坐标避免重叠）
ax.text(0.15, 0.92, r'$f(x) = x + 2 \ (x \neq 2),\ f(2) = 0$',
        fontsize=11, color='blue', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('../imgs/3.1_案例2_有定义但极限不等.png', dpi=150, bbox_inches='tight')
plt.close()

print("案例2 生成完成：f(2)有定义，但极限值 ≠ 函数值")

print("\n>> 3.1 案例配图生成完成！")
