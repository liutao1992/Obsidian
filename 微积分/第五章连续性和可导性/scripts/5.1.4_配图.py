import matplotlib.pyplot as plt
import numpy as np
import os

# 设置中文字体
plt.rcParams['font.family'] = ['Hiragino Sans GB', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# 输出目录
output_dir = os.path.join(os.path.dirname(__file__), '..', 'imgs')
os.makedirs(output_dir, exist_ok=True)

# ========== 图1：介值定理直觉 ==========
fig, ax = plt.subplots(figsize=(10, 6))

# 画一条从负到正穿过x轴的连续曲线
x = np.linspace(0.5, 4.5, 300)
y = 0.5 * (x - 2)**3 - 0.5 * (x - 2) + 0.3
ax.plot(x, y, 'b-', linewidth=2.5)

# 标记端点
a, b = 0.8, 4.2
f_a = 0.5 * (a - 2)**3 - 0.5 * (a - 2) + 0.3
f_b = 0.5 * (b - 2)**3 - 0.5 * (b - 2) + 0.3
ax.plot(a, f_a, 'ro', markersize=10)
ax.plot(b, f_b, 'go', markersize=10)

ax.text(a, f_a - 0.5, f'$(a, f(a))$\n$f(a) < 0$', fontsize=10, color='red', ha='center')
ax.text(b, f_b + 0.3, f'$(b, f(b))$\n$f(b) > 0$', fontsize=10, color='green', ha='center')

# 找到并标记x轴截距
# 手动标记一个近似的根位置（约 x=2.3）
root = 2.3
ax.plot(root, 0, 'mo', markersize=12, zorder=5)
ax.axvline(root, color='purple', linestyle=':', alpha=0.5, ymax=0.15)
ax.text(root, -0.6, f'$c \\approx {root:.1f}$\n$f(c) = 0$', fontsize=10, color='purple', ha='center')

# x轴
ax.axhline(0, color='black', linewidth=1)

# 区间标注
ax.annotate('', xy=(b, -2.0), xytext=(a, -2.0),
            arrowprops=dict(arrowstyle='<->', color='orange', lw=2))
ax.text((a+b)/2, -2.4, '区间 $[a, b]$', fontsize=11, color='orange', ha='center')

# 连续性说明
ax.text(2.5, 2.0, '连续函数从下方到上方\n必然穿过 x 轴', fontsize=12, color='blue',
        bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))

ax.set_xlim(0, 5)
ax.set_ylim(-2.5, 3)
ax.set_title('介值定理：连续函数必然穿过 x 轴', fontsize=15)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.4_图1_介值定理.png'), dpi=200, bbox_inches='tight')
plt.close()

# ========== 图2：不连续函数跳过x轴 ==========
fig, ax = plt.subplots(figsize=(10, 6))

# 左半段在x轴下方
x_left = np.linspace(0.5, 2.5, 150)
y_left = -0.5 * (x_left - 1.5)**2 - 0.5
ax.plot(x_left, y_left, 'b-', linewidth=2.5)

# 右半段在x轴上方（跳过x轴）
x_right = np.linspace(2.5, 4.5, 150)
y_right = 0.5 * (x_right - 3.5)**2 + 0.5
ax.plot(x_right, y_right, 'b-', linewidth=2.5)

# 断点
ax.plot(2.5, -0.5*(2.5-1.5)**2 - 0.5, 'ro', markersize=10)
ax.plot(2.5, 0.5*(2.5-3.5)**2 + 0.5, 'bo', markersize=10, fillstyle='none', markeredgewidth=2)

# 跳跃箭头
ax.annotate('', xy=(2.5, 0.5*(2.5-3.5)**2 + 0.5), xytext=(2.5, -0.5*(2.5-1.5)**2 - 0.5),
            arrowprops=dict(arrowstyle='<->', color='red', lw=2))
ax.text(2.7, 0, '跳跃！', fontsize=12, color='red')

# 端点
ax.plot(0.8, -0.5*(0.8-1.5)**2 - 0.5, 'ro', markersize=8)
ax.plot(4.2, 0.5*(4.2-3.5)**2 + 0.5, 'go', markersize=8)
ax.text(0.8, -1.3, '$f(a) < 0$', fontsize=10, color='red', ha='center')
ax.text(4.2, 1.3, '$f(b) > 0$', fontsize=10, color='green', ha='center')

# x轴
ax.axhline(0, color='black', linewidth=1)

# 标记不连续点
ax.plot(2.5, 0, 'rx', markersize=12, markeredgewidth=2)
ax.text(2.7, -0.5, '不连续点\n跳过 x 轴', fontsize=10, color='red',
        bbox=dict(boxstyle='round', facecolor='white', edgecolor='red', alpha=0.7))

ax.set_xlim(0, 5)
ax.set_ylim(-2, 2.5)
ax.set_title('不连续函数可以跳过 x 轴', fontsize=15)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.4_图2_不连续跳过.png'), dpi=200, bbox_inches='tight')
plt.close()

# ========== 图3：x = cos(x) 的解 ==========
fig, ax = plt.subplots(figsize=(10, 6))

x = np.linspace(0, np.pi/2 + 0.2, 300)
ax.plot(x, x, 'b-', linewidth=2.5, label='$y = x$')
ax.plot(x, np.cos(x), 'r-', linewidth=2.5, label='$y = \\cos(x)$')

