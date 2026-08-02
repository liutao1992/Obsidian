#!/usr/bin/env python3
"""
绘制函数基础概念配图
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
plt.rcParams['axes.unicode_minus'] = False

fig = plt.figure(figsize=(16, 12))

# ============ 标题 ============
fig.suptitle('函数基础概念', fontsize=20, fontweight='bold', y=0.98)

# ============ 图1：区间表示 ============
ax1 = fig.add_axes([0.05, 0.68, 0.42, 0.26])

# 画数轴
ax1.set_xlim(-6, 6)
ax1.set_ylim(-0.5, 2)
ax1.axhline(y=0, color='black', linewidth=1)
ax1.axvline(x=0, color='black', linewidth=0.5)

# 标注点
for x, label in [(-3, 'a'), (3, 'b'), (0, '0')]:
    ax1.plot([x], [0], 'ko', markersize=8)
    ax1.text(x, -0.3, f'{label}', ha='center', fontsize=11)

# 闭区间 [a, b]
ax1.plot([-3, 3], [0.8, 0.8], 'b-', linewidth=3)
ax1.plot([-3], [0.8], '|', color='blue', markersize=15, markeredgewidth=3)
ax1.plot([3], [0.8], '|', color='blue', markersize=15, markeredgewidth=3)
ax1.text(0, 1.1, r'$[a, b]$  闭区间：$a \leq x \leq b$', ha='center', fontsize=12)

# 开区间 (a, b) - 向下偏移
ax1.plot([-3, 3], [1.5, 1.5], 'r-', linewidth=3)
ax1.plot([-3], [1.5], 'o', color='white', markersize=8, markeredgecolor='red', markeredgewidth=2)
ax1.plot([3], [1.5], 'o', color='white', markersize=8, markeredgecolor='red', markeredgewidth=2)
ax1.text(0, 1.8, r'$(a, b)$  开区间：$a < x < b$', ha='center', fontsize=12)

ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_title('区间表示', fontsize=14, fontweight='bold')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)

# ============ 图2：上域与值域 ============
ax2 = fig.add_axes([0.55, 0.68, 0.42, 0.26])
x = np.linspace(-3, 3, 400)
y = x**2

ax2.plot(x, y, 'b-', linewidth=2)
ax2.axhline(y=4, color='red', linestyle='--', linewidth=1.5, alpha=0.7)
ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.axvline(x=0, color='black', linewidth=0.5)

# 标注上域和值域
ax2.annotate('', xy=(3.5, 1.5), xytext=(3.5, 9),
            arrowprops=dict(arrowstyle='<->', color='green', lw=2))
ax2.text(3.8, 5, '上域\n(可能输出)', fontsize=10, color='green')

ax2.annotate('', xy=(4.5, 0), xytext=(4.5, 9),
            arrowprops=dict(arrowstyle='<->', color='orange', lw=2))
ax2.text(4.8, 5, '值域\n(实际输出)', fontsize=10, color='orange')

ax2.set_xlim(-4, 6)
ax2.set_ylim(-1, 10)
ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('y', fontsize=12)
ax2.set_title('上域 vs 值域', fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3)

# ============ 图3：垂线检验 ============
ax3 = fig.add_axes([0.05, 0.38, 0.42, 0.26])

# 子图3a：抛物线 - 通过垂线检验
ax3a = fig.add_axes([0.08, 0.40, 0.17, 0.22])
x = np.linspace(-2, 2, 400)
y = x**2
ax3a.plot(x, y, 'b-', linewidth=2)
ax3a.axvline(x=1, color='red', linestyle='--', linewidth=2)
ax3a.plot([1], [1], 'ro', markersize=10)
ax3a.set_xlim(-2.5, 2.5)
ax3a.set_ylim(-1, 5)
ax3a.set_xlabel('x', fontsize=9)
ax3a.set_ylabel('y', fontsize=9)
ax3a.set_title('抛物线: 通过', fontsize=11, fontweight='bold', color='green')
ax3a.grid(True, alpha=0.3)

# 子图3b：圆 - 不通过垂线检验
ax3b = fig.add_axes([0.30, 0.40, 0.17, 0.22])
theta = np.linspace(0, 2*np.pi, 400)
r = 2
x_circle = r * np.cos(theta)
y_circle = r * np.sin(theta)
ax3b.plot(x_circle, y_circle, 'b-', linewidth=2)
ax3b.axvline(x=1, color='red', linestyle='--', linewidth=2)
ax3b.plot([1, 1], [np.sqrt(3), -np.sqrt(3)], 'ro', markersize=8)
ax3b.set_xlim(-3, 3)
ax3b.set_ylim(-3, 3)
ax3b.set_xlabel('x', fontsize=9)
ax3b.set_ylabel('y', fontsize=9)
ax3b.set_title('圆: 不通过', fontsize=11, fontweight='bold', color='red')
ax3b.grid(True, alpha=0.3)
ax3b.set_aspect('equal')

# 说明文字
ax3.text(0.5, 0.02,
        r'$\text{垂线检验：固定 } x \text{，画垂线，与图像只能有1个交点}$',
        ha='center', fontsize=12, transform=ax3.transAxes,
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

ax3.axis('off')
ax3.set_title('垂线检验法', fontsize=14, fontweight='bold')

# ============ 图4：水平线检验 ============
ax4 = fig.add_axes([0.55, 0.38, 0.42, 0.26])

# 子图4a：x^3 - 通过水平线检验
ax4a = fig.add_axes([0.58, 0.40, 0.17, 0.22])
x = np.linspace(-2, 2, 400)
y = x**3
ax4a.plot(x, y, 'b-', linewidth=2)
ax4a.axhline(y=4, color='red', linestyle='--', linewidth=2)
ax4a.plot([np.cbrt(4)], [4], 'ro', markersize=10)
ax4a.set_xlim(-2.5, 2.5)
ax4a.set_ylim(-6, 6)
ax4a.set_xlabel('x', fontsize=9)
ax4a.set_ylabel('y', fontsize=9)
ax4a.set_title(r'$x^3$: 有反函数', fontsize=11, fontweight='bold', color='green')
ax4a.grid(True, alpha=0.3)

# 子图4b：x^2 - 不通过水平线检验
ax4b = fig.add_axes([0.80, 0.40, 0.17, 0.22])
x = np.linspace(-2, 2, 400)
y = x**2
ax4b.plot(x, y, 'b-', linewidth=2)
ax4b.axhline(y=4, color='red', linestyle='--', linewidth=2)
ax4b.plot([-2, 2], [4, 4], 'ro', markersize=10)
ax4b.set_xlim(-2.5, 2.5)
ax4b.set_ylim(-1, 6)
ax4b.set_xlabel('x', fontsize=9)
ax4b.set_ylabel('y', fontsize=9)
ax4b.set_title(r'$x^2$: 无反函数', fontsize=11, fontweight='bold', color='red')
ax4b.grid(True, alpha=0.3)

# 说明文字
ax4.text(0.5, 0.02,
        r'$\text{水平线检验：固定 } y \text{，画水平线，交点个数决定是否有反函数}$',
        ha='center', fontsize=12, transform=ax4.transAxes,
        bbox=dict(boxstyle='round', facecolor='lightcyan', alpha=0.8))

ax4.axis('off')
ax4.set_title('水平线检验法', fontsize=14, fontweight='bold')

# ============ 图5：求定义域 ============
ax5 = fig.add_axes([0.05, 0.06, 0.42, 0.26])

# 分母不为0
x1 = np.linspace(-3, -0.5, 300)
x2 = np.linspace(0.5, 3, 300)
y = 1/(x1**2)
y2 = 1/(x2**2)

ax5.plot(x1, y, 'b-', linewidth=2)
ax5.plot(x2, y2, 'b-', linewidth=2)
ax5.axvline(x=0, color='red', linestyle='--', linewidth=2)
ax5.fill_between(x1, y, alpha=0.3, color='blue')
ax5.fill_between(x2, y2, alpha=0.3, color='blue')
ax5.text(0, 8, r'$\times$', fontsize=20, color='red', ha='center')
ax5.text(0, 12, r'$f(x) = \frac{1}{x^2}$', fontsize=14, ha='center')

ax5.set_xlim(-3.5, 3.5)
ax5.set_ylim(-2, 15)
ax5.set_xlabel('x', fontsize=12)
ax5.set_ylabel('y', fontsize=12)
ax5.set_title(r'定义域: 分母 $\neq 0$', fontsize=14, fontweight='bold')
ax5.grid(True, alpha=0.3)

# ============ 图6：用图像求值域 ============
ax6 = fig.add_axes([0.55, 0.06, 0.42, 0.26])
x = np.linspace(-2, 1, 400)
y = x**2

ax6.plot(x, y, 'b-', linewidth=2)
ax6.fill_between(x, y, alpha=0.3, color='blue')

# 标注 y 轴范围
ax6.annotate('', xy=(-2.5, 0), xytext=(-2.5, 4),
            arrowprops=dict(arrowstyle='<->', color='red', lw=2))
ax6.text(-2.7, 2, '值域\n[0, 4]', fontsize=11, color='red', ha='center')

# 标注 x 轴范围
ax6.annotate('', xy=(-2, -0.5), xytext=(1, -0.5),
            arrowprops=dict(arrowstyle='<->', color='green', lw=2))
ax6.text(-0.5, -1, '定义域 [-2, 1]', fontsize=10, color='green', ha='center')

ax6.set_xlim(-3, 2)
ax6.set_ylim(-1, 6)
ax6.set_xlabel('x', fontsize=12)
ax6.set_ylabel('y', fontsize=12)
ax6.set_title(r'$y = x^2, x \in [-2, 1]$ 的值域', fontsize=14, fontweight='bold')
ax6.grid(True, alpha=0.3)

plt.savefig('/Users/liutao/Documents/Obsidian/微积分/imgs/function_basics.png',
            dpi=150, bbox_inches='tight')
print("Saved: imgs/function_basics.png")
plt.close()
