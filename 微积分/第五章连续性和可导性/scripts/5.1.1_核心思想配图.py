import matplotlib.pyplot as plt
import numpy as np
import os

# 设置中文字体
plt.rcParams['font.family'] = ['Hiragino Sans GB', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# 输出目录
output_dir = os.path.join(os.path.dirname(__file__), '..', 'imgs')
os.makedirs(output_dir, exist_ok=True)

# ========== 图：连续的核心思想 ==========
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# 左图：连续 —— x→a 时 f(x)→f(a)
ax1 = axes[0]

# 画一条光滑的连续曲线
x = np.linspace(0, 4, 300)
y = 0.8 * np.sin(x - 1) + 2.5
ax1.plot(x, y, 'b-', linewidth=2.5)

# 标记点 a
a = 2.0
f_a = 0.8 * np.sin(a - 1) + 2.5
ax1.plot(a, f_a, 'go', markersize=12, zorder=5)

# 从左边趋近的点和箭头
x_left_points = [1.2, 1.5, 1.8]
for x_pt in x_left_points:
    y_pt = 0.8 * np.sin(x_pt - 1) + 2.5
    ax1.plot(x_pt, y_pt, 'o', color='orange', markersize=6, zorder=4)
    ax1.annotate('', xy=(x_pt + 0.12, y_pt), xytext=(x_pt, y_pt),
                arrowprops=dict(arrowstyle='->', color='orange', lw=1.8))

# 从右边趋近的点和箭头
x_right_points = [2.8, 2.5, 2.2]
for x_pt in x_right_points:
    y_pt = 0.8 * np.sin(x_pt - 1) + 2.5
    ax1.plot(x_pt, y_pt, 'o', color='orange', markersize=6, zorder=4)
    ax1.annotate('', xy=(x_pt - 0.12, y_pt), xytext=(x_pt, y_pt),
                arrowprops=dict(arrowstyle='->', color='orange', lw=1.8))

# 标注 a 和 f(a)
ax1.axvline(a, color='gray', linestyle=':', alpha=0.5, ymax=0.85)
ax1.axhline(f_a, color='gray', linestyle=':', alpha=0.5, xmax=0.85)
ax1.text(a + 0.1, 0.8, '$x = a$', fontsize=11, color='gray')
ax1.text(0.3, f_a + 0.15, '$f(a)$', fontsize=11, color='green')

# 标注趋近过程
ax1.annotate('x 从左边靠近 a\nf(x) 靠近 f(a)',
             xy=(1.5, 0.8 * np.sin(1.5 - 1) + 2.5),
             textcoords="offset points", xytext=(-60, -40),
             fontsize=10, color='orange',
             arrowprops=dict(arrowstyle='->', color='orange'))

ax1.annotate('x 从右边靠近 a\nf(x) 也靠近 f(a)',
             xy=(2.5, 0.8 * np.sin(2.5 - 1) + 2.5),
             textcoords="offset points", xytext=(20, -40),
             fontsize=10, color='orange',
             arrowprops=dict(arrowstyle='->', color='orange'))

ax1.set_xlim(0, 4)
ax1.set_ylim(1, 4)
ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)
ax1.set_title('连续：$\\lim_{x \\to a} f(x) = f(a)$', fontsize=14)
ax1.set_xlabel('x', fontsize=12)
ax1.set_ylabel('y', fontsize=12)
ax1.grid(True, alpha=0.3)

# 右图：不连续 —— 必须"抬笔"
ax2 = axes[1]

# 左半段
x_left = np.linspace(0, 2, 150)
y_left = 0.5 * x_left + 1.2
ax2.plot(x_left, y_left, 'b-', linewidth=2.5)

# 右半段
x_right = np.linspace(2, 4, 150)
y_right = 0.5 * x_right + 2.8
ax2.plot(x_right, y_right, 'b-', linewidth=2.5)

a = 2.0
left_lim = 0.5 * a + 1.2   # 2.2
right_lim = 0.5 * a + 2.8  # 3.8

# 空心点表示极限
ax2.plot(a, left_lim, 'bo', markersize=10, fillstyle='none', markeredgewidth=2)
ax2.plot(a, right_lim, 'bo', markersize=10, fillstyle='none', markeredgewidth=2)

# 从左边趋近
x_left_pts = [1.2, 1.5, 1.8]
for x_pt in x_left_pts:
    y_pt = 0.5 * x_pt + 1.2
    ax2.plot(x_pt, y_pt, 'o', color='orange', markersize=6)
    ax2.annotate('', xy=(x_pt + 0.12, y_pt), xytext=(x_pt, y_pt),
                arrowprops=dict(arrowstyle='->', color='orange', lw=1.8))

# 从右边趋近
x_right_pts = [2.8, 2.5, 2.2]
for x_pt in x_right_pts:
    y_pt = 0.5 * x_pt + 2.8
    ax2.plot(x_pt, y_pt, 'o', color='orange', markersize=6)
    ax2.annotate('', xy=(x_pt - 0.12, y_pt), xytext=(x_pt, y_pt),
                arrowprops=dict(arrowstyle='->', color='orange', lw=1.8))

# 垂直渐近/间断线
ax2.axvline(a, color='gray', linestyle=':', alpha=0.5)
ax2.text(a + 0.1, 0.8, '$x = a$', fontsize=11, color='gray')

# 标注极限值
ax2.annotate('左极限 = 2.2', xy=(a, left_lim), textcoords="offset points",
             xytext=(-70, 5), fontsize=10, color='blue',
             arrowprops=dict(arrowstyle='->', color='blue'))
ax2.annotate('右极限 = 3.8', xy=(a, right_lim), textcoords="offset points",
             xytext=(15, -15), fontsize=10, color='blue',
             arrowprops=dict(arrowstyle='->', color='blue'))

# 标注"断了"
ax2.annotate('', xy=(a - 0.05, 3.0), xytext=(a + 0.05, 3.0),
            arrowprops=dict(arrowstyle='<->', color='red', lw=2))
ax2.text(a + 0.15, 3.0, '断了！', fontsize=11, color='red',
         verticalalignment='center')

ax2.set_xlim(0, 4)
ax2.set_ylim(0.5, 4.5)
ax2.axhline(0, color='black', linewidth=0.5)
ax2.axvline(0, color='black', linewidth=0.5)
ax2.set_title('不连续：左右极限不相等', fontsize=14)
ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('y', fontsize=12)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.1_图3_核心思想.png'), dpi=200, bbox_inches='tight')
plt.close()

print("配图生成完成！")
