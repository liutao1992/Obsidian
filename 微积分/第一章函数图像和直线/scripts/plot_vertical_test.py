#!/usr/bin/env python3
"""
绘制垂线检验图
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
matplotlib.use('Agg')

font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
font_prop = font_manager.FontProperties(fname=font_path)

plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# ============ 左图：抛物线 - 通过 ============
ax1 = axes[0]
x = np.linspace(-2, 2, 400)
y = x**2

ax1.plot(x, y, 'b-', linewidth=2.5, label=r'$f(x) = x^2$')
ax1.axvline(x=1, color='red', linestyle='--', linewidth=2.5, label=r'$x = 1$')
ax1.plot([1], [1], 'ro', markersize=12)

ax1.annotate('1个交点\n通过', xy=(1.5, 3), fontsize=14,
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8), fontproperties=font_prop)

ax1.set_xlim(-3, 3)
ax1.set_ylim(-1, 6)
ax1.set_xlabel('x', fontsize=13)
ax1.set_ylabel('y', fontsize=13)
ax1.set_title('抛物线: 通过', fontsize=15, fontweight='bold', color='green', fontproperties=font_prop)
ax1.legend(loc='upper right', fontsize=11)
ax1.grid(True, alpha=0.3)

# ============ 右图：圆 - 不通过 ============
ax2 = axes[1]
theta = np.linspace(0, 2*np.pi, 400)
r = 2
x_circle = r * np.cos(theta)
y_circle = r * np.sin(theta)

ax2.plot(x_circle, y_circle, 'b-', linewidth=2.5, label=r'$x^2 + y^2 = 4$')
ax2.axvline(x=1, color='red', linestyle='--', linewidth=2.5, label=r'$x = 1$')
ax2.plot([1, 1], [np.sqrt(3), -np.sqrt(3)], 'ro', markersize=12)

ax2.annotate('2个交点\n不通过', xy=(1.5, 2.5), fontsize=14,
            bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.8), fontproperties=font_prop)

ax2.set_xlim(-3, 3)
ax2.set_ylim(-3, 3)
ax2.set_xlabel('x', fontsize=13)
ax2.set_ylabel('y', fontsize=13)
ax2.set_title('圆: 不通过', fontsize=15, fontweight='bold', color='red', fontproperties=font_prop)
ax2.legend(loc='lower right', fontsize=11)
ax2.grid(True, alpha=0.3)
ax2.set_aspect('equal')

fig.suptitle('垂线检验法', fontsize=17, fontweight='bold', y=1.02, fontproperties=font_prop)

plt.tight_layout()
plt.savefig('/Users/liutao/Documents/Obsidian/微积分/imgs/vertical_line_test.png', dpi=150, bbox_inches='tight')
print("Saved: imgs/vertical_line_test.png")
plt.close()
