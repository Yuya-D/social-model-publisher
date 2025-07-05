import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 初期パラメータ
R0 = 100  # 初期リソース
D0 = 80   # 初期欲望
years = st.sidebar.slider("シミュレーション年数", 1, 50, 20)

# 各階層の文化成熟度 T_i(n)
st.sidebar.markdown("### 各階層の文化的成熟度 T_i(n)")
t1 = st.sidebar.slider("外交・安全保障", 0.0, 1.0, 0.5)
t2 = st.sidebar.slider("産業基盤（一次産業・エネルギー）", 0.0, 1.0, 0.5)
t3 = st.sidebar.slider("教育・医療・福祉", 0.0, 1.0, 0.5)
t4 = st.sidebar.slider("文化・哲学・精神性", 0.0, 1.0, 0.5)

# α, β の係数調整
alpha = st.sidebar.slider("欲望の増加係数 α", 0.1, 2.0, 1.0)
beta = st.sidebar.slider("リソースの増加係数 β", 0.1, 2.0, 0.5)

# ページ選択
page = st.sidebar.radio("ページを選択", ["モデルの可視化", "背景と思想", "スコア表"])

# T(n), S(n) の定義
Tn = np.mean([t1, t2, t3, t4])
Sn = min(t1, t2, t3, t4)

# ---- ページごとの内容 ----
if page == "モデルの可視化":
    st.title("摂理AIモデル：文化的成熟と持続性")

    R, D = R0, D0
    R_vals, D_vals, score_vals, Sn_vals = [R], [D], [Tn * (R - D)], [Sn]

    for _ in range(years):
        R = R + beta * Tn
        D = D + alpha * (1 - Tn)
        R_vals.append(R)
        D_vals.append(D)
        score_vals.append(Tn * (R - D))
        Sn_vals.append(Sn)  # Snは固定ならそのまま

    # グラフ1: リソースと欲望の推移
    st.subheader("リソースと欲望の推移")
    fig1, ax1 = plt.subplots()
    ax1.plot(R_vals, label="リソース R(n)", color="green")
    ax1.plot(D_vals, label="欲望 D(n)", color="red")
    ax1.set_xlabel("年数")
    ax1.set_ylabel("量")
    ax1.legend()
    st.pyplot(fig1)

    # グラフ2: 成熟スコアの推移
    st.subheader("成熟スコア T(n) × (R - D) の推移")
    fig2, ax2 = plt.subplots()
    ax2.plot(score_vals, label="成熟スコア", color="blue")
    ax2.axhline(0, color="gray", linestyle="--")
    ax2.set_xlabel("年数")
    ax2.set_ylabel("スコア")
    ax2.legend()
    st.pyplot(fig2)

    # グラフ3: S(n)の推移
    st.subheader("社会調和指数 S(n) の推移")
    fig3, ax3 = plt.subplots()
    ax3.plot(Sn_vals, label="S(n): 社会調和（最も弱い階層）", color="purple")
    ax3.set_xlabel("年数")
    ax3.set_ylabel("S(n)の値")
    ax3.legend()
    st.pyplot(fig3)

    # 判定
    final_score = score_vals[-1]
    if final_score > 0:
        st.success(f"最終スコア {final_score:.2f} → 持続可能な発展が期待できます。")
    else:
        st.error(f"最終スコア {final_score:.2f} → 持続性に課題があります。文化的成熟か技術革新が必要です。")

elif page == "背景と思想":
    st.title("このモデルの背景と思想")

    st.markdown("""
    ### なぜこのモデルが必要か？

    現代社会は「欲望の無限性」と「リソースの有限性」という根本的なジレンマを抱えています。
    その中で、**文化的成熟度 T(n)** と **社会調和指数 S(n)** を導入することで、国家・社会の持続性を定量的に評価しようとするのがこのモデルの目的です。

    ### T(n) の階層的定義（価値観の成熟）

    T(n) = 平均値 [ t1(n), t2(n), t3(n), t4(n) ]
    - t1: 外交・安全保障
    - t2: 産業基盤（一次産業・エネルギー）
    - t3: 教育・医療・福祉
    - t4: 文化・哲学・精神性

    ### S(n) の定義（社会調和の脆弱性）

    S(n) = min(t1(n), t2(n), ... )
    → 一番弱い階層がボトルネックになる

    ### 数式

    - R(n+1) = R(n) + β × T(n)
    - D(n+1) = D(n) + α × (1 − T(n))
    - スコア = T(n) × (R(n) − D(n))

    ### このモデルが目指すもの

    - 経済的な豊かさだけでなく「精神的・文化的な調和と繁栄」
    - 政策評価・教育・投票行動に活用できる **摂理に基づいた知的判断基盤**
    """)

elif page == "スコア表":
    st.title("スコア評価基準")

    st.markdown("""
    ### スコア T(n) × (R - D) の意味

    このスコアは、「文化的成熟度 × 社会の余力」を意味し、持続可能性の評価指標となります。

    | スコア範囲 | 評価 | 説明 |
    |------------|------|------|
    | ≧ +20      | 🌟 持続性高い | 成熟と余力の両立。 |
    | +10 ～ +20 | ✅ 持続性あり | 比較的安定している。 |
    | 0 ～ +10   | ⚠️ 要注意     | 欲望が拡大傾向。 |
    | ＜ 0       | ❌ 持続性低い | 欲望がリソースを上回っている。 |
    """)
