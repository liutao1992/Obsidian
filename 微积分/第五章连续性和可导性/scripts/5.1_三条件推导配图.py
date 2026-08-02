import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib

# 兼容中文显示
matplotlib.rcParams['font.family'] = ['Hiragino Sans GB', 'Heiti TC', 'STHeiti', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

save_path = '../imgs/5.1_图5_三条件推导.png'

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# 颜色
color_top = '#2E86AB'
color_mid = '#F6AE2D'
color_box1 = '#A23B72'
color_box2 = '#D9534F'
color_box3 = '#6A994E'

def draw_box(ax, x, y, width, height, text, facecolor, edgecolor='black', fontsize=12):
    rect = patches.FancyBboxPatch((x - width/2, y - height/2), width, height,
                                   boxstyle="round,pad=0.05,rounding_size=0.2",
                                   facecolor=facecolor, edgecolor=edgecolor, linewidth=2)
    ax.add_patch(rect)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            color='white', fontweight='bold', wrap=True)

def draw_text(ax, x, y, text, fontsize=11, color='black'):
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize, color=color)

def draw_arrow(ax, x1, y1, x2, y2, color='black'):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=2))

# 顶部：定义
draw_box(ax, 5, 8.8, 5.5, 1.0,
         r'$\lim_{x \to a} f(x) = f(a)$',
         color_top, fontsize=14)

draw_text(ax, 5, 7.9, '一个等式成立，需要三个条件', fontsize=13)
draw_arrow(ax, 5, 8.3, 5, 8.2)

# 中间连接点
draw_text(ax, 5, 7.0, '↓', fontsize=20)

# 三个条件框（并排）
box_y = 5.5
box_w = 2.6
box_h = 1.2
gap = 0.5

positions = [
    (5 - box_w - gap, box_y),
    (5, box_y),
    (5 + box_w + gap, box_y)
]

colors = [color_box1, color_box2, color_box3]
texts = [
    '左边存在\n↓\n极限存在',
    '右边存在\n↓\n函数值存在',
    '左右相等\n↓\n极限 = 函数值'
]

for (x, y), color, text in zip(positions, colors, texts):
    draw_box(ax, x, y, box_w, box_h, text, color, fontsize=11)
    draw_arrow(ax, 5, 6.8, x, y + box_h/2 + 0.1, color='gray')

# 底部结论
draw_text(ax, 5, 3.5, '三个条件同时满足', fontsize=13, color=color_top)
draw_arrow(ax, 5, 4.9, 5, 3.8, color='gray')

draw_box(ax, 5, 2.3, 4.5, 1.0, '函数在 $a$ 点连续', '#1D3557', fontsize=13)
draw_arrow(ax, 5, 3.2, 5, 2.8, color='gray')

# 标题
ax.set_title('从等式自然推导出连续的三个条件', fontsize=15, pad=20)

plt.tight_layout()
plt.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

print(f'图片已保存到：{save_path}')
