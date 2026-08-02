#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3.3 配图脚本：何时不存在极限
生成三张图：跳跃间断、无穷间断、振荡间断
"""

import numpy as np
import matplotlib.pyplot as plt

# 配置中文字体
import os

# 获取脚本所在目录的父目录（即第三章极限导论）
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
imgs_dir = os.path.join(base_dir, 'imgs')

# 确保imgs目录存在
os.makedirs(imgs_dir, exist_ok=True)

# 配置中文字体
plt.rcParams['font.sans-serif'] = ['Hiragino Sans GB', 'Arial Unicode MS', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ========== 图1：跳跃间断 ==========
fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 分段函数
x1 = np.linspace(-1, 1.9, 500)
x2 = np.linspace(2.1, 5, 500)

y1 = np.ones_like(x1)
y2 = np.ones_like(x2) * 3

# 左图：完整视图
ax1.plot(x1, y1, 'b-', linewidth=2, label=r'$f(x) = 1 \ (x < 2)$')
ax1.plot(x2, y2, 'r-', linewidth=2, label=r'$f(x) = 3 \ (x \geq 2)$')

# 空心点和实心点
ax1.scatter([2], [1], s=100, facecolors='none', edgecolors='blue', zorder=5, label='左极限 = 1')
ax1.scatter([2], [3], s=100, color='red', zorder=5, label=r'右极限 = 3')

ax1.axvline(x=2, color='gray', linestyle='--', alpha=0.7)
ax1.set_xlabel(r'$x$', fontsize=12)
ax1.set_ylabel(r'$f(x)$', fontsize=12)
ax1.set_title('跳跃间断点示意', fontsize=14, fontweight='bold')
ax1.legend(loc='upper right', fontsize=9)
ax1.set_xlim(-1, 5)
ax1.set_ylim(-0.5, 4)
ax1.grid(True, alpha=0.3)

# 标注
ax1.annotate(r'$\lim_{x \to 2^-} f(x) = 1$', xy=(1.5, 1), xytext=(0.5, 1.5),
              fontsize=11, arrowprops=dict(arrowstyle='->', color='blue'))
ax1.annotate(r'$\lim_{x \to 2^+} f(x) = 3$', xy=(2.5, 3), xytext=(3.5, 2.5),
             fontsize=11, arrowprops=dict(arrowstyle='->', color='red'))

# 右图：放大视图
ax2.plot(x1, y1, 'b-', linewidth=2)
ax2.plot(x2, y2, 'r-', linewidth=2)
ax2.scatter([2], [1], s=150, facecolors='none', edgecolors='blue', zorder=5)
ax2.scatter([2], [3], s=150, color='red', zorder=5)
ax2.axvline(x=2, color='gray', linestyle='--', alpha=0.7)

ax2.set_xlabel(r'$x$', fontsize=12)
ax2.set_ylabel(r'$f(x)$', fontsize=12)
ax2.set_title('放大视图：左右极限不相等', fontsize=14, fontweight='bold')
ax2.set_xlim(1.5, 2.5)
ax2.set_ylim(0, 4)
ax2.grid(True, alpha=0.3)

# 添加DNE标注
ax2.text(2, 2, r'$\lim_{x \to 2} f(x) = \text{DNE}$', fontsize=14,
         ha='center', va='center', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.tight_layout()
fig1.savefig(os.path.join(imgs_dir, '3.3_图1_跳跃间断.png'), dpi=150, bbox_inches='tight')
print(f"图1已保存: {imgs_dir}/3.3_图1_跳跃间断.png")

# ========== 图2：无穷间断 ==========
fig2, (ax3, ax4) = plt.subplots(1, 2, figsize=(12, 5))

# y = 1/x
x3 = np.linspace(-2, -0.01, 500)
x4 = np.linspace(0.01, 2, 500)

y3 = 1 / x3
y4 = 1 / x4

ax3.plot(x3, y3, 'b-', linewidth=2, label=r'$y = \frac{1}{x}$')
ax3.plot(x4, y4, 'r-', linewidth=2)
ax3.axvline(x=0, color='gray', linestyle='--', alpha=0.7)
ax3.axhline(y=0, color='gray', linestyle='-', alpha=0.3)

# 渐近线标注
ax3.annotate(r'$x = 0$（垂直渐近线）', xy=(0.02, 0), xytext=(0.5, -20),
             fontsize=11, color='gray')

# 极限标注
ax3.annotate(r'$\lim_{x \to 0^+} \frac{1}{x} = +\infty$', xy=(0.1, 10), xytext=(0.5, 15),
             fontsize=10, color='red', arrowprops=dict(arrowstyle='->', color='red'))
ax3.annotate(r'$\lim_{x \to 0^-} \frac{1}{x} = -\infty$', xy=(-0.1, -10), xytext=(-0.8, -15),
             fontsize=10, color='blue', arrowprops=dict(arrowstyle='->', color='blue'))

ax3.set_xlabel(r'$x$', fontsize=12)
ax3.set_ylabel(r'$y$', fontsize=12)
ax3.set_title(r'$y = \frac{1}{x}$：左右极限都不存在', fontsize=14, fontweight='bold')
ax3.legend(loc='upper right', fontsize=10)
ax3.set_xlim(-2, 2)
ax3.set_ylim(-30, 30)
ax3.grid(True, alpha=0.3)

# y = 1/x^2
x5 = np.linspace(-2, -0.1, 500)
x6 = np.linspace(0.1, 2, 500)

y5 = 1 / (x5**2)
y6 = 1 / (x6**2)

ax4.plot(x5, y5, 'b-', linewidth=2, label=r'$y = \frac{1}{x^2}$')
ax4.plot(x6, y6, 'r-', linewidth=2)
ax4.axvline(x=0, color='gray', linestyle='--', alpha=0.7)

# 极限标注
ax4.annotate(r'$\lim_{x \to 0} \frac{1}{x^2} = +\infty$', xy=(0.15, 100), xytext=(0.6, 50),
             fontsize=11, arrowprops=dict(arrowstyle='->', color='purple'))

ax4.set_xlabel(r'$x$', fontsize=12)
ax4.set_ylabel(r'$y$', fontsize=12)
ax4.set_title(r'$y = \frac{1}{x^2}$：两侧都趋于正无穷', fontsize=14, fontweight='bold')
ax4.legend(loc='upper right', fontsize=10)
ax4.set_xlim(-2, 2)
ax4.set_ylim(0, 120)
ax4.grid(True, alpha=0.3)

plt.tight_layout()
fig2.savefig(os.path.join(imgs_dir, '3.3_图2_无穷间断.png'), dpi=150, bbox_inches='tight')
print(f"图2已保存: {imgs_dir}/3.3_图2_无穷间断.png")

# ========== 图3：振荡间断 ==========
fig3, (ax5, ax6) = plt.subplots(1, 2, figsize=(14, 5))

# y = sin(1/x) - 使用对数采样以捕捉靠近0时的密集振荡
x7 = np.geomspace(0.0005, 0.5, 5000)  # 对数采样，更密集地覆盖靠近0的区域
y7 = np.sin(1 / x7)

ax5.plot(x7, y7, 'b-', linewidth=0.8)
ax5.axhline(y=1, color='red', linestyle='--', alpha=0.5, label=r'$y = 1$')
ax5.axhline(y=-1, color='red', linestyle='--', alpha=0.5, label=r'$y = -1$')
ax5.axvline(x=0, color='gray', linestyle='--', alpha=0.7)

ax5.set_xlabel(r'$x$', fontsize=12)
ax5.set_ylabel(r'$y$', fontsize=12)
ax5.set_title(r'$y = \sin\frac{1}{x}$：在原点附近无限振荡', fontsize=14, fontweight='bold')
ax5.legend(loc='upper right', fontsize=10)
ax5.set_xlim(0, 0.5)
ax5.set_ylim(-1.5, 1.5)
ax5.grid(True, alpha=0.3)

# 标注
ax5.text(0.25, 1.2, r'震荡越来越快', fontsize=11, ha='center')
ax5.annotate('', xy=(0.1, 0), xytext=(0.3, 0),
             arrowprops=dict(arrowstyle='->', color='gray'))
ax5.text(0.1, 0.8, r'$\lim_{x \to 0} \sin\frac{1}{x} = \text{DNE}$',
         fontsize=12, ha='center', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# y = x * sin(1/x) - 被压制的振荡
x8 = np.linspace(-0.1, 0.1, 2000)
y8 = x8 * np.sin(1 / x8)

# 处理x=0处的奇点
x8_clean = x8[np.abs(x8) > 0.005]
y8_clean = x8_clean * np.sin(1 / x8_clean)

ax6.plot(x8_clean, y8_clean, 'b-', linewidth=1)
ax6.axhline(y=0, color='gray', linestyle='-', alpha=0.3)
ax6.axvline(x=0, color='gray', linestyle='--', alpha=0.7)

# 边界线
x9 = np.linspace(-0.1, 0.1, 500)
ax6.plot(x9, np.abs(x9), 'r--', linewidth=1, alpha=0.7, label=r'$y = |x|$')
ax6.plot(x9, -np.abs(x9), 'r--', linewidth=1, alpha=0.7, label=r'$y = -|x|$')

ax6.set_xlabel(r'$x$', fontsize=12)
ax6.set_ylabel(r'$y$', fontsize=12)
ax6.set_title(r'$y = x \cdot \sin\frac{1}{x}$：振幅被压制，极限存在', fontsize=14, fontweight='bold')
ax6.legend(loc='upper right', fontsize=10)
ax6.set_xlim(-0.1, 0.1)
ax6.set_ylim(-0.15, 0.15)
ax6.grid(True, alpha=0.3)

# 极限标注
ax6.text(0, 0, r'$\lim_{x \to 0} x \cdot \sin\frac{1}{x} = 0$',
         fontsize=12, ha='center', va='bottom',
         bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))

plt.tight_layout()
fig3.savefig(os.path.join(imgs_dir, '3.3_图3_振荡间断.png'), dpi=150, bbox_inches='tight')
print(f"图3已保存: {imgs_dir}/3.3_图3_振荡间断.png")

print("\n所有配图已生成完毕！")
