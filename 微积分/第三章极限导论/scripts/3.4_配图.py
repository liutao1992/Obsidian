#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3.4 在 ∞ 和 −∞ 处的极限 配图脚本

本节内容：
1. x趋于无穷的六种情况
2. 函数在无穷处的极限（存在/不存在）
3. 水平渐近线
4. 大的数与小的数
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Hiragino Sans GB', 'Arial Unicode MS', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# ========== 图1: y=1/x 的水平渐近线 ==========

fig, ax = plt.subplots(figsize=(10, 7))

# y = 1/x
x_pos = np.linspace(0.1, 10, 400)
x_neg = np.linspace(-10, -0.1, 400)
y_pos = 1 / x_pos
y_neg = 1 / x_neg

ax.plot(x_pos, y_pos, 'b-', linewidth=2.5, label=r'$y = \frac{1}{x}, x > 0$')
ax.plot(x_neg, y_neg, 'r-', linewidth=2.5, label=r'$y = \frac{1}{x}, x < 0$')

# 水平渐近线 y = 0
ax.axhline(y=0, color='green', linestyle='--', linewidth=2, alpha=0.8)
ax.text(8, 0.2, r'$y = 0$ (水平渐近线)', fontsize=12, color='green', fontweight='bold')

# 标注
ax.annotate(r'$\lim_{x \to +\infty} \frac{1}{x} = 0$', xy=(8, 0.125), xytext=(6, 1),
            fontsize=12, color='blue',
            arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))

ax.annotate(r'$\lim_{x \to -\infty} \frac{1}{x} = 0$', xy=(-8, -0.125), xytext=(-6, -1),
            fontsize=12, color='red',
            arrowprops=dict(arrowstyle='->', color='red', lw=1.5))

ax.set_xlim(-10, 10)
ax.set_ylim(-3, 3)
ax.set_xlabel(r'$x$', fontsize=14)
ax.set_ylabel(r'$f(x)$', fontsize=14)
ax.set_title(r'$y = \frac{1}{x}$ 的水平渐近线', fontsize=15, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.legend(loc='upper right', fontsize=11)

plt.tight_layout()
plt.savefig('../imgs/3.4_图1_1overx水平渐近线.png', dpi=150, bbox_inches='tight')
plt.close()

print("图1 已保存: 3.4_图1_1overx水平渐近线.png")

# ========== 图2: y = sin(1/x) 在无穷远处趋于0 ==========

fig, ax = plt.subplots(figsize=(14, 6))

# y = sin(1/x)，用大范围展示无穷远处的情况
x = np.linspace(0.01, 100, 2000)
y = np.sin(1/x)

ax.plot(x, y, 'b-', linewidth=1.5, label=r'$y = \sin\frac{1}{x}$')

# 水平渐近线 y = 0
ax.axhline(y=0, color='green', linestyle='--', linewidth=2, alpha=0.8)

# 标注
ax.annotate(r'$x \to +\infty$', xy=(80, 0), xytext=(60, 0.8),
            fontsize=12, color='blue',
            arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))

ax.annotate(r'$\frac{1}{x} \to 0$', xy=(60, 0.1), xytext=(40, 1.2),
            fontsize=11, color='purple',
            arrowprops=dict(arrowstyle='->', color='purple', lw=1.5))

ax.annotate(r'$\sin\frac{1}{x} \to 0$', xy=(40, 0.05), xytext=(15, 0.6),
            fontsize=11, color='green',
            arrowprops=dict(arrowstyle='->', color='green', lw=1.5))

# 局部放大示意（右侧小图）
ax_inset = fig.add_axes([0.7, 0.55, 0.25, 0.35])  # 右侧插入小图
x_small = np.linspace(0.01, 0.3, 500)
y_small = np.sin(1/x_small)
ax_inset.plot(x_small, y_small, 'b-', linewidth=0.8)
ax_inset.axhline(y=0, color='green', linestyle='--', linewidth=1, alpha=0.8)
ax_inset.set_xlim(0, 0.3)
ax_inset.set_ylim(-1.5, 1.5)
ax_inset.set_title(r'局部：$x \to 0^+$ 时震荡', fontsize=9)
ax_inset.grid(True, alpha=0.3)

ax.set_xlim(0, 100)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel(r'$x$', fontsize=14)
ax.set_ylabel(r'$f(x)$', fontsize=14)
ax.set_title(r'$y = \sin\frac{1}{x}$ 在 $x \to +\infty$ 时趋于 0', fontsize=15, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.legend(loc='upper right', fontsize=11)

plt.tight_layout()
plt.savefig('../imgs/3.4_图2_sin1overx趋于0.png', dpi=150, bbox_inches='tight')
plt.close()

print("图2 已保存: 3.4_图2_sin1overx趋于0.png")

# ========== 图3: y = x² 在无穷处趋于无穷 ==========

fig, ax = plt.subplots(figsize=(10, 7))

# y = x²
x = np.linspace(-5, 5, 400)
y = x ** 2

ax.plot(x, y, 'b-', linewidth=2.5)

# 渐近线/趋势标注
ax.annotate(r'$\lim_{x \to +\infty} x^2 = +\infty$', xy=(4, 16), xytext=(2, 10),
            fontsize=12, color='blue',
            arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))

ax.annotate(r'$\lim_{x \to -\infty} x^2 = +\infty$', xy=(-4, 16), xytext=(-2, 10),
            fontsize=12, color='blue',
            arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))

