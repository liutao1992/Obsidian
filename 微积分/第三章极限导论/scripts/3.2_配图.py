#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3.2 左极限和右极限 配图脚本

本节内容主线：
1. 左极限和右极限的概念
2. 左右极限的表示方法（x→a⁻, x→a⁺）
3. 极限存在的条件：左极限 = 右极限
4. 极限不存在的情况（DNE）
5. 负数示例：x→-1⁻, x→-1⁺, x→0⁻, x→0⁺
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Hiragino Sans GB', 'Arial Unicode MS', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# ========== 图1: 左右极限概念示意（笔记中的例子：x→3⁻→1, x→3⁺→-2） ==========

fig, ax = plt.subplots(figsize=(10, 7))

# x < 3 的部分：y = x - 2（蓝色），当 x→3⁻ 时，y→1
x_left = np.linspace(1, 2.97, 100)
y_left = x_left - 2

# x > 3 的部分：y = -2（红色）
x_right = np.linspace(3.03, 5, 100)
y_right = np.full_like(x_right, -2)

# 绘制线段
ax.plot(x_left, y_left, 'b-', linewidth=2.5)
ax.plot(x_right, y_right, 'r-', linewidth=2.5)

# x=3处的空心点（函数未定义）
ax.scatter([3], [1], color='blue', s=150, zorder=5, facecolors='none', edgecolors='blue', linewidths=3)
ax.scatter([3], [-2], color='red', s=150, zorder=5, facecolors='none', edgecolors='red', linewidths=3)

# 左侧逼近箭头和标注
ax.annotate('', xy=(2.97, 1), xytext=(2.5, 1),
            arrowprops=dict(arrowstyle='->', color='blue', lw=2))
ax.annotate(r'$\lim_{x \to 3^-} f(x) = 1$', xy=(2.5, 1), xytext=(1.8, 1.5),
            fontsize=14, color='blue', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))

# 右侧逼近箭头和标注
ax.annotate('', xy=(3.03, -2), xytext=(3.5, -2),
            arrowprops=dict(arrowstyle='->', color='red', lw=2))
ax.annotate(r'$\lim_{x \to 3^+} f(x) = -2$', xy=(3.6, -2), xytext=(4.0, -1.5),
            fontsize=14, color='red', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='red', lw=1.5))

# x=3 垂直参考线
ax.axvline(x=3, color='gray', linestyle='--', alpha=0.6, linewidth=1.5)
ax.text(3.05, 1.8, r'$x = 3$', fontsize=11, color='gray')

# 参考线（虚线）
ax.axhline(y=1, color='blue', linestyle=':', alpha=0.4)
ax.axhline(y=-2, color='red', linestyle=':', alpha=0.4)

