import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# 兼容中文显示
matplotlib.rcParams['font.family'] = ['Hiragino Sans GB', 'Heiti TC', 'STHeiti', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

save_path = '../imgs/5.1_图6_四种典型情况.png'

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('连续性四种典型情况', fontsize=16, y=0.98)

# 参数
a = 1.0
x_left = np.linspace(-1.5, a - 0.05, 100)
x_right = np.linspace(a + 0.05, 2.5, 100)

# 通用绘图函数
def setup_axis(ax, title, status):
    ax.set_title(title, fontsize=13, pad=10)
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.set_xlim(-1.5, 2.5)
    ax.set_ylim(-0.5, 3.5)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True, alpha=0.3)
    # 在右下角显示结果
    status_text = '不连续' if '不连续' in status else '连续'
    status_symbol = '×' if '不连续' in status else '√'
    color = '#D9534F' if '不连续' in status else '#6A994E'
    ax.text(2.3, -0.3, f'{status_symbol} {status_text}', fontsize=14, ha='right', va='bottom',
            color=color, fontweight='bold')

# 第一类：极限不存在（跳跃间断点）
ax1 = axes[0, 0]
ax1.plot(x_left, 0.5 * x_left + 1.5, color='#2E86AB', linewidth=2.5)
ax1.plot(x_right, 0.5 * x_right + 0.5, color='#2E86AB', linewidth=2.5)
ax1.plot(a, 2.0, 'o', color='#2E86AB', markersize=9, fillstyle='none', markeredgewidth=2)
ax1.plot(a, 1.0, 'o', color='#2E86AB', markersize=9, fillstyle='none', markeredgewidth=2)
setup_axis(ax1, '第一类：极限不存在（左右极限不同）', '❌ 不连续')

# 第二类：函数值不存在（可去间断点-洞）
ax2 = axes[0, 1]
ax2.plot(x_left, x_left**2, color='#2E86AB', linewidth=2.5)
ax2.plot(x_right, x_right**2, color='#2E86AB', linewidth=2.5)
ax2.plot(a, 1.0, 'o', color='#2E86AB', markersize=10, fillstyle='none', markeredgewidth=2.5)
setup_axis(ax2, '第二类：函数值不存在（该点无定义）', '❌ 不连续')

# 第三类：极限和函数值不同（可去间断点-点错位）
ax3 = axes[1, 0]
ax3.plot(x_left, x_left**2, color='#2E86AB', linewidth=2.5)
ax3.plot(x_right, x_right**2, color='#2E86AB', linewidth=2.5)
ax3.plot(a, 1.0, 'o', color='#2E86AB', markersize=10, fillstyle='none', markeredgewidth=2.5)
ax3.plot(a, 2.5, 'o', color='#D9534F', markersize=10)
setup_axis(ax3, '第三类：极限和函数值不同', '❌ 不连续')

# 第四类：真正连续
ax4 = axes[1, 1]
x_smooth = np.linspace(-1.5, 2.5, 200)
ax4.plot(x_smooth, x_smooth**2, color='#2E86AB', linewidth=2.5)
ax4.plot(a, 1.0, 'o', color='#2E86AB', markersize=10)
setup_axis(ax4, '第四类：真正连续', '✅ 连续')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

print(f'图片已保存到：{save_path}')
