import matplotlib.pyplot as plt
import numpy as np
import os

# 设置中文字体
plt.rcParams['font.family'] = ['Hiragino Sans GB', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# 输出目录
output_dir = os.path.join(os.path.dirname(__file__), '..', 'imgs')
os.makedirs(output_dir, exist_ok=True)

# ========== 图1：y = x² 连续函数 ==========
fig, ax = plt.subplots(figsize=(8, 6))

x = np.linspace(-3, 3, 400)
y = x**2

ax.plot(x, y, 'b-', linewidth=2.5, label=r'$y = x^2$')

# 标注几个点
for px in [-2, -1, 0, 1, 2]:
    py = px**2
    ax.plot(px, py, 'bo', markersize=7)
    ax.annotate(f'({px}, {py})', xy=(px, py), textcoords="offset points",
                xytext=(8, 8), fontsize=11)

ax.set_xlim(-3, 3)
ax.set_ylim(-1, 9)
ax.set_xlabel('x', fontsize=13)
ax.set_ylabel('y', fontsize=13)
ax.set_title('连续函数：可以一笔画出', fontsize=15)
ax.legend(loc='upper center', fontsize=12)
ax.grid(True, alpha=0.3)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1_图1_x2连续.png'), dpi=200, bbox_inches='tight')
plt.close()

# ========== 图2：y = 1/x 不连续函数 ==========
fig, ax = plt.subplots(figsize=(8, 6))

x_left = np.linspace(-3, -0.05, 200)
x_right = np.linspace(0.05, 3, 200)
y_left = 1 / x_left
y_right = 1 / x_right

ax.plot(x_left, y_left, 'r-', linewidth=2.5, label=r'$y = \frac{1}{x}$')
ax.plot(x_right, y_right, 'r-', linewidth=2.5)

# 垂直渐近线
ax.axvline(0, color='gray', linestyle='--', linewidth=1.5, alpha=0.7)
ax.text(0.15, 5, '垂直渐近线\n$x = 0$', fontsize=11, color='gray',
        verticalalignment='center')

# 标注不连续点
ax.plot(0, 0, 'rx', markersize=12, markeredgewidth=2)
ax.annotate('不连续点\n(无定义)', xy=(0, 0), textcoords="offset points",
            xytext=(25, -30), fontsize=11, color='red',
            arrowprops=dict(arrowstyle='->', color='red'))

# 标注左右两部分
ax.text(-2, 3, '左支', fontsize=13, color='darkred', alpha=0.8)
ax.text(2, 3, '右支', fontsize=13, color='darkred', alpha=0.8)

ax.set_xlim(-3, 3)
ax.set_ylim(-6, 6)
ax.set_xlabel('x', fontsize=13)
ax.set_ylabel('y', fontsize=13)
ax.set_title('不连续函数：图像被分成两部分', fontsize=15)
ax.legend(loc='upper right', fontsize=12)
ax.grid(True, alpha=0.3)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1_图2_1x不连续.png'), dpi=200, bbox_inches='tight')
plt.close()

# ========== 图3：连续性的直观对比 ==========
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 左图：连续
ax1 = axes[0]
x1 = np.linspace(-2, 2, 400)
y1 = x1**2
ax1.plot(x1, y1, 'b-', linewidth=2.5)
ax1.set_title('连续：$y = x^2$', fontsize=14)
ax1.set_xlim(-2, 2)
ax1.set_ylim(-0.5, 4.5)
ax1.grid(True, alpha=0.3)
ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)
ax1.set_xlabel('x', fontsize=12)
ax1.set_ylabel('y', fontsize=12)
# 画一笔画效果
ax1.annotate('', xy=(1.8, 3.24), xytext=(-1.8, 3.24),
            arrowprops=dict(arrowstyle='->', color='blue', lw=2))
ax1.text(0, 4, '一笔画出 ✓', fontsize=12, ha='center', color='blue')

# 右图：不连续
ax2 = axes[1]
x2_left = np.linspace(-2, -0.1, 100)
x2_right = np.linspace(0.1, 2, 100)
ax2.plot(x2_left, 1/x2_left, 'r-', linewidth=2.5)
ax2.plot(x2_right, 1/x2_right, 'r-', linewidth=2.5)
ax2.axvline(0, color='gray', linestyle='--', linewidth=1.5, alpha=0.7)
ax2.set_title('不连续：$y = \\frac{1}{x}$', fontsize=14)
ax2.set_xlim(-2, 2)
ax2.set_ylim(-5, 5)
ax2.grid(True, alpha=0.3)
ax2.axhline(0, color='black', linewidth=0.5)
ax2.axvline(0, color='black', linewidth=0.5)
ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('y', fontsize=12)
ax2.text(0, 4.5, '一笔画不出 ✗', fontsize=12, ha='center', color='red')
ax2.text(-1, 2.5, '断开了', fontsize=11, color='darkred', alpha=0.8)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1_图3_对比.png'), dpi=200, bbox_inches='tight')
plt.close()

print("配图生成完成！")