# 标注"左右不同"
ax.text(3.5, 0.3, r'左右不相等', fontsize=13, color='purple', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
ax.annotate('', xy=(3.2, 0), xytext=(3.5, 0.3),
            arrowprops=dict(arrowstyle='->', color='purple', lw=1.5))

# 结论
ax.text(2.0, -2.7, r'$\Rightarrow$ 极限不存在 (DNE)', fontsize=14, color='red', fontweight='bold')

ax.set_xlim(1, 5.2)
ax.set_ylim(-3, 3)
ax.set_xlabel(r'$x$', fontsize=14)
ax.set_ylabel(r'$f(x)$', fontsize=14)
ax.set_title(r'左右极限可以不同——跳跃间断点示例', fontsize=15, fontweight='bold')
ax.grid(True, alpha=0.3)

# 图例
blue_patch = mpatches.Patch(color='blue', label=r'$x < 3$ 时')
red_patch = mpatches.Patch(color='red', label=r'$x > 3$ 时')
ax.legend(handles=[blue_patch, red_patch], loc='upper right', fontsize=11)

plt.tight_layout()
plt.savefig('../imgs/3.2_图1_左右极限.png', dpi=150, bbox_inches='tight')
plt.close()

print("图1 生成完成：左右极限概念示意（x→3⁻→1, x→3⁺→-2）")

# ========== 图2: 极限存在 vs 极限不存在 ==========

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# ---------- 左图：极限存在 ----------
ax1 = axes[0]

# 连续函数：f(x) = x - 1
x1 = np.linspace(0.5, 3.5, 300)
y1 = x1 - 1
# x=2 处：空心点表示函数值（用另一个点覆盖）
mask = np.abs(x1 - 2) > 0.08
ax1.plot(x1[mask], y1[mask], 'b-', linewidth=2.5)

# x=2 处的空心点（函数未定义或单独定义）
ax1.scatter([2], [1], color='white', s=120, zorder=6, edgecolors='blue', linewidths=3)
ax1.scatter([2], [1], color='blue', s=80, zorder=7, facecolors='none', edgecolors='blue', linewidths=2)

# 标注
ax1.axvline(x=2, color='gray', linestyle=':', alpha=0.6)
ax1.annotate(r'$\lim_{x \to 2^-} f(x) = 1$', xy=(1.95, 1), xytext=(1.3, 1.6),
            fontsize=12, color='green',
            arrowprops=dict(arrowstyle='->', color='green', lw=1.5))
ax1.annotate(r'$\lim_{x \to 2^+} f(x) = 1$', xy=(2.05, 1), xytext=(2.4, 1.6),
            fontsize=12, color='green',
            arrowprops=dict(arrowstyle='->', color='green', lw=1.5))

ax1.set_xlim(0.5, 3.5)
ax1.set_ylim(-0.5, 2.5)
ax1.set_xlabel(r'$x$', fontsize=13)
ax1.set_ylabel(r'$f(x)$', fontsize=13)
ax1.set_title(r'【情况1】极限存在', fontsize=14, fontweight='bold', color='green')
ax1.grid(True, alpha=0.3)
ax1.text(2, 2.1, r'$\lim_{x \to 2^-} f(x) = \lim_{x \to 2^+} f(x) = 1$',
        ha='center', fontsize=11, color='green', fontweight='bold')

# ---------- 右图：极限不存在 ----------
ax2 = axes[1]

# 分段函数：跳跃间断点
# x<2 时 y=1（蓝色），x>2 时 y=3（红色）
x2_left = np.linspace(0.5, 1.97, 100)
y2_left = np.full_like(x2_left, 1)
x2_right = np.linspace(2.03, 3.5, 100)
y2_right = np.full_like(x2_right, 3)

ax2.plot(x2_left, y2_left, 'b-', linewidth=2.5)
ax2.plot(x2_right, y2_right, 'r-', linewidth=2.5)

# x=2 处的空心点
ax2.scatter([2], [1], color='blue', s=100, zorder=5, facecolors='none', edgecolors='blue', linewidths=2)
ax2.scatter([2], [3], color='red', s=100, zorder=5, facecolors='none', edgecolors='red', linewidths=2)

# 标注
ax2.axvline(x=2, color='gray', linestyle=':', alpha=0.6)
ax2.annotate(r'$\lim_{x \to 2^-} f(x) = 1$', xy=(1.9, 1), xytext=(1.1, 1.8),
            fontsize=12, color='blue',
            arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))
ax2.annotate(r'$\lim_{x \to 2^+} f(x) = 3$', xy=(2.1, 3), xytext=(2.5, 3.5),
            fontsize=12, color='red',
            arrowprops=dict(arrowstyle='->', color='red', lw=1.5))

ax2.set_xlim(0.5, 3.5)
ax2.set_ylim(-0.5, 4)
ax2.set_xlabel(r'$x$', fontsize=13)
ax2.set_ylabel(r'$f(x)$', fontsize=13)
ax2.set_title(r'【情况2】极限不存在 (DNE)', fontsize=14, fontweight='bold', color='red')
ax2.grid(True, alpha=0.3)
ax2.text(2, 3.8, r'$1 \neq 3 \Rightarrow DNE$',
        ha='center', fontsize=12, color='red', fontweight='bold')

plt.suptitle('极限存在条件对比', fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('../imgs/3.2_图2_极限存在条件.png', dpi=150, bbox_inches='tight')
plt.close()

print("图2 生成完成：极限存在与不存在对比")

# ========== 图3: 负数示例——x→-1⁻ 和 x→-1⁺ ==========

fig, ax = plt.subplots(figsize=(10, 7))

# x < -1 的部分：y = x + 2（蓝色），当 x→-1⁻ 时，y→1
x_left = np.linspace(-3, -1.03, 100)
y_left = x_left + 2

# x > -1 的部分：y = -1（红色）
x_right = np.linspace(-0.97, 1, 100)
y_right = np.full_like(x_right, -1)

# 绘制线段
ax.plot(x_left, y_left, 'b-', linewidth=2.5)
ax.plot(x_right, y_right, 'r-', linewidth=2.5)

# x=-1处的空心点
ax.scatter([-1], [1], color='blue', s=150, zorder=5, facecolors='none', edgecolors='blue', linewidths=3)
ax.scatter([-1], [-1], color='red', s=150, zorder=5, facecolors='none', edgecolors='red', linewidths=3)

# 左侧逼近标注
ax.annotate('', xy=(-1.03, 1), xytext=(-1.5, 1),
            arrowprops=dict(arrowstyle='->', color='blue', lw=2))
ax.annotate(r'$\lim_{x \to -1^-} f(x) = 1$', xy=(-1.5, 1), xytext=(-2.3, 1.5),
            fontsize=14, color='blue', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))

# 右侧逼近标注
ax.annotate('', xy=(-0.97, -1), xytext=(-0.5, -1),
            arrowprops=dict(arrowstyle='->', color='red', lw=2))
