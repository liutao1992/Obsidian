import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams['font.family'] = ['Hiragino Sans GB', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

output_dir = os.path.join(os.path.dirname(__file__), '..', 'imgs')
os.makedirs(output_dir, exist_ok=True)

fig, ax = plt.subplots(figsize=(8, 7))

x_left = np.linspace(-3, 0, 200)
x_right = np.linspace(0, 3, 200)

ax.plot(x_left, np.abs(x_left), color='navy', linewidth=2.5)
ax.plot(x_right, np.abs(x_right), color='navy', linewidth=2.5, label='y = |x|')

ax.plot(0, 0, 'ko', markersize=10, zorder=5)
ax.annotate('尖点\n(x = 0)', xy=(0, 0), xytext=(1.2, 1.5),
            fontsize=11,
            arrowprops=dict(arrowstyle='->', color='red', lw=1.5))

# 右侧割线/切线
ax.plot([0, 2], [0, 2], '--', color='green', linewidth=2)
ax.text(1.5, 2.2, '右侧斜率 = 1\n(右导数)', fontsize=10, color='green', fontweight='bold',
        ha='center')

# 左侧割线/切线
ax.plot([-2, 0], [2, 0], '--', color='blue', linewidth=2)
ax.text(-1.5, 2.2, '左侧斜率 = -1\n(左导数)', fontsize=10, color='blue', fontweight='bold',
        ha='center')

ax.text(0, -0.8, '左侧斜率 ≠ 右侧斜率\n导数不存在', fontsize=11, color='red',
        ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow', edgecolor='red', alpha=0.9))

ax.set_xlim(-3, 3)
ax.set_ylim(-1.5, 3.5)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('y = |x| 在 x = 0 处的尖点：左导数 ≠ 右导数', fontsize=14, fontweight='bold', pad=15)
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.grid(True, alpha=0.3)
ax.legend(loc='upper center', fontsize=11)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.2.10_图1_尖点不可导.png'), dpi=200, bbox_inches='tight')
plt.close()

print("配图生成完成！")