# 向上发散的箭头
ax.annotate('', xy=(3.5, 12), xytext=(3.5, 8),
            arrowprops=dict(arrowstyle='->', color='purple', lw=2))
ax.text(3.7, 9, r'$\to +\infty$', fontsize=12, color='purple', fontweight='bold')

ax.set_xlim(-5, 5)
ax.set_ylim(-2, 25)
ax.set_xlabel(r'$x$', fontsize=14)
ax.set_ylabel(r'$f(x)$', fontsize=14)
ax.set_title(r'$y = x^2$ 在无穷处趋于正无穷（极限不存在）', fontsize=15, fontweight='bold')
ax.grid(True, alpha=0.3)

# 结论框
ax.text(0, 22, r'$\infty$ 不是有限的极限值 → DNE',
        ha='center', fontsize=13, color='red', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.tight_layout()
plt.savefig('../imgs/3.4_图3_x平方趋于无穷.png', dpi=150, bbox_inches='tight')
plt.close()

print("图3 已保存: 3.4_图3_x平方趋于无穷.png")

# ========== 图4: y = sin x 在无穷处震荡 ==========

fig, ax = plt.subplots(figsize=(12, 6))

# y = sin x
x = np.linspace(0, 50, 1000)
y = np.sin(x)

ax.plot(x, y, 'b-', linewidth=1.5, label=r'$y = \sin x$')

# 标注震荡
ax.axhline(y=1, color='red', linestyle=':', alpha=0.5)
ax.axhline(y=-1, color='red', linestyle=':', alpha=0.5)

# 标注文字
ax.text(45, 1.15, r'$y = 1$', fontsize=11, color='red')
ax.text(45, -1.25, r'$y = -1$', fontsize=11, color='red')

ax.annotate(r'$\lim_{x \to +\infty} \sin x$ 不存在', xy=(35, 0), xytext=(25, 1.5),
            fontsize=13, color='red', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='red', lw=1.5))

ax.text(25, -1.6, r'永远在 $[-1, 1]$ 之间震荡，不会趋于任何固定值',
        fontsize=11, color='gray', style='italic')

ax.set_xlim(0, 50)
ax.set_ylim(-2, 2)
ax.set_xlabel(r'$x$', fontsize=14)
ax.set_ylabel(r'$f(x)$', fontsize=14)
ax.set_title(r'$y = \sin x$ 在 $x \to +\infty$ 时震荡（极限不存在）', fontsize=15, fontweight='bold')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('../imgs/3.4_图4_sinx无穷处震荡.png', dpi=150, bbox_inches='tight')
plt.close()

print("图4 已保存: 3.4_图4_sinx无穷处震荡.png")

# ========== 图5: 水平渐近线概念图 ==========

fig, ax = plt.subplots(figsize=(12, 7))

# 绘制函数 y = 1 + 1/x（逐渐靠近 y=1）
x_pos = np.linspace(0.1, 20, 500)
y_pos = 1 + 1/x_pos

ax.plot(x_pos, y_pos, 'b-', linewidth=2.5, label=r'$y = 1 + \frac{1}{x}$')

# 水平渐近线 y = 1
ax.axhline(y=1, color='red', linestyle='--', linewidth=2.5, alpha=0.8)
ax.text(18, 1.15, r'$y = L$ (水平渐近线)', fontsize=14, color='red', fontweight='bold')

# 标注函数逐渐靠近的过程
ax.annotate('', xy=(5, 1.2), xytext=(5, 1.02),
            arrowprops=dict(arrowstyle='<->', color='green', lw=1.5))
ax.text(5.1, 1.1, r'$\to 0$', fontsize=11, color='green')

ax.annotate('', xy=(10, 1.1), xytext=(10, 1.005),
            arrowprops=dict(arrowstyle='<->', color='green', lw=1.5))
ax.text(10.1, 1.05, r'$\to 0$', fontsize=11, color='green')

ax.annotate('', xy=(15, 1.07), xytext=(15, 1.003),
            arrowprops=dict(arrowstyle='<->', color='green', lw=1.5))
ax.text(15.1, 1.04, r'$\to 0$', fontsize=11, color='green')

# 标注极限
ax.annotate(r'$\lim_{x \to +\infty} \left(1 + \frac{1}{x}\right) = 1$',
            xy=(12, 1.07), xytext=(8, 1.5),
            fontsize=13, color='blue',
            arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))

# 说明文字
ax.text(2, 2.5, r'当 $x \to +\infty$ 时，$f(x) \to L$',
        fontsize=12, color='blue',
        bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))

ax.text(2, 2.1, r'则 $y = L$ 是水平渐近线',
        fontsize=12, color='red', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))

ax.set_xlim(-1, 20)
ax.set_ylim(0, 3)
ax.set_xlabel(r'$x$', fontsize=14)
ax.set_ylabel(r'$f(x)$', fontsize=14)
ax.set_title('水平渐近线概念图', fontsize=15, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.legend(loc='upper right', fontsize=12)

plt.tight_layout()
plt.savefig('../imgs/3.4_图5_水平渐近线概念.png', dpi=150, bbox_inches='tight')
plt.close()

print("图5 已保存: 3.4_图5_水平渐近线概念.png")

print("\n>> 3.4 全部配图生成完毕！")
