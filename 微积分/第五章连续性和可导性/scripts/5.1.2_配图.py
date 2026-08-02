import matplotlib.pyplot as plt
import numpy as np
import os

# 设置中文字体
plt.rcParams['font.family'] = ['Hiragino Sans GB', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# 输出目录
output_dir = os.path.join(os.path.dirname(__file__), '..', 'imgs')
os.makedirs(output_dir, exist_ok=True)

# ========== 图0：开区间 (a,b) 上的连续 ==========
fig, ax = plt.subplots(figsize=(10, 6))

# 画一条在 (a,b) 上的曲线，端点用空心圆表示（不包含）
a, b = 1.0, 4.0
x = np.linspace(a + 0.05, b - 0.05, 300)
y = 0.5 * np.sin(x - 2) + 2.5
ax.plot(x, y, 'b-', linewidth=2.5)

# 端点用空心圆表示（不在开区间内）
f_a = 0.5 * np.sin(a + 0.05 - 2) + 2.5
f_b = 0.5 * np.sin(b - 0.05 - 2) + 2.5
ax.plot(a, f_a, 'bo', markersize=10, fillstyle='none', markeredgewidth=2)
ax.plot(b, f_b, 'bo', markersize=10, fillstyle='none', markeredgewidth=2)

# 端点标签 - 用黑色与蓝色空心圆区分
ax.text(a - 0.15, f_a - 0.4, 'a（不在区间内）', fontsize=11, color='black', ha='right', fontweight='bold')
ax.text(b + 0.15, f_b - 0.4, 'b（不在区间内）', fontsize=11, color='black', ha='left', fontweight='bold')

# 内部某点 c，展示双侧极限
c = 2.5
f_c = 0.5 * np.sin(c - 2) + 2.5
ax.plot(c, f_c, 'go', markersize=10, zorder=5)

# 双侧极限箭头
ax.annotate('', xy=(c - 0.4, 0.5 * np.sin(c - 0.4 - 2) + 2.5), xytext=(c - 0.05, f_c),
            arrowprops=dict(arrowstyle='->', color='green', lw=2))
ax.annotate('', xy=(c + 0.4, 0.5 * np.sin(c + 0.4 - 2) + 2.5), xytext=(c + 0.05, f_c),
            arrowprops=dict(arrowstyle='->', color='green', lw=2))
# 文字用黑色与绿色点区分，放在点上方避免重叠
ax.text(c, f_c + 0.45, '区间内任意点 c\n双侧连续', fontsize=10, color='black', ha='center', fontweight='bold')

# 区间标注（开区间，端点空心）
ax.annotate('', xy=(b, -0.3), xytext=(a, -0.3),
            arrowprops=dict(arrowstyle='<->', color='green', lw=2))
ax.text((a + b) / 2, -0.65, '开区间 $(a, b)$', fontsize=12, color='black', ha='center', fontweight='bold')

# 虚线表示区间范围
ax.axvline(a, color='gray', linestyle=':', alpha=0.5, ymax=0.85)
ax.axvline(b, color='gray', linestyle=':', alpha=0.5, ymax=0.85)

# 强调：端点不需要检查
ax.text(a, 0.3, '不检查', fontsize=10, color='darkred', ha='center',
        bbox=dict(boxstyle='round', facecolor='white', edgecolor='red', alpha=0.7))
ax.text(b, 0.3, '不检查', fontsize=10, color='darkred', ha='center',
        bbox=dict(boxstyle='round', facecolor='white', edgecolor='red', alpha=0.7))

ax.set_xlim(0, 5)
ax.set_ylim(-1, 4)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_title('开区间 $(a, b)$ 上的连续', fontsize=15)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.2_图0_开区间连续.png'), dpi=200, bbox_inches='tight')
plt.close()

# ========== 图1：闭区间 [a,b] 上的连续 ==========
fig, ax = plt.subplots(figsize=(10, 6))

# 画一条在 [a,b] 上连续的曲线
a, b = 1.0, 4.0
x = np.linspace(a, b, 300)
y = 0.5 * np.sin(x - 2) + 2.5
ax.plot(x, y, 'b-', linewidth=2.5)

# 标记端点（实心，表示包含在区间内）
f_a = 0.5 * np.sin(a - 2) + 2.5
f_b = 0.5 * np.sin(b - 2) + 2.5
ax.plot(a, f_a, 'bo', markersize=10)
ax.plot(b, f_b, 'bo', markersize=10)

# 端点标签 - 黑色与蓝色端点区分
ax.text(a - 0.15, f_a - 0.4, '$(a, f(a))$', fontsize=11, color='black', ha='right', fontweight='bold')
ax.text(b + 0.15, f_b - 0.4, '$(b, f(b))$', fontsize=11, color='black', ha='left', fontweight='bold')

# 在 a 处只有右极限（左边没有定义）
ax.annotate('', xy=(a + 0.4, 0.5 * np.sin(a + 0.4 - 2) + 2.5), xytext=(a, f_a),
            arrowprops=dict(arrowstyle='->', color='orange', lw=2))
# 文字放在箭头右侧上方，避免重叠
ax.text(a + 0.5, f_a + 0.55, '右连续\n（只看右边）', fontsize=10, color='black')

# 在 b 处只有左极限（右边没有定义）
ax.annotate('', xy=(b - 0.4, 0.5 * np.sin(b - 0.4 - 2) + 2.5), xytext=(b, f_b),
            arrowprops=dict(arrowstyle='->', color='orange', lw=2))
# 文字放在箭头左侧上方，避免重叠
ax.text(b - 0.9, f_b + 0.55, '左连续\n（只看左边）', fontsize=10, color='black')

# 区间标注
ax.annotate('', xy=(b, -0.3), xytext=(a, -0.3),
            arrowprops=dict(arrowstyle='<->', color='green', lw=2))
ax.text((a + b) / 2, -0.65, '区间 $[a, b]$', fontsize=12, color='black', ha='center', fontweight='bold')

# 虚线表示区间范围
ax.axvline(a, color='gray', linestyle=':', alpha=0.5, ymax=0.85)
ax.axvline(b, color='gray', linestyle=':', alpha=0.5, ymax=0.85)

# 内部某点 c，展示双侧极限
c = 2.5
f_c = 0.5 * np.sin(c - 2) + 2.5
ax.plot(c, f_c, 'go', markersize=8)
ax.text(c, f_c + 0.45, '区间内任意点 $c$\n双侧极限', fontsize=10, color='black', ha='center')

ax.set_xlim(0, 5)
ax.set_ylim(-1, 4)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_title('闭区间 $[a, b]$ 上的连续', fontsize=15)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.2_图1_闭区间连续.png'), dpi=200, bbox_inches='tight')
plt.close()

# ========== 图2：f(x)=1/x 在不同区间上的连续性 ==========
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 子图1：在 (0, +∞) 上连续
ax1 = axes[0]
x1 = np.linspace(0.1, 4, 200)
y1 = 1 / x1
ax1.plot(x1, y1, 'b-', linewidth=2.5)
ax1.axvline(0, color='gray', linestyle='--', alpha=0.7)
ax1.text(0.15, 8, '垂直渐近线\n$x=0$', fontsize=10, color='gray')
ax1.annotate('', xy=(3.5, 1/3.5), xytext=(0.5, 1/0.5),
            arrowprops=dict(arrowstyle='->', color='orange', lw=1.5))
ax1.set_xlim(-0.5, 4)
ax1.set_ylim(-1, 10)
ax1.set_title('$f(x) = \\frac{1}{x}$ 在 $(0, +\\infty)$ 上连续', fontsize=12)
ax1.set_xlabel('x', fontsize=11)
ax1.set_ylabel('y', fontsize=11)
ax1.grid(True, alpha=0.3)
ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)
ax1.text(2, 7, '0 不在区间内 ✓', fontsize=11, color='darkgreen',
         bbox=dict(boxstyle='round', facecolor='white', edgecolor='green', alpha=0.8))

