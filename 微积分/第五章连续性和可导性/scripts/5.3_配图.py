import matplotlib.pyplot as plt
import numpy as np
import os

# 设置中文字体
plt.rcParams['font.family'] = ['Hiragino Sans GB', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# 输出目录
output_dir = os.path.join(os.path.dirname(__file__), '..', 'imgs')
os.makedirs(output_dir, exist_ok=True)

# ========== 图1：割线趋近切线（分步展示）==========
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 参数
a = 1.5
f_a = a**2
slope_tangent = 2 * a

# 四个子图的数据：x 越来越靠近 a
configs = [
    {'x': 2.5, 'title': '第一步：$x_1$ 离 $a$ 较远', 'color': '#E67E22', 'label': r'$x_1$'},
    {'x': 2.0, 'title': '第二步：$x_2$ 靠近 $a$', 'color': '#9B59B6', 'label': r'$x_2$'},
    {'x': 1.7, 'title': '第三步：$x_3$ 更接近 $a$', 'color': '#E74C3C', 'label': r'$x_3$'},
    {'x': None, 'title': '第四步：极限 → 切线', 'color': '#C0392B', 'label': None},
]

for idx, (ax, cfg) in enumerate(zip(axes.flat, configs)):
    # 画函数曲线
    x = np.linspace(-0.5, 3, 300)
    y = x**2
    ax.plot(x, y, 'b-', linewidth=2.5, label=r'$y = x^2$')

    # 固定点
    ax.plot(a, f_a, 'go', markersize=11, zorder=5)
    ax.annotate(r'$(a, f(a))$', xy=(a, f_a), textcoords="offset points",
                xytext=(-45, 12), fontsize=11, color='green',
                arrowprops=dict(arrowstyle='->', color='green', lw=1.5))

    # 标注 x = a
    ax.axvline(a, color='gray', linestyle=':', alpha=0.5)
    ax.text(a + 0.05, 7.2, r'$x = a$', fontsize=11, color='gray')

    if cfg['x'] is not None:
        x_val = cfg['x']
        f_x = x_val**2

        # 画割线（加粗，更明显）
        slope = (f_x - f_a) / (x_val - a)
        x_line = np.linspace(0.8, 3, 100)
        y_line = f_a + slope * (x_line - a)
        ax.plot(x_line, y_line, color=cfg['color'], linewidth=2.5,
                linestyle='--', label=f'割线（斜率={slope:.2f}）')

        # 动点（加大空心圆+实心点）
        ax.plot(x_val, f_x, 'o', color=cfg['color'], markersize=14,
                markeredgewidth=2.5, markerfacecolor='white', zorder=5)
        # 醒目标注坐标：白色背景框+加粗字体+粗箭头
        point_label = cfg['label'] + r'$, f(' + cfg['label'].replace('$', '') + r'))$'
        ax.annotate(point_label, xy=(x_val, f_x), textcoords="offset points",
                    xytext=(18, 18), fontsize=13, color=cfg['color'],
                    fontweight='bold',
                    bbox=dict(boxstyle='round,pad=0.35', facecolor='white',
                              edgecolor=cfg['color'], linewidth=1.5, alpha=0.95),
                    arrowprops=dict(arrowstyle='->', color=cfg['color'], lw=2))
        # 画连接线（虚线）帮助看清割线
        ax.plot([a, x_val], [f_a, f_x], color=cfg['color'], linewidth=1,
                linestyle=':', alpha=0.5)

        # 在x轴下方醒目标注 x1/x2/x3 位置
        ax.axvline(x_val, ymin=0, ymax=0.05, color=cfg['color'], linewidth=3, clip_on=False)
        ax.text(x_val, -0.5, cfg['label'], fontsize=14, color='white',
                ha='center', va='center', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=cfg['color'],
                          edgecolor=cfg['color'], alpha=0.95))

    else:
        # 最后一个子图：只画切线
        x_tan = np.linspace(0.8, 3, 100)
        y_tan = f_a + slope_tangent * (x_tan - a)
        ax.plot(x_tan, y_tan, 'r-', linewidth=3, label=f'切线（斜率={slope_tangent:.2f}）')

        # 添加公式（放在左下角避免溢出）
        ax.text(0.04, 0.06,
                r"$f'(a) = \lim_{x \to a} \frac{f(x)-f(a)}{x-a}$",
                transform=ax.transAxes, fontsize=12, color='darkblue',
                bbox=dict(boxstyle='round', facecolor='lightyellow',
                          edgecolor='darkblue', alpha=0.9))

    # 统一坐标轴
    ax.set_xlim(-0.3, 3.2)
    ax.set_ylim(-1.0, 8)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_title(cfg['title'], fontsize=13)
    ax.set_xlabel('x', fontsize=11)
    ax.set_ylabel('y', fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper left', fontsize=10)

# 总标题
fig.suptitle('割线趋近切线的过程：$x$ 一步步靠近 $a$', fontsize=16, y=1.02)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.3_图1_割线趋近切线.png'),
            dpi=200, bbox_inches='tight')
plt.close()

# ========== 图2：连续但不可导（尖角） ==========
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# 左图：y = |x| 在 x=0 处有尖角
ax1 = axes[0]
x_left = np.linspace(-2, 0, 150)
y_left = np.abs(x_left)
x_right = np.linspace(0, 2, 150)
y_right = np.abs(x_right)

ax1.plot(x_left, y_left, 'b-', linewidth=2.5)
ax1.plot(x_right, y_right, 'b-', linewidth=2.5)

