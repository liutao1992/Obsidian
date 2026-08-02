#!/usr/bin/env python3
"""
绘制反函数相关图像
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # 非交互式后端

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def plot_horizontal_line_test():
    """水平线检验对比图：x^2 (无反函数) vs x^3 (有反函数)"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    x = np.linspace(-3, 3, 500)

    # 图1: y = x^2 (无反函数)
    ax1 = axes[0]
    y1 = x**2
    ax1.plot(x, y1, 'b-', linewidth=2, label=r'$f(x) = x^2$')
    ax1.axhline(y=4, color='red', linestyle='--', linewidth=2, label=r'$y = 4$')
    ax1.axhline(y=1, color='orange', linestyle='--', linewidth=2, label=r'$y = 1$')

    # 标注交点
    ax1.plot([-2, 2], [4, 4], 'ro', markersize=10)
    ax1.plot([-1, 1], [1, 1], 'o', color='orange', markersize=10)

    ax1.annotate(r'$(-2, 4)$', xy=(-2, 4), xytext=(-2.5, 4.5), fontsize=12)
    ax1.annotate(r'$(2, 4)$', xy=(2, 4), xytext=(2.1, 4.5), fontsize=12)

    ax1.set_xlim(-3, 3)
    ax1.set_ylim(-1, 10)
    ax1.set_xlabel('x', fontsize=12)
    ax1.set_ylabel('y', fontsize=12)
    ax1.set_title(r'水平线检验：$f(x) = x^2$ (无反函数)', fontsize=14, color='red')
    ax1.legend(loc='upper right')
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=0, color='black', linewidth=0.5)
    ax1.axvline(x=0, color='black', linewidth=0.5)

    # 图2: y = x^3 (有反函数)
    ax2 = axes[1]
    y2 = x**3
    ax2.plot(x, y2, 'b-', linewidth=2, label=r'$f(x) = x^3$')
    ax2.axhline(y=8, color='red', linestyle='--', linewidth=2, label=r'$y = 8$')
    ax2.axhline(y=1, color='orange', linestyle='--', linewidth=2, label=r'$y = 1$')

    # 标注交点
    ax2.plot([2], [8], 'ro', markersize=10)
    ax2.plot([1], [1], 'o', color='orange', markersize=10)

    ax2.annotate(r'$(2, 8)$', xy=(2, 8), xytext=(2.1, 8.3), fontsize=12)
    ax2.annotate(r'$(1, 1)$', xy=(1, 1), xytext=(1.1, 1.3), fontsize=12)

    ax2.set_xlim(-3, 3)
    ax2.set_ylim(-10, 10)
    ax2.set_xlabel('x', fontsize=12)
    ax2.set_ylabel('y', fontsize=12)
    ax2.set_title(r'水平线检验：$f(x) = x^3$ (有反函数)', fontsize=14, color='green')
    ax2.legend(loc='lower right')
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=0, color='black', linewidth=0.5)
    ax2.axvline(x=0, color='black', linewidth=0.5)

    plt.tight_layout()
    plt.savefig('/Users/liutao/Documents/Obsidian/微积分/imgs/horizontal_line_test.png', dpi=150, bbox_inches='tight')
    print("已保存: imgs/horizontal_line_test.png")
    plt.close()


def plot_restricted_domain():
    """限制定义域使函数有反函数"""
    fig, ax = plt.subplots(figsize=(10, 8))

    x = np.linspace(-3, 3, 500)

    # 完整的抛物线（灰色虚线）
    ax.plot(x, x**2, 'gray', linewidth=1, linestyle='--', alpha=0.5, label=r'$f(x) = x^2$ (完整)')

    # 限制定义域 x >= 0
    x_pos = np.linspace(0, 3, 500)
    y_pos = x_pos**2
    ax.plot(x_pos, y_pos, 'b-', linewidth=2.5, label=r'$f(x) = x^2, x \geq 0$')

    # 水平线检验
    ax.axhline(y=4, color='red', linestyle='--', linewidth=2, label=r'$y = 4$')
    ax.axhline(y=1, color='orange', linestyle='--', linewidth=2, label=r'$y = 1$')

    # 交点
    ax.plot([0, 2], [4, 4], 'ro', markersize=10)
    ax.plot([0, 1], [1, 1], 'o', color='orange', markersize=10)

    # 标注
    ax.annotate(r'$(2, 4)$', xy=(2, 4), xytext=(2.2, 4.3), fontsize=12)
    ax.annotate(r'$(1, 1)$', xy=(1, 1), xytext=(1.2, 1.3), fontsize=12)
    ax.annotate(r'$(0, 0)$', xy=(0, 0), xytext=(0.1, 0.3), fontsize=12)

    # 箭头说明
    ax.annotate('', xy=(1.8, 4), xytext=(0.5, 4),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(0.6, 4.3, '唯一交点!', fontsize=11, color='red')

    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 10)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title(r'限制定义域：$f(x) = x^2, x \geq 0$ (有反函数)', fontsize=14)
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='black', linewidth=0.5)
    ax.axvline(x=0, color='black', linewidth=0.5)

    plt.tight_layout()
    plt.savefig('/Users/liutao/Documents/Obsidian/微积分/imgs/restricted_domain.png', dpi=150, bbox_inches='tight')
    print("已保存: imgs/restricted_domain.png")
    plt.close()


