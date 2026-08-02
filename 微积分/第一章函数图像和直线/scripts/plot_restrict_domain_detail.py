#!/usr/bin/env python3
"""
限制定义域 - 详细配图
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
matplotlib.use('Agg')

# 注册中文字体
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
font_manager.fontManager.addfont(font_path)
prop = font_manager.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()

fig = plt.figure(figsize=(16, 12))

# ============ 标题 ============
fig.suptitle('限制定义域：让函数变成一对一', fontsize=18, fontweight='bold', y=0.98)

# ============ 上排：问题 + 解决方案 ============
# 问题区域
ax_problem = fig.add_axes([0.05, 0.72, 0.42, 0.22])
x_full = np.linspace(-3, 3, 500)
y_full = x_full**2
ax_problem.plot(x_full, y_full, 'b-', linewidth=2)
ax_problem.axhline(y=4, color='red', linestyle='--', linewidth=2)
ax_problem.plot([-2, 2], [4, 4], 'ro', markersize=12)
ax_problem.set_xlim(-3.5, 3.5)
ax_problem.set_ylim(-1, 10)
ax_problem.set_xlabel('x', fontsize=11)
ax_problem.set_ylabel('y', fontsize=11)
ax_problem.set_title('问题：f(x) = x^2 (不是一对一)', fontsize=13, fontweight='bold', color='red')
ax_problem.grid(True, alpha=0.3)
ax_problem.axhline(y=0, color='black', linewidth=0.5)
ax_problem.axvline(x=0, color='black', linewidth=0.5)
ax_problem.text(2.5, 4.3, r'$y=4$', fontsize=10, color='red')
ax_problem.text(-0.5, 3, '2个交点\n=> 不是一对一', fontsize=10, ha='center', color='red')

# 箭头
ax_arrow = fig.add_axes([0.48, 0.78, 0.04, 0.10])
ax_arrow.axis('off')
ax_arrow.annotate('', xy=(0.9, 0.5), xytext=(0.1, 0.5),
                  arrowprops=dict(arrowstyle='->', lw=3, color='darkgreen'),
                  xycoords='axes fraction')
ax_arrow.text(0.5, 0.5, '限制\n定义域', fontsize=9, ha='center', va='center',
              transform=ax_arrow.transAxes, fontweight='bold', color='darkgreen')

# 解决方案区域
ax_solution = fig.add_axes([0.55, 0.72, 0.42, 0.22])
x_right = np.linspace(0, 3, 500)
y_right = x_right**2
ax_solution.plot(x_full, y_full, 'gray', linewidth=1, linestyle='--', alpha=0.4)
ax_solution.plot(x_right, y_right, 'b-', linewidth=2.5)
ax_solution.axhline(y=4, color='red', linestyle='--', linewidth=2)
ax_solution.plot([2], [4], 'ro', markersize=12)
ax_solution.set_xlim(-3.5, 3.5)
ax_solution.set_ylim(-1, 10)
ax_solution.set_xlabel('x', fontsize=11)
ax_solution.set_ylabel('y', fontsize=11)
ax_solution.set_title('解法：限制 x >= 0', fontsize=13, fontweight='bold', color='green')
ax_solution.grid(True, alpha=0.3)
ax_solution.axhline(y=0, color='black', linewidth=0.5)
ax_solution.axvline(x=0, color='black', linewidth=0.5)
ax_solution.axvline(x=0, color='green', linewidth=3, alpha=0.3)
ax_solution.text(2.5, 4.3, r'$y=4$', fontsize=10, color='red')
ax_solution.text(1.5, 3, '1个交点\n=> 一对一', fontsize=10, ha='center', color='green')

# ============ 中排：两种限制方式 ============

# Case 1: x >= 0 (右半边)
ax1 = fig.add_axes([0.05, 0.40, 0.42, 0.28])
x_r = np.linspace(0, 3, 500)
y_r = x_r**2
ax1.plot(x_full, y_full, 'gray', linewidth=1, linestyle='--', alpha=0.4)
ax1.plot(x_r, y_r, 'b-', linewidth=2.5, label=r'$h(x) = x^2, x \geq 0$')
ax1.fill_between(x_r, y_r, alpha=0.2, color='blue')
ax1.axhline(y=4, color='red', linestyle='--', linewidth=2)
ax1.plot([2], [4], 'ro', markersize=12)
ax1.set_xlim(-1, 4)
ax1.set_ylim(-1, 10)
ax1.set_xlabel('x', fontsize=11)
ax1.set_ylabel('y', fontsize=11)
ax1.set_title('情况 1：保留右半边 (x >= 0)', fontsize=14, fontweight='bold', color='blue')
ax1.grid(True, alpha=0.3)
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.axvline(x=0, color='black', linewidth=0.5)
ax1.legend(loc='upper right', fontsize=11)

# 公式框
textstr1 = '\n'.join([
    r'$y = x^2 \Rightarrow x = \sqrt{y}$',
    r'(取正根，因为 $x \geq 0$)',
    r'',
    r'$h^{-1}(x) = \sqrt{x}$',
])
props = dict(boxstyle='round', facecolor='lightblue', alpha=0.8, edgecolor='blue', linewidth=2)
ax1.text(0.02, 0.98, textstr1, transform=ax1.transAxes, fontsize=12,
         verticalalignment='top', bbox=props)

# Case 2: x <= 0 (左半边)
ax2 = fig.add_axes([0.55, 0.40, 0.42, 0.28])
x_l = np.linspace(-3, 0, 500)
y_l = x_l**2
ax2.plot(x_full, y_full, 'gray', linewidth=1, linestyle='--', alpha=0.4)
ax2.plot(x_l, y_l, 'b-', linewidth=2.5, label=r'$j(x) = x^2, x \leq 0$')
ax2.fill_between(x_l, y_l, alpha=0.2, color='orange')
ax2.axhline(y=4, color='red', linestyle='--', linewidth=2)
ax2.plot([-2], [4], 'ro', markersize=12)
ax2.set_xlim(-4, 1)
ax2.set_ylim(-1, 10)
ax2.set_xlabel('x', fontsize=11)
ax2.set_ylabel('y', fontsize=11)
ax2.set_title('情况 2：保留左半边 (x <= 0)', fontsize=14, fontweight='bold', color='darkorange')
ax2.grid(True, alpha=0.3)
ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.axvline(x=0, color='black', linewidth=0.5)
ax2.legend(loc='upper right', fontsize=11)

# 公式框
textstr2 = '\n'.join([
    r'$y = x^2 \Rightarrow x = -\sqrt{y}$',
    r'(取负根，因为 $x \leq 0$)',
    r'',
    r'$j^{-1}(x) = -\sqrt{x}$',
])
props2 = dict(boxstyle='round', facecolor='lightyellow', alpha=0.8, edgecolor='darkorange', linewidth=2)
ax2.text(0.02, 0.98, textstr2, transform=ax2.transAxes, fontsize=12,
         verticalalignment='top', bbox=props2)

# ============ 下排：关键原则 + 镜像对称 ============

# 关键原则
ax_key = fig.add_axes([0.05, 0.08, 0.42, 0.28])
ax_key.axis('off')
ax_key.set_xlim(0, 10)
ax_key.set_ylim(0, 10)
ax_key.set_title('关键原则', fontsize=14, fontweight='bold', color='purple')

# 表格形式展示
table_data = [
    ['原函数定义域', '反函数根'],
    ['x >= 0（右半边）', '+ sqrt(x)'],
    ['x <= 0（左半边）', '- sqrt(x)'],
]
table = ax_key.table(cellText=table_data,
                     loc='center',
                     cellLoc='center',
                     colWidths=[0.4, 0.4])
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.2, 2)

# 设置表头样式
for j in range(2):
    table[(0, j)].set_facecolor('#4472C4')
    table[(0, j)].set_text_props(color='white', fontweight='bold')
table[(1, 0)].set_facecolor('#D6DCE4')
table[(1, 1)].set_facecolor('#D6DCE4')
table[(2, 0)].set_facecolor('#EDD4B3')
table[(2, 1)].set_facecolor('#EDD4B3')

ax_key.text(0.5, 0.15,
            r'$\text{Inverse domain} = \text{Original range}$',
            fontsize=13, ha='center', transform=ax_key.transAxes,
            bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.8))

# 镜像对称解释
ax_mirror = fig.add_axes([0.55, 0.08, 0.42, 0.28])
x_sym = np.linspace(0, 3, 300)
y_sym = x_sym**2
y_inv_sym = np.linspace(0, 3, 300)
x_inv_sym = y_inv_sym**0.5

ax_mirror.plot(x_sym, y_sym, 'b-', linewidth=2, label=r'$h(x) = x^2, x \geq 0$')
ax_mirror.plot(y_inv_sym, x_inv_sym, 'r--', linewidth=2, label=r'$h^{-1}(x) = \sqrt{x}$')
ax_mirror.plot(x_sym, x_sym, 'g:', linewidth=1.5, label=r'$y = x$ (对称轴)')
ax_mirror.set_xlim(-0.5, 3.5)
ax_mirror.set_ylim(-0.5, 3.5)
ax_mirror.set_xlabel('x', fontsize=11)
ax_mirror.set_ylabel('y', fontsize=11)
ax_mirror.set_title('镜像对称（关于 y = x）', fontsize=14, fontweight='bold', color='darkgreen')
ax_mirror.grid(True, alpha=0.3)
ax_mirror.axhline(y=0, color='black', linewidth=0.5)
ax_mirror.axvline(x=0, color='black', linewidth=0.5)
ax_mirror.legend(loc='upper right', fontsize=10)
ax_mirror.set_aspect('equal')

# 标注
ax_mirror.annotate('(4, 2)', xy=(4, 2), xytext=(4.1, 2.2), fontsize=10)
ax_mirror.annotate('(2, 4)', xy=(2, 4), xytext=(1.4, 4.3), fontsize=10)

plt.savefig('/Users/liutao/Documents/Obsidian/微积分/第一章函数图像和直线/imgs/restrict_domain_detail.png',
            dpi=150, bbox_inches='tight')
print("Saved: imgs/restrict_domain_detail.png")
plt.close()