# 子图2：在 (-∞, 0) 上连续
ax2 = axes[1]
x2 = np.linspace(-4, -0.1, 200)
y2 = 1 / x2
ax2.plot(x2, y2, 'b-', linewidth=2.5)
ax2.axvline(0, color='gray', linestyle='--', alpha=0.7)
ax2.text(0.15, -8, '垂直渐近线\n$x=0$', fontsize=10, color='gray')
ax2.set_xlim(-4, 0.5)
ax2.set_ylim(-10, 1)
ax2.set_title('$f(x) = \\frac{1}{x}$ 在 $(-\\infty, 0)$ 上连续', fontsize=12)
ax2.set_xlabel('x', fontsize=11)
ax2.set_ylabel('y', fontsize=11)
ax2.grid(True, alpha=0.3)
ax2.axhline(0, color='black', linewidth=0.5)
ax2.axvline(0, color='black', linewidth=0.5)
ax2.text(-2, -7, '0 不在区间内 ✓', fontsize=11, color='darkgreen',
         bbox=dict(boxstyle='round', facecolor='white', edgecolor='green', alpha=0.8))

# 子图3：在 (-2, 3) 上不连续
ax3 = axes[2]
x3_left = np.linspace(-2, -0.15, 100)
x3_right = np.linspace(0.15, 3, 100)
ax3.plot(x3_left, 1 / x3_left, 'b-', linewidth=2.5)
ax3.plot(x3_right, 1 / x3_right, 'b-', linewidth=2.5)
ax3.axvline(0, color='gray', linestyle='--', alpha=0.7)
ax3.set_xlim(-2.5, 3.5)
ax3.set_ylim(-10, 10)
ax3.set_title('$f(x) = \\frac{1}{x}$ 在 $(-2, 3)$ 上不连续', fontsize=12)
ax3.set_xlabel('x', fontsize=11)
ax3.set_ylabel('y', fontsize=11)
ax3.grid(True, alpha=0.3)
ax3.axhline(0, color='black', linewidth=0.5)
ax3.axvline(0, color='black', linewidth=0.5)

