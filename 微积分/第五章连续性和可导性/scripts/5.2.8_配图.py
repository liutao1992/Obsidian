import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams['font.family'] = ['Hiragino Sans GB', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

output_dir = os.path.join(os.path.dirname(__file__), '..', 'imgs')
os.makedirs(output_dir, exist_ok=True)

# ========== 图1：线性函数的导数 ==========
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

x = np.linspace(-2, 2, 100)

# 子图1：正斜率
ax1 = axes[0]
ax1.plot(x, 2*x + 1, color='navy', linewidth=2.5, label='$y = 2x + 1$')
ax1.axhline(0, color='black', linewidth=0.8)
ax1.axvline(0, color='black', linewidth=0.8)
ax1.set_xlim(-2, 2)
ax1.set_ylim(-4, 5)
ax1.set_xlabel('$x$', fontsize=12)
ax1.set_ylabel('$y$', fontsize=12)
ax1.set_title('斜率 m = 2 > 0\n$f^{\prime}(x) = 2$', fontsize=13, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.legend(loc='upper left', fontsize=11)
# 标注切线就是自身
ax1.annotate('切线就是这条直线本身', xy=(0, 1), xytext=(-1.5, 3),
            fontsize=10, color='red',
            arrowprops=dict(arrowstyle='->', color='red', lw=1.2))

# 子图2：负斜率
ax2 = axes[1]
ax2.plot(x, -1.5*x + 2, color='green', linewidth=2.5, label='$y = -1.5x + 2$')
ax2.axhline(0, color='black', linewidth=0.8)
ax2.axvline(0, color='black', linewidth=0.8)
ax2.set_xlim(-2, 2)
ax2.set_ylim(-2, 5)
ax2.set_xlabel('$x$', fontsize=12)
ax2.set_ylabel('$y$', fontsize=12)
ax2.set_title('斜率 m = -1.5 < 0\n$f^{\prime}(x) = -1.5$', fontsize=13, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.legend(loc='upper right', fontsize=11)

# 子图3：常数函数
ax3 = axes[2]
ax3.plot(x, 2*np.ones_like(x), color='purple', linewidth=2.5, label='$y = 2$')
ax3.axhline(0, color='black', linewidth=0.8)
ax3.axvline(0, color='black', linewidth=0.8)
ax3.set_xlim(-2, 2)
ax3.set_ylim(-1, 4)
ax3.set_xlabel('$x$', fontsize=12)
ax3.set_ylabel('$y$', fontsize=12)
ax3.set_title('斜率 m = 0（常数函数）\n$f^{\prime}(x) = 0$', fontsize=13, fontweight='bold')
ax3.grid(True, alpha=0.3)
ax3.legend(loc='upper center', fontsize=11)
# 标注水平
ax3.annotate('水平线，导数为0', xy=(0, 2), xytext=(0.5, 0.5),
            fontsize=10, color='red',
            arrowprops=dict(arrowstyle='->', color='red', lw=1.2))

fig.suptitle('线性函数的导数 = 斜率（常数）', fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.2.8_图1_线性函数的导数.png'), dpi=200, bbox_inches='tight')
plt.close()

print("配图生成完成！")