# 标记尖角
ax1.plot(0, 0, 'ro', markersize=12, zorder=5)
ax1.annotate('尖角：连续但不可导', xy=(0, 0), textcoords="offset points",
             xytext=(25, 30), fontsize=12, color='red',
             arrowprops=dict(arrowstyle='->', color='red'))

# 画左右切线
x_line = np.linspace(-1.5, 1.5, 100)
# 左切线斜率 = -1
ax1.plot(x_line, -x_line, 'g--', linewidth=1.5, alpha=0.7, label='左切线（斜率=-1）')
# 右切线斜率 = 1
ax1.plot(x_line, x_line, 'orange', linestyle='--', linewidth=1.5, alpha=0.7, label='右切线（斜率=1）')

ax1.set_xlim(-2.2, 2.2)
ax1.set_ylim(-0.3, 2.5)
ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)
ax1.set_title(r'$y = |x|$ 在 $x = 0$ 处连续但不可导', fontsize=14)
ax1.set_xlabel('x', fontsize=12)
ax1.set_ylabel('y', fontsize=12)
ax1.grid(True, alpha=0.3)
ax1.legend(loc='upper center', fontsize=10)

# 右图：y = x^3 在 x=0 处切线穿过曲线
ax2 = axes[1]
x = np.linspace(-1.5, 1.5, 300)
y = x**3
ax2.plot(x, y, 'b-', linewidth=2.5, label=r'$y = x^3$')

# 切线 y = 0（在 x=0 处）
x_tan = np.linspace(-1.5, 1.5, 100)
y_tan = np.zeros_like(x_tan)
ax2.plot(x_tan, y_tan, 'r-', linewidth=2, label='切线：$y = 0$')

# 标记切点
ax2.plot(0, 0, 'go', markersize=12, zorder=5)
ax2.annotate('切点 (0, 0)', xy=(0, 0), textcoords="offset points",
             xytext=(20, 20), fontsize=12, color='green',
             arrowprops=dict(arrowstyle='->', color='green'))

ax2.annotate('切线穿过曲线！', xy=(0.8, 0), textcoords="offset points",
             xytext=(10, 30), fontsize=12, color='red',
             arrowprops=dict(arrowstyle='->', color='red'))

ax2.set_xlim(-1.8, 1.8)
ax2.set_ylim(-3.5, 3.5)
ax2.axhline(0, color='black', linewidth=0.5)
ax2.axvline(0, color='black', linewidth=0.5)
ax2.set_title(r'$y = x^3$ 的切线可以穿过曲线', fontsize=14)
ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('y', fontsize=12)
ax2.grid(True, alpha=0.3)
ax2.legend(loc='lower right', fontsize=11)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.3_图2_连续但不可导.png'), dpi=200, bbox_inches='tight')
plt.close()

# ========== 图3：导数定义的两种写法对比 ==========
fig, ax = plt.subplots(figsize=(10, 7))

# 绘制函数曲线
x = np.linspace(0.5, 3, 300)
y = np.sin(x) + 0.3 * x
ax.plot(x, y, 'b-', linewidth=2.5, label=r'$y = f(x)$')

# 固定点 a = 2
a = 2
f_a = np.sin(a) + 0.3 * a
ax.plot(a, f_a, 'go', markersize=12, zorder=5)
ax.annotate(r'$(a, f(a))$', xy=(a, f_a), textcoords="offset points",
            xytext=(-50, 20), fontsize=12, color='green',
            arrowprops=dict(arrowstyle='->', color='green'))

# 动点 x = a + h
h = 0.8
x_val = a + h
f_x = np.sin(x_val) + 0.3 * x_val
ax.plot(x_val, f_x, 'mo', markersize=10, zorder=5)
ax.annotate(r'$(x, f(x))$ 或 $(a+h, f(a+h))$', xy=(x_val, f_x), textcoords="offset points",
            xytext=(15, 20), fontsize=11, color='purple',
            arrowprops=dict(arrowstyle='->', color='purple'))

# 画割线
slope = (f_x - f_a) / h
x_line = np.linspace(1, 3.5, 100)
y_line = f_a + slope * (x_line - a)
ax.plot(x_line, y_line, 'orange', linestyle='--', linewidth=2, alpha=0.8, label='割线')

# 画水平和垂直辅助线
ax.plot([a, x_val], [f_a, f_a], 'gray', linestyle=':', alpha=0.6)
ax.plot([x_val, x_val], [f_a, f_x], 'gray', linestyle=':', alpha=0.6)

# 标注 h 和 f(a+h)-f(a)
mid_x = (a + x_val) / 2
ax.annotate(r'$h = x - a$', xy=(mid_x, f_a), textcoords="offset points",
            xytext=(0, -25), fontsize=11, color='gray', ha='center')
ax.annotate(r'$f(a+h) - f(a)$', xy=(x_val, (f_a + f_x)/2), textcoords="offset points",
            xytext=(15, 0), fontsize=11, color='gray')

# 标注公式
ax.text(0.12, 0.82, r'写法一：$f^{\prime}(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}$',
        transform=ax.transAxes, fontsize=13, color='darkblue',
        bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='darkblue', alpha=0.9))
ax.text(0.12, 0.72, r'写法二：$f^{\prime}(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$',
        transform=ax.transAxes, fontsize=13, color='darkred',
        bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='darkred', alpha=0.9))

ax.axvline(a, color='gray', linestyle=':', alpha=0.4)
ax.set_xlim(0.5, 3.5)
ax.set_ylim(0.5, 2.5)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_title('导数定义的两种等价写法', fontsize=15)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.grid(True, alpha=0.3)
ax.legend(loc='lower right', fontsize=11)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.3_图3_导数定义两种写法.png'), dpi=200, bbox_inches='tight')
plt.close()

print("配图生成完成！")
