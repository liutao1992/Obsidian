import matplotlib.pyplot as plt
import numpy as np
import os

# 设置中文字体
plt.rcParams['font.family'] = ['Hiragino Sans GB', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# 定义函数
def f(t):
    return 0.5 * t**2

# 输出目录
output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'imgs')
os.makedirs(output_dir, exist_ok=True)

# ==================== 图1：割线与平均速度 ====================
fig, ax = plt.subplots(figsize=(8, 6))

t = 2.0
u = 4.5

t_vals = np.linspace(0, 6, 200)
y_vals = f(t_vals)

# 画曲线
ax.plot(t_vals, y_vals, 'k-', linewidth=2, label=r'$y = f(t)$')

# 标记两点
ax.plot(t, f(t), 'ko', markersize=8, zorder=5)
ax.plot(u, f(u), 'ko', markersize=8, zorder=5)

# 虚线垂直到x轴
ax.plot([t, t], [0, f(t)], 'k--', linewidth=0.8, alpha=0.6)
ax.plot([u, u], [0, f(u)], 'k--', linewidth=0.8, alpha=0.6)

# 画割线（虚线）
slope = (f(u) - f(t)) / (u - t)
line_x = np.linspace(1, 5.5, 100)
line_y = f(t) + slope * (line_x - t)
ax.plot(line_x, line_y, 'b--', linewidth=1.8, alpha=0.8, label='割线')

# 标注点
ax.text(t, -0.8, r'$t$', fontsize=14, ha='center', va='top')
ax.text(u, -0.8, r'$u$', fontsize=14, ha='center', va='top')
ax.text(t + 0.15, f(t) + 0.3, r'$(t, f(t))$', fontsize=12)
ax.text(u + 0.15, f(u) + 0.3, r'$(u, f(u))$', fontsize=12)

# 标注斜率公式（中文用普通文本，公式用数学模式）
ax.text(0.05, 0.88, '斜率 =',
        transform=ax.transAxes, fontsize=14)
ax.text(0.05, 0.74, r'$\dfrac{f(u) - f(t)}{u - t}$',
        transform=ax.transAxes, fontsize=14,
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

ax.set_xlabel('时间', fontsize=13)
ax.set_ylabel('位置', fontsize=13)
ax.set_xlim(0, 6)
ax.set_ylim(-1, 14)
ax.legend(loc='upper right', fontsize=11)
ax.set_aspect('equal', adjustable='box')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.2.4_图1_割线与平均速度.png'),
            dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print("图1 已生成")

# ==================== 图2：割线趋近切线 ====================
fig, axes = plt.subplots(1, 3, figsize=(14, 5))

t = 2.0
u_values = [4.0, 3.0, 2.3]
titles = [r'$u$ 离 $t$ 较远', r'$u$ 靠近 $t$', r'$u$ 非常接近 $t$']

for idx, (ax, u, title) in enumerate(zip(axes, u_values, titles)):
    t_vals = np.linspace(0, 5, 200)
    y_vals = f(t_vals)

    # 画曲线
    ax.plot(t_vals, y_vals, 'k-', linewidth=2)

    # 标记点
    ax.plot(t, f(t), 'ko', markersize=7, zorder=5)
    ax.plot(u, f(u), 'ko', markersize=7, zorder=5)

    # 虚线垂直到x轴
    ax.plot([t, t], [0, f(t)], 'k--', linewidth=0.6, alpha=0.5)
    ax.plot([u, u], [0, f(u)], 'k--', linewidth=0.6, alpha=0.5)

    # 画割线
    slope = (f(u) - f(t)) / (u - t)
    line_x = np.linspace(1, 4.5, 100)
    line_y = f(t) + slope * (line_x - t)
    ax.plot(line_x, line_y, 'b--', linewidth=1.5, alpha=0.7)

    # 标注
    ax.text(t, -0.6, r'$t$', fontsize=12, ha='center', va='top')
    ax.text(u, -0.6, r'$u$', fontsize=12, ha='center', va='top')
    ax.set_title(title, fontsize=13)

    ax.set_xlabel('时间', fontsize=11)
    if idx == 0:
        ax.set_ylabel('位置', fontsize=11)
    ax.set_xlim(0, 5)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal', adjustable='box')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

# 在最右图添加"切线"标注
ax = axes[2]
# 计算切线斜率（f'(t) = t，在t=2处斜率为2）
tangent_slope = t  # f'(t) = d/dt(0.5*t^2) = t
tangent_x = np.linspace(1, 3.5, 100)
tangent_y = f(t) + tangent_slope * (tangent_x - t)
ax.plot(tangent_x, tangent_y, 'r-', linewidth=2, alpha=0.9, label='切线（极限位置）')
ax.legend(loc='upper left', fontsize=9)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.2.4_图2_割线趋近切线.png'),
            dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print("图2 已生成")

print("所有配图生成完毕！")
