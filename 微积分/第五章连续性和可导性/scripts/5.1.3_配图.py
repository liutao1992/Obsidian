import matplotlib.pyplot as plt
import numpy as np
import os

# 设置中文字体
plt.rcParams['font.family'] = ['Hiragino Sans GB', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# 输出目录
output_dir = os.path.join(os.path.dirname(__file__), '..', 'imgs')
os.makedirs(output_dir, exist_ok=True)

# ========== 图0：常数函数 f(x) = 1 的连续性 ==========
fig, ax = plt.subplots(figsize=(8, 6))

# 画常数函数 y = 1
x = np.linspace(-3, 3, 300)
y = np.ones_like(x)
ax.plot(x, y, 'b-', linewidth=2.5)

# 任取一点 a，展示连续性
a = 1.0
ax.plot(a, 1, 'go', markersize=10, zorder=5)

# 从左右两侧趋近 a 的箭头
ax.annotate('', xy=(a - 0.3, 1), xytext=(a - 0.05, 1),
            arrowprops=dict(arrowstyle='->', color='orange', lw=2))
ax.annotate('', xy=(a + 0.3, 1), xytext=(a + 0.05, 1),
            arrowprops=dict(arrowstyle='->', color='orange', lw=2))

# 标注
ax.text(a, 1.35, 'f(a) = 1', fontsize=12, color='black', ha='center', fontweight='bold')
ax.text(a - 0.8, 0.6, '左极限 = 1', fontsize=10, color='black')
ax.text(a + 0.2, 0.6, '右极限 = 1', fontsize=10, color='black')
ax.text(a, 0.15, 'lim f(x) = 1 = f(a) ✓', fontsize=11, color='black', ha='center')

ax.set_xlim(-3, 3)
ax.set_ylim(-0.5, 2.5)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_title('常数函数 $f(x) = 1$：处处连续', fontsize=14)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.3_图0_常数函数连续.png'), dpi=200, bbox_inches='tight')
plt.close()

# ========== 图1：恒等函数 g(x) = x 的连续性 ==========
fig, ax = plt.subplots(figsize=(8, 6))

# 画恒等函数 y = x
x = np.linspace(-3, 3, 300)
y = x
ax.plot(x, y, 'b-', linewidth=2.5)

# 任取一点 a，展示连续性
a = 1.5
ax.plot(a, a, 'go', markersize=10, zorder=5)

# 从左右两侧趋近 a 的箭头
ax.annotate('', xy=(a - 0.3, a - 0.3), xytext=(a - 0.05, a - 0.05),
            arrowprops=dict(arrowstyle='->', color='orange', lw=2))
ax.annotate('', xy=(a + 0.3, a + 0.3), xytext=(a + 0.05, a + 0.05),
            arrowprops=dict(arrowstyle='->', color='orange', lw=2))

# 标注
ax.text(a + 0.3, a + 0.5, 'g(a) = a', fontsize=12, color='black', fontweight='bold')
ax.text(a - 1.0, a - 0.6, '左极限 = a', fontsize=10, color='black')
ax.text(a + 0.4, a - 0.5, '右极限 = a', fontsize=10, color='black')
ax.text(a, a - 1.0, 'lim g(x) = a = g(a) ✓', fontsize=11, color='black', ha='center')

# 画虚线帮助看坐标
ax.plot([a, a], [0, a], 'k:', alpha=0.3)
ax.plot([0, a], [a, a], 'k:', alpha=0.3)
ax.text(a, -0.2, 'a', fontsize=11, color='black', ha='center')
ax.text(-0.2, a, 'a', fontsize=11, color='black', ha='right')

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_title('恒等函数 $g(x) = x$：处处连续', fontsize=14)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.3_图1_恒等函数连续.png'), dpi=200, bbox_inches='tight')
plt.close()

# ========== 图2：从 x 构造多项式 ==========
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 子图1：基础 g(x) = x
ax1 = axes[0, 0]
x = np.linspace(-2, 2, 300)
ax1.plot(x, x, 'b-', linewidth=2.5)
ax1.set_xlim(-2.5, 2.5)
ax1.set_ylim(-2.5, 2.5)
ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)
ax1.set_title('$g(x) = x$：连续', fontsize=13)
ax1.set_xlabel('x', fontsize=11)
ax1.set_ylabel('y', fontsize=11)
ax1.grid(True, alpha=0.3)
ax1.text(0.7, 1.5, '基础函数\n连续', fontsize=10, color='black',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

# 子图2：乘法得到 x²
ax2 = axes[0, 1]
ax2.plot(x, x**2, 'b-', linewidth=2.5)
ax2.set_xlim(-2.5, 2.5)
ax2.set_ylim(-1, 5)
ax2.axhline(0, color='black', linewidth=0.5)
ax2.axvline(0, color='black', linewidth=0.5)
ax2.set_title('$x^2 = x \\cdot x$：连续', fontsize=13)
ax2.set_xlabel('x', fontsize=11)
ax2.set_ylabel('y', fontsize=11)
ax2.grid(True, alpha=0.3)
ax2.text(0.8, 3.5, '连续 × 连续\n= 连续', fontsize=10, color='black',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

# 子图3：再乘得到 x³
ax3 = axes[1, 0]
ax3.plot(x, x**3, 'b-', linewidth=2.5)
ax3.set_xlim(-2.5, 2.5)
ax3.set_ylim(-8, 8)
ax3.axhline(0, color='black', linewidth=0.5)
ax3.axvline(0, color='black', linewidth=0.5)
ax3.set_title('$x^3 = x^2 \\cdot x$：连续', fontsize=13)
ax3.set_xlabel('x', fontsize=11)
ax3.set_ylabel('y', fontsize=11)
ax3.grid(True, alpha=0.3)
ax3.text(1.0, 5, '再乘一次\n仍然连续', fontsize=10, color='black',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

# 子图4：多项式 P(x) = x³ - 2x + 1
ax4 = axes[1, 1]
P = x**3 - 2*x + 1
ax4.plot(x, P, 'b-', linewidth=2.5)
ax4.set_xlim(-2.5, 2.5)
ax4.set_ylim(-8, 8)
ax4.axhline(0, color='black', linewidth=0.5)
ax4.axvline(0, color='black', linewidth=0.5)
ax4.set_title('$P(x) = x^3 - 2x + 1$：连续', fontsize=13)
ax4.set_xlabel('x', fontsize=11)
ax4.set_ylabel('y', fontsize=11)
ax4.grid(True, alpha=0.3)
ax4.text(0.5, 5, '常数倍 + 相加\n仍然连续', fontsize=10, color='black',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.3_图2_多项式构造.png'), dpi=200, bbox_inches='tight')
plt.close()

# ========== 图3：f(x) = x * sin(1/x) 在 x=0 处有洞 ==========
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 左图：整体视图
ax1 = axes[0]
x_pos = np.linspace(0.02, 0.3, 500)
x_neg = np.linspace(-0.3, -0.02, 500)
y_pos = x_pos * np.sin(1 / x_pos)
y_neg = x_neg * np.sin(1 / x_neg)

ax1.plot(x_pos, y_pos, 'b-', linewidth=1.2)
ax1.plot(x_neg, y_neg, 'b-', linewidth=1.2)

# 包络线
ax1.plot(x_pos, x_pos, 'r--', linewidth=1, alpha=0.5, label='$y = x$')
ax1.plot(x_pos, -x_pos, 'r--', linewidth=1, alpha=0.5, label='$y = -x$')
ax1.plot(x_neg, x_neg, 'r--', linewidth=1, alpha=0.5)
ax1.plot(x_neg, -x_neg, 'r--', linewidth=1, alpha=0.5)

# x=0 处的洞
ax1.plot(0, 0, 'ro', markersize=8, fillstyle='none', markeredgewidth=2)
ax1.annotate('洞：$f(0)$ 无定义', xy=(0, 0), textcoords="offset points",
             xytext=(30, 20), fontsize=11, color='red',
             arrowprops=dict(arrowstyle='->', color='red'))

ax1.set_xlim(-0.35, 0.35)
ax1.set_ylim(-0.35, 0.35)
ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)
ax1.set_title('$f(x) = x \\sin(1/x)$：在 $x=0$ 处有洞', fontsize=13)
ax1.set_xlabel('x', fontsize=11)
ax1.set_ylabel('y', fontsize=11)
ax1.grid(True, alpha=0.3)
ax1.legend(loc='upper right', fontsize=9)

# 右图：放大视图，展示振荡
ax2 = axes[1]
x_zoom = np.linspace(0.01, 0.05, 800)
y_zoom = x_zoom * np.sin(1 / x_zoom)
ax2.plot(x_zoom, y_zoom, 'b-', linewidth=1.2)
ax2.plot(x_zoom, x_zoom, 'r--', linewidth=1, alpha=0.5)
ax2.plot(x_zoom, -x_zoom, 'r--', linewidth=1, alpha=0.5)

ax2.set_xlim(0, 0.055)
ax2.set_ylim(-0.06, 0.06)
ax2.axhline(0, color='black', linewidth=0.5)
ax2.axvline(0, color='black', linewidth=0.5)
ax2.set_title('放大看：越靠近 0，振荡越密', fontsize=13)
ax2.set_xlabel('x', fontsize=11)
ax2.set_ylabel('y', fontsize=11)
ax2.grid(True, alpha=0.3)
ax2.text(0.025, 0.045, '振幅被 $\\pm x$ 限制', fontsize=10, color='red',
         bbox=dict(boxstyle='round', facecolor='white', edgecolor='red', alpha=0.7))

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.3_图3_xsin洞.png'), dpi=200, bbox_inches='tight')
plt.close()

# ========== 图2：g(x) 补上洞，处处连续 ==========
fig, ax = plt.subplots(figsize=(8, 6))

x_pos = np.linspace(0.02, 0.3, 500)
x_neg = np.linspace(-0.3, -0.02, 500)
y_pos = x_pos * np.sin(1 / x_pos)
y_neg = x_neg * np.sin(1 / x_neg)

ax.plot(x_pos, y_pos, 'b-', linewidth=1.5)
ax.plot(x_neg, y_neg, 'b-', linewidth=1.5)

# 补上原点
ax.plot(0, 0, 'go', markersize=10, zorder=5)
ax.annotate('$g(0) = 0$\n把洞补上了', xy=(0, 0), textcoords="offset points",
            xytext=(35, 25), fontsize=11, color='green',
            arrowprops=dict(arrowstyle='->', color='green'))

# 包络线
ax.plot(x_pos, x_pos, 'r--', linewidth=1, alpha=0.4)
ax.plot(x_pos, -x_pos, 'r--', linewidth=1, alpha=0.4)
ax.plot(x_neg, x_neg, 'r--', linewidth=1, alpha=0.4)
ax.plot(x_neg, -x_neg, 'r--', linewidth=1, alpha=0.4)

ax.set_xlim(-0.35, 0.35)
ax.set_ylim(-0.35, 0.35)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_title('$g(x)$：处处连续（分段定义补上 $x=0$）', fontsize=14)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.grid(True, alpha=0.3)

# 标注函数定义
ax.text(0.15, 0.25, r'$g(x) = x \sin(1/x) \ (x \neq 0),\ g(0) = 0$',
        fontsize=12, bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.3_图4_补上洞.png'), dpi=200, bbox_inches='tight')
plt.close()

# ========== 图3：三明治定理示意图 ==========
fig, ax = plt.subplots(figsize=(8, 6))

x = np.linspace(0.02, 0.3, 500)
y = x * np.sin(1 / x)

ax.plot(x, y, 'b-', linewidth=2, label='$y = x \\sin(1/x)$')
ax.plot(x, x, 'r--', linewidth=1.5, label='$y = x$')
ax.plot(x, -x, 'g--', linewidth=1.5, label='$y = -x$')

# 标注三明治
ax.fill_between(x, -x, x, alpha=0.1, color='yellow')
ax.text(0.15, 0.08, '被夹在中间', fontsize=11, color='darkorange',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

# 标注 x→0 时三者都→0
ax.annotate('', xy=(0.02, 0.02), xytext=(0.08, 0.08),
            arrowprops=dict(arrowstyle='->', color='red', lw=2))
ax.text(0.1, 0.1, '当 $x \\to 0$ 时\n三者都 $\\to 0$', fontsize=10, color='red')

ax.set_xlim(-0.02, 0.35)
ax.set_ylim(-0.35, 0.35)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_title('三明治定理：$|x \\sin(1/x)| \\leq |x|$', fontsize=14)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.grid(True, alpha=0.3)
ax.legend(loc='upper right', fontsize=10)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.3_图5_三明治.png'), dpi=200, bbox_inches='tight')
plt.close()

# ========== 图4：连续性求极限 ==========
fig, ax = plt.subplots(figsize=(8, 6))

# 画函数 f(x) = (x^2 - 3x + 2) / (x - 2) = x - 1
x = np.linspace(-3, 4, 300)
# 排除 x=2
x = x[x != 2]
y = (x**2 - 3*x + 2) / (x - 2)

ax.plot(x, y, 'b-', linewidth=2.5, label=r'$f(x) = \frac{x^2-3x+2}{x-2} = x-1 \ (x \neq 2)$')

# 标记 x = -1
a = -1
f_a = a - 1
ax.plot(a, f_a, 'go', markersize=10, zorder=5)
ax.annotate(f'$(-1, f(-1)) = (-1, {f_a})$\n直接代入！',
            xy=(a, f_a), textcoords="offset points",
            xytext=(30, 20), fontsize=11, color='green',
            arrowprops=dict(arrowstyle='->', color='green'))

# 标记 x = 2 处的洞
ax.plot(2, 1, 'ro', markersize=10, fillstyle='none', markeredgewidth=2)
ax.annotate('$x=2$ 处无定义\n（分母为零）', xy=(2, 1), textcoords="offset points",
            xytext=(20, -40), fontsize=10, color='red',
            arrowprops=dict(arrowstyle='->', color='red'))

ax.set_xlim(-3.5, 4.5)
ax.set_ylim(-5, 4)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_title('连续性让求极限变得简单：$\\lim_{x \\to -1} f(x) = f(-1)$', fontsize=13)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.grid(True, alpha=0.3)
ax.legend(loc='upper left', fontsize=10)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.3_图6_代入求极限.png'), dpi=200, bbox_inches='tight')
plt.close()

print("配图生成完成！")
