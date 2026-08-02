#!/usr/bin/env python3
"""
绘制上域与值域图
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
matplotlib.use('Agg')

font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
font_prop = font_manager.FontProperties(fname=font_path)

plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(12, 8))

x = np.linspace(-3, 3, 400)
y = x**2

ax.plot(x, y, 'b-', linewidth=2.5, label=r'$f(x) = x^2$')
ax.axhline(y=0, color='black', linewidth=0.5)
ax.axvline(x=0, color='black', linewidth=0.5)

# 填充值域区域（y >= 0的部分）
ax.fill_between(x, y, alpha=0.2, color='orange')

# ============ 上域箭头（绿色）============
# 上域 = ℝ，整个y轴
ax.annotate('', xy=(3.5, 8), xytext=(3.5, -4),
            arrowprops=dict(arrowstyle='<->', color='green', lw=2.5, shrinkA=0, shrinkB=0))
# 上域标签
ax.text(3.8, 2, '上域\nCodomain\n(可能输出)', fontsize=12, color='green', va='center', fontproperties=font_prop)
# 上域说明
ax.text(3.8, -5, r'$\mathbb{R}$ (全体实数)', fontsize=11, color='green', ha='center', fontproperties=font_prop)

# ============ 值域箭头（橙色）============
# 值域 = [0, +∞)，从0开始向上
ax.annotate('', xy=(4.8, 8), xytext=(4.8, 0),
            arrowprops=dict(arrowstyle='->', color='orange', lw=2.5, shrinkA=0, shrinkB=0))
# 值域起点标记
ax.plot(4.8, 0, 'o', color='orange', markersize=8)
ax.text(4.8, 0, '0', fontsize=10, color='orange', ha='left', va='top', fontproperties=font_prop)
# 值域标签
ax.text(5.3, 4, '值域\nRange\n(实际输出)', fontsize=12, color='orange', va='center', fontproperties=font_prop)
# 值域说明
ax.text(5.3, 9, r'$[0, +\infty)$', fontsize=11, color='orange', ha='center', fontproperties=font_prop)

# 标注
ax.text(0, 10.5, r'$f(x) = x^2,$ 定义域 $= \mathbb{R}$', fontsize=14, ha='center', fontproperties=font_prop)

ax.set_xlim(-4, 6.5)
ax.set_ylim(-2, 12)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_title('上域 vs 值域', fontsize=18, fontweight='bold', fontproperties=font_prop)
ax.legend(loc='upper left', fontsize=12)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/Users/liutao/Documents/Obsidian/微积分/imgs/domain_range.png', dpi=150, bbox_inches='tight')
print("Saved: imgs/domain_range.png")
plt.close()
