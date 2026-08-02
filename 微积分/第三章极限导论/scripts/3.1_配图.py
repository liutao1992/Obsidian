#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3.1 极限：基本思想 配图
使用 matplotlib 绘制精美的插图
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch
from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.lines as mlines

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'STHeiti']
plt.rcParams['axes.unicode_minus'] = False

# ============ 图1: 函数图像上的"洞" ============
def draw_function_with_hole():
    """绘制 f(x) = x - 1 (x ≠ 2) 的函数图像，展示 x=2 处的洞"""
    fig, ax = plt.subplots(figsize=(12, 8))

    # 绘制 y = x - 1 直线
    x_line = np.linspace(-1, 4, 100)
    y_line = x_line - 1
    ax.plot(x_line, y_line, 'b-', linewidth=2, label=r'$f(x) = x - 1$')

    # 标记 x=2 处的空心点（洞）
    hole_x = 2
    hole_y = hole_x - 1  # = 1
    ax.plot(hole_x, hole_y, 'wo', markersize=15, markeredgecolor='red', markeredgewidth=3, zorder=5)
    ax.text(hole_x + 0.1, hole_y + 0.15, r'$(2, 1)$', fontsize=12, color='red', fontweight='bold')

    # 标注"空心点"
    ax.annotate(r'$x = 2$ 处无定义', xy=(hole_x, hole_y), xytext=(hole_x + 0.8, hole_y + 0.5),
                fontsize=11, color='red',
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
                bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', edgecolor='red', alpha=0.9))

    # 绘制靠近点时的 y 范围 [1-δ, 1+δ]
    delta = 0.1
    ax.axhline(y=1 + delta, color='green', linestyle='--', linewidth=1.5, alpha=0.7)
    ax.axhline(y=1 - delta, color='green', linestyle='--', linewidth=1.5, alpha=0.7, label=r'$y \in [1-\delta, 1+\delta]$')

    # 填充 y 的范围
    ax.fill_between(x_line, 1 - delta, 1 + delta, alpha=0.1, color='green')

    # 标注 y 范围
    ax.text(3.5, 1 + delta + 0.05, r'$1 + \delta$', fontsize=10, color='green')
    ax.text(3.5, 1 - delta - 0.08, r'$1 - \delta$', fontsize=10, color='green')

    # 标注 x 范围
    ax.axvline(x=2 - delta, color='purple', linestyle=':', linewidth=1.5, alpha=0.7)
    ax.axvline(x=2 + delta, color='purple', linestyle=':', linewidth=1.5, alpha=0.7)
    ax.text(2 - delta - 0.15, -0.8, r'$2 - \delta$', fontsize=10, color='purple', ha='right')
    ax.text(2 + delta + 0.05, -0.8, r'$2 + \delta$', fontsize=10, color='purple')

    # 标注极限过程
    ax.annotate('', xy=(2.05, -0.3), xytext=(1.8, -0.3),
                arrowprops=dict(arrowstyle='->', color='gray', lw=2))
    ax.text(1.9, -0.5, r'$x \to 2$', fontsize=11, ha='center', color='gray')

    # 坐标轴
    ax.axhline(y=0, color='black', linewidth=0.8)
    ax.axvline(x=0, color='black', linewidth=0.8)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-1.5, 3.5)
    ax.set_xlabel(r'$x$', fontsize=12)
    ax.set_ylabel(r'$y$', fontsize=12)
    ax.set_title(r'极限示例：$f(x) = x - 1 \ (x \neq 2)$，当 $x \to 2$ 时，$f(x) \to 1$', fontsize=14, fontweight='bold')
    ax.legend(loc='upper left')
    ax.grid(True, alpha=0.3)

    # 添加说明框
    note_text = (
        r"$\lim_{x \to 2} f(x) = 1$" + "\n"
        "即使 f(2) 无定义，极限依然存在！"
    )
    ax.text(0.5, 2.8, note_text, fontsize=11,
           bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', edgecolor='orange'))

    plt.tight_layout()
    plt.savefig('../imgs/3.1_图1_函数洞.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("已生成: 3.1_图1_函数洞.png")


# ============ 图2: x 逼近 2 的过程 ============
def draw_x_approaching():
    """展示 x 从左右两侧逼近 2 的过程"""
    fig, ax = plt.subplots(figsize=(14, 6))

    # 左侧逼近
    ax1 = fig.add_subplot(1, 2, 1)

    # 绘制函数
    x = np.linspace(-1, 4, 200)
    y = x - 1
    ax1.plot(x, y, 'b-', linewidth=2)

    # 标记特殊点
    ax1.plot(2, 1, 'wo', markersize=15, markeredgecolor='red', markeredgewidth=3)
    ax1.plot(2, 1.5, 'ro', markersize=10, zorder=5)  # 假设定义值 f(2) = 1.5

    # 绘制逼近路径
    approach_points_x = [1.5, 1.7, 1.8, 1.9, 1.95, 1.99]
    approach_points_y = [p - 1 for p in approach_points_x]
    ax1.plot(approach_points_x, approach_points_y, 'g-o', markersize=8, linewidth=2, label=r'$x \to 2^-$')

    # 标注
    ax1.annotate(r'$f(2) = 1.5$（假设定义值）', xy=(2, 1.5), xytext=(2.5, 1.8),
                fontsize=10, color='red',
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
    ax1.annotate(r'$lim_{x \to 2^-} f(x) = 1$', xy=(1.95, 0.95), xytext=(1.2, 0.3),
                fontsize=11, color='green', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='green', lw=1.5))

    ax1.axhline(y=0, color='black', linewidth=0.8)
    ax1.axvline(x=0, color='black', linewidth=0.8)
    ax1.set_xlim(-0.5, 4)
    ax1.set_ylim(-1, 3)
    ax1.set_xlabel(r'$x$', fontsize=12)
    ax1.set_ylabel(r'$y$', fontsize=12)
    ax1.set_title(r'左侧逼近：$x \to 2^-$', fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='upper left')

    # 右侧逼近
    ax2 = fig.add_subplot(1, 2, 2)

    # 绘制函数
    x = np.linspace(-1, 4, 200)
    y = x - 1
    ax2.plot(x, y, 'b-', linewidth=2)

    # 标记特殊点
    ax2.plot(2, 1, 'wo', markersize=15, markeredgecolor='red', markeredgewidth=3)
    ax2.plot(2, 1.5, 'ro', markersize=10, zorder=5)

    # 绘制逼近路径
    approach_points_x = [2.5, 2.3, 2.2, 2.1, 2.05, 2.01]
    approach_points_y = [p - 1 for p in approach_points_x]
    ax2.plot(approach_points_x, approach_points_y, 'orange', marker='o', markersize=8, linewidth=2, label=r'$x \to 2^+$')

    # 标注
    ax2.annotate(r'$f(2) = 1.5$（假设定义值）', xy=(2, 1.5), xytext=(2.5, 1.8),
                fontsize=10, color='red',
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
    ax2.annotate(r'$lim_{x \to 2^+} f(x) = 1$', xy=(2.05, 1.05), xytext=(2.6, 1.5),
                fontsize=11, color='orange', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='orange', lw=1.5))

    ax2.axhline(y=0, color='black', linewidth=0.8)
    ax2.axvline(x=0, color='black', linewidth=0.8)
    ax2.set_xlim(-0.5, 4)
    ax2.set_ylim(-1, 3)
    ax2.set_xlabel(r'$x$', fontsize=12)
    ax2.set_ylabel(r'$y$', fontsize=12)
    ax2.set_title(r'右侧逼近：$x \to 2^+$', fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper left')

    plt.suptitle(r'左右侧逼近：$lim_{x \to 2} f(x) = lim_{x \to 2^-} f(x) = lim_{x \to 2^+} f(x) = 1$',
                fontsize=14, fontweight='bold', y=1.05)
    plt.tight_layout()
    plt.savefig('../imgs/3.1_图2_左右逼近.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("已生成: 3.1_图2_左右逼近.png")


# ============ 图3: 极限存在与否的对比 ============
def draw_limit_existence():
    """展示极限存在与不存在的情况"""
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # 子图1: 极限存在
    ax1 = axes[0]
    x = np.linspace(0, 4, 200)
    y = x - 1
    y[abs(x - 2) < 0.01] = np.nan  # 在x=2处挖空
    ax1.plot(x, y, 'b-', linewidth=2)
    ax1.plot(2, 1, 'wo', markersize=15, markeredgecolor='red', markeredgewidth=3)
    ax1.axhline(y=1, color='green', linestyle='--', linewidth=1.5, alpha=0.7)
    ax1.text(3.5, 1.05, r'$lim_{x \to 2} f(x) = 1$', fontsize=11, color='green', fontweight='bold')
    ax1.set_title(r'极限存在', fontsize=13, fontweight='bold', color='green')
    ax1.set_xlim(0, 4)
    ax1.set_ylim(-1, 3)
    ax1.set_xlabel(r'$x$')
    ax1.set_ylabel(r'$y$')
    ax1.grid(True, alpha=0.3)

    # 子图2: 左右极限不相等
    ax2 = axes[1]
    x1 = np.linspace(0, 2, 100)
    x2 = np.linspace(2, 4, 100)
    y1 = x1 - 1
    y2 = x1  # 注意：这里用x1代替x2来保持数组形状
    # 创建分段函数：x<2时y=x-1, x>2时y=x
    x_piecewise = np.concatenate([x1, x2])
    y_piecewise = np.concatenate([y1, x2])
    y_piecewise[abs(x_piecewise - 2) < 0.01] = np.nan

    ax2.plot(x1, y1, 'b-', linewidth=2)
    ax2.plot(x2, x2, 'orange', linewidth=2)
    ax2.plot(2, 1, 'wo', markersize=12, markeredgecolor='blue', markeredgewidth=2)
    ax2.plot(2, 2, 'wo', markersize=12, markeredgecolor='orange', markeredgewidth=2)

    ax2.annotate(r'$lim_{x \to 2^-} f(x) = 1$', xy=(1.8, 0.8), xytext=(0.3, 2.3),
                fontsize=10, color='blue',
                arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))
    ax2.annotate(r'$lim_{x \to 2^+} f(x) = 2$', xy=(2.3, 2.3), xytext=(2.8, 2.8),
                fontsize=10, color='orange',
                arrowprops=dict(arrowstyle='->', color='orange', lw=1.5))

    ax2.set_title(r'极限不存在（左右不等）', fontsize=13, fontweight='bold', color='red')
    ax2.set_xlim(0, 4)
    ax2.set_ylim(-1, 4)
    ax2.set_xlabel(r'$x$')
    ax2.set_ylabel(r'$y$')
    ax2.grid(True, alpha=0.3)

    # 子图3: 函数值与极限值不同
    ax3 = axes[2]
    x = np.linspace(0, 4, 200)
    y = x - 1
    ax3.plot(x, y, 'b-', linewidth=2)
    ax3.plot(2, 1, 'wo', markersize=15, markeredgecolor='red', markeredgewidth=3)  # 极限值
    ax3.plot(2, 3, 'ro', markersize=12, zorder=5)  # 函数定义值

    ax3.axhline(y=1, color='green', linestyle='--', linewidth=1.5, alpha=0.7, label=r'极限值 = 1')
    ax3.plot(2, 3, 'ro', markersize=12, label=r'定义值 $f(2) = 3$')

    ax3.annotate(r'$lim_{x \to 2} f(x) = 1$', xy=(2, 1), xytext=(2.5, 0.5),
                fontsize=11, color='green', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='green', lw=1.5))
    ax3.annotate(r'$f(2) = 3$', xy=(2, 3), xytext=(2.8, 3.2),
                fontsize=11, color='red', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5))

    ax3.set_title(r'定义值 $\neq$ 极限值', fontsize=13, fontweight='bold', color='purple')
    ax3.set_xlim(0, 4)
    ax3.set_ylim(-1, 4)
    ax3.set_xlabel(r'$x$')
    ax3.set_ylabel(r'$y$')
    ax3.grid(True, alpha=0.3)
    ax3.legend(loc='upper left')

    plt.suptitle('极限的三种情况', fontsize=15, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('../imgs/3.1_图3_极限存在性.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("已生成: 3.1_图3_极限存在性.png")


# ============ 图4: 虚拟变量演示 ============
def draw_dummy_variable():
    """展示虚拟变量（哑变量）的概念"""
    fig, ax = plt.subplots(figsize=(12, 8))

    # 绘制坐标系
    ax.axhline(y=0, color='black', linewidth=1)
    ax.axvline(x=0, color='black', linewidth=1)

    # 创建一个示意性的框图说明变量可替换性
    # 框1
    box1 = FancyBboxPatch((0.5, 2), 2, 1.5, boxstyle="round,pad=0.05",
                          facecolor='lightblue', edgecolor='blue', linewidth=2)
    ax.add_patch(box1)
    ax.text(1.5, 2.75, r'$lim_{x \to 1} (x + t)$', fontsize=14, ha='center', va='center')

    # 框2
    box2 = FancyBboxPatch((3.5, 2), 2, 1.5, boxstyle="round,pad=0.05",
                          facecolor='lightgreen', edgecolor='green', linewidth=2)
    ax.add_patch(box2)
    ax.text(4.5, 2.75, r'$lim_{q \to 1} (q + t)$', fontsize=14, ha='center', va='center')

    # 框3
    box3 = FancyBboxPatch((6.5, 2), 2, 1.5, boxstyle="round,pad=0.05",
                          facecolor='lightyellow', edgecolor='orange', linewidth=2)
    ax.add_patch(box3)
    ax.text(7.5, 2.75, r'$lim_{b \to 1} (b + t)$', fontsize=14, ha='center', va='center')

    # 箭头和等号
    ax.annotate('', xy=(2.7, 2.75), xytext=(2.3, 2.75),
                arrowprops=dict(arrowstyle='->', color='gray', lw=2))
    ax.annotate('', xy=(6.3, 2.75), xytext=(5.7, 2.75),
                arrowprops=dict(arrowstyle='->', color='gray', lw=2))
    ax.text(3.2, 2.4, r'$= t + 1$', fontsize=12, ha='center', color='red', fontweight='bold')
    ax.text(6.2, 2.4, r'$= t + 1$', fontsize=12, ha='center', color='red', fontweight='bold')

    # 说明文字
    ax.text(4, 0.8,
           r'虚拟变量只起"占位"作用，' + '\n'
           r'可以换成任意符号！',
           fontsize=13, ha='center', va='center',
           bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', edgecolor='orange'))

    # 底部说明
    ax.text(4, -0.5,
           r'注意：极限结果 $1 + t$ 中，$t$ 不是虚拟变量，保留在结果中！',
           fontsize=11, ha='center', va='center',
           bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFCCCC', edgecolor='red'),
           color='red')

    ax.set_xlim(-0.5, 9.5)
    ax.set_ylim(-1.5, 4.5)
    ax.axis('off')
    ax.set_title(r'虚拟变量（哑变量）的可替换性：$lim_{x \to 1} (x + t) = lim_{q \to 1} (q + t) = 1 + t$',
               fontsize=14, fontweight='bold', pad=20)

    plt.tight_layout()
    plt.savefig('../imgs/3.1_图4_虚拟变量.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("已生成: 3.1_图4_虚拟变量.png")


# ============ 主程序 ============
if __name__ == '__main__':
    print("开始生成 3.1 极限：基本思想 配图...")
    print("=" * 50)

    draw_function_with_hole()
    draw_x_approaching()
    draw_limit_existence()
    draw_dummy_variable()

    print("=" * 50)
    print("所有配图生成完成！")
    print("图片文件位于 ../imgs/ 目录下")
