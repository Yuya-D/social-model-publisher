import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------
# 初期設定とパラメータ
# ------------------------------

R0 = 100   # 初期リソース
D0 = 80    # 初期欲望
T0 = 0.5   # 初期文化的成熟度

# 年数
years = st.sidebar.slider("シミュレーション年数", 1, 50, 20)

# 外交・安全保障、一次産業、教育福祉、文化精神
t1 = st.sidebar.slider("外交・安全保障 (t1)", 0.0, 1.0, 0.5)
t2 = st.sidebar.slider("一次産業・エネルギー (t2)", 0.0, 1.0, 0.5)
t3 = st.sidebar.slider("教育・福祉 (t3)", 0.0, 1.0, 0.5)
t4 = st.sidebar.slider("文化・精神性 (t4)", 0.0, 1.0, 0.5)

# 重み
w1, w2, w3, w4 = 0.3, 0.3, 0.2, 0.2

# T(n) の計算
Tn = (w1 * t1 + w2 * t2 + w3 * t3 + w4 * t4) / (w1 + w2 + w3 + w4)

# 欲望とリソースの変化係数
alpha = st.sidebar.slider("欲望の増加係数 α", 0.1, 2.0, 1.0)
beta = st.sidebar.slider("リソースの増加係数 β", 0.1, 2.0, 0.5)

# ------------------------------
# ページ選択
# ------------------------------

page = st.sidebar.radio("ページを選択", ["モデルの可視化", "背景と思想", "スコア解釈"])

# ------------------------------
# モデル可視化ページ
# ------------------------------

if page == "モデルの可視化":
    st.title("摂理AIモデル：文化的成熟と持続性")

    R, D = R0, D0
    R_vals, D_vals, score_vals = [R], [D], [Tn * (R - D)]

    for _ in range(years):
        R = R + beta * Tn
        D = D + alpha * (1 - Tn)
        R_vals.append(R)
        D_vals.append(D)
        score_vals.append(Tn * (R - D))

    # リソースと欲望の推移
    st.subheader("リソースと欲望の推移")
    fig1, ax1 = plt.subplots()
    ax1.plot(R_vals, label="リソース R(n)", color="green")
    ax1.plot(D_vals, label="欲望 D(n)", color="red")
    ax1.set_xlabel("年数")
    ax1.set_ylabel("量")
    ax1.legend()
    st.pyplot(fig1)

    # スコアの推移
    st.subheader("スコア（T(n) × (R − D)）の推移")
    fig2, ax2 = plt.subplots()
    ax2.plot(score_vals, label="成熟スコア", color="blue")
    ax2.axhline(0, color="gray", linestyle="--")
    ax2.set_xlabel("年数")
    ax2.set_ylabel("スコア")
    ax2.legend()
    st.pyplot(fig2)

    # 最終スコアと判定
    final_score = score_vals[-1]
    if final_score > 20:
        st.success(f"最終スコア {final_score:.2f} → 十分な持続性が見込まれます。")
    elif final_score > 0:
        st.warning(f"最終スコア {final_score:.2f} → 部分的に持続性がありますが、改善余地あり。")
    else:
        st.error(f"最終スコア {final_score:.2f} → 持続性に課題があります。文化的成熟または資源政策の見直しが必要です。")

# ------------------------------
# 背景と思想ページ
# ------------------------------

elif page == "背景と思想":
    st.title("このモデルの背景と思想")

    st.markdown("""
    ### 🎯 モデルの目的
    - 欲望とリソースの不均衡を文化的成熟度（T(n)）で調整し、持続可能性を評価します。

    ### 🧩 文化的成熟度 T(n) の構成要素
    - t₁：外交・安全保障（暴力や侵略への備え）
    - t₂：一次産業・エネルギー（自給・持続的生産）
    - t₃：教育・福祉（人材と社会の基盤）
    - t₄：文化・精神性（規範や倫理）

    ### 🔢 基本式
    - R(n+1) = R(n) + β × T(n)
    - D(n+1) = D(n) + α × (1 − T(n))
    - Score(n) = T(n) × (R − D)

    ### 🧠 このモデルが目指すもの
    - 「繁栄」ではなく「持続可能な繁栄」
    - 感情ではなく「摂理」に基づく判断
    - 政策・投票行動における思考補助
    """)

# ------------------------------
# スコア解釈ページ
# ------------------------------

elif page == "スコア解釈":
    st.title("スコア解釈表")

    st.markdown("""
    | スコア範囲 | 解釈 |
    |-------------|--------------------------------------------------|
    | > 20        | ✅ 高度に持続可能な社会。安定した繁栄が可能。 |
    | 0〜20       | ⚠️ 条件付き持続性。リスクはあるが安定可能。 |
    | < 0         | ❌ 持続性に深刻な課題あり。抜本的な対策が必要。 |
    """)

    st.markdown("""
    スコアは **文化的成熟度と社会のバランス** を評価する指標です。
    将来的には、国家ごとの比較や政策評価にも応用可能です。
    """)
