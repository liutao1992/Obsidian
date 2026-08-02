#!/usr/bin/env python3
"""
绘制用图像求值域图
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

# ============ 左图：y = x^2, x in [-2, 1] ============
ax1 = axes[0]
x = np.linspace(-2, 1, 400)
y = x**2

ax1.plot(x, y, 'b-', linewidth=2.5, label=r'$f(x) = x^2$')
ax1.fill_between(x, y, alpha=0.3, color='blue')

# 标注 y 轴范围
ax1.annotate('', xy=(-2.5, 0), xytext=(-2.5, 4),
            arrowprops=dict(arrowstyle='<->', color='red', lw=2))
ax1.text(-2.9, 2, '值域\n[0, 4]', fontsize=12, color='red', ha='center', va='center', fontproperties=font_prop)

# 标注 x 轴范围
ax1.annotate('', xy=(-2, -0.5), xytext=(1, -0.5),
            arrowprops=dict(arrowstyle='<->', color='green', lw=2))
ax1.text(-0.5, -1, '定义域 [-2, 1]', fontsize=11, color='green', ha='center', fontproperties=font_prop)

# 标注最值点
ax1.plot([0], [0], 'ro', markersize=10)
ax1.plot([-2], [4], 'ro', markersize=10)
ax1.annotate('(0, 0)\n最小值', xy=(0, 0), xytext=(0.5, 0.5), fontsize=10, fontproperties=font_prop)
ax1.annotate('(-2, 4)\n最大值', xy=(-2, 4), xytext=(-2.8, 4.3), fontsize=10, fontproperties=font_prop)

ax1.set_xlim(-3, 2)
ax1.set_ylim(-1, 6)
ax1.set_xlabel('x', fontsize=13)
ax1.set_ylabel('y', fontsize=13)
ax1.set_title(r'$y = x^2, x \in [-2, 1]$', fontsize=15, fontweight='bold')
ax1.grid(True, alpha=0.3)

# ============ 右图：y = 2x, x in (2, 4) ============
ax2 = axes[1]
x = np.linspace(2, 4, 400)
y = 2*x

ax2.plot(x, y, 'b-', linewidth=2.5, label=r'$f(x) = 2x$')
ax2.fill_between(x, y, alpha=0.3, color='blue')

# 标注 y 轴范围（开区间）
ax2.annotate('', xy=(4.5, 4), xytext=(4.5, 8),
            arrowprops=dict(arrowstyle='<->', color='red', lw=2))
ax2.text(5, 6, '值域\n(4, 8)', fontsize=12, color='red', ha='center', va='center', fontproperties=font_prop)

# 标注 x 轴范围
ax2.annotate('', xy=(2, -0.5), xytext=(4, -0.5),
            arrowprops=dict(arrowstyle='<->', color='green', lw=2))
ax2.text(3, -1, '定义域 (2, 4)', fontsize=11, color='green', ha='center', fontproperties=font_prop)

# 虚线表示开区间
ax2.plot([2, 2], [4, 8], 'r:', linewidth=1.5)
ax2.plot([4, 4], [4, 8], 'r:', linewidth=1.5)
ax2.plot([2], [4], 'ro', markersize=8, fillstyle='none')
ax2.plot([4], [8], 'ro', markersize=8, fillstyle='none')

ax2.set_xlim(1, 5.5)
ax2.set_ylim(-1, 10)
ax2.set_xlabel('x', fontsize=13)
ax2.set_ylabel('y', fontsize=13)
ax2.set_title(r'$y = 2x, x \in (2, 4)$', fontsize=15, fontweight='bold')
ax2.grid(True, alpha=0.3)

fig.suptitle('用图像求值域', fontsize=17, fontweight='bold', fontproperties=font_prop)

plt.tight_layout()
plt.savefig('/Users/liutao/Documents/Obsidian/微积分/imgs/find_range.png', dpi=150, bbox_inches='tight')
print("Saved: imgs/find_range.png")
plt.close()
