import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 中文字体设置（与 mathtext 兼容）
plt.rcParams['font.sans-serif'] = ['Hiragino Sans GB', 'DejaVu Sans', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 矩形尺寸
u = 3.0
du = 1.0
v = 2.0
dv = 0.8

fig, ax = plt.subplots(figsize=(8, 6))

# 原矩形（浅蓝）
orig = patches.Rectangle((0, 0), u, v, linewidth=1.5, edgecolor='black', facecolor='#dbeafe')
ax.add_patch(orig)

# 右边长条：v * Δu（浅绿）
right = patches.Rectangle((u, 0), du, v, linewidth=1.5, edgecolor='black', facecolor='#bbf7d0')
ax.add_patch(right)

# 上长条：u * Δv（浅黄）
top = patches.Rectangle((0, v), u, dv, linewidth=1.5, edgecolor='black', facecolor='#fef08a')
ax.add_patch(top)

# 右上角小角：Δu * Δv（浅红）
corner = patches.Rectangle((u, v), du, dv, linewidth=1.5, edgecolor='black', facecolor='#fecaca')
ax.add_patch(corner)

# 标注原矩形
ax.text(u / 2, v / 2, '$u \\times v$', ha='center', va='center', fontsize=14, color='#1e40af')

# 标注三块新增区域
ax.text(u + du / 2, v / 2, '$v \\Delta u$\n右长条', ha='center', va='center', fontsize=12, color='#166534')
ax.text(u / 2, v + dv / 2, '$u \\Delta v$\n上长条', ha='center', va='center', fontsize=12, color='#854d0e')
ax.text(u + du / 2, v + dv / 2, '$\\Delta u \\Delta v$\n小角', ha='center', va='center', fontsize=11, color='#991b1b')

# 尺寸标注
ax.annotate('', xy=(u, -0.25), xytext=(0, -0.25),
            arrowprops=dict(arrowstyle='<->', color='black'))
ax.text(u / 2, -0.45, '$u$', ha='center', va='top', fontsize=12)

ax.annotate('', xy=(u + du, -0.25), xytext=(u, -0.25),
            arrowprops=dict(arrowstyle='<->', color='black'))
ax.text(u + du / 2, -0.45, '$\\Delta u$', ha='center', va='top', fontsize=12)

ax.annotate('', xy=(-0.25, v), xytext=(-0.25, 0),
            arrowprops=dict(arrowstyle='<->', color='black'))
ax.text(-0.45, v / 2, '$v$', ha='right', va='center', fontsize=12)

ax.annotate('', xy=(-0.25, v + dv), xytext=(-0.25, v),
            arrowprops=dict(arrowstyle='<->', color='black'))
ax.text(-0.45, v + dv / 2, '$\\Delta v$', ha='right', va='center', fontsize=12)

# 总宽度/高度标注
ax.annotate('', xy=(u + du, -0.6), xytext=(0, -0.6),
            arrowprops=dict(arrowstyle='<->', color='#4b5563'))
ax.text((u + du) / 2, -0.85, '$u+\\Delta u$', ha='center', va='top', fontsize=11, color='#4b5563')

ax.annotate('', xy=(-0.6, v + dv), xytext=(-0.6, 0),
            arrowprops=dict(arrowstyle='<->', color='#4b5563'))
ax.text(-0.85, (v + dv) / 2, '$v+\\Delta v$', ha='right', va='center', fontsize=11, color='#4b5563', rotation=90)

# 设置坐标轴
ax.set_xlim(-1.2, u + du + 0.5)
ax.set_ylim(-1.0, v + dv + 0.5)
ax.set_aspect('equal')
ax.axis('off')

# 标题
ax.set_title('乘积法则的几何解释：面积增加分解', fontsize=16, pad=20)

plt.tight_layout()
plt.savefig('../imgs/product_rule_area.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('已生成 ../imgs/product_rule_area.png')
