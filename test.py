import matplotlib.pyplot as plt

# 전역 설정 (글자색 흰색)
plt.rcParams.update({
    'text.color': 'white',
    'axes.labelcolor': 'white',
    'xtick.color': 'white',
    'ytick.color': 'white'
})

# 데이터는 동일...
versions = ["V2", "Append", "V3", "V4X", "NT", "NT v2.0", "V6 AI"]
years = [2007, 2010, 2013, 2016, 2020, 2025, 2026]
descriptions = ["Initial Release", "Vocal Mood", "English Bank", "Growl/EVEC", "Proprietary", "Enhanced", "Neural AI"]

# 1. figsize 높이를 5에서 3으로 변경 (더 납작하게)
fig, ax = plt.subplots(figsize=(10, 3), constrained_layout=True)
fig.set_facecolor("#1a1a1e")

# 제목 여백(pad) 줄이기
ax.set_title("Hatsune Miku Software Evolution Timeline", fontsize=14, fontweight='bold', pad=10)

ax.axhline(0, color="white", linewidth=1.5, zorder=1)
ax.scatter(years, [0]*len(years), s=80, color="#39C5BB", edgecolors="white", zorder=3)

for i, (version, year, desc) in enumerate(zip(versions, years, descriptions)):
    # 높이가 낮아졌으므로 텍스트 오프셋도 조금 더 조밀하게 조정
    offset = 0.12 if i % 2 == 0 else -0.25
    va = 'bottom' if i % 2 == 0 else 'top'
    
    ax.text(year, offset, f"{version}\n({year})", 
            ha='center', va=va, fontweight='bold', fontsize=9, 
            color='white',
            bbox=dict(facecolor='#1a1a1e', edgecolor='#39C5BB', boxstyle='round,pad=0.3', alpha=0.8))
    
    desc_offset = offset + 0.18 if i % 2 == 0 else offset - 0.18
    ax.text(year, desc_offset, desc, ha='center', va=va, fontsize=7, style='italic', color='white')

# 2. Y축 범위를 좁혀서 빈 공간 제거 (핵심!)
ax.set_ylim(-0.6, 0.6)
ax.set_xlim(2005, 2028)
ax.set_facecolor("#1a1a1e")
ax.get_yaxis().set_visible(False)
for spine in ['left', 'right', 'top']:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_color('white')
ax.set_xticks(years)

plt.show()
