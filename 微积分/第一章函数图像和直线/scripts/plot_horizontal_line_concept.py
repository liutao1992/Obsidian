#!/usr/bin/env python3
"""
水平线检验教学图
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
matplotlib.use('Agg')

font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
font_prop = font_manager.FontProperties(fname=font_path)

plt.rcParams['axes.unicode_minus'] = False

fig = plt.figure(figsize=(16, 12))

# ============ 上方：概念示意图 ============
ax_top = fig.add_axes([0.05, 0.55, 0.9, 0.38])
ax_top.set_xlim(0, 10)
ax_top.set_ylim(0, 6)
ax_top.axis('off')
ax_top.set_title('水平线检验 (Horizontal Line Test)', fontsize=18, fontweight='bold', pad=15, fontproperties=font_prop)

# 左侧示意图 - 固定 y
ax_left = fig.add_axes([0.08, 0.57, 0.25, 0.30])
x = np.linspace(-2.5, 2.5, 400)
y = x**2
ax_left.plot(x, y, 'b-', linewidth=2)
ax_left.axhline(y=4, color='red', linestyle='--', linewidth=2)
ax_left.plot([-2, 2], [4, 4], 'ro', markersize=10)
ax_left.set_xlim(-3, 3)
ax_left.set_ylim(-1, 10)
ax_left.set_xlabel('x', fontsize=12)
ax_left.set_ylabel('y', fontsize=12)
ax_left.set_title('步骤1: 固定 y 值', fontsize=14, fontweight='bold', fontproperties=font_prop)
ax_left.grid(True, alpha=0.3)
ax_left.axhline(y=0, color='black', linewidth=0.5)
ax_left.axvline(x=0, color='black', linewidth=0.5)
ax_left.text(2.5, 4.2, r'$y = c$', fontsize=11, color='red')

# 中间箭头
ax_mid = fig.add_axes([0.36, 0.62, 0.08, 0.20])
ax_mid.axis('off')
ax_mid.annotate('', xy=(0.9, 0.5), xytext=(0.1, 0.5),
                arrowprops=dict(arrowstyle='->', lw=3, color='darkblue'),
                xycoords='axes fraction')
ax_mid.text(0.5, 0.8, '步骤1\n步骤2\n步骤3', fontsize=10, ha='center',
            va='top', transform=ax_mid.transAxes, fontproperties=font_prop)

# 中间示意图 - 画水平线
ax_center = fig.add_axes([0.47, 0.57, 0.25, 0.30])
ax_center.plot(x, y, 'b-', linewidth=2)
ax_center.axhline(y=4, color='red', linestyle='--', linewidth=2)
ax_center.plot([-2, 2], [4, 4], 'ro', markersize=10)
ax_center.set_xlim(-3, 3)
ax_center.set_ylim(-1, 10)
ax_center.set_xlabel('x', fontsize=12)
ax_center.set_ylabel('y', fontsize=12)
ax_center.set_title('步骤2: 画水平线', fontsize=14, fontweight='bold', fontproperties=font_prop)
ax_center.grid(True, alpha=0.3)
ax_center.axhline(y=0, color='black', linewidth=0.5)
ax_center.axvline(x=0, color='black', linewidth=0.5)

# 右侧箭头
ax_right = fig.add_axes([0.75, 0.62, 0.08, 0.20])
ax_right.axis('off')
ax_right.annotate('', xy=(0.9, 0.5), xytext=(0.1, 0.5),
                  arrowprops=dict(arrowstyle='->', lw=3, color='darkblue'),
                  xycoords='axes fraction')

# 右侧文字
ax_equation = fig.add_axes([0.82, 0.57, 0.15, 0.30])
ax_equation.axis('off')
ax_equation.text(0.5, 0.7, '步骤3:', fontsize=12, ha='center', fontweight='bold',
                 transform=ax_equation.transAxes, fontproperties=font_prop)
ax_equation.text(0.5, 0.45, r'$f(x) = y$', fontsize=16, ha='center',
                 fontweight='bold', transform=ax_equation.transAxes)
ax_equation.text(0.5, 0.15, '有几个解?', fontsize=11, ha='center',
                 transform=ax_equation.transAxes, fontproperties=font_prop)

# ============ 下方：三情况对比 ============

# Case 1: 一点 - 通过
ax1 = fig.add_axes([0.05, 0.08, 0.27, 0.38])
x1 = np.linspace(-2, 2, 400)
y1 = x1**3
ax1.plot(x1, y1, 'b-', linewidth=2)
ax1.axhline(y=1, color='red', linestyle='--', linewidth=2)
ax1.plot([1], [1], 'ro', markersize=10)
ax1.set_xlim(-2.5, 2.5)
ax1.set_ylim(-6, 6)
ax1.set_xlabel('x', fontsize=11)
ax1.set_ylabel('y', fontsize=11)
ax1.set_title('情况1: 一点 (通过)', fontsize=13, fontweight='bold', color='green', fontproperties=font_prop)
ax1.grid(True, alpha=0.3)
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.axvline(x=0, color='black', linewidth=0.5)
# Result box
ax1.text(0.5, -0.08, r'$\checkmark$ 是: 一一对应', fontsize=11, ha='center',
         transform=ax1.transAxes, color='green', fontweight='bold',
         bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7), fontproperties=font_prop)

# Case 2: 两点 - 不通过
ax2 = fig.add_axes([0.38, 0.08, 0.27, 0.38])
x2 = np.linspace(-2.5, 2.5, 400)
y2 = x2**2
ax2.plot(x2, y2, 'b-', linewidth=2)
ax2.axhline(y=4, color='red', linestyle='--', linewidth=2)
ax2.plot([-2, 2], [4, 4], 'ro', markersize=10)
ax2.set_xlim(-3, 3)
ax2.set_ylim(-1, 10)
ax2.set_xlabel('x', fontsize=11)
ax2.set_ylabel('y', fontsize=11)
ax2.set_title('情况2: 两点 (不通过)', fontsize=13, fontweight='bold', color='red', fontproperties=font_prop)
ax2.grid(True, alpha=0.3)
ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.axvline(x=0, color='black', linewidth=0.5)
# Result box
ax2.text(0.5, -0.08, r'$\times$ 否: 非一一对应', fontsize=11, ha='center',
         transform=ax2.transAxes, color='red', fontweight='bold',
         bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7), fontproperties=font_prop)

# Case 3: 零 - 通过 (但 y 不在值域)
ax3 = fig.add_axes([0.71, 0.08, 0.27, 0.38])
x3 = np.linspace(-2, 2, 400)
y3 = x3**3
ax3.plot(x3, y3, 'b-', linewidth=2)
ax3.axhline(y=-5, color='orange', linestyle='--', linewidth=2)
ax3.set_xlim(-2.5, 2.5)
ax3.set_ylim(-6, 6)
ax3.set_xlabel('x', fontsize=11)
ax3.set_ylabel('y', fontsize=11)
ax3.set_title('情况3: 零 (通过)', fontsize=13, fontweight='bold', color='blue', fontproperties=font_prop)
ax3.grid(True, alpha=0.3)
ax3.axhline(y=0, color='black', linewidth=0.5)
ax3.axvline(x=0, color='black', linewidth=0.5)
# Result box - 移到底部避免遮挡
ax3.text(0.5, -0.15, r'$\checkmark$ 是: 一一对应', fontsize=11, ha='center',
         transform=ax3.transAxes, color='blue', fontweight='bold',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7), fontproperties=font_prop)
ax3.text(0.5, -0.25, '(y 不在值域)', fontsize=9, ha='center',
         transform=ax3.transAxes, color='gray', fontproperties=font_prop)

# ============ 底部总结 ============
fig.text(0.5, 0.02,
         '总结: 水平线检验判断函数是否为一对一函数',
         ha='center', fontsize=14, style='italic', color='darkblue', fontproperties=font_prop)

plt.savefig('/Users/liutao/Documents/Obsidian/微积分/imgs/horizontal_line_concept.png',
            dpi=150, bbox_inches='tight')
print("Saved: imgs/horizontal_line_concept.png")
plt.close()
