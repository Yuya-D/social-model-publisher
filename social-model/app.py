import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="摂理AIプロトタイプ", layout="centered")
st.title("初期版：摂理AIプロトタイプ")

st.markdown("""
このアプリは、人類社会の持続性を数理モデルにより可視化する試みです。
文化的成熟度 \\( T(n) \\)、リソース量 \\( R(n) \\)、欲望量 \\( D(n) \\) の関係をもとに、
将来的な持続性スコアを評価します。
""")

# 初期値
R0 = st.slider("初期リソース量 R(0)", 0, 1000, 500)
D0 = st.slider("初期欲望量 D(0)", 0, 1000, 300)
T0 = st.slider("初期文化的成熟度 T(0)", 0.0, 1.0, 0.7, step=0.01)

α = st.slider("欲望の増加係数 α", 0.0, 1.0, 0.3, step=0.01)
β = st.slider("リソースの増加係数 β", 0.0, 1.0, 0.2, step=0.01)

years = st.slider("シミュレーション年数", 1, 100, 30)

# データ格納用
R_vals = [R0]
D_vals = [D0]
T_vals = [T0]
S_vals = []  # R(n) - D(n)
Tn_RD_scores = []  # T(n) × [R(n) − D(n)]

R, D, T = R0, D0, T0

for n in range(years):
    next_R = R + β * T
    next_D = D + α * (1 - T)
    
    R_vals.append(next_R)
    D_vals.append(next_D)
    T_vals.append(T)
    S_vals.append(next_R - next_D)
    Tn_RD_scores.append(T * (next_R - next_D))

    R, D = next_R, next_D

# グラフ描画
st.subheader("各年次における数値の推移")
fig, ax = plt.subplots()
ax.plot(R_vals, label="リソース量 R(n)", color="blue")
ax.plot(D_vals, label="欲望量 D(n)", color="red")
ax.plot(T_vals, label="文化的成熟度 T(n)", color="orange")
ax.legend()
st.pyplot(fig)

st.subheader("文化的成熟度 × リソース超過度（T(n) × [R(n) − D(n)]）")
fig2, ax2 = plt.subplots()
ax2.plot(Tn_RD_scores, label="文化調整済み持続性スコア", color='green')
ax2.axhline(y=0, color='gray', linestyle='--', label="持続の閾値（0）")
ax2.legend()
st.pyplot(fig2)

# 判定結果
final_score = Tn_RD_scores[-1]

st.subheader("最終評価")
if final_score > 0:
    st.success("✅ この社会モデルは文化的にも成熟し、持続可能な未来が期待できます。")
elif final_score == 0:
    st.warning("⚠️ 社会は拮抗しています。文化やリソースの強化が求められます。")
else:
    st.error("❌ このままではリソースが枯渇し、社会は持続困難です。")

st.markdown("---")
st.markdown("""
#### 📘 モデルの補足説明
- **T(n)**：文化的成熟度（理性・節度・共有の意識）
- **R(n)**：社会におけるリソース量（技術、土地、食料など）
- **D(n)**：欲望量（消費、浪費、エゴ的要求）
- **T(n) × [R(n) − D(n)]**：リソース超過に文化の力を掛けた持続可能性の目安です。
""")