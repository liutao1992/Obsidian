#!/usr/bin/env python3
"""
绘制求定义域图
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
matplotlib.use('Agg')

font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
font_prop = font_manager.FontProperties(fname=font_path)

plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# ============ 图1：分母不为0 ============
ax1 = axes[0, 0]
x1 = np.linspace(-3, -0.3, 300)
x2 = np.linspace(0.3, 3, 300)
y1 = 1/(x1**2)
y2 = 1/(x2**2)

ax1.plot(x1, y1, 'b-', linewidth=2)
ax1.plot(x2, y2, 'b-', linewidth=2)
ax1.axvline(x=0, color='red', linestyle='--', linewidth=2)
ax1.fill_between(x1, y1, alpha=0.3, color='blue')
ax1.fill_between(x2, y2, alpha=0.3, color='blue')
ax1.text(0, 10, r'$\times$', fontsize=25, color='red', ha='center')
ax1.text(0, 14, r'$f(x) = \frac{1}{x^2}$', fontsize=14, ha='center', fontweight='bold')
ax1.text(0, 8, r'定义域: $x \neq 0$', fontsize=12,
        bbox=dict(boxstyle='round', facecolor='lightyellow'), fontproperties=font_prop)

ax1.set_xlim(-3.5, 3.5)
ax1.set_ylim(-2, 18)
ax1.set_xlabel('x', fontsize=12)
ax1.set_ylabel('y', fontsize=12)
ax1.set_title('1. 分母不为0', fontsize=14, fontweight='bold', fontproperties=font_prop)
ax1.grid(True, alpha=0.3)

# ============ 图2：偶次根号 >= 0 ============
ax2 = axes[0, 1]
x = np.linspace(0, 3, 400)
y = np.sqrt(x)

ax2.plot(x, y, 'b-', linewidth=2)
ax2.fill_between(x, y, alpha=0.3, color='blue')
ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.set_xlim(-0.5, 3.5)
ax2.set_ylim(-0.5, 2)
ax2.text(1.5, 1.2, r'$f(x) = \sqrt{x}$', fontsize=14, ha='center', fontweight='bold')
ax2.text(1.5, -0.3, r'定义域: $x \geq 0$', fontsize=12, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow'), fontproperties=font_prop)

ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('y', fontsize=12)
ax2.set_title('2. 偶次根号 >= 0', fontsize=14, fontweight='bold', fontproperties=font_prop)
ax2.grid(True, alpha=0.3)

# ============ 图3：奇次根号 ============
ax3 = axes[1, 0]
x = np.linspace(-2, 2, 400)
y = np.cbrt(x)

ax3.plot(x, y, 'b-', linewidth=2)
ax3.fill_between(x, y, alpha=0.3, color='blue')
ax3.axhline(y=0, color='black', linewidth=0.5)
ax3.set_xlim(-2.5, 2.5)
ax3.set_ylim(-2, 2)
ax3.text(0, 1.3, r'$f(x) = \sqrt[3]{x}$', fontsize=14, ha='center', fontweight='bold')
ax3.text(0, -1.5, '定义域: 全体实数', fontsize=12, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow'), fontproperties=font_prop)

ax3.set_xlabel('x', fontsize=12)
ax3.set_ylabel('y', fontsize=12)
ax3.set_title('3. 奇次根号: x取任意值', fontsize=14, fontweight='bold', fontproperties=font_prop)
ax3.grid(True, alpha=0.3)

# ============ 图4：对数 ============
ax4 = axes[1, 1]
x = np.linspace(0.1, 3, 400)
y = np.log(x)

ax4.plot(x, y, 'b-', linewidth=2)
ax4.fill_between(x, y, alpha=0.3, color='blue')
ax4.axvline(x=0, color='red', linestyle='--', linewidth=2)
ax4.fill_betweenx(y, -0.5, 0, alpha=0.3, color='red')
ax4.text(0, -1, r'$\times$', fontsize=25, color='red', ha='center')
ax4.text(1.5, -0.5, r'$f(x) = \ln(x)$', fontsize=14, ha='center', fontweight='bold')
ax4.text(1.5, 1.2, r'定义域: $x > 0$', fontsize=12, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow'), fontproperties=font_prop)

ax4.set_xlim(-0.5, 3.5)
ax4.set_ylim(-3, 2)
ax4.set_xlabel('x', fontsize=12)
ax4.set_ylabel('y', fontsize=12)
ax4.set_title('4. 对数: 真数 > 0', fontsize=14, fontweight='bold', fontproperties=font_prop)
ax4.grid(True, alpha=0.3)

fig.suptitle('求定义域（常见情况）', fontsize=17, fontweight='bold', fontproperties=font_prop)

plt.tight_layout()
plt.savefig('/Users/liutao/Documents/Obsidian/微积分/imgs/find_domain.png', dpi=150, bbox_inches='tight')
print("Saved: imgs/find_domain.png")
plt.close()
