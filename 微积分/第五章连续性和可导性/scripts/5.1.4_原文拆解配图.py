import matplotlib.pyplot as plt
import numpy as np
import os

# 设置中文字体
plt.rcParams['font.family'] = ['Hiragino Sans GB', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# 输出目录
output_dir = os.path.join(os.path.dirname(__file__), '..', 'imgs')
os.makedirs(output_dir, exist_ok=True)

# ========== 图0：从地下走到地上 ==========
fig, ax = plt.subplots(figsize=(10, 6))

# 画一条从负到正穿过x轴的连续曲线（类似一条S形曲线）
x = np.linspace(0.3, 4.7, 300)
y = 0.8 * (x - 2.5)**3 / 3 - 0.3 * (x - 2.5) + 0.2
ax.plot(x, y, color='#2E7AD1', linewidth=2.5, zorder=3)

# x轴（作为"地面"）
ax.axhline(0, color='#333333', linewidth=1.5, zorder=2)

# 标记端点 a 和 b
a, b = 0.6, 4.4
f_a = 0.8 * (a - 2.5)**3 / 3 - 0.3 * (a - 2.5) + 0.2
f_b = 0.8 * (b - 2.5)**3 / 3 - 0.3 * (b - 2.5) + 0.2

ax.plot(a, f_a, 'o', color='#D93A3A', markersize=10, zorder=5)
ax.plot(b, f_b, 'o', color='#3A9B3A', markersize=10, zorder=5)

# 端点标注（偏移避免遮挡曲线）
ax.text(a - 0.15, f_a - 0.55, f'$(a, f(a))$\n$f(a) < 0$',
        fontsize=11, color='#D93A3A', ha='center', va='top',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#D93A3A', alpha=0.9))

ax.text(b + 0.15, f_b + 0.55, f'$(b, f(b))$\n$f(b) > 0$',
        fontsize=11, color='#3A9B3A', ha='center', va='bottom',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#3A9B3A', alpha=0.9))

# 找到并标记穿过x轴的点 c
# 手动近似 root ≈ 2.65
root = 2.65
ax.plot(root, 0, 'o', color='#9B3AD9', markersize=12, zorder=5)
ax.axvline(root, color='#9B3AD9', linestyle=':', alpha=0.5, ymax=0.12, zorder=1)
ax.text(root, -0.45, f'$c$\n$f(c) = 0$',
        fontsize=11, color='#9B3AD9', ha='center', va='top',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#9B3AD9', alpha=0.9))

# 区域标注：地下（负数区）和地上（正数区）
ax.text(0.15, 0.92, '地上（正数区）', transform=ax.transAxes,
        fontsize=13, color='#3A9B3A', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#E8F5E9', edgecolor='#3A9B3A', alpha=0.9))

ax.text(0.15, 0.08, '地下（负数区）', transform=ax.transAxes,
        fontsize=13, color='#D93A3A', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFEBEE', edgecolor='#D93A3A', alpha=0.9))

# 地面标注
ax.text(4.6, 0.25, '地面（x轴）', fontsize=11, color='#555555', ha='right')

# 区间 [a,b] 标注
ax.annotate('', xy=(b, -1.8), xytext=(a, -1.8),
            arrowprops=dict(arrowstyle='<->', color='#E67E22', lw=2))
ax.text((a + b) / 2, -2.1, '区间 $[a, b]$', fontsize=12, color='#E67E22', ha='center')

# 垂直引导线到区间标注
ax.plot([a, a], [f_a, -1.8], color='#E67E22', linestyle='--', alpha=0.5, lw=1)
ax.plot([b, b], [f_b, -1.8], color='#E67E22', linestyle='--', alpha=0.5, lw=1)

# 标题
ax.set_title('连续函数从地下走到地上，必然穿过地面', fontsize=15, pad=15)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)

# 坐标轴范围
ax.set_xlim(-0.2, 5)
ax.set_ylim(-2.5, 2.2)

# 隐藏顶部和右侧边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 轻网格
ax.grid(True, alpha=0.2, linestyle='--')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.4_图0_从地下到地上.png'),
            dpi=200, bbox_inches='tight', facecolor='white')
plt.close()

print("配图 5.1.4_图0_从地下到地上.png 生成完成！")
