import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 输出目录
output_dir = Path(__file__).resolve().parent.parent / 'imgs'
output_dir.mkdir(parents=True, exist_ok=True)

# 函数 f(x) = (x^2 - 3x + 2) / (x - 2) = x - 1 (x != 2)
def f(x):
    return (x**2 - 3*x + 2) / (x - 2)

# 图1：有理函数整体图像，显示 x=2 处的洞
fig, ax = plt.subplots(figsize=(7, 5), dpi=150)

x_left = np.linspace(-4, 1.85, 200)
x_right = np.linspace(2.15, 6, 200)

ax.plot(x_left, f(x_left), color='#1f77b4', linewidth=2.5, label=r'$f(x)=\dfrac{x^2-3x+2}{x-2}$')
ax.plot(x_right, f(x_right), color='#1f77b4', linewidth=2.5)

# 在 x=2 处画空心圆（洞）
ax.plot(2, 1, 'o', color='#1f77b4', markersize=8, fillstyle='none', markeredgewidth=2)
ax.annotate('洞\n$x=2$', xy=(2, 1), xytext=(3.3, 2.5),
            fontsize=11, color='#d62728',
            arrowprops=dict(arrowstyle='->', color='#d62728'))

# 标出 x=-1 的点
ax.plot(-1, f(-1), 'o', color='#2ca02c', markersize=8, zorder=5)
ax.annotate(r'$x=-1$ 连续', xy=(-1, f(-1)), xytext=(-3.5, -1.5),
            fontsize=11, color='#2ca02c',
            arrowprops=dict(arrowstyle='->', color='#2ca02c'))

ax.set_title(r'函数 $f(x)=\dfrac{x^2-3x+2}{x-2}$ 在 $x=2$ 处无定义', fontsize=14)
ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('y', fontsize=11)
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xlim(-5, 7)
ax.set_ylim(-4, 5)
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig(output_dir / 'rational_function.png', bbox_inches='tight')
plt.close()

# 图2：x=-1 附近放大，显示连续性
fig, ax = plt.subplots(figsize=(7, 5), dpi=150)

x_near = np.linspace(-2.5, -0.5, 300)
ax.plot(x_near, f(x_near), color='#2ca02c', linewidth=3, label=r'$f(x)$ 在 $x=-1$ 附近')

# 标出 x=-1 的点
ax.plot(-1, f(-1), 'o', color='#d62728', markersize=10, zorder=5)
ax.annotate(r'$(-1, f(-1))=(-1,-2)$', xy=(-1, f(-1)), xytext=(-2.2, -1.0),
            fontsize=11, color='#d62728',
            arrowprops=dict(arrowstyle='->', color='#d62728'))

ax.set_title(r'只看 $x=-1$ 附近，函数表现正常、没有断裂', fontsize=14)
ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('y', fontsize=11)
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper right')
plt.tight_layout()
plt.savefig(output_dir / 'rational_at_minus1.png', bbox_inches='tight')
plt.close()

# 图3：道路有坑的示意图
fig, ax = plt.subplots(figsize=(8, 3), dpi=150)

# 道路
road_y = np.zeros(400)
road_x = np.linspace(0, 10, 400)
ax.plot(road_x, road_y, color='#8B4513', linewidth=6, solid_capstyle='butt')

# 坑（在 x=5 附近）
ax.plot([4.7, 5.3], [0, 0], color='white', linewidth=6, solid_capstyle='butt')
ax.plot(4.7, 0, 'o', color='#8B4513', markersize=6)
ax.plot(5.3, 0, 'o', color='#8B4513', markersize=6)

# 标注
ax.text(5, 0.5, '坑\n（函数无定义）', ha='center', fontsize=11, color='#d62728')
ax.text(2, -0.6, 'x=-1 处\n道路正常', ha='center', fontsize=11, color='#2ca02c')
ax.text(8, -0.6, '其他地方\n也正常', ha='center', fontsize=11, color='#2ca02c')

ax.set_title(r'连续性像道路：某个地方有坑，不代表所有地方都不通', fontsize=14)
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)
ax.axis('off')
plt.tight_layout()
plt.savefig(output_dir / 'local_continuity_road.png', bbox_inches='tight')
plt.close()

# 图4：总结示意图：x=2 有洞，x=-1 正常
fig, ax = plt.subplots(figsize=(8, 5), dpi=150)

x_left = np.linspace(-4, 1.9, 200)
x_right = np.linspace(2.1, 6, 200)

ax.plot(x_left, f(x_left), color='#1f77b4', linewidth=2.5)
ax.plot(x_right, f(x_right), color='#1f77b4', linewidth=2.5)
ax.plot(2, 1, 'o', color='#d62728', markersize=10, fillstyle='none', markeredgewidth=2.5)
ax.plot(-1, -2, 'o', color='#2ca02c', markersize=10)

ax.annotate(r'$x=2$ 处无定义', xy=(2, 1), xytext=(3.5, 2.5),
            fontsize=12, color='#d62728',
            arrowprops=dict(arrowstyle='->', color='#d62728'))
ax.annotate(r'$x=-1$ 处连续', xy=(-1, -2), xytext=(-3.5, -0.5),
            fontsize=12, color='#2ca02c',
            arrowprops=dict(arrowstyle='->', color='#2ca02c'))

ax.set_title(r'核心：有一个断点，不等于所有地方都不连续', fontsize=15)
ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('y', fontsize=11)
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xlim(-5, 7)
ax.set_ylim(-4, 5)
plt.tight_layout()
plt.savefig(output_dir / 'rational_summary.png', bbox_inches='tight')
plt.close()

print(f'已保存 4 张配图到：{output_dir}')
