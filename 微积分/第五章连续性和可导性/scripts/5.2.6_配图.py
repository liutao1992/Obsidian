import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams['font.family'] = ['Hiragino Sans GB', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

output_dir = os.path.join(os.path.dirname(__file__), '..', 'imgs')
os.makedirs(output_dir, exist_ok=True)

# ========== 图1：y=x^2 及其切线（导函数的几何意义）==========
fig, ax = plt.subplots(figsize=(10, 8))

# 绘制抛物线
x = np.linspace(-2.5, 2.5, 500)
y = x**2
ax.plot(x, y, color='navy', linewidth=2.5, label='$y = x^2$', zorder=3)

# 切点及其切线数据
tangent_points = [
    (-1, 1, -2, 'blue'),
    (0, 0, 0, 'green'),
    (1, 1, 2, 'red'),
    (2, 4, 4, 'purple'),
]

for x0, y0, slope, color in tangent_points:
    # 切点
    ax.plot(x0, y0, 'o', color=color, markersize=10, zorder=5)

    # 切线（延长显示）
    x_tan = np.linspace(x0 - 1.2, x0 + 1.2, 100)
    y_tan = y0 + slope * (x_tan - x0)
    ax.plot(x_tan, y_tan, '--', color=color, linewidth=2, zorder=4)

    # 标注切点和斜率
    offset_x = 0.3 if x0 >= 0 else -0.3
    offset_y = 0.6 if y0 >= 1 else -0.8
    ha = 'left' if x0 >= 0 else 'right'

    ax.annotate(
        f'$x={x0}$，斜率 $={slope}$',
        xy=(x0, y0),
        xytext=(x0 + offset_x, y0 + offset_y),
        fontsize=11,
        color=color,
        fontweight='bold',
        ha=ha,
        arrowprops=dict(arrowstyle='->', color=color, lw=1.2),
    )

# 标注导函数关系
ax.text(
    0.5, 5.5,
    r"$f(x) = x^2 \quad \Rightarrow \quad f'(x) = 2x$" + "\n" +
    r"任意点 $x$ 处的切线斜率 $= 2x$",
    fontsize=13,
    ha='center',
    bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', edgecolor='orange', alpha=0.9),
)

ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-1.5, 6.5)
ax.set_xlabel('$x$', fontsize=12)
ax.set_ylabel('$y$', fontsize=12)
ax.set_title(r'$y = x^2$ 及其在各点的切线（斜率 = $f^{\prime}(x) = 2x$）', fontsize=14, fontweight='bold', pad=15)
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.grid(True, alpha=0.3)
ax.legend(loc='upper left', fontsize=11)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.2.6_图1_导函数切线.png'), dpi=200, bbox_inches='tight')
plt.close()

print("配图生成完成！")