# 标注区间包含 0
ax3.annotate('', xy=(3, -0.5), xytext=(-2, -0.5),
            arrowprops=dict(arrowstyle='<->', color='red', lw=2))
ax3.text(0.5, -2, '区间 $(-2, 3)$', fontsize=11, color='black')
ax3.plot(0, 0, 'rx', markersize=12, markeredgewidth=2)
ax3.text(0.2, 2, '0 在区间内！\n$f(0)$ 无定义', fontsize=10, color='black',
         bbox=dict(boxstyle='round', facecolor='white', edgecolor='red', alpha=0.8))

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.2_图2_1x区间连续.png'), dpi=200, bbox_inches='tight')
plt.close()

# ========== 图3：单侧连续示意图 ==========
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 左图：右连续
ax1 = axes[0]
x_left = np.linspace(-1, 2, 150)
x_right = np.linspace(2, 4, 150)
y_left = -0.5 * (x_left - 2) + 3
y_right = 0.3 * (x_right - 2) + 2
ax1.plot(x_left, y_left, 'b-', linewidth=2.5)
ax1.plot(x_right, y_right, 'b-', linewidth=2.5)

a = 2.0
f_a = 2.0

# 左极限 ≠ 右极限，但只看右边时等于 f(a)
left_lim = 3.0
right_lim = 2.0

ax1.plot(a, f_a, 'go', markersize=10, zorder=5)
ax1.plot(a, left_lim, 'bo', markersize=10, fillstyle='none', markeredgewidth=2)

# 只画右极限的箭头
x_right_pts = [2.5, 3.0, 3.5]
for x_pt in x_right_pts:
    y_pt = 0.3 * (x_pt - 2) + 2
    ax1.plot(x_pt, y_pt, 'o', color='orange', markersize=5)
    ax1.annotate('', xy=(x_pt - 0.15, y_pt), xytext=(x_pt, y_pt),
                arrowprops=dict(arrowstyle='->', color='orange', lw=1.5))

