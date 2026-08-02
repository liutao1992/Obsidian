import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams['font.family'] = ['Hiragino Sans GB', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

output_dir = os.path.join(os.path.dirname(__file__), '..', 'imgs')
os.makedirs(output_dir, exist_ok=True)

# ========== 图2：割线逼近切线（瞬时速度的核心直觉）==========
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

def setup_ax(ax, title):
    ax.set_xlim(-0.3, 4.5)
    ax.set_ylim(0, 280)
    ax.set_title(title, fontsize=13, fontweight='bold', pad=12)
    ax.set_xlabel('时间 t（小时）', fontsize=11)
    ax.set_ylabel('位置 f(t) = 15t² + 7（英里）', fontsize=11)
    ax.grid(True, alpha=0.3)

# 位置函数
t = np.linspace(0, 4, 500)
f = 15 * t**2 + 7

# 固定点
t0 = 3
f0 = 15 * t0**2 + 7  # 142

# 四个不同的时间间隔
intervals = [
    (4.0,   'h = 1',    'blue'),
    (3.5,   'h = 0.5',  'green'),
    (3.1,   'h = 0.1',  'orange'),
    (3.01,  'h = 0.01', 'red'),
]

for idx, (ax, (u, h_label, color)) in enumerate(zip(axes.flat, intervals)):
    setup_ax(ax, f'情况 {idx+1}：时间间隔 {h_label}')

    # 绘制曲线
    ax.plot(t, f, color='navy', linewidth=2.5, label='位置函数 f(t) = 15t² + 7', zorder=3)

    # 固定点 P
    ax.plot(t0, f0, 'ko', markersize=10, zorder=5)
    ax.annotate(f'P(t=3, f=142)', xy=(t0, f0), xytext=(t0-1.2, f0+25),
                fontsize=10, color='black', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

    # 另一个点 Q
    fu = 15 * u**2 + 7
    ax.plot(u, fu, 'o', color=color, markersize=10, zorder=5)
    ax.annotate(f'Q(t={u}, f={fu:.1f})', xy=(u, fu), xytext=(u+0.15, fu+20 if idx < 2 else fu-30),
                fontsize=10, color=color, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5))

    # 割线
    slope = (fu - f0) / (u - t0)
    # 割线延长一点
    t_line = np.array([t0 - 0.5, u + 0.3])
    f_line = f0 + slope * (t_line - t0)
    ax.plot(t_line, f_line, '--', color=color, linewidth=2, zorder=4)

    # 标注斜率
    ax.text(0.5, 250, f'割线斜率 = {slope:.2f}', fontsize=12, color=color, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=color, alpha=0.9))

    # 时间间隔箭头
    ax.annotate('', xy=(u, 15), xytext=(t0, 15),
                arrowprops=dict(arrowstyle='<->', color='purple', lw=1.5))
    mid_t = (t0 + u) / 2
    ax.text(mid_t, 22, h_label, fontsize=10, color='purple', ha='center', fontweight='bold')

# 添加总标题
fig.suptitle('割线斜率逼近切线斜率：当时间间隔越来越小时', fontsize=15, fontweight='bold', y=1.02)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.2.1_图2_割线逼近切线.png'), dpi=200, bbox_inches='tight')
plt.close()

print("配图2生成完成！")
