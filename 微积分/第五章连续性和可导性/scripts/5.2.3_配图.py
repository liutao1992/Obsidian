import matplotlib.pyplot as plt
import numpy as np
import os

# 设置中文字体
plt.rcParams['font.family'] = ['Hiragino Sans GB', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# 输出目录
output_dir = os.path.join(os.path.dirname(__file__), '..', 'imgs')
os.makedirs(output_dir, exist_ok=True)

# ========== 图1：割线逼近切线（瞬时速度的极限思想）==========
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# 位置函数
def f(t):
    return 15 * t**2 + 7

# 导数（切线斜率）
def df(t):
    return 30 * t

# 公共曲线数据
t_curve = np.linspace(0, 2.5, 300)
y_curve = f(t_curve)

t0 = 1.0  # 我们关心的时刻
y0 = f(t0)
slope_tangent = df(t0)  # 切线斜率 = 30

# ---------- 左图：多条割线逼近切线 ----------
ax1 = axes[0]
ax1.plot(t_curve, y_curve, color='#2E86AB', linewidth=2.5, label=r'$f(t) = 15t^2 + 7$', zorder=3)

# 画切线
t_tangent = np.linspace(0.3, 1.8, 100)
y_tangent = y0 + slope_tangent * (t_tangent - t0)
ax1.plot(t_tangent, y_tangent, color='#E94F37', linewidth=2.5, linestyle='--', label='切线（瞬时速度）', zorder=4)

# 不同 h 值的割线
h_values = [1.0, 0.5, 0.2]
colors_secant = ['#F18F01', '#C73E1D', '#6A994E']
labels_secant = [r'$h=1.0$', r'$h=0.5$', r'$h=0.2$']

for h, color, label in zip(h_values, colors_secant, labels_secant):
    t1 = t0 + h
    y1 = f(t1)
    slope = (y1 - y0) / h
    t_secant = np.linspace(t0 - 0.3, t1 + 0.2, 100)
    y_secant = y0 + slope * (t_secant - t0)
    ax1.plot(t_secant, y_secant, color=color, linewidth=1.8, alpha=0.8, label=f'割线 {label}', zorder=2)
    # 标出终点
    ax1.plot(t1, y1, 'o', color=color, markersize=7, zorder=5)

# 标出切点
ax1.plot(t0, y0, 'o', color='#E94F37', markersize=10, zorder=6)
ax1.annotate(r'$(t, f(t))$', xy=(t0, y0), xytext=(t0 + 0.15, y0 - 4),
            fontsize=12, color='#E94F37', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#E94F37', lw=1.5))

ax1.set_xlim(0, 2.3)
ax1.set_ylim(0, 110)
ax1.set_xlabel('时间 t（小时）', fontsize=13)
ax1.set_ylabel('位置 f(t)（英里）', fontsize=13)
ax1.set_title('割线逼近切线：当 h 越来越小时', fontsize=14, fontweight='bold')
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True, alpha=0.3)
ax1.text(0.55, 0.35, r'平均速度 = $\frac{f(t+h)-f(t)}{h}$' + '\n' + r'当 $h \to 0$ 时 → 瞬时速度 = $f\'(t)$',
         transform=ax1.transAxes, fontsize=12, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# ---------- 右图：h→0 的数值逼近 ----------
ax2 = axes[1]

h_vals = np.array([1.0, 0.5, 0.2, 0.1, 0.05, 0.01, 0.001])
avg_speeds = [(f(t0 + h) - f(t0)) / h for h in h_vals]

ax2.barh(range(len(h_vals)), avg_speeds, color=['#F18F01']*3 + ['#6A994E']*3 + ['#2E86AB'], zorder=3)
ax2.set_yticks(range(len(h_vals)))
ax2.set_yticklabels([f'h = {h}' for h in h_vals])
ax2.axvline(x=slope_tangent, color='#E94F37', linewidth=2.5, linestyle='--', label=f'瞬时速度 = {slope_tangent}', zorder=4)
ax2.set_xlabel('平均速度（英里/小时）', fontsize=13)
ax2.set_title(r'在 $t=1$ 处，平均速度随 $h$ 变小而趋近瞬时速度', fontsize=14, fontweight='bold')
ax2.legend(loc='lower right', fontsize=11)
ax2.grid(True, alpha=0.3, axis='x')

# 在柱子上标注数值
for i, v in enumerate(avg_speeds):
    ax2.text(v + 0.5, i, f'{v:.1f}', va='center', fontsize=10, color='#333')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.2.3_图1_割线逼近切线.png'), dpi=200, bbox_inches='tight')
plt.close()

print("配图生成完成！")
