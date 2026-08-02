import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# 兼容中文显示：优先使用系统自带中文字体
matplotlib.rcParams['font.family'] = ['Hiragino Sans GB', 'Heiti TC', 'STHeiti', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

# 保存路径
save_path = '../imgs/5.1_图4_可去间断点示例.png'

# 创建图形
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制抛物线 y = x^2，但在 x=1 处断开
x_left = np.linspace(-2.5, 0.97, 200)
x_right = np.linspace(1.03, 2.5, 200)

ax.plot(x_left, x_left**2, color='#2E86AB', linewidth=2.5, label=r'$y = x^2$')
ax.plot(x_right, x_right**2, color='#2E86AB', linewidth=2.5)

# 在 x=1 处画空心点（极限位置）
ax.plot(1, 1, 'o', color='#2E86AB', markersize=10, fillstyle='none', markeredgewidth=2.5)

# 在 x=1 处画实心点（实际函数值）
ax.plot(1, 5, 'o', color='#D9534F', markersize=10, label=r'$f(1) = 5$')

# 画虚线连接两个点，帮助观察错位
ax.plot([1, 1], [1, 5], 'k--', linewidth=1.5, alpha=0.6)

# 标注
ax.annotate(r'极限位置：$(1, 1)$', xy=(1, 1), xytext=(0.2, 2.2),
            fontsize=12, color='#2E86AB',
            arrowprops=dict(arrowstyle='->', color='#2E86AB', lw=1.5))

ax.annotate(r'实际函数值：$f(1) = 5$', xy=(1, 5), xytext=(1.4, 4.2),
            fontsize=12, color='#D9534F',
            arrowprops=dict(arrowstyle='->', color='#D9534F', lw=1.5))

# 标题和标签（避免在 mathtext 中使用 cases 环境）
ax.set_title('可去间断点示例：x≠1 时 f(x)=x²，f(1)=5', fontsize=14)
ax.set_xlabel(r'$x$', fontsize=12)
ax.set_ylabel(r'$f(x)$', fontsize=12)

# 设置坐标轴
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-0.5, 6)
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.grid(True, alpha=0.3)
ax.legend(loc='upper left', fontsize=11)

# 让坐标轴比例更自然
ax.set_aspect('equal', adjustable='box')

plt.tight_layout()
plt.savefig(save_path, dpi=150, bbox_inches='tight')
plt.close()

print(f'图片已保存到：{save_path}')