ax.annotate(r'$\lim_{x \to -1^+} f(x) = -1$', xy=(-0.4, -1), xytext=(0.2, -0.5),
            fontsize=14, color='red', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='red', lw=1.5))

# x=-1 垂直参考线
ax.axvline(x=-1, color='gray', linestyle='--', alpha=0.6, linewidth=1.5)
ax.text(-0.95, 1.8, r'$x = -1$', fontsize=11, color='gray')

# 参考线（虚线）
ax.axhline(y=1, color='blue', linestyle=':', alpha=0.4)
ax.axhline(y=-1, color='red', linestyle=':', alpha=0.4)

# 结论
ax.text(-2.5, -1.7, r'$\Rightarrow$ 极限不存在 (DNE)', fontsize=14, color='red', fontweight='bold')

ax.set_xlim(-3, 1.2)
ax.set_ylim(-2, 2.5)
ax.set_xlabel(r'$x$', fontsize=14)
ax.set_ylabel(r'$f(x)$', fontsize=14)
ax.set_title(r'负数示例：$x \to -1^-$ 和 $x \to -1^+$', fontsize=15, fontweight='bold')
ax.grid(True, alpha=0.3)

# 图例
blue_patch = mpatches.Patch(color='blue', label=r'$x < -1$ 时')
red_patch = mpatches.Patch(color='red', label=r'$x > -1$ 时')
ax.legend(handles=[blue_patch, red_patch], loc='upper right', fontsize=11)

plt.tight_layout()
plt.savefig('../imgs/3.2_图3_负数示例.png', dpi=150, bbox_inches='tight')
plt.close()

print("图3 生成完成：负数示例（x→-1⁻→1, x→-1⁺→-1）")

# ========== 图4: 多种间断点类型展示 ==========

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# ---------- 左上：可去间断点 ----------
ax = axes[0, 0]
x = np.linspace(0, 4, 400)
y = np.where(x < 2, x - 1, x - 1)
# 在 x=2 处制造一个洞
mask = np.abs(x - 2) > 0.06
ax.plot(x[mask], y[mask], 'b-', linewidth=2)
ax.scatter([2], [1], color='white', s=100, zorder=6, edgecolors='red', linewidths=3)
ax.scatter([2], [3], color='red', s=120, zorder=7, facecolors='none', edgecolors='red', linewidths=2)

ax.axvline(x=2, color='gray', linestyle=':', alpha=0.5)
ax.set_xlim(0, 4)
ax.set_ylim(-1, 4)
ax.set_xlabel(r'$x$', fontsize=12)
ax.set_ylabel(r'$f(x)$', fontsize=12)
ax.set_title('可去间断点：左右极限相等，但函数未定义', fontsize=12, color='blue')
ax.grid(True, alpha=0.3)
ax.text(2.1, 2.5, r'极限 = 1', fontsize=10, color='green')
ax.text(2.1, 0.5, r'函数值未定义', fontsize=10, color='red')

# ---------- 右上：跳跃间断点 ----------
ax = axes[0, 1]
x_left = np.linspace(0, 1.97, 100)
y_left = np.full_like(x_left, 1)
x_right = np.linspace(2.03, 4, 100)
y_right = np.full_like(x_right, 3)
ax.plot(x_left, y_left, 'b-', linewidth=2.5)
ax.plot(x_right, y_right, 'r-', linewidth=2.5)
ax.scatter([2], [1], color='blue', s=100, zorder=5, facecolors='none', edgecolors='blue', linewidths=2)
ax.scatter([2], [3], color='red', s=100, zorder=5, facecolors='none', edgecolors='red', linewidths=2)

ax.axvline(x=2, color='gray', linestyle=':', alpha=0.5)
ax.annotate(r'$\lim_{x \to 2^-} = 1$', xy=(1.9, 1), xytext=(0.8, 0.5),
            fontsize=11, color='blue', arrowprops=dict(arrowstyle='->', color='blue'))
ax.annotate(r'$\lim_{x \to 2^+} = 3$', xy=(2.1, 3), xytext=(2.5, 3.5),
            fontsize=11, color='red', arrowprops=dict(arrowstyle='->', color='red'))

ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.set_xlabel(r'$x$', fontsize=12)
ax.set_ylabel(r'$f(x)$', fontsize=12)
ax.set_title('跳跃间断点：左右极限不相等', fontsize=12, color='red')
ax.grid(True, alpha=0.3)
ax.text(1.5, 2, r'1 ≠ 3\n→ DNE', fontsize=12, color='purple', fontweight='bold')

# ---------- 左下：无穷间断点 ----------
ax = axes[1, 0]
x1 = np.linspace(0.1, 1.9, 200)
y1 = 1 / (2 - x1)
x2 = np.linspace(2.1, 3.9, 200)
y2 = 1 / (2 - x2)
ax.plot(x1, y1, 'b-', linewidth=2)
ax.plot(x2, y2, 'r-', linewidth=2)

