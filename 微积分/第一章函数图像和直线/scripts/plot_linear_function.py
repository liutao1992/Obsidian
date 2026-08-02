#!/usr/bin/env python3
"""
绘制一次函数相关图像
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

fig = plt.figure(figsize=(16, 14))

# ============ 标题 ============
fig.suptitle('一次函数与直线', fontsize=20, fontweight='bold', y=0.98)

# ============ 图1：不同斜率 ============
ax1 = fig.add_axes([0.05, 0.68, 0.42, 0.26])
x = np.linspace(-3, 3, 400)

# 不同斜率的直线
ax1.plot(x, 2*x + 1, 'b-', linewidth=2, label=r'$m=2, b=1$')
ax1.plot(x, 1*x + 1, 'g-', linewidth=2, label=r'$m=1, b=1$')
ax1.plot(x, 0*x + 1, 'orange', linewidth=2, label=r'$m=0, b=1$')
ax1.plot(x, -1*x + 1, 'r-', linewidth=2, label=r'$m=-1, b=1$')
ax1.plot(x, 0.5*x + 1, 'purple', linewidth=2, label=r'$m=0.5, b=1$')

ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.axvline(x=0, color='black', linewidth=0.5)
ax1.set_xlim(-3, 3)
ax1.set_ylim(-5, 8)
ax1.set_xlabel('x', fontsize=12)
ax1.set_ylabel('y', fontsize=12)
ax1.set_title('不同斜率 m (b 相同)', fontsize=14, fontweight='bold')
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True, alpha=0.3)

# ============ 图2：不同截距 ============
ax2 = fig.add_axes([0.55, 0.68, 0.42, 0.26])
x = np.linspace(-3, 3, 400)

# 不同截距的直线
ax2.plot(x, 1*x + 2, 'b-', linewidth=2, label=r'$m=1, b=2$')
ax2.plot(x, 1*x + 1, 'g-', linewidth=2, label=r'$m=1, b=1$')
ax2.plot(x, 1*x + 0, 'orange', linewidth=2, label=r'$m=1, b=0$')
ax2.plot(x, 1*x - 1, 'r-', linewidth=2, label=r'$m=1, b=-1$')
ax2.plot(x, 1*x - 2, 'purple', linewidth=2, label=r'$m=1, b=-2$')

ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.axvline(x=0, color='black', linewidth=0.5)
ax2.set_xlim(-3, 3)
ax2.set_ylim(-5, 8)
ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('y', fontsize=12)
ax2.set_title('不同截距 b (m 相同)', fontsize=14, fontweight='bold')
ax2.legend(loc='upper left', fontsize=10)
ax2.grid(True, alpha=0.3)

# ============ 图3：斜率的几何意义 ============
ax3 = fig.add_axes([0.05, 0.38, 0.42, 0.26])
x = np.linspace(-1, 4, 400)
y = 2*x

ax3.plot(x, y, 'b-', linewidth=2.5, label=r'$y = 2x$')
ax3.plot([1, 1], [0, 2], 'r--', linewidth=1.5)
ax3.plot([1, 3], [2, 2], 'r--', linewidth=1.5)
ax3.plot([1], [2], 'ro', markersize=12)
ax3.plot([3], [6], 'ro', markersize=12)

# 标注
ax3.annotate(r'$(1, 2)$', xy=(1, 2), xytext=(1.2, 2.3), fontsize=12)
ax3.annotate(r'$(3, 6)$', xy=(3, 6), xytext=(3.2, 6.3), fontsize=12)
ax3.annotate(r'$\Delta x = 2$', xy=(2, 0), xytext=(2, -0.8), fontsize=11, ha='center')
ax3.annotate(r'$\Delta y = 4$', xy=(3.5, 4), xytext=(3.8, 4), fontsize=11)
ax3.annotate(r'$m = \frac{\Delta y}{\Delta x} = \frac{4}{2} = 2$',
            xy=(0.5, 7), fontsize=13, color='red',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

ax3.axhline(y=0, color='black', linewidth=0.5)
ax3.axvline(x=0, color='black', linewidth=0.5)
ax3.set_xlim(-1, 4.5)
ax3.set_ylim(-1, 8)
ax3.set_xlabel('x', fontsize=12)
ax3.set_ylabel('y', fontsize=12)
ax3.set_title('斜率的几何意义', fontsize=14, fontweight='bold')
ax3.grid(True, alpha=0.3)

# ============ 图4：平行与垂直 ============
ax4 = fig.add_axes([0.55, 0.38, 0.42, 0.26])
x = np.linspace(-3, 3, 400)

# 两条平行线
ax4.plot(x, 2*x + 1, 'b-', linewidth=2, label=r'$y = 2x + 1$ (m=2)')
ax4.plot(x, 2*x - 2, 'b--', linewidth=2, label=r'$y = 2x - 2$ (m=2, 平行)')

# 一条垂直线
ax4.plot([1, 1], [-6, 4], 'r-', linewidth=2, label=r'$x = 1$ (垂直)')
ax4.plot(x, -0.5*x + 3.5, 'g-', linewidth=2, label=r'$y = -0.5x + 3.5$ (m=-0.5, 垂直)')

# 标注垂直符号
ax4.annotate('', xy=(0.5, 2), xytext=(1.5, 2),
            arrowprops=dict(arrowstyle='<->', color='purple', lw=2))
ax4.text(1, 1.3, r'$\perp$', fontsize=20, color='purple', ha='center')

ax4.axhline(y=0, color='black', linewidth=0.5)
ax4.axvline(x=0, color='black', linewidth=0.5)
ax4.set_xlim(-3, 3)
ax4.set_ylim(-6, 5)
ax4.set_xlabel('x', fontsize=12)
ax4.set_ylabel('y', fontsize=12)
ax4.set_title('平行与垂直', fontsize=14, fontweight='bold')
ax4.legend(loc='upper left', fontsize=9)
ax4.grid(True, alpha=0.3)

# ============ 图5：特殊直线 ============
ax5 = fig.add_axes([0.05, 0.08, 0.42, 0.26])
x = np.linspace(-3, 3, 400)

# 水平线
ax5.plot(x, 0*x + 2, 'b-', linewidth=2.5, label=r'$y = 2$ (水平线, m=0)')
# 垂直线（用不同方式绘制）
ax5.plot([1, 1], [-3, 3], 'r-', linewidth=2.5, label=r'$x = 1$ (垂直线)')
# 过原点
ax5.plot(x, 1.5*x, 'g-', linewidth=2, label=r'$y = 1.5x$ (过原点)')
ax5.plot(x, -x, 'orange', linewidth=2, label=r'$y = -x$ (过原点, m<0)')

ax5.axhline(y=0, color='black', linewidth=0.5)
ax5.axvline(x=0, color='black', linewidth=0.5)
ax5.set_xlim(-3, 3)
ax5.set_ylim(-4, 4)
ax5.set_xlabel('x', fontsize=12)
ax5.set_ylabel('y', fontsize=12)
ax5.set_title('特殊直线', fontsize=14, fontweight='bold')
ax5.legend(loc='upper right', fontsize=9)
ax5.grid(True, alpha=0.3)

# ============ 图6：截距式 ============
ax6 = fig.add_axes([0.55, 0.08, 0.42, 0.26])
x = np.linspace(-5, 5, 400)

# 截距式演示
# x/3 + y/2 = 1 => y = 2*(1 - x/3) = 2 - 2x/3
y = 2 - 2*x/3
ax6.plot(x, y, 'b-', linewidth=2.5, label=r'$\frac{x}{3} + \frac{y}{2} = 1$')
ax6.plot([3], [0], 'ro', markersize=12, label='x轴截距 a=3')
ax6.plot([0], [2], 'go', markersize=12, label='y轴截距 b=2')

ax6.axhline(y=0, color='black', linewidth=0.5)
ax6.axvline(x=0, color='black', linewidth=0.5)
ax6.set_xlim(-1, 5)
ax6.set_ylim(-1, 4)
ax6.set_xlabel('x', fontsize=12)
ax6.set_ylabel('y', fontsize=12)
ax6.set_title('截距式：x/a + y/b = 1', fontsize=14, fontweight='bold')
ax6.legend(loc='upper right', fontsize=9)
ax6.grid(True, alpha=0.3)

plt.savefig('/Users/liutao/Documents/Obsidian/微积分/第一章函数图像和直线/imgs/linear_function.png',
            dpi=150, bbox_inches='tight')
print("Saved: imgs/linear_function.png")
plt.close()
