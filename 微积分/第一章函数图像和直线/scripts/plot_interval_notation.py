#!/usr/bin/env python3
"""
绘制区间表示图
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
matplotlib.use('Agg')

font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
font_prop = font_manager.FontProperties(fname=font_path)

plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(12, 6))

# 画数轴
ax.set_xlim(-6, 6)
ax.set_ylim(-0.5, 3)
ax.axhline(y=0, color='black', linewidth=1.5)

# 标注点
for x, label in [(-3, 'a'), (3, 'b'), (0, '0')]:
    ax.plot([x], [0], 'ko', markersize=10)
    ax.text(x, -0.4, f'{label}', ha='center', fontsize=14)

# 闭区间 [a, b]
ax.plot([-3, 3], [1.0, 1.0], 'b-', linewidth=4)
ax.plot([-3], [1.0], '|', color='blue', markersize=20, markeredgewidth=4)
ax.plot([3], [1.0], '|', color='blue', markersize=20, markeredgewidth=4)
ax.text(0, 1.5, r'$[a, b]$', ha='center', fontsize=16, fontproperties=font_prop)
ax.text(0, 1.15, '闭区间: 端点都能取到', ha='center', fontsize=12, fontproperties=font_prop, color='blue')

# 开区间 (a, b)
ax.plot([-3, 3], [2.2, 2.2], 'r-', linewidth=4)
ax.plot([-3], [2.2], 'o', color='white', markersize=12, markeredgecolor='red', markeredgewidth=3)
ax.plot([3], [2.2], 'o', color='white', markersize=12, markeredgecolor='red', markeredgewidth=3)
ax.text(0, 2.7, r'$(a, b)$', ha='center', fontsize=16, fontproperties=font_prop)
ax.text(0, 2.35, '开区间: 端点不能取到', ha='center', fontsize=12, fontproperties=font_prop, color='red')

ax.set_xticks([])
ax.set_yticks([])
ax.set_title('区间表示', fontsize=18, fontweight='bold', y=0.98, fontproperties=font_prop)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.tight_layout()
plt.savefig('/Users/liutao/Documents/Obsidian/微积分/imgs/interval_notation.png', dpi=150, bbox_inches='tight')
print("Saved: imgs/interval_notation.png")
plt.close()
