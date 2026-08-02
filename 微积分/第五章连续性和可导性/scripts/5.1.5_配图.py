import matplotlib.pyplot as plt
import numpy as np
import os

# 设置中文字体
plt.rcParams['font.family'] = ['Hiragino Sans GB', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# 输出目录
output_dir = os.path.join(os.path.dirname(__file__), '..', 'imgs')
os.makedirs(output_dir, exist_ok=True)

# ========== 图1：奇数次多项式必有根 ==========
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# 左图：一个具体的奇数次多项式
ax1 = axes[0]

x = np.linspace(-3, 3, 400)
y = x**3 - 3*x + 1
ax1.plot(x, y, 'b-', linewidth=2.5, label=r'$p(x) = x^3 - 3x + 1$')

# x轴
ax1.axhline(0, color='black', linewidth=1)

# 找到根（近似）
roots = []
for guess in [-2, 0, 2]:
    # 简单牛顿迭代
    r = guess
    for _ in range(20):
        r = r - (r**3 - 3*r + 1) / (3*r**2 - 3)
    if -3 < r < 3:
        roots.append(r)

roots = sorted(set([round(r, 2) for r in roots]))
for r in roots:
    ax1.plot(r, 0, 'mo', markersize=10, zorder=5)
    ax1.text(r, 0.4, f'根', fontsize=9, color='purple', ha='center')

# 标记两端的行为
ax1.text(-2.5, -10, r'$x \to -\infty$' + '\n' + r'$p(x) \to -\infty$', fontsize=10, color='red',
         bbox=dict(boxstyle='round', facecolor='white', edgecolor='red', alpha=0.7))
ax1.text(1.5, 10, r'$x \to +\infty$' + '\n' + r'$p(x) \to +\infty$', fontsize=10, color='green',
         bbox=dict(boxstyle='round', facecolor='white', edgecolor='green', alpha=0.7))

ax1.set_xlim(-3, 3)
ax1.set_ylim(-12, 14)
ax1.axvline(0, color='black', linewidth=0.5)
ax1.set_title(r'奇数次多项式 $p(x) = x^3 - 3x + 1$', fontsize=14)
ax1.set_xlabel('x', fontsize=12)
ax1.set_ylabel('y', fontsize=12)
ax1.grid(True, alpha=0.3)
ax1.legend(loc='upper left', fontsize=11)

# 右图：两端趋向相反的无穷
ax2 = axes[1]

x = np.linspace(-4, 4, 400)
y = x**3
ax2.plot(x, y, 'b-', linewidth=2.5, label=r'$p(x) = x^3$（首项主导）')

ax2.axhline(0, color='black', linewidth=1)

# 标记A和B
A, B = -3, 3
p_A = A**3
p_B = B**3

ax2.plot(A, p_A, 'ro', markersize=10)
ax2.plot(B, p_B, 'go', markersize=10)

ax2.text(A, p_A - 8, r'$p(A) < 0$', fontsize=11, color='red', ha='center')
ax2.text(B, p_B + 3, r'$p(B) > 0$', fontsize=11, color='green', ha='center')

# 介值定理
ax2.annotate('', xy=(B, 0), xytext=(A, 0),
            arrowprops=dict(arrowstyle='<->', color='orange', lw=2))
ax2.text(0, 2, '介值定理：\n必有根', fontsize=11, color='orange', ha='center',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

ax2.set_xlim(-4, 4)
ax2.set_ylim(-40, 40)
ax2.axvline(0, color='black', linewidth=0.5)
ax2.set_title(r'奇数次：两端趋向相反的无穷', fontsize=14)
ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('y', fontsize=12)
ax2.grid(True, alpha=0.3)
ax2.legend(loc='upper left', fontsize=11)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.5_图1_奇数次必有根.png'), dpi=200, bbox_inches='tight')
plt.close()

# ========== 图2：p(x) 和首项 a_n x^n 的关系 ==========
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 左图：x 很大时，p(x) ≈ a_n x^n
ax1 = axes[0]

x = np.linspace(5, 15, 300)
p_x = x**3 - 3*x + 1
leading = x**3

ax1.plot(x, p_x, 'b-', linewidth=2.5, label=r'$p(x) = x^3 - 3x + 1$')
ax1.plot(x, leading, 'r--', linewidth=1.5, label=r'$a_n x^n = x^3$（首项）')

# 放大显示差异很小
ax1.set_xlim(5, 15)
ax1.set_ylim(80, 3400)
ax1.set_title(r'$|x|$ 很大时：$p(x) \approx a_n x^n$', fontsize=14)
ax1.set_xlabel('x', fontsize=12)
ax1.set_ylabel('y', fontsize=12)
ax1.grid(True, alpha=0.3)
ax1.legend(loc='upper left', fontsize=11)

# 右图：比值趋近于1
ax2 = axes[1]

x = np.linspace(1, 20, 300)
ratio = (x**3 - 3*x + 1) / x**3

ax2.plot(x, ratio, 'b-', linewidth=2.5)
ax2.axhline(1, color='red', linestyle='--', linewidth=1.5, label='y = 1')

ax2.set_xlim(0, 20)
ax2.set_ylim(0.5, 1.2)
ax2.set_title(r'比值 $\frac{p(x)}{a_n x^n} \to 1$（当 $x \to \infty$）', fontsize=14)
ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel(r'$\frac{p(x)}{a_n x^n}$', fontsize=13)
ax2.grid(True, alpha=0.3)
ax2.legend(loc='lower right', fontsize=11)

ax2.text(10, 0.85, '比值越来越接近 1\n说明两者符号相同', fontsize=10,
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.5_图2_首项主导.png'), dpi=200, bbox_inches='tight')
plt.close()

# ========== 图3：证明思路流程图 ==========
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis('off')

# 定义框的绘制函数
def draw_box(ax, x, y, w, h, text, color='lightblue', fontsize=11):
    rect = plt.Rectangle((x - w/2, y - h/2), w, h,
                          facecolor=color, edgecolor='black', linewidth=1.5, alpha=0.8)
    ax.add_patch(rect)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize, wrap=True)

def draw_arrow(ax, x1, y1, x2, y2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

# 步骤1
draw_box(ax, 6, 9, 10, 0.8, '设 p(x) 是奇数次多项式，首项为 $a_n x^n$（n 为奇数）', 'lightyellow', 12)

# 步骤2
draw_arrow(ax, 6, 8.5, 6, 8.0)
draw_box(ax, 6, 7.6, 10, 0.8, '当 |x| 很大时，p(x) 和首项 a_n x^n 几乎一样\n两者符号相同', 'lightblue', 12)

# 步骤3：分支
draw_arrow(ax, 6, 7.2, 3, 6.5)
draw_arrow(ax, 6, 7.2, 9, 6.5)

# 左分支
draw_box(ax, 3, 6.1, 4.5, 0.8, '取 A 为很大的负数\np(A) 与 a_n*A^n 同号', 'lightcoral', 11)
draw_arrow(ax, 3, 5.7, 3, 5.2)
draw_box(ax, 3, 4.8, 4.5, 0.8, 'n 为奇数\na_n*A^n < 0', 'lightcoral', 11)

# 右分支
draw_box(ax, 9, 6.1, 4.5, 0.8, '取 B 为很大的正数\np(B) 与 a_n*B^n 同号', 'lightgreen', 11)
draw_arrow(ax, 9, 5.7, 9, 5.2)
draw_box(ax, 9, 4.8, 4.5, 0.8, 'n 为奇数\na_n*B^n > 0', 'lightgreen', 11)

# 汇合
draw_arrow(ax, 3, 4.4, 6, 3.8)
draw_arrow(ax, 9, 4.4, 6, 3.8)
draw_box(ax, 6, 3.4, 10, 0.8, '因此 p(A) < 0 且 p(B) > 0，符号相反！', 'lightyellow', 12)

# 结论
draw_arrow(ax, 6, 3.0, 6, 2.4)
draw_box(ax, 6, 1.8, 10, 1.0, 'p 是多项式，处处连续\n由介值定理：存在 c 在 (A, B) 之间使得 p(c) = 0\n即奇数次多项式至少有一个根', 'lightgreen', 12)

ax.set_title('证明思路：奇数次多项式必有根', fontsize=16, pad=20)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.5_图3_证明思路.png'), dpi=200, bbox_inches='tight')
plt.close()

print("配图生成完成！")
