import matplotlib.pyplot as plt
import numpy as np
import os

# 设置中文字体
plt.rcParams['font.family'] = ['Hiragino Sans GB', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# 输出目录
output_dir = os.path.join(os.path.dirname(__file__), '..', 'imgs')
os.makedirs(output_dir, exist_ok=True)

# ========== 图1：距离 vs 位移 ==========
fig, axes = plt.subplots(4, 1, figsize=(12, 13))

# 公共设置
def setup_ax(ax, title):
    ax.set_xlim(-3, 13)
    ax.set_ylim(-0.8, 1.8)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.axhline(0, color='black', linewidth=1.5)
    ax.set_yticks([])
    ax.set_xlabel('位置（英里）', fontsize=12)
    ax.grid(True, alpha=0.3, axis='x')

# 数字标记
for pos in [-1, 0, 2, 5, 11]:
    for ax in axes:
        ax.plot(pos, 0, 'k|', markersize=15, markeredgewidth=2)

# ---------- 子图1：从2到5（向右行驶）----------
ax1 = axes[0]
setup_ax(ax1, '情况一：从位置 2 驶到位置 5（向右）')

# 起点和终点
ax1.plot(2, 0.3, 'go', markersize=14, zorder=5)
ax1.plot(5, 0.3, 'ro', markersize=14, zorder=5)
ax1.text(2, 0.6, '起点\n2', fontsize=11, color='green', ha='center', fontweight='bold')
ax1.text(5, 0.6, '终点\n5', fontsize=11, color='red', ha='center', fontweight='bold')

# 箭头表示行驶方向
ax1.annotate('', xy=(4.8, 1.0), xytext=(2.2, 1.0),
            arrowprops=dict(arrowstyle='->', color='blue', lw=3))
ax1.text(3.5, 1.3, '距离 = 3 英里', fontsize=12, color='blue', ha='center')
ax1.text(3.5, 0.15, '位移 = 5 - 2 = +3 英里', fontsize=12, color='purple', ha='center')

# 位置标记
for pos in [-1, 0, 2, 5, 11]:
    ax1.text(pos, -0.5, str(pos), fontsize=10, ha='center', color='gray')

# ---------- 子图2：从2到-1（向左行驶）----------
ax2 = axes[1]
setup_ax(ax2, '情况二：从位置 2 驶到位置 -1（向左）')

ax2.plot(2, 0.3, 'go', markersize=14, zorder=5)
ax2.plot(-1, 0.3, 'ro', markersize=14, zorder=5)
ax2.text(2, 0.6, '起点\n2', fontsize=11, color='green', ha='center', fontweight='bold')
ax2.text(-1, 0.6, '终点\n-1', fontsize=11, color='red', ha='center', fontweight='bold')

# 箭头表示行驶方向
ax2.annotate('', xy=(-0.8, 1.0), xytext=(1.8, 1.0),
            arrowprops=dict(arrowstyle='->', color='blue', lw=3))
ax2.text(0.5, 1.3, '距离 = 3 英里', fontsize=12, color='blue', ha='center')
ax2.text(0.5, 0.15, '位移 = -1 - 2 = -3 英里', fontsize=12, color='purple', ha='center')

for pos in [-1, 0, 2, 5, 11]:
    ax2.text(pos, -0.5, str(pos), fontsize=10, ha='center', color='gray')

# ---------- 子图3：往返（从2到11再返回5）----------
ax3 = axes[2]
setup_ax(ax3, '情况三：从 2 到 11 再返回 5（往返）')

ax3.plot(2, 0.3, 'go', markersize=14, zorder=5)
ax3.plot(5, 0.3, 'ro', markersize=14, zorder=5)
ax3.text(2, 0.6, '起点\n2', fontsize=11, color='green', ha='center', fontweight='bold')
ax3.text(5, 0.6, '终点\n5', fontsize=11, color='red', ha='center', fontweight='bold')

# 去程箭头
ax3.annotate('', xy=(10.8, 1.2), xytext=(2.2, 1.2),
            arrowprops=dict(arrowstyle='->', color='orange', lw=2.5))
ax3.text(6.5, 1.45, '去程：走了 9 英里', fontsize=11, color='orange', ha='center')

# 回程箭头
ax3.annotate('', xy=(5.2, 0.85), xytext=(10.8, 0.85),
            arrowprops=dict(arrowstyle='->', color='brown', lw=2.5))
ax3.text(8, 0.65, '回程：走了 6 英里', fontsize=11, color='brown', ha='center')

ax3.text(8, 0.15, '总距离 = 9 + 6 = 15 英里，位移 = 5 - 2 = 3 英里', fontsize=12, color='purple', ha='center')

for pos in [-1, 0, 2, 5, 11]:
    ax3.text(pos, -0.5, str(pos), fontsize=10, ha='center', color='gray')

# ---------- 子图4：往返原点（从2到-4再返回2）----------
ax4 = axes[3]
setup_ax(ax4, '情况四：从 2 到 -4 再返回 2（往返原点）')
ax4.set_xlim(-6, 8)

ax4.plot(2, 0.3, 'go', markersize=14, zorder=5)
ax4.plot(2, 0.3, 'ro', markersize=14, zorder=5)
ax4.text(2, 0.8, '起点 = 终点\n2', fontsize=11, color='green', ha='center', fontweight='bold')

# 去程箭头
ax4.annotate('', xy=(-3.8, 1.2), xytext=(1.8, 1.2),
            arrowprops=dict(arrowstyle='->', color='orange', lw=2.5))
ax4.text(-1, 1.45, '去程：走了 6 英里', fontsize=11, color='orange', ha='center')

# 回程箭头
ax4.annotate('', xy=(1.8, 0.85), xytext=(-3.8, 0.85),
            arrowprops=dict(arrowstyle='->', color='brown', lw=2.5))
ax4.text(-1, 0.65, '回程：走了 6 英里', fontsize=11, color='brown', ha='center')

ax4.text(-1, 0.15, '总距离 = 6 + 6 = 12 英里，位移 = 2 - 2 = 0 英里', fontsize=12, color='purple', ha='center')

for pos in [-4, -1, 0, 2, 5]:
    ax4.text(pos, -0.5, str(pos), fontsize=10, ha='center', color='gray')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.2.1_图1_距离vs位移.png'), dpi=200, bbox_inches='tight')
plt.close()

print("配图生成完成！")
