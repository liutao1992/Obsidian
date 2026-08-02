#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2.2 扩展三角函数定义域配图
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, Wedge
from matplotlib.font_manager import FontProperties
import os

# 使用系统字体文件的绝对路径
FONT_FILE = '/System/Library/Fonts/Hiragino Sans GB.ttc'

# 创建字体对象
zh_font = FontProperties(FONT_FILE)
print(f"Using font: {FONT_FILE}")

plt.rcParams['axes.unicode_minus'] = False


def text(ax, x, y, s, **kwargs):
    """Helper function to draw text with Chinese font"""
    ax.text(x, y, s, fontproperties=zh_font, **kwargs)


# ============ 图1: 四个象限坐标系 ============
def draw_four_quadrants():
    """四象限坐标系，标注关键角度"""
    fig, ax = plt.subplots(figsize=(10, 10))

    ax.plot([-1.8, 1.8], [0, 0], 'k-', linewidth=2)
    ax.plot([0, 0], [-1.8, 1.8], 'k-', linewidth=2)

    for start, end, color in [(0, 90, 'red'), (90, 180, 'orange'), (180, 270, 'green'), (270, 360, 'blue')]:
        wedge = Wedge((0, 0), 1.5, start, end, alpha=0.15, color=color)
        ax.add_patch(wedge)

    for x, y, num, color in [(0.8, 0.8, 'I', 'darkred'), (-0.8, 0.8, 'II', 'darkorange'),
                               (-0.8, -0.8, 'III', 'darkgreen'), (0.8, -0.8, 'IV', 'darkblue')]:
        ax.text(x, y, num, fontsize=24, fontweight='bold', color=color, ha='center', va='center')

    for x, y, sign in [(1.0, 1.0, '(+,+)'), (-1.0, 1.0, '(-,+)'),
                        (-1.0, -1.0, '(-,-)'), (1.0, -1.0, '(+,-)')]:
        ax.text(x, y, sign, fontsize=12, color='gray', ha='center', va='center')

    circle = Circle((0, 0), 1, fill=False, color='black', linewidth=2)
    ax.add_patch(circle)

    for angle_deg, label_pos, label_text in [
        (0, (1.15, 0.1), '0=360\n(2π)'),
        (90, (0.1, 1.15), 'π/2\n(90°)'),
        (180, (-1.15, 0.1), 'π\n(180°)'),
        (270, (0.1, -1.15), '3π/2\n(270°)')
    ]:
        px, py = np.cos(np.radians(angle_deg)), np.sin(np.radians(angle_deg))
        ax.plot([0, px * 1.1], [0, py * 1.1], 'b-', linewidth=2, alpha=0.7)
        ax.plot(px, py, 'ro', markersize=10)
        text(ax, label_pos[0], label_pos[1], label_text, fontsize=10, ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', edgecolor='orange', alpha=0.9))

    ax.text(1.7, 0, 'x', fontsize=14, fontweight='bold')
    ax.text(0, 1.7, 'y', fontsize=14, fontweight='bold')

    arc = Arc((0, 0), 0.6, 0.6, angle=0, theta1=10, theta2=80, color='purple', linewidth=2)
    ax.add_patch(arc)
    text(ax, 0.35, 0.35, '逆时针', fontsize=10, color='purple', ha='center', va='center')

    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-1.8, 1.8)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('四象限坐标系', fontsize=16, fontweight='bold', pad=20, fontproperties=zh_font)

    plt.tight_layout()
    plt.savefig('../imgs/2.2_图1_四象限.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("已生成: 2.2_图1_四象限.png")


# ============ 图2: 旋转与射线 ============
def draw_rotation_ray():
    """人在原点旋转、沿射线行走"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 14))

    titles = ['步骤1: 站在原点, 面向+x轴',
              '步骤2: 旋转π/2, 面向+y轴',
              '步骤3: 旋转π, 面向-x轴',
              '步骤4: 旋转3π/2, 面向-y轴']

    for idx, ax in enumerate(axes.flat):
        ax.plot([-1.5, 1.5], [0, 0], 'k-', linewidth=1.5)
        ax.plot([0, 0], [-1.5, 1.5], 'k-', linewidth=1.5)

        circle = Circle((0, 0.6), 0.15, fill=True, color='orange', ec='black', linewidth=1.5)
        ax.add_patch(circle)
        ax.plot([0, 0], [0.45, 0.1], 'k-', linewidth=2)

        dirs = [(0.5, 0.5), (0, 0.7), (-0.5, 0.5), (0, -0.7)]
        ax.annotate('', xy=dirs[idx], xytext=(0.15, 0.5),
                    arrowprops=dict(arrowstyle='->', color='red', lw=2))

        if idx == 1:
            ax.plot([0, 0], [0, 1.3], 'g--', linewidth=2, alpha=0.7)
            text(ax, 0.15, 0.8, '射线', fontsize=10, color='green')
        elif idx == 2:
            ax.plot([0, -1.3], [0, 0], 'g--', linewidth=2, alpha=0.7)
            text(ax, -0.7, 0.1, '射线', fontsize=10, color='green')
        elif idx == 3:
            ax.plot([0, 0], [0, -1.3], 'g--', linewidth=2, alpha=0.7)
            text(ax, 0.15, -0.8, '射线', fontsize=10, color='green')

        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(titles[idx], fontsize=13, fontweight='bold', fontproperties=zh_font)

    plt.suptitle('旋转的物理意义: 站在原点, 转身, 沿直线走', fontsize=16, fontweight='bold', y=1.02, fontproperties=zh_font)
    plt.tight_layout()
    plt.savefig('../imgs/2.2_图2_旋转射线.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("已生成: 2.2_图2_旋转射线.png")


# ============ 图3: 任意角三角函数定义 ============
def draw_any_angle_trig():
    """第三象限例子: x,y可正可负, 但r恒正"""
    fig, ax = plt.subplots(figsize=(12, 10))

    ax.plot([-2.5, 2.5], [0, 0], 'k-', linewidth=1.5)
    ax.plot([0, 0], [-2.5, 2.5], 'k-', linewidth=1.5)

    wedge = Wedge((0, 0), 2, 180, 270, alpha=0.2, color='green')
    ax.add_patch(wedge)

    theta = np.linspace(np.pi, 3*np.pi/2, 50)
    ax.plot(np.cos(theta), np.sin(theta), 'b-', linewidth=2, alpha=0.5)

    angle_deg, angle_rad, r = 225, np.radians(225), 1.5
    x_pt, y_pt = r * np.cos(angle_rad), r * np.sin(angle_rad)

    ax.plot([0, x_pt * 1.1], [0, y_pt * 1.1], 'r-', linewidth=2.5,
           label=f'射线: θ={angle_deg}° ({angle_rad:.2f}π rad)')

    ax.plot([x_pt, x_pt], [0, y_pt], 'b--', linewidth=1.5, alpha=0.8)
    ax.plot([0, x_pt], [0, 0], 'k-', linewidth=1)

    ax.plot(x_pt, y_pt, 'ko', markersize=10)
    ax.plot(x_pt, 0, 'bo', markersize=8)

    ax.annotate('', xy=(x_pt, 0.15), xytext=(0, 0.15),
               arrowprops=dict(arrowstyle='<->', color='blue', lw=1.5))
    ax.text(x_pt/2, 0.25, f'x={x_pt:.2f}', fontsize=12, ha='center', color='blue', fontweight='bold')

    ax.annotate('', xy=(-0.15, y_pt), xytext=(-0.15, 0),
               arrowprops=dict(arrowstyle='<->', color='red', lw=1.5))
    ax.text(x_pt - 0.35, y_pt/2, f'y={y_pt:.2f}', fontsize=12, va='center', color='red', fontweight='bold')

    ax.annotate('', xy=(x_pt * 0.9, y_pt * 0.9), xytext=(0.2, 0.2),
               arrowprops=dict(arrowstyle='<->', color='green', lw=1.5))
    ax.text(0.5, 0.5, f'r={r}', fontsize=12, color='green', fontweight='bold')

    arc = Arc((0, 0), 0.5, 0.5, angle=0, theta1=180, theta2=225, color='purple', linewidth=2)
    ax.add_patch(arc)
    text(ax, -0.45, -0.25, f'θ={angle_deg}°', fontsize=11, color='purple', fontweight='bold')

    formula = (f"三角函数定义 (第三象限角 θ={angle_deg}°):\n\n"
              f"sin θ = y/r = {y_pt:.2f}/{r} = {y_pt/r:.2f}\n"
              f"cos θ = x/r = {x_pt:.2f}/{r} = {x_pt/r:.2f}\n"
              f"tan θ = y/x = {y_pt/x_pt:.2f}\n\n"
              f"注意: x<0, y<0 (第三象限)\n"
              f"但 r>0 恒成立 (距离)")
    ax.text(1.5, -1.5, formula, fontsize=11, va='top', ha='left',
           bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', edgecolor='orange', alpha=0.9),
           family='monospace')

    ax.text(-1.8, -1.8, 'III', fontsize=20, fontweight='bold', color='darkgreen', alpha=0.5)
    ax.text(2.3, 0, 'x', fontsize=14, fontweight='bold')
    ax.text(0, 2.3, 'y', fontsize=14, fontweight='bold')

    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('任意角三角函数定义: 以第三象限为例', fontsize=16, fontweight='bold', pad=20, fontproperties=zh_font)

    plt.tight_layout()
    plt.savefig('../imgs/2.2_图3_任意角定义.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("已生成: 2.2_图3_任意角定义.png")


# ============ 图4: 单位圆三角函数 ============
def draw_unit_circle_trig():
    """单位圆上: P(cosθ, sinθ), sin=竖直距离, cos=水平距离"""
    fig, ax = plt.subplots(figsize=(12, 12))

    ax.plot([-1.8, 1.8], [0, 0], 'k-', linewidth=1.5)
    ax.plot([0, 0], [-1.8, 1.8], 'k-', linewidth=1.5)

    circle = Circle((0, 0), 1, fill=False, color='black', linewidth=2.5)
    ax.add_patch(circle)

    angles = [(30, 'red'), (150, 'blue'), (210, 'green'), (330, 'purple')]
    qnames = {30: '一', 150: '二', 210: '三', 330: '四'}

    for angle_deg, color in angles:
        angle_rad = np.radians(angle_deg)
        x, y = np.cos(angle_rad), np.sin(angle_rad)

        ax.plot([0, x], [0, y], '-', color=color, linewidth=2, alpha=0.8)
        ax.plot([x, x], [0, y], '--', color=color, linewidth=1.5, alpha=0.6)
        ax.plot(x, y, 'o', color=color, markersize=12)
        ax.plot(x, 0, 's', color=color, markersize=8, alpha=0.6)

        text(ax, x * 1.15, y * 1.15, f'{angle_deg}°\n(第{qnames[angle_deg]}象限)',
             fontsize=10, ha='center', color=color, fontweight='bold')

        ax.text(-1.5, y + 0.05 if y > 0 else y - 0.1, f'sin={y:.2f}',
               fontsize=9, ha='right', va='center' if abs(y) > 0.1 else 'center',
               color=color, alpha=0.8)
        ax.text(x + 0.05, -1.5, f'cos={x:.2f}',
               fontsize=9, ha='center', va='top', color=color, alpha=0.8)

    ax.text(1.6, 0.1, 'x', fontsize=14, fontweight='bold')
    ax.text(0.1, 1.6, 'y', fontsize=14, fontweight='bold')
    text(ax, 0.3, -1.4, '(cosθ, sinθ) 在单位圆上',
         fontsize=12,
         bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', edgecolor='orange'),
         ha='center')
    ax.text(1.02, 0.02, '1', fontsize=12, va='bottom', color='gray')

    legend = ("在单位圆上 (r=1):\n"
             "- 点 P(cosθ, sinθ)\n"
             "- sinθ = 竖直距离\n"
             "- cosθ = 水平距离\n"
             "- tanθ = y/x (x≠0)")
    ax.text(-1.6, 1.5, legend, fontsize=11, va='top', ha='left',
           bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='gray', alpha=0.9))

    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-1.8, 1.8)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('单位圆上的三角函数几何意义', fontsize=18, fontweight='bold', pad=20, fontproperties=zh_font)

    plt.tight_layout()
    plt.savefig('../imgs/2.2_图4_单位圆三角函数.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("已生成: 2.2_图4_单位圆三角函数.png")


# ============ 图5: 象限符号 ============
def draw_trig_signs_quadrants():
    """四个象限中 sin, cos, tan 的正负"""
    fig, ax = plt.subplots(figsize=(12, 12))

    ax.plot([-2.5, 2.5], [0, 0], 'k-', linewidth=2)
    ax.plot([0, 0], [-2.5, 2.5], 'k-', linewidth=2)

    for start, end, color in [(0, 90, 'red'), (90, 180, 'orange'), (180, 270, 'green'), (270, 360, 'blue')]:
        wedge = Wedge((0, 0), 2, start, end, alpha=0.15, color=color)
        ax.add_patch(wedge)

    quadrant_data = [
        (1.0, 1.0, 'I', 'sin (+)\ncos (+)\ntan (+)', 'red'),
        (-1.0, 1.0, 'II', 'sin (+)\ncos (-)\ntan (-)', 'orange'),
        (-1.0, -1.0, 'III', 'sin (-)\ncos (-)\ntan (+)', 'green'),
        (1.0, -1.0, 'IV', 'sin (-)\ncos (+)\ntan (-)', 'blue'),
    ]

    for x, y, name, signs, color in quadrant_data:
        ax.text(x, y + 0.4, name, fontsize=20, fontweight='bold',
               ha='center', va='center', color=color)
        ax.text(x, y - 0.3, signs, fontsize=12,
               ha='center', va='center', color='black',
               bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=color, alpha=0.8))

    ax.text(2.3, 0.1, 'x', fontsize=14, fontweight='bold')
    ax.text(0.1, 2.3, 'y', fontsize=14, fontweight='bold')

    ax.text(0, -2.2,
           '记忆口诀:\n'
           '"一全正, 二正弦,\n'
           '三正切, 四余弦"\n'
           '(描述各象限为正的函数)',
           fontsize=11, ha='center', va='top', fontproperties=zh_font,
           bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', edgecolor='orange'))

    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('四个象限中三角函数值的正负', fontsize=18, fontweight='bold', pad=20, fontproperties=zh_font)

    plt.tight_layout()
    plt.savefig('../imgs/2.2_图5_象限符号.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("已生成: 2.2_图5_象限符号.png")


# ============ Main ============
if __name__ == '__main__':
    print("开始生成 2.2 扩展三角函数定义域配图...")
    print("=" * 50)

    draw_four_quadrants()
    draw_rotation_ray()
    draw_any_angle_trig()
    draw_unit_circle_trig()
    draw_trig_signs_quadrants()

    print("=" * 50)
    print("所有配图生成完成!")
