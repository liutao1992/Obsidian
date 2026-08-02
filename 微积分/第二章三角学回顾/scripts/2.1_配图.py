#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
三角函数基础知识配图
使用 matplotlib 绘制精美的插图
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Arc, FancyBboxPatch
import matplotlib.lines as mlines

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'STHeiti']
plt.rcParams['axes.unicode_minus'] = False

# ============ 图1: 单位圆弧度图 ============
def draw_unit_circle_radians():
    """绘制单位圆弧度图"""
    fig, ax = plt.subplots(figsize=(10, 10))

    # 绘制单位圆
    circle = plt.Circle((0, 0), 1, fill=False, color='black', linewidth=2)
    ax.add_patch(circle)

    # 绘制坐标轴
    ax.axhline(y=0, color='gray', linewidth=0.5)
    ax.axvline(x=0, color='gray', linewidth=0.5)
    ax.plot([-1.5, 1.5], [0, 0], 'k-', linewidth=1)
    ax.plot([0, 0], [-1.5, 1.5], 'k-', linewidth=1)

    # 标注关键点和角度
    angles_deg = [0, 30, 45, 60, 90, 120, 180, 270, 360]
    angles_rad = [np.radians(a) for a in angles_deg]
    labels = ['0°\n(0)', '30°\n(π/6)', '45°\n(π/4)', '60°\n(π/3)',
              '90°\n(π/2)', '120°\n(2π/3)', '180°\n(π)', '270°\n(3π/2)', '360°\n(2π)']

    for angle_rad, angle_deg, label in zip(angles_rad, angles_deg, labels):
        x = np.cos(angle_rad)
        y = np.sin(angle_rad)
        # 绘制角度线和点
        if angle_deg in [0, 90, 180, 270, 360]:
            ax.plot([0, x], [0, y], 'b-', linewidth=1.5, alpha=0.7)
        ax.plot(x, y, 'ro', markersize=8)
        # 标注位置（避开重叠）
        if angle_deg == 0:
            ax.text(x + 0.1, y - 0.15, label, ha='left', va='top', fontsize=10)
        elif angle_deg == 90:
            ax.text(x + 0.05, y + 0.1, label, ha='left', va='bottom', fontsize=10)
        elif angle_deg == 180:
            ax.text(x - 0.1, y - 0.15, label, ha='right', va='top', fontsize=10)
        elif angle_deg == 270:
            ax.text(x - 0.15, y - 0.1, label, ha='right', va='top', fontsize=10)
        elif angle_deg == 360:
            ax.text(x + 0.1, y + 0.1, label, ha='left', va='bottom', fontsize=10)
        else:
            # 内圈标注
            text_x = x * 0.65
            text_y = y * 0.65
            ax.text(text_x, text_y, label, ha='center', va='center', fontsize=9,
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', edgecolor='orange', alpha=0.8))

    # 标注坐标轴
    ax.text(1.1, 0, 'x', fontsize=12, fontweight='bold')
    ax.text(0, 1.1, 'y', fontsize=12, fontweight='bold')
    ax.text(1, 0, '1', fontsize=10, ha='left', va='bottom')

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('单位圆与弧度制', fontsize=16, fontweight='bold', pad=20)

    plt.tight_layout()
    plt.savefig('../imgs/2.1_图1_单位圆弧度图.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("已生成: 2.1_图1_单位圆弧度图.png")


# ============ 图2: 直角三角形三角函数定义 ============
def draw_trig_definitions():
    """绘制三角函数定义的直角三角形"""
    fig, ax = plt.subplots(figsize=(8, 8))

    # 30-60-90 三角形
    # 边长比例: 短边=1, 长边=√3, 斜边=2
    scale = 2
    A = (0, 0)
    B = (scale * np.sqrt(3), 0)  # 长边在x轴
    C = (0, scale)  # 短边在y轴

    # 绘制三角形
    triangle = plt.Polygon([A, B, C], fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(triangle)

    # 标注顶点
    ax.text(A[0] - 0.2, A[1] - 0.2, 'A', fontsize=14, fontweight='bold')
    ax.text(B[0] + 0.1, B[1] - 0.2, 'B', fontsize=14, fontweight='bold')
    ax.text(C[0] - 0.2, C[1] + 0.1, 'C', fontsize=14, fontweight='bold')

    # 标注边长
    ax.text((A[0] + B[0]) / 2, A[1] - 0.3, f'√3', fontsize=12, ha='center')
    ax.text(A[0] - 0.4, (A[1] + C[1]) / 2, f'1', fontsize=12, va='center')
    ax.text((B[0] + C[0]) / 2 + 0.2, (B[1] + C[1]) / 2 - 0.1, f'2', fontsize=12)

    # 标注直角
    ax.text(A[0] + 0.15, A[1] + 0.1, '90°', fontsize=10)

    # 标注角度
    # 在B点的角度 (60度)
    angle_b = np.arctan(C[1] / B[0])
    ax.text(B[0] - 0.5, B[1] - 0.3, '60°', fontsize=12, ha='center')

    # 在C点的角度 (30度)
    angle_c = np.arctan(B[0] / C[1])
    ax.text(C[0] - 0.4, C[1] - 0.2, '30°', fontsize=12, ha='center')

    # 标注对边、邻边、斜边
    # 对边(opposite) = AC, 邻边(adjacent) = AB, 斜边(hypotenuse) = BC
    ax.text((A[0] + C[0]) / 2 - 0.4, (A[1] + C[1]) / 2 + 0.1, '对边\n(Opposite)', fontsize=10, ha='center', color='red')
    ax.text((A[0] + B[0]) / 2, (A[1] + B[1]) / 2 + 0.15, '邻边\n(Adjacent)', fontsize=10, ha='center', color='blue')
    mid_bc = ((B[0] + C[0]) / 2, (B[1] + C[1]) / 2)
    ax.text(mid_bc[0] + 0.3, mid_bc[1] + 0.2, '斜边\n(Hypotenuse)', fontsize=10, ha='left', color='green')

    # 标注θ角位置
    theta_x = C[0] + 0.3
    theta_y = C[1] - 0.3
    ax.text(theta_x, theta_y, 'θ', fontsize=14, fontweight='bold')

    ax.set_xlim(-1, 4.5)
    ax.set_ylim(-0.5, 3)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('直角三角形三角函数定义', fontsize=16, fontweight='bold', pad=20)

    # 添加公式说明
    formula_text = """
    sin(θ) = 对边 / 斜边 = 1 / 2 = 1/2
    cos(θ) = 邻边 / 斜边 = √3 / 2 = √3/2
    tan(θ) = 对边 / 邻边 = 1 / √3 = √3/3
    """
    ax.text(3.5, 2, formula_text, fontsize=10, va='top', ha='left',
           bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', edgecolor='orange'))

    plt.tight_layout()
    plt.savefig('../imgs/2.1_图2_三角函数定义.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("已生成: 2.1_图2_三角函数定义.png")


# ============ 图3: 特殊三角形边长比例 ============
def draw_special_triangles():
    """绘制 30-60-90 和 45-45-90 特殊三角形"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # 30-60-90 三角形
    ax1 = axes[0]
    scale = 2
    A1 = (0, 0)
    B1 = (scale * np.sqrt(3), 0)
    C1 = (0, scale)

    triangle1 = plt.Polygon([A1, B1, C1], fill=False, edgecolor='black', linewidth=2)
    ax1.add_patch(triangle1)

    # 顶点标注
    ax1.text(A1[0] - 0.2, A1[1] - 0.2, 'A', fontsize=14, fontweight='bold')
    ax1.text(B1[0] + 0.1, B1[1] - 0.2, 'B', fontsize=14, fontweight='bold')
    ax1.text(C1[0] - 0.2, C1[1] + 0.1, 'C', fontsize=14, fontweight='bold')

    # 边长标注
    ax1.text((A1[0] + B1[0]) / 2, A1[1] - 0.25, '√3', fontsize=12, ha='center')
    ax1.text(A1[0] - 0.3, (A1[1] + C1[1]) / 2, '1', fontsize=12, va='center')
    ax1.text((B1[0] + C1[0]) / 2 + 0.15, (B1[1] + C1[1]) / 2 - 0.1, '2', fontsize=12)

    # 角度标注
    ax1.text(B1[0] - 0.6, B1[1] - 0.25, '60°', fontsize=12, ha='center')
    ax1.text(C1[0] - 0.35, C1[1] - 0.25, '30°', fontsize=12, ha='center')
    ax1.text(A1[0] + 0.15, A1[1] + 0.1, '90°', fontsize=10)

    ax1.set_xlim(-1, 4.5)
    ax1.set_ylim(-0.5, 3)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('30°-60°-90° 三角形\n边长比例: 1 : √3 : 2', fontsize=14, fontweight='bold')

    # 45-45-90 三角形
    ax2 = axes[1]
    scale = 2
    A2 = (0, 0)
    B2 = (scale, 0)
    C2 = (0, scale)

    triangle2 = plt.Polygon([A2, B2, C2], fill=False, edgecolor='black', linewidth=2)
    ax2.add_patch(triangle2)

    # 顶点标注
    ax2.text(A2[0] - 0.2, A2[1] - 0.2, 'A', fontsize=14, fontweight='bold')
    ax2.text(B2[0] + 0.1, B2[1] - 0.2, 'B', fontsize=14, fontweight='bold')
    ax2.text(C2[0] - 0.2, C2[1] + 0.1, 'C', fontsize=14, fontweight='bold')

    # 边长标注
    ax2.text((A2[0] + B2[0]) / 2, A2[1] - 0.25, '1', fontsize=12, ha='center')
    ax2.text(A2[0] - 0.3, (A2[1] + C2[1]) / 2, '1', fontsize=12, va='center')
    ax2.text((B2[0] + C2[0]) / 2 + 0.15, (B2[1] + C2[1]) / 2 - 0.1, '√2', fontsize=12)

    # 角度标注
    ax2.text(B2[0] - 0.35, B2[1] - 0.25, '45°', fontsize=12, ha='center')
    ax2.text(C2[0] - 0.35, C2[1] - 0.25, '45°', fontsize=12, ha='center')
    ax2.text(A2[0] + 0.15, A2[1] + 0.1, '90°', fontsize=10)

    ax2.set_xlim(-1, 3.5)
    ax2.set_ylim(-0.5, 3)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('45°-45°-90° 三角形\n边长比例: 1 : 1 : √2', fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig('../imgs/2.1_图3_特殊三角形.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("已生成: 2.1_图3_特殊三角形.png")


# ============ 图4: 三角函数值可视化 ============
def draw_trig_values_unit_circle():
    """在单位圆上可视化三角函数值"""
    fig, ax = plt.subplots(figsize=(10, 10))

    # 绘制单位圆
    circle = plt.Circle((0, 0), 1, fill=False, color='black', linewidth=2)
    ax.add_patch(circle)

    # 绘制坐标轴
    ax.plot([-1.6, 1.6], [0, 0], 'k-', linewidth=1)
    ax.plot([0, 0], [-1.6, 1.6], 'k-', linewidth=1)

    # 常见角度
    angles = [0, 30, 45, 60, 90]
    angles_rad = [np.radians(a) for a in angles]
    colors = ['purple', 'blue', 'green', 'orange', 'red']

    for angle_deg, angle_rad, color in zip(angles, angles_rad, colors):
        x = np.cos(angle_rad)
        y = np.sin(angle_rad)

        # 绘制角度线
        ax.plot([0, x], [0, y], color=color, linewidth=2, alpha=0.7)

        # 绘制点
        ax.plot(x, y, 'o', color=color, markersize=10)

        # 标注 sin 和 cos 值
        # 正弦值 (y坐标)
        ax.plot([x, x], [0, y], '--', color=color, linewidth=1.5, alpha=0.5)
        sin_val = y
        cos_val = x

        # 在坐标轴上标注值
        if angle_deg == 0:
            ax.text(0.05, y, f'sin={sin_val:.2f}', fontsize=10, va='center', color=color)
            ax.text(x, -0.15, f'cos={cos_val:.2f}', fontsize=10, ha='center', color=color)
        elif angle_deg == 90:
            ax.text(x + 0.05, y/2, f'sin={sin_val:.2f}', fontsize=10, va='center', color=color)
            ax.text(x - 0.2, -0.05, f'cos={cos_val:.2f}', fontsize=10, ha='center', color=color)
        else:
            # 为每个角度设置不同的垂直偏移，避免重叠
            cos_offsets = {30: -1.35, 45: -1.5, 60: -1.65}
            sin_offsets = {30: 0.7, 45: 0.9, 60: 1.1}

            # sin 标注在 y 轴附近
            ax.text(-1.4, sin_offsets.get(angle_deg, y), f'sin {angle_deg}°={sin_val:.2f}', fontsize=10, va='center', ha='left', color=color)
            # cos 标注在 x 轴附近
            ax.text(x, cos_offsets.get(angle_deg, -1.4), f'cos {angle_deg}°={cos_val:.2f}', fontsize=10, ha='center', color=color)

    # 标注关键点
    ax.text(1.3, 0, 'x', fontsize=12, fontweight='bold')
    ax.text(0, 1.3, 'sin θ', fontsize=12, fontweight='bold')
    ax.text(0, -1.3, 'cos θ', fontsize=12, fontweight='bold')

    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.6, 1.6)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('单位圆上的三角函数值', fontsize=16, fontweight='bold', pad=20)

    plt.tight_layout()
    plt.savefig('../imgs/2.1_图4_三角函数值.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("已生成: 2.1_图4_三角函数值.png")


# ============ 图5: tan 90度无定义说明 ============
def draw_tan_asymptote():
    """说明 tan 90° 无定义的原因"""
    fig, ax = plt.subplots(figsize=(12, 6))

    x = np.linspace(-np.pi/2 + 0.1, np.pi/2 - 0.1, 1000)
    y = np.tan(x)

    # 绘制 tan 图像
    ax.plot(np.degrees(x), y, 'b-', linewidth=2, label='tan θ')

    # 绘制渐近线
    ax.axvline(x=90, color='red', linestyle='--', linewidth=2, label='θ = 90° (渐近线)')

    # 标注关键点
    ax.plot(0, 0, 'bo', markersize=8)
    ax.text(0, 0.3, 'tan 0° = 0', fontsize=11, ha='center')

    ax.plot(60, np.tan(np.radians(60)), 'bo', markersize=8)
    ax.text(60, np.tan(np.radians(60)) + 0.5, f'tan 60° = √3 ≈ 1.73', fontsize=11, ha='center')

    ax.plot(45, 1, 'bo', markersize=8)
    ax.text(45, 1.5, 'tan 45° = 1', fontsize=11, ha='center')

    # 标注无定义区域
    ax.annotate('', xy=(88, 20), xytext=(88, 5),
               arrowprops=dict(arrowstyle='->', color='gray'))
    ax.annotate('', xy=(92, -20), xytext=(92, -5),
               arrowprops=dict(arrowstyle='->', color='gray'))
    ax.text(95, 0, 'tan → +∞', fontsize=10, color='gray')
    ax.text(95, -2, 'tan → -∞', fontsize=10, color='gray')

    ax.set_xlim(-10, 180)
    ax.set_ylim(-10, 10)
    ax.set_xlabel('角度 θ (度)', fontsize=12)
    ax.set_ylabel('tan θ', fontsize=12)
    ax.set_title('正切函数图像: θ = 90° 处无定义（渐近线）', fontsize=14, fontweight='bold')
    ax.legend(loc='upper left')
    ax.grid(True, alpha=0.3)

    # 标注公式
    formula = r'tan θ = $\frac{\sin θ}{\cos θ}$, 当 θ = 90° 时, cos θ = 0'
    ax.text(100, 7, formula, fontsize=11,
           bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', edgecolor='orange'))

    plt.tight_layout()
    plt.savefig('../imgs/2.1_图5_tan90无定义.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("已生成: 2.1_图5_tan90无定义.png")


# ============ 主程序 ============
if __name__ == '__main__':
    print("开始生成三角函数配图...")
    print("=" * 50)

    draw_unit_circle_radians()
    draw_trig_definitions()
    draw_special_triangles()
    draw_trig_values_unit_circle()
    draw_tan_asymptote()

    print("=" * 50)
    print("所有配图生成完成！")
    print("图片文件位于当前目录下")
