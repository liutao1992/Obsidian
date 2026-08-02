import matplotlib.pyplot as plt
import numpy as np
import os

# 设置中文字体
plt.rcParams['font.family'] = ['Hiragino Sans GB', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# 输出目录
output_dir = os.path.join(os.path.dirname(__file__), '..', 'imgs')
os.makedirs(output_dir, exist_ok=True)

# ========== 图1：四种有最大最小值的情况 ==========
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

a, b = 0, 4

def setup_axis(ax, title):
    ax.set_xlim(-0.5, 4.5)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_title(title, fontsize=13)
    ax.set_xlabel('x', fontsize=11)
    ax.set_ylabel('y', fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.axvline(a, color='gray', linestyle=':', alpha=0.5)
    ax.axvline(b, color='gray', linestyle=':', alpha=0.5)
    ax.text(a, -0.8, 'a', fontsize=11, color='gray', ha='center')
    ax.text(b, -0.8, 'b', fontsize=11, color='gray', ha='center')

# 子图1：最大值和最小值都在内部
ax1 = axes[0, 0]
setup_axis(ax1, '最大值和最小值都在区间内部')
x = np.linspace(a, b, 300)
y = -0.5 * (x - 1)**2 + 3 + 0.3 * np.sin(2*x)
ax1.plot(x, y, 'b-', linewidth=2.5)
# 最大值在 x=1
ax1.plot(1, 3, 'r^', markersize=12, zorder=5)
ax1.text(1, 3.3, '最大值', fontsize=10, color='red', ha='center')
# 最小值在 x≈3.5
min_idx = np.argmin(y)
min_x = x[min_idx]
min_y = y[min_idx]
ax1.plot(min_x, min_y, 'gv', markersize=12, zorder=5)
ax1.text(min_x, min_y - 0.5, '最小值', fontsize=10, color='green', ha='center')
ax1.set_ylim(-1, 5)

# 子图2：最小值在左端点
ax2 = axes[0, 1]
setup_axis(ax2, '最小值在左端点 x = a')
x = np.linspace(a, b, 300)
y = 0.3 * (x - 1)**2 + 0.5
ax2.plot(x, y, 'b-', linewidth=2.5)
# 最大值在 x=b
ax2.plot(b, y[-1], 'r^', markersize=12, zorder=5)
ax2.text(b, y[-1] + 0.3, '最大值', fontsize=10, color='red', ha='center')
# 最小值在 x=a
ax2.plot(a, y[0], 'gv', markersize=12, zorder=5)
ax2.text(a, y[0] - 0.5, '最小值', fontsize=10, color='green', ha='center')
ax2.set_ylim(-0.5, 4)

# 子图3：最大值在右端点，多个最小值
ax3 = axes[1, 0]
setup_axis(ax3, '最大值在右端点，多个最小值')
x = np.linspace(a, b, 300)
y = 0.3 * (x - 2)**4 - 1.5 * (x - 2)**2 + 3
ax3.plot(x, y, 'b-', linewidth=2.5)
# 最大值在 x=b
ax3.plot(b, y[-1], 'r^', markersize=12, zorder=5)
ax3.text(b, y[-1] + 0.3, '最大值', fontsize=10, color='red', ha='center')
# 两个最小值
ax3.plot(0.5, 0.3*(0.5-2)**4 - 1.5*(0.5-2)**2 + 3, 'gv', markersize=10, zorder=5)
ax3.plot(3.5, 0.3*(3.5-2)**4 - 1.5*(3.5-2)**2 + 3, 'gv', markersize=10, zorder=5)
ax3.text(2, 0.5, '两个最小值 ✓', fontsize=10, color='green', ha='center')
ax3.set_ylim(-1, 5)

# 子图4：常数函数
ax4 = axes[1, 1]
setup_axis(ax4, '常数函数：每点都是最大/最小值')
x = np.linspace(a, b, 300)
y = np.ones_like(x) * 2
ax4.plot(x, y, 'b-', linewidth=2.5)
ax4.plot(1, 2, 'r^', markersize=10, zorder=5)
ax4.plot(2, 2, 'gv', markersize=10, zorder=5)
ax4.plot(3, 2, 'r^', markersize=10, zorder=5)
ax4.text(2, 2.5, '每一点都是最大值\n也是最小值', fontsize=10, color='purple', ha='center')
ax4.set_ylim(0, 4)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.6_图1_四种情况.png'), dpi=200, bbox_inches='tight')
plt.close()

# ========== 图2：反例 ==========
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 左图：不连续函数（渐近线）无最大最小值
ax1 = axes[0]
ax1.set_xlim(-0.5, 4.5)
ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)
ax1.set_title('不连续函数：无最大值，无最小值', fontsize=14)
ax1.set_xlabel('x', fontsize=12)
ax1.set_ylabel('y', fontsize=12)
ax1.grid(True, alpha=0.3)

# 渐近线在 x=2
x_left = np.linspace(0, 1.9, 100)
x_right = np.linspace(2.1, 4, 100)
ax1.plot(x_left, 1/(x_left - 2), 'b-', linewidth=2.5)
ax1.plot(x_right, 1/(x_right - 2), 'b-', linewidth=2.5)
ax1.axvline(2, color='gray', linestyle='--', linewidth=1.5, alpha=0.7)
ax1.text(2.2, 5, '渐近线\nx=2', fontsize=10, color='gray')

# 标注区间
ax1.axvline(0, color='gray', linestyle=':', alpha=0.5)
ax1.axvline(4, color='gray', linestyle=':', alpha=0.5)
ax1.text(0, -6, 'a', fontsize=11, color='gray', ha='center')
ax1.text(4, -6, 'b', fontsize=11, color='gray', ha='center')

ax1.annotate('无限上升\n无最大值', xy=(1.5, -5), textcoords="offset points",
             xytext=(-50, 30), fontsize=10, color='red',
             arrowprops=dict(arrowstyle='->', color='red'))
ax1.annotate('无限下降\n无最小值', xy=(2.5, 5), textcoords="offset points",
             xytext=(20, 30), fontsize=10, color='red',
             arrowprops=dict(arrowstyle='->', color='red'))

ax1.set_ylim(-10, 10)

# 右图：开区间连续函数无最大值
ax2 = axes[1]
ax2.set_xlim(-0.5, 4.5)
ax2.axhline(0, color='black', linewidth=0.5)
ax2.axvline(0, color='black', linewidth=0.5)
ax2.set_title('开区间上的连续函数：无最大值', fontsize=14)
ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('y', fontsize=12)
ax2.grid(True, alpha=0.3)

# 只在 (0, 4) 上定义
x = np.linspace(0.05, 3.95, 300)
y = -0.5 * (x - 2)**2 + 3.5
ax2.plot(x, y, 'b-', linewidth=2.5)

# 空心端点
ax2.plot(0, -0.5*(0-2)**2 + 3.5, 'bo', markersize=10, fillstyle='none', markeredgewidth=2)
ax2.plot(4, -0.5*(4-2)**2 + 3.5, 'bo', markersize=10, fillstyle='none', markeredgewidth=2)

# 标注开区间
ax2.annotate('', xy=(3.9, -0.5), xytext=(0.1, -0.5),
            arrowprops=dict(arrowstyle='<->', color='orange', lw=2))
ax2.text(2, -0.9, '开区间 (a, b)', fontsize=11, color='orange', ha='center')

# 最小值在 x=2
ax2.plot(2, 3.5, 'gv', markersize=10, zorder=5)
ax2.text(2, 3.9, '最小值 ✓', fontsize=10, color='green', ha='center')

# 最大值应该在 x=0 附近，但 x=0 不在区间内
ax2.annotate('最大值应该在这里\n但 x=a 不在区间内！', xy=(0.1, 3.45), textcoords="offset points",
             xytext=(30, 30), fontsize=10, color='red',
             arrowprops=dict(arrowstyle='->', color='red'))
ax2.text(1, 2.5, '无论多接近 a\n总有更接近的点', fontsize=10, color='red',
         bbox=dict(boxstyle='round', facecolor='white', edgecolor='red', alpha=0.5))

ax2.set_ylim(-1, 5)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.6_图2_反例.png'), dpi=200, bbox_inches='tight')
plt.close()

# ========== 图3：EVT核心结论 ==========
fig, ax = plt.subplots(figsize=(10, 6))

x = np.linspace(0.5, 4.5, 300)
y = 0.8 * np.sin(x) + 0.3 * np.cos(3*x) + 2
ax.plot(x, y, 'b-', linewidth=2.5)

# 找最大值和最小值
max_idx = np.argmax(y)
min_idx = np.argmin(y)
max_x, max_y = x[max_idx], y[max_idx]
min_x, min_y = x[min_idx], y[min_idx]

ax.plot(max_x, max_y, 'r^', markersize=14, zorder=5)
ax.plot(min_x, min_y, 'gv', markersize=14, zorder=5)

ax.annotate('最大值', xy=(max_x, max_y), textcoords="offset points",
            xytext=(10, 15), fontsize=12, color='red',
            arrowprops=dict(arrowstyle='->', color='red'))
ax.annotate('最小值', xy=(min_x, min_y), textcoords="offset points",
            xytext=(-30, -20), fontsize=12, color='green',
            arrowprops=dict(arrowstyle='->', color='green'))

# 区间标注
ax.axvline(0.5, color='gray', linestyle=':', alpha=0.5)
ax.axvline(4.5, color='gray', linestyle=':', alpha=0.5)
ax.text(0.5, 0.5, 'a', fontsize=12, color='gray', ha='center')
ax.text(4.5, 0.5, 'b', fontsize=12, color='gray', ha='center')

ax.annotate('', xy=(4.5, 0.3), xytext=(0.5, 0.3),
            arrowprops=dict(arrowstyle='<->', color='orange', lw=2))
ax.text(2.5, -0.1, '闭区间 [a, b]', fontsize=12, color='orange', ha='center')

# 水平参考线
ax.axhline(max_y, color='red', linestyle='--', alpha=0.3, xmax=0.85)
ax.axhline(min_y, color='green', linestyle='--', alpha=0.3, xmax=0.85)

ax.set_xlim(-0.2, 5.2)
ax.set_ylim(-0.5, 4.5)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_title('最大值与最小值定理：闭区间上的连续函数必有最大/最小值', fontsize=14)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.6_图3_EVT核心.png'), dpi=200, bbox_inches='tight')
plt.close()

print("配图生成完成！")
