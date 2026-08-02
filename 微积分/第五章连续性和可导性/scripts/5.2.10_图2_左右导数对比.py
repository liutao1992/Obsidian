import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams['font.family'] = ['Hiragino Sans GB', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

output_dir = os.path.join(os.path.dirname(__file__), '..', 'imgs')
os.makedirs(output_dir, exist_ok=True)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# ========== 左图：可导的例子 y = x^2 ==========
ax1 = axes[0]

x = np.linspace(-2, 2, 200)
ax1.plot(x, x**2, color='navy', linewidth=2.5, label='y = x²')

# 在 x=0 处的切线（水平线 y=0）
ax1.axhline(0, color='red', linewidth=2, linestyle='--', label='切线（斜率 = 0）')

# 标出原点
ax1.plot(0, 0, 'ko', markersize=10, zorder=5)
ax1.annotate('(0, 0)', xy=(0, 0), xytext=(0.5, 0.8),
            fontsize=11,
            arrowprops=dict(arrowstyle='->', color='black', lw=1.2))

# 左右导数相等的标注
ax1.text(0, -0.6, '左导数 = 0    右导数 = 0', fontsize=12, color='green',
         fontweight='bold', ha='center',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', edgecolor='green', alpha=0.8))

ax1.text(0, -1.4, '左右相等 → 导数存在', fontsize=13, color='darkgreen',
         fontweight='bold', ha='center')

ax1.set_xlim(-2, 2)
ax1.set_ylim(-2, 4)
ax1.set_xlabel('x', fontsize=12)
ax1.set_ylabel('y', fontsize=12)
ax1.set_title('可导：左右导数相等', fontsize=14, fontweight='bold', color='darkgreen')
ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)
ax1.grid(True, alpha=0.3)
ax1.legend(loc='upper center', fontsize=10)

# ========== 右图：不可导的例子 y = |x| ==========
ax2 = axes[1]

x_left = np.linspace(-2, 0, 100)
x_right = np.linspace(0, 2, 100)
ax2.plot(x_left, np.abs(x_left), color='navy', linewidth=2.5)
ax2.plot(x_right, np.abs(x_right), color='navy', linewidth=2.5, label='y = |x|')

# 左侧切线（斜率 -1）
ax2.plot([-1.5, 0], [1.5, 0], '--', color='blue', linewidth=2, label='左侧切线（斜率 = -1）')
# 右侧切线（斜率 +1）
ax2.plot([0, 1.5], [0, 1.5], '--', color='green', linewidth=2, label='右侧切线（斜率 = 1）')

# 标出原点
ax2.plot(0, 0, 'ko', markersize=10, zorder=5)
ax2.annotate('尖点\n(0, 0)', xy=(0, 0), xytext=(0.8, 1.2),
            fontsize=11,
            arrowprops=dict(arrowstyle='->', color='red', lw=1.2))

# 左右导数不相等的标注
ax2.text(0, -0.6, '左导数 = -1    右导数 = 1', fontsize=12, color='red',
         fontweight='bold', ha='center',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', edgecolor='red', alpha=0.8))

ax2.text(0, -1.4, '左右不等 → 导数不存在', fontsize=13, color='darkred',
         fontweight='bold', ha='center')

ax2.set_xlim(-2, 2)
ax2.set_ylim(-2, 4)
ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('y', fontsize=12)
ax2.set_title('不可导：左右导数不相等', fontsize=14, fontweight='bold', color='darkred')
ax2.axhline(0, color='black', linewidth=0.5)
ax2.axvline(0, color='black', linewidth=0.5)
ax2.grid(True, alpha=0.3)
ax2.legend(loc='upper center', fontsize=10)

fig.suptitle('导数存在的条件：左导数 = 右导数', fontsize=16, fontweight='bold', y=1.02)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.2.10_图2_左右导数对比.png'), dpi=200, bbox_inches='tight')
plt.close()

print("配图生成完成！")