def plot_inverse_symmetry():
    """原函数与反函数的图像对称性"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    x = np.linspace(-3, 3, 500)

    # 图1: y = 2x 及其反函数
    ax1 = axes[0]
    y1 = 2 * x
    y1_inv = 0.5 * x

    ax1.plot(x, y1, 'b-', linewidth=2, label=r'$f(x) = 2x$')
    ax1.plot(x, y1_inv, 'r-', linewidth=2, label=r'$f^{-1}(x) = \frac{1}{2}x$')
    ax1.plot(x, x, 'g--', linewidth=1.5, label=r'$y = x$ (对称轴)')

    # 示例点
    ax1.plot([1], [2], 'bo', markersize=10)
    ax1.plot([2], [1], 'ro', markersize=10)
    ax1.annotate(r'$(1, 2)$ on $f$', xy=(1, 2), xytext=(1.2, 2.3), fontsize=11)
    ax1.annotate(r'$(2, 1)$ on $f^{-1}$', xy=(2, 1), xytext=(2.2, 1.3), fontsize=11)

    ax1.set_xlim(-1, 4)
    ax1.set_ylim(-1, 4)
    ax1.set_xlabel('x', fontsize=12)
    ax1.set_ylabel('y', fontsize=12)
    ax1.set_title(r'$f(x) = 2x$ 与 $f^{-1}(x) = \frac{1}{2}x$', fontsize=14)
    ax1.legend(loc='upper right')
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=0, color='black', linewidth=0.5)
    ax1.axvline(x=0, color='black', linewidth=0.5)
    ax1.set_aspect('equal')

    # 图2: y = x^3 及其反函数
    ax2 = axes[1]
    y2 = x**3
    y2_inv = np.sign(x) * np.abs(x)**(1/3)  # 立方根

    ax2.plot(x, y2, 'b-', linewidth=2, label=r'$f(x) = x^3$')
    ax2.plot(x, y2_inv, 'r-', linewidth=2, label=r'$f^{-1}(x) = \sqrt[3]{x}$')
    ax2.plot(x, x, 'g--', linewidth=1.5, label=r'$y = x$ (对称轴)')

    # 示例点
    ax2.plot([2], [8], 'bo', markersize=10)
    ax2.plot([8], [2], 'ro', markersize=10)
    ax2.annotate(r'$(2, 8)$ on $f$', xy=(2, 8), xytext=(0.5, 9), fontsize=11)
    ax2.annotate(r'$(8, 2)$ on $f^{-1}$', xy=(8, 2), xytext=(8.2, 2.3), fontsize=11)

    ax2.set_xlim(-4, 4)
    ax2.set_ylim(-4, 4)
    ax2.set_xlabel('x', fontsize=12)
    ax2.set_ylabel('y', fontsize=12)
    ax2.set_title(r'$f(x) = x^3$ 与 $f^{-1}(x) = \sqrt[3]{x}$', fontsize=14)
    ax2.legend(loc='upper right')
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=0, color='black', linewidth=0.5)
    ax2.axvline(x=0, color='black', linewidth=0.5)
    ax2.set_aspect('equal')

    plt.tight_layout()
    plt.savefig('/Users/liutao/Documents/Obsidian/微积分/imgs/inverse_symmetry.png', dpi=150, bbox_inches='tight')
    print("已保存: imgs/inverse_symmetry.png")
    plt.close()


if __name__ == '__main__':
    import os
    os.makedirs('/Users/liutao/Documents/Obsidian/微积分/第一章函数图像和直线/imgs', exist_ok=True)

    plot_horizontal_line_test()
    plot_restricted_domain()
    plot_inverse_symmetry()
    print("\n所有图像生成完成!")