# 交点
root = 0.739  # x = cos(x) 的近似解
ax.plot(root, root, 'mo', markersize=12, zorder=5)
ax.axvline(root, color='purple', linestyle=':', alpha=0.5, ymax=0.85)
ax.axhline(root, color='purple', linestyle=':', alpha=0.5, xmax=0.85)
ax.text(root + 0.05, root + 0.15, f'$x \\approx {root:.3f}$\n$\\cos(x) \\approx {np.cos(root):.3f}$',
        fontsize=10, color='purple')

# 标注区间
ax.axvline(0, color='gray', linestyle=':', alpha=0.5, ymax=0.6)
ax.axvline(np.pi/2, color='gray', linestyle=':', alpha=0.5, ymax=0.6)
ax.text(0, -0.15, '$0$', fontsize=11, color='gray', ha='center')
ax.text(np.pi/2, -0.15, '$\\pi/2$', fontsize=11, color='gray', ha='center')
ax.annotate('', xy=(np.pi/2, -0.05), xytext=(0, -0.05),
            arrowprops=dict(arrowstyle='<->', color='orange', lw=2))
ax.text(np.pi/4, -0.12, '区间 $(0, \\pi/2)$', fontsize=11, color='orange', ha='center')

ax.set_xlim(-0.2, 1.8)
ax.set_ylim(-0.2, 1.2)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_title('$x = \\cos(x)$ 在 $(0, \\pi/2)$ 内有解', fontsize=15)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.grid(True, alpha=0.3)
ax.legend(loc='upper left', fontsize=12)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.4_图3_x等于cosx.png'), dpi=200, bbox_inches='tight')
plt.close()

# ========== 图4：f(x) = x - cos(x) 的图像 ==========
fig, ax = plt.subplots(figsize=(10, 6))

x = np.linspace(-0.5, 2, 300)
y = x - np.cos(x)
ax.plot(x, y, 'b-', linewidth=2.5, label='$f(x) = x - \\cos(x)$')

# x轴
ax.axhline(0, color='black', linewidth=1)

# 标记 f(0) 和 f(π/2)
f_0 = 0 - np.cos(0)
f_pi2 = np.pi/2 - np.cos(np.pi/2)

ax.plot(0, f_0, 'ro', markersize=10)
ax.plot(np.pi/2, f_pi2, 'go', markersize=10)

ax.text(0, f_0 - 0.25, f'$f(0) = -1 < 0$', fontsize=10, color='red', ha='center')
ax.text(np.pi/2, f_pi2 + 0.15, f'$f(\\pi/2) = \\pi/2 > 0$', fontsize=10, color='green', ha='center')

# 标记零点
root = 0.739  # x = cos(x) 的近似解
ax.plot(root, 0, 'mo', markersize=12, zorder=5)
ax.text(root + 0.05, 0.15, f'$f(c) = 0$', fontsize=11, color='purple')

# 区间标注
ax.annotate('', xy=(np.pi/2, -1.3), xytext=(0, -1.3),
            arrowprops=dict(arrowstyle='<->', color='orange', lw=2))
ax.text(np.pi/4, -1.5, '区间 $(0, \\pi/2)$', fontsize=11, color='orange', ha='center')

ax.set_xlim(-0.5, 2)
ax.set_ylim(-1.8, 1.5)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_title('介值定理：$f(x) = x - \\cos(x)$ 在 $(0, \\pi/2)$ 上有零点', fontsize=13)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.grid(True, alpha=0.3)
ax.legend(loc='upper left', fontsize=11)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.4_图4_fx零点.png'), dpi=200, bbox_inches='tight')
plt.close()

# ========== 图5：介值定理推广（任意M） ==========
fig, ax = plt.subplots(figsize=(10, 6))

# 画一条曲线
x = np.linspace(0, 4, 300)
y = 0.3 * x**2 + 1
ax.plot(x, y, 'b-', linewidth=2.5, label='$f(x) = 3x + x^2$（示例）')

# 画水平线 y = M
M = 5
ax.axhline(M, color='purple', linestyle='--', linewidth=1.5, label=f'$y = M = {M}$')

# 标记f(0)和f(2)
ax.plot(0, 1, 'ro', markersize=10)
ax.plot(2, 0.3*4 + 1, 'go', markersize=10)
ax.text(0, 0.7, f'$f(0) = 1 < {M}$', fontsize=10, color='red', ha='center')
ax.text(2, 0.3*4 + 1.3, f'$f(2) = 13 > {M}$', fontsize=10, color='green', ha='center')

# 交点
ax.plot(np.sqrt((M-1)/0.3), M, 'mo', markersize=12, zorder=5)
ax.text(np.sqrt((M-1)/0.3) + 0.15, M + 0.2, f'$f(c) = {M}$', fontsize=11, color='purple')

# 区间标注
ax.annotate('', xy=(2, 0.3), xytext=(0, 0.3),
            arrowprops=dict(arrowstyle='<->', color='orange', lw=2))
ax.text(1, 0.1, '区间 $[0, 2]$', fontsize=11, color='orange', ha='center')

ax.set_xlim(-0.3, 4.3)
ax.set_ylim(0, 8)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_title('介值定理推广：可以找到 $f(c) = M$ 的点', fontsize=14)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.grid(True, alpha=0.3)
ax.legend(loc='upper left', fontsize=11)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.4_图5_推广.png'), dpi=200, bbox_inches='tight')
plt.close()

print("配图生成完成！")
