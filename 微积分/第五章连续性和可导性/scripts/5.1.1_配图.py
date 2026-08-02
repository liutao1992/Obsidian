import matplotlib.pyplot as plt
import numpy as np
import os

# 设置中文字体
plt.rcParams['font.family'] = ['Hiragino Sans GB', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# 输出目录
output_dir = os.path.join(os.path.dirname(__file__), '..', 'imgs')
os.makedirs(output_dir, exist_ok=True)

# ========== 图1：四种连续性情况对比 ==========
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

def setup_axis(ax, title, case_num):
    ax.set_xlim(-1, 3)
    ax.set_ylim(-1, 4)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_title(f'图 {case_num}：{title}', fontsize=13)
    ax.set_xlabel('x', fontsize=11)
    ax.set_ylabel('y', fontsize=11)
    ax.grid(True, alpha=0.3)
    # 标记 a 的位置
    ax.axvline(1.5, color='gray', linestyle=':', alpha=0.5)
    ax.text(1.55, 3.5, '$x = a$', fontsize=11, color='gray')

a = 1.5

# 图1：左右极限不相等（跳跃间断点）
ax1 = axes[0, 0]
setup_axis(ax1, '左右极限不相等', 1)

x_left = np.linspace(-0.5, a, 100)
x_right = np.linspace(a, 3, 100)
y_left = 0.5 * x_left + 1
y_right = 0.5 * x_right + 2.5

ax1.plot(x_left[:-1], y_left[:-1], 'b-', linewidth=2.5)
ax1.plot(x_right[1:], y_right[1:], 'b-', linewidth=2.5)

# 左极限点（空心）
left_lim = 0.5 * a + 1
right_lim = 0.5 * a + 2.5
ax1.plot(a, left_lim, 'bo', markersize=10, fillstyle='none', markeredgewidth=2)
ax1.plot(a, right_lim, 'bo', markersize=10, fillstyle='none', markeredgewidth=2)

ax1.annotate(f'左极限 = {left_lim:.1f}', xy=(a, left_lim), textcoords="offset points",
             xytext=(-60, 10), fontsize=10, color='blue',
             arrowprops=dict(arrowstyle='->', color='blue'))
ax1.annotate(f'右极限 = {right_lim:.1f}', xy=(a, right_lim), textcoords="offset points",
             xytext=(15, -25), fontsize=10, color='blue',
             arrowprops=dict(arrowstyle='->', color='blue'))

ax1.text(0.5, 3.2, '双侧极限不存在', fontsize=11, color='red',
         bbox=dict(boxstyle='round', facecolor='white', edgecolor='red', alpha=0.8))

# 图2：极限存在但 f(a) 无定义（可去间断点）
ax2 = axes[0, 1]
setup_axis(ax2, 'f(a) 无定义', 2)

x_all = np.linspace(-0.5, 3, 200)
y_all = -0.3 * (x_all - 1.5)**2 + 3

# 在 a 处断开
mask = np.abs(x_all - a) > 0.05
ax2.plot(x_all[mask], y_all[mask], 'b-', linewidth=2.5)

# 极限值（空心点）
lim_val = 3
ax2.plot(a, lim_val, 'bo', markersize=10, fillstyle='none', markeredgewidth=2)
ax2.annotate(f'极限 = {lim_val}', xy=(a, lim_val), textcoords="offset points",
             xytext=(20, 15), fontsize=10, color='blue',
             arrowprops=dict(arrowstyle='->', color='blue'))

# 标记无定义
ax2.plot(a, 1.5, 'rx', markersize=12, markeredgewidth=2)
ax2.annotate('f(a) 无定义', xy=(a, 1.5), textcoords="offset points",
             xytext=(15, -30), fontsize=10, color='red',
             arrowprops=dict(arrowstyle='->', color='red'))

ax2.text(0.5, 3.2, '双侧极限存在', fontsize=11, color='blue',
         bbox=dict(boxstyle='round', facecolor='white', edgecolor='blue', alpha=0.8))

# 图3：极限存在且 f(a) 有定义，但不相等
def setup_axis(ax, title, case_num):
    ax.set_xlim(-1, 3)
    ax.set_ylim(-1, 4)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_title(f'图 {case_num}：{title}', fontsize=13)
    ax.set_xlabel('x', fontsize=11)
    ax.set_ylabel('y', fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.axvline(1.5, color='gray', linestyle=':', alpha=0.5)
    ax.text(1.55, 3.5, '$x = a$', fontsize=11, color='gray')

# 重新设置（被覆盖）
# 图3
ax3 = axes[1, 0]
ax3.set_xlim(-1, 3)
ax3.set_ylim(-1, 4)
ax3.axhline(0, color='black', linewidth=0.5)
ax3.axvline(0, color='black', linewidth=0.5)
ax3.set_title('图 3：极限值 ≠ 函数值', fontsize=13)
ax3.set_xlabel('x', fontsize=11)
ax3.set_ylabel('y', fontsize=11)
ax3.grid(True, alpha=0.3)
ax3.axvline(1.5, color='gray', linestyle=':', alpha=0.5)
ax3.text(1.55, 3.5, '$x = a$', fontsize=11, color='gray')

x_all = np.linspace(-0.5, 3, 200)
y_all = -0.3 * (x_all - 1.5)**2 + 3
mask = np.abs(x_all - a) > 0.05
ax3.plot(x_all[mask], y_all[mask], 'b-', linewidth=2.5)

lim_val = 3
f_a_val = 1.2

# 极限值（空心）
ax3.plot(a, lim_val, 'bo', markersize=10, fillstyle='none', markeredgewidth=2)
ax3.annotate(f'极限 = {lim_val}', xy=(a, lim_val), textcoords="offset points",
             xytext=(20, 15), fontsize=10, color='blue',
             arrowprops=dict(arrowstyle='->', color='blue'))

# 函数值（实心）
ax3.plot(a, f_a_val, 'ro', markersize=10)
ax3.annotate(f'f(a) = {f_a_val}', xy=(a, f_a_val), textcoords="offset points",
             xytext=(20, -20), fontsize=10, color='red',
             arrowprops=dict(arrowstyle='->', color='red'))

ax3.text(0.5, 3.2, '极限 ≠ f(a)', fontsize=11, color='red',
         bbox=dict(boxstyle='round', facecolor='white', edgecolor='red', alpha=0.8))

# 图4：连续
ax4 = axes[1, 1]
ax4.set_xlim(-1, 3)
ax4.set_ylim(-1, 4)
ax4.axhline(0, color='black', linewidth=0.5)
ax4.axvline(0, color='black', linewidth=0.5)
ax4.set_title('图 4：连续', fontsize=13)
ax4.set_xlabel('x', fontsize=11)
ax4.set_ylabel('y', fontsize=11)
ax4.grid(True, alpha=0.3)
ax4.axvline(1.5, color='gray', linestyle=':', alpha=0.5)
ax4.text(1.55, 3.5, '$x = a$', fontsize=11, color='gray')

x_all = np.linspace(-0.5, 3, 200)
y_all = -0.3 * (x_all - 1.5)**2 + 3
ax4.plot(x_all, y_all, 'b-', linewidth=2.5)

# 点(a, f(a))
f_a_val = 3
ax4.plot(a, f_a_val, 'go', markersize=10)
ax4.annotate(f'(a, f(a))\n极限 = f(a) = {f_a_val}',
             xy=(a, f_a_val), textcoords="offset points",
             xytext=(20, -35), fontsize=10, color='green',
             arrowprops=dict(arrowstyle='->', color='green'))

ax4.text(0.5, 3.2, '✓ 连续', fontsize=12, color='green',
         bbox=dict(boxstyle='round', facecolor='white', edgecolor='green', alpha=0.8))

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.1_图1_四种情况.png'), dpi=200, bbox_inches='tight')
plt.close()

# ========== 图2：连续的三条件 ==========
fig, ax = plt.subplots(figsize=(10, 6))

# 画一个连续的曲线
x = np.linspace(-1, 4, 300)
y = 0.5 * np.sin(x) + 2
ax.plot(x, y, 'b-', linewidth=2.5)

# 标记点 a
a = 1.5
f_a = 0.5 * np.sin(a) + 2
ax.plot(a, f_a, 'go', markersize=12, zorder=5)

# 画 x 趋近 a 的箭头
arrow_x_left = np.array([0.5, 1.0, 1.3])
arrow_x_right = np.array([2.5, 2.0, 1.7])
for x_val in arrow_x_left:
    y_val = 0.5 * np.sin(x_val) + 2
    dx = a - x_val
    ax.annotate('', xy=(x_val + dx*0.4, y_val), xytext=(x_val, y_val),
                arrowprops=dict(arrowstyle='->', color='orange', lw=1.5))
for x_val in arrow_x_right:
    y_val = 0.5 * np.sin(x_val) + 2
    dx = a - x_val
    ax.annotate('', xy=(x_val + dx*0.4, y_val), xytext=(x_val, y_val),
                arrowprops=dict(arrowstyle='->', color='orange', lw=1.5))

ax.annotate('x 从两边趋近 a', xy=(a, f_a), textcoords="offset points",
            xytext=(30, 30), fontsize=11, color='orange',
            arrowprops=dict(arrowstyle='->', color='orange'))

ax.annotate('f(a)', xy=(a, f_a), textcoords="offset points",
            xytext=(-30, 15), fontsize=12, color='green',
            arrowprops=dict(arrowstyle='->', color='green'))

ax.set_xlim(-1, 4)
ax.set_ylim(0.5, 3.5)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.axvline(a, color='gray', linestyle=':', alpha=0.5)
ax.text(a + 0.1, 3.2, '$x = a$', fontsize=11, color='gray')
ax.set_title('连续的本质：$\\lim_{x \\to a} f(x) = f(a)$', fontsize=15)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.1_图2_连续本质.png'), dpi=200, bbox_inches='tight')
plt.close()

# ========== 图3：分段函数示例 ==========
fig, ax = plt.subplots(figsize=(8, 6))

# 左半部分：x^2 (x < 1)
x_left = np.linspace(-0.5, 1, 150)
y_left = x_left ** 2

# 右半部分：2x (x >= 1)
x_right = np.linspace(1, 3, 100)
y_right = 2 * x_right

ax.plot(x_left, y_left, 'b-', linewidth=2.5, label=r'$y = x^2 \ (x < 1)$')
ax.plot(x_right, y_right, 'r-', linewidth=2.5, label=r'$y = 2x \ (x \geq 1)$')

# 标记分界点 x=1
ax.plot(1, 1, 'ko', markersize=10, zorder=5)
ax.annotate('分界点 (1, 1)', xy=(1, 1), textcoords="offset points",
            xytext=(20, 20), fontsize=12, color='black',
            arrowprops=dict(arrowstyle='->', color='black'))

# 标记 x=1 竖线
ax.axvline(1, color='gray', linestyle=':', alpha=0.6)
ax.text(1.05, 5.5, '$x = 1$', fontsize=11, color='gray')

# 标注两段函数
ax.text(0.2, 0.7, '$x^2$', fontsize=14, color='blue')
ax.text(2.2, 4.5, '$2x$', fontsize=14, color='red')

# 设置坐标轴
ax.set_xlim(-0.8, 3.5)
ax.set_ylim(-0.5, 7)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_title(r'分段函数 $f(x) = x^2 \ (x < 1), \ f(x) = 2x \ (x \geq 1)$',
             fontsize=14)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.grid(True, alpha=0.3)
ax.legend(loc='upper left', fontsize=11)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.1_图3_分段函数.png'), dpi=200, bbox_inches='tight')
plt.close()

# ========== 图4：|x|/x 的左右极限 ==========
fig, ax = plt.subplots(figsize=(8, 6))

# 左半部分：|x|/x = -1 (x < 0)
x_left = np.linspace(-3, -0.01, 200)
y_left = np.ones_like(x_left) * (-1)

# 右半部分：|x|/x = 1 (x > 0)
x_right = np.linspace(0.01, 3, 200)
y_right = np.ones_like(x_right)

ax.plot(x_left, y_left, 'b-', linewidth=2.5)
ax.plot(x_right, y_right, 'r-', linewidth=2.5)

# 在 x=0 处标记断裂（空心点）
ax.plot(0, -1, 'bo', markersize=10, fillstyle='none', markeredgewidth=2)
ax.plot(0, 1, 'ro', markersize=10, fillstyle='none', markeredgewidth=2)

# 标注左右极限
ax.annotate('左极限 = -1', xy=(0, -1), textcoords="offset points",
            xytext=(-80, -25), fontsize=12, color='blue',
            arrowprops=dict(arrowstyle='->', color='blue'))
ax.annotate('右极限 = 1', xy=(0, 1), textcoords="offset points",
            xytext=(-70, 15), fontsize=12, color='red',
            arrowprops=dict(arrowstyle='->', color='red'))

# 标注 x=0 竖线
ax.axvline(0, color='gray', linestyle=':', alpha=0.6)
ax.text(0.1, 0.5, '左右不等\n极限不存在', fontsize=11, color='red',
        bbox=dict(boxstyle='round', facecolor='white', edgecolor='red', alpha=0.8))

# 标注函数值
ax.text(-2, -0.6, '$y = -1 \\ (x < 0)$', fontsize=12, color='blue')
ax.text(1.5, 1.3, '$y = 1 \\ (x > 0)$', fontsize=12, color='red')

# 设置坐标轴
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-2, 2)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_title(r'$\lim_{x \to 0} \frac{|x|}{x}$  左右极限不相等，极限不存在', fontsize=14)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5.1.1_图4_左右极限不等.png'), dpi=200, bbox_inches='tight')
plt.close()

print("配图生成完成！")