ax.axvline(x=2, color='gray', linestyle=':', alpha=0.5)
ax.annotate(r'$x \to 2^+$', xy=(2.1, 50), xytext=(2.5, 70),
            fontsize=11, color='red', arrowprops=dict(arrowstyle='->', color='red'))
ax.annotate(r'$x \to 2^-$', xy=(1.9, 50), xytext=(1.0, 70),
            fontsize=11, color='blue', arrowprops=dict(arrowstyle='->', color='blue'))

ax.set_xlim(0, 4)
ax.set_ylim(-20, 100)
ax.set_xlabel(r'$x$', fontsize=12)
ax.set_ylabel(r'$f(x)$', fontsize=12)
ax.set_title('无穷间断点', fontsize=12, color='purple')
ax.grid(True, alpha=0.3)

# ---------- 右下：阶跃函数 ----------
ax = axes[1, 1]
x_left = np.linspace(-1, 0, 100)
y_left = np.zeros_like(x_left)
x_right = np.linspace(0, 1, 100)
y_right = np.ones_like(x_right)
ax.plot(x_left, y_left, 'b-', linewidth=2.5)
ax.plot(x_right, y_right, 'r-', linewidth=2.5)
ax.scatter([0], [0], color='blue', s=100, zorder=5, facecolors='none', edgecolors='blue', linewidths=2)
ax.scatter([0], [1], color='red', s=100, zorder=5)

ax.axvline(x=0, color='gray', linestyle=':', alpha=0.5)
ax.annotate(r'$\lim_{x \to 0^-} f(x) = 0$', xy=(-0.1, 0), xytext=(-0.7, -0.3),
            fontsize=11, color='blue', arrowprops=dict(arrowstyle='->', color='blue'))
ax.annotate(r'$\lim_{x \to 0^+} f(x) = 1$', xy=(0.1, 1), xytext=(0.3, 1.4),
            fontsize=11, color='red', arrowprops=dict(arrowstyle='->', color='red'))

ax.set_xlim(-1, 1)
ax.set_ylim(-0.5, 1.5)
ax.set_xlabel(r'$x$', fontsize=12)
ax.set_ylabel(r'$f(x)$', fontsize=12)
ax.set_title('阶跃函数：左右极限不相等', fontsize=12, color='red')
ax.grid(True, alpha=0.3)
ax.text(0.5, 0.5, r'0 ≠ 1 → DNE', fontsize=12, color='purple', fontweight='bold')

plt.suptitle('间断点的四种类型', fontsize=15, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig('../imgs/3.2_图4_间断点类型.png', dpi=150, bbox_inches='tight')
plt.close()

print("图4 生成完成：四种间断点类型")

# ========== 图5: 极限存在（连续函数） ==========

fig, ax = plt.subplots(figsize=(10, 6))

# 连续函数示例
x = np.linspace(0, 4, 400)
y = (x - 2)**2 + 1

# x=2 处的函数值
f_2 = 1

# 绘制函数
ax.plot(x, y, 'b-', linewidth=2.5)

# 标注
ax.axvline(x=2, color='gray', linestyle=':', alpha=0.6)
ax.scatter([2], [f_2], color='blue', s=120, zorder=5, edgecolors='blue', linewidths=2)

# 左侧逼近
ax.annotate(r'$\lim_{x \to 2^-} f(x) = 1$', xy=(2, 1), xytext=(1.2, 2.5),
            fontsize=13, color='green',
            arrowprops=dict(arrowstyle='->', color='green', lw=1.5))

# 右侧逼近
ax.annotate(r'$\lim_{x \to 2^+} f(x) = 1$', xy=(2, 1), xytext=(2.6, 2.5),
            fontsize=13, color='green',
            arrowprops=dict(arrowstyle='->', color='green', lw=1.5))

# 结论
ax.text(2, 3.5, r'$\lim_{x \to 2^-} f(x) = \lim_{x \to 2^+} f(x) = 1$',
        ha='center', fontsize=14, color='green', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

ax.text(2.8, 0.5, r'>> 极限存在 = 1', fontsize=14, color='green', fontweight='bold')

ax.set_xlim(0, 4)
ax.set_ylim(0, 5)
ax.set_xlabel(r'$x$', fontsize=14)
ax.set_ylabel(r'$f(x)$', fontsize=14)
ax.set_title('连续函数：左右极限相等，极限存在', fontsize=15, fontweight='bold')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('../imgs/3.2_图5_极限存在.png', dpi=150, bbox_inches='tight')
plt.close()

print("图5 生成完成：极限存在示例")

print("\n>> 3.2 全部配图生成完成！")