import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# --- Prepare data ---
df = hypertension_clean_df

# Binary target
df['_hyp_binary'] = (df['Has_Hypertension'] == 'Yes').astype(int)

# Bin Stress_Score (0–10) into Low / Medium / High
df['_stress_band'] = pd.cut(
    df['Stress_Score'],
    bins=[-1, 3, 6, 10],
    labels=['Low (0–3)', 'Medium (4–6)', 'High (7–10)']
)

# Aggregate
_agg = (
    df.groupby(['Family_History', '_stress_band'], observed=True)['_hyp_binary']
    .agg(rate='mean', count='count')
    .reset_index()
)
_agg['rate_pct'] = _agg['rate'] * 100

# --- Plot ---
stress_bands = ['Low (0–3)', 'Medium (4–6)', 'High (7–10)']
family_groups = ['No', 'Yes']

bar_colors = {
    'Low (0–3)':    '#A1C9F4',
    'Medium (4–6)': '#FFB482',
    'High (7–10)':  '#FF9F9B',
}

x = np.arange(len(family_groups))
n_bands = len(stress_bands)
bar_width = 0.22
offsets = np.linspace(-(n_bands - 1) / 2, (n_bands - 1) / 2, n_bands) * bar_width

fig, ax = plt.subplots(figsize=(9, 6))
fig.patch.set_facecolor('#1D1D20')
ax.set_facecolor('#1D1D20')

for i, band in enumerate(stress_bands):
    _subset = _agg[_agg['_stress_band'] == band]
    _rates = [
        float(_subset.loc[_subset['Family_History'] == fg, 'rate_pct'].values[0])
        if fg in _subset['Family_History'].values else 0.0
        for fg in family_groups
    ]
    _counts = [
        int(_subset.loc[_subset['Family_History'] == fg, 'count'].values[0])
        if fg in _subset['Family_History'].values else 0
        for fg in family_groups
    ]
    bars = ax.bar(
        x + offsets[i], _rates,
        width=bar_width,
        color=bar_colors[band],
        alpha=0.92,
        label=band,
        zorder=3
    )
    # Annotate bars with rate %
    for bar, rate, cnt in zip(bars, _rates, _counts):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1.0,
            f'{rate:.1f}%',
            ha='center', va='bottom',
            fontsize=8.5, color='#fbfbff', fontweight='bold'
        )

# Formatting
ax.set_xticks(x)
ax.set_xticklabels(['No Family History', 'Family History: Yes'], fontsize=12, color='#fbfbff')
ax.set_yticks([0, 20, 40, 60, 80, 100])
ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'], color='#909094', fontsize=10)
ax.set_ylim(0, 110)
ax.set_ylabel('Hypertension Rate (%)', color='#909094', fontsize=11)
ax.set_title('Hypertension Rate by Family History & Stress Level', color='#fbfbff', fontsize=14, pad=14)

ax.tick_params(colors='#909094', which='both')
for spine in ax.spines.values():
    spine.set_edgecolor('#444')
ax.yaxis.grid(True, color='#333', linewidth=0.7, zorder=0)
ax.set_axisbelow(True)

legend = ax.legend(
    title='Stress Band',
    title_fontsize=10,
    fontsize=9,
    framealpha=0.2,
    facecolor='#2a2a2e',
    edgecolor='#555',
    labelcolor='#fbfbff',
    loc='upper left'
)
legend.get_title().set_color('#fbfbff')

plt.tight_layout()

hypertension_stress_family_chart = fig
plt.show()
print("\n=== Underlying Rates ===")
print(_agg[['Family_History','_stress_band','rate_pct','count']].to_string(index=False))
