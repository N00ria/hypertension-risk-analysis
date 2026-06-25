import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Data from model block
feat_labels = ['Family History', 'Age', 'Stress Score', 'BMI']
coefficients = [0.603718, 0.515294, 0.460933, 0.345614]
colors = ['#A1C9F4', '#8DE5A1', '#FFB482', '#D0BBFF']

fig, ax = plt.subplots(figsize=(8, 5))
fig.patch.set_facecolor('#1D1D20')
ax.set_facecolor('#1D1D20')

bars = ax.barh(feat_labels, coefficients, color=colors, height=0.55, zorder=3)

# Value labels on bars
for bar, coef in zip(bars, coefficients):
    ax.text(coef + 0.01, bar.get_y() + bar.get_height() / 2,
            f'{coef:.3f}', va='center', ha='left',
            color='#fbfbff', fontsize=11, fontweight='bold')

ax.set_xlim(0, 0.78)
ax.set_xlabel('Standardised Coefficient (log-odds)', color='#909094', fontsize=11)
ax.set_title('Feature Importance — Logistic Regression\nHypertension Prediction', 
             color='#fbfbff', fontsize=13, fontweight='bold', pad=14)

ax.tick_params(colors='#fbfbff', labelsize=11)
ax.xaxis.label.set_color('#909094')
for spine in ax.spines.values():
    spine.set_visible(False)
ax.xaxis.set_tick_params(color='#555558')
ax.grid(axis='x', color='#333337', linewidth=0.7, zorder=0)

# Accuracy annotation
ax.text(0.98, 0.04, f'Test Accuracy: 71.3%', transform=ax.transAxes,
        ha='right', va='bottom', color='#ffd400', fontsize=11, fontweight='bold')

plt.tight_layout()
feature_importance_chart = fig