# 文字标注全部用黑色，与图形元素区分
ax1.text(a + 0.2, f_a + 0.35, 'f(a)', fontsize=11, color='black', fontweight='bold')
ax1.text(a - 0.8, left_lim + 0.2, '左极限 ≠ f(a)', fontsize=10, color='black')
ax1.text(a + 0.9, right_lim + 0.35, '右极限 = f(a)', fontsize=10, color='black')
# 对勾用绿色单独标出
ax1.text(a + 2.0, right_lim + 0.35, '✓', fontsize=12, color='green', fontweight='bold')

# 标注"只看右边" - 放在箭头上方的空白区域
ax1.annotate('只看这一侧', xy=(3.2, 2.36), xytext=(3.5, 3.2),
             fontsize=11, color='black',
             arrowprops=dict(arrowstyle='->', color='orange'))

ax1.set_xlim(0, 4)
ax1.set_ylim(0.5, 4)
ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)
ax1.axvline(a, color='gray', linestyle=':', alpha=0.5)
ax1.set_title('右连续：$\\lim_{x \\to a^+} f(x) = f(a)$', fontsize=14)
ax1.set_xlabel('x', fontsize=12)
ax1.set_ylabel('y', fontsize=12)
ax1.grid(True, alpha=0.3)

# 右图：左连续
ax2 = axes[1]
x_left = np.linspace(0, 2, 150)
x_right = np.linspace(2, 5, 150)
y_left = -0.3 * (x_left - 2) + 3
y_right = 0.5 * (x_right - 2) + 2
ax2.plot(x_left, y_left, 'b-', linewidth=2.5)
ax2.plot(x_right, y_right, 'b-', linewidth=2.5)

b = 2.0
f_b = 3.0

left_lim = 3.0
right_lim = 2.0

ax2.plot(b, f_b, 'go', markersize=10, zorder=5)
ax2.plot(b, right_lim, 'bo', markersize=10, fillstyle='none', markeredgewidth=2)

# 只画左极限的箭头
x_left_pts = [1.5, 1.0, 0.5]
for x_pt in x_left_pts:
    y_pt = -0.3 * (x_pt - 2) + 3
    ax2.plot(x_pt, y_pt, 'o', color='orange', markersize=5)
    ax2.annotate('', xy=(x_pt + 0.15, y_pt), xytext=(x_pt, y_pt),
                arrowprops=dict(arrowstyle='->', color='orange', lw=1.5))

# 文字标注全部用黑色
ax2.text(b - 0.25, f_b + 0.35, 'f(b)', fontsize=11, color='black', ha='right', fontweight='bold')
ax2.text(b + 0.4, right_lim + 0.2, '右极限 ≠ f(b)', fontsize=10, color='black')
ax2.text(b - 1.4, left_lim + 0.2, '左极限 = f(b)', fontsize=10, color='black')
# 对勾用绿色单独标出
ax2.text(b - 2.1, left_lim + 0.2, '✓', fontsize=12, color='green', fontweight='bold')

# 标注"只看左边" - 放在箭头上方的空白区域
ax2.annotate('只看这一侧', xy=(0.8, 2.64), xytext=(0.1, 3.5),
             fontsize=11, color='black',
             arrowprops=dict(arrowstyle='->', color='orange'))

ax2.set_xlim(0, 5)
ax2.set_ylim(0.5, 4)
ax2.axhline(0, color='black', linewidth=0.5)
ax2.axvline(0, color='black', linewidth=0.5)
ax2.axvline(b, color='gray', linestyle=':', alpha=0.5)
ax2.set_title('左连续：$\\lim_{x \\to b^-} f(x) = f(b)$', fontsize=14)
ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('y', fontsize=12)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.2_图3_单侧连续.png'), dpi=200, bbox_inches='tight')
plt.close()

print("配图生成完成！")
