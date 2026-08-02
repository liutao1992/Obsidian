#!/usr/bin/env python3
"""
绘制两点式详解图
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
matplotlib.use('Agg')

# 注册中文字体
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
font_prop = font_manager.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(12, 10))

# 两点式直线
x = np.linspace(-1, 6, 400)
# 过点 (1, 2) 和 (4, 5)，斜率 m = (5-2)/(4-1) = 1
y = x + 1

ax.plot(x, y, 'b-', linewidth=2.5, label=r'$y = x + 1$')

# 两点
P1 = (1, 2)
P2 = (4, 5)
ax.plot([P1[0]], [P1[1]], 'ro', markersize=14, label=f'P1{P1}')
ax.plot([P2[0]], [P2[1]], 'go', markersize=14, label=f'P2{P2}')

# 标注两点
ax.annotate(r'$P_1(x_1, y_1) = (1, 2)$', xy=P1, xytext=(0.3, 2.3), fontsize=13,
            arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
ax.annotate(r'$P_2(x_2, y_2) = (4, 5)$', xy=P2, xytext=(4.2, 5.5), fontsize=13,
            arrowprops=dict(arrowstyle='->', color='green', lw=1.5))

# 画 delta 线
ax.plot([P1[0], P2[0]], [P1[1], P1[1]], 'r--', linewidth=1.5)
ax.plot([P2[0], P2[0]], [P1[1], P2[1]], 'r--', linewidth=1.5)

# delta 标注
ax.annotate(r'$\Delta x = x_2 - x_1 = 3$', xy=(2.5, 1.5), fontsize=12,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
ax.annotate(r'$\Delta y = y_2 - y_1 = 3$', xy=(5, 3.5), fontsize=12,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

# 公式框 - 使用普通文本替代 LaTeX 的 \text{}
textstr = '\n'.join([
    '两点式方程：',
    r'$\frac{y - y_1}{y_2 - y_1} = \frac{x - x_1}{x_2 - x_1}$',
    '',
    '代入 P1(1,2), P2(4,5):',
    r'$\frac{y - 2}{5 - 2} = \frac{x - 1}{4 - 1}$',
    '',
    r'$\Rightarrow \frac{y - 2}{3} = \frac{x - 1}{3}$',
    '',
    r'$\Rightarrow y = x + 1$',
])
props = dict(boxstyle='round', facecolor='lightcyan', alpha=0.9, edgecolor='blue', linewidth=2)
ax.text(0.02, 0.98, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=props, fontproperties=font_prop)

# 斜率说明
ax.text(0.5, -0.12,
        r'斜率 $m = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}$',
        transform=ax.transAxes, fontsize=14, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8),
        fontproperties=font_prop)

ax.axhline(y=0, color='black', linewidth=0.5)
ax.axvline(x=0, color='black', linewidth=0.5)
ax.set_xlim(-0.5, 6.5)
ax.set_ylim(-1, 8)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_title('两点式方程', fontsize=18, fontweight='bold', fontproperties=font_prop)
ax.legend(loc='lower right', fontsize=12)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/Users/liutao/Documents/Obsidian/微积分/imgs/two_point_form.png',
            dpi=150, bbox_inches='tight')
print("Saved: imgs/two_point_form.png")
plt.close()
