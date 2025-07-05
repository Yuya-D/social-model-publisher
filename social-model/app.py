import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------
# 初期設定
# -------------------------------
st.set_page_config(page_title="摂理AIモデル", layout="wide")

# -------------------------------
# ユーザー入力
# -------------------------------
st.sidebar.title("パラメータ調整")
years = st.sidebar.slider("シミュレーション年数", 1, 50, 20)

# 各 t_i の文化的パラメータ
st.sidebar.subheader("社会構成パラメータ (tᵢ)")
t1 = st.sidebar.slider("共感性 (t₁)", 0.0, 1.0, 0.5)
t2 = st.sidebar.slider("公共心 (t₂)", 0.0, 1.0, 0.5)
t3 = st.sidebar.slider("倫理性 (t₃)", 0.0, 1.0, 0.5)
t4 = st.sidebar.slider("持続志向 (t₄)", 0.0, 1.0, 0.5)

# リソースと欲望の成長係数
alpha = st.sidebar.slider("欲望の増加係数 α", 0.1, 2.0, 1.0)
beta = st.sidebar.slider("リソースの増加係数 β", 0.1, 2.0, 0.5)

# 初期値
R0 = 100
D0 = 80

# -------------------------------
# S(n), T(n) の計算
# -------------------------------
S = min(t1, t2, t3, t4)  # 最小値モデル
Tn = S  # 今回はT(n) = S(n)

# -------------------------------
# ページ構成
# -------------------------------
page = st.sidebar.radio("ページを選択", ["モデルの可視化", "背景と思想", "S(n) 構造と思想"])

# -------------------------------
# モデルの可視化ページ
# -------------------------------
if page == "モデルの可視化":
    st.title("摂理AIモデル：文化的成熟と持続性の可視化")

    R, D = R0, D0
    R_vals, D_vals, T_vals, S_vals, score_vals = [R], [D], [Tn], [S], [Tn * (R - D)]

    for _ in range(years):
        R = R + beta * Tn
        D = D + alpha * (1 - Tn)
        R_vals.append(R)
        D_vals.append(D)
        S_vals.append(S)
        T_vals.append(Tn)
        score_vals.append(Tn * (R - D))

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("リソースと欲望の推移")
        fig1, ax1 = plt.subplots()
        ax1.plot(R_vals, label="リソース R(n)", color="green")
        ax1.plot(D_vals, label="欲望 D(n)", color="red")
        ax1.set_xlabel("年数")
        ax1.set_ylabel("量")
        ax1.legend()
        st.pyplot(fig1)

    with col2:
        st.subheader("成熟スコアの推移 T(n) × (R - D)")
        fig2, ax2 = plt.subplots()
        ax2.plot(score_vals, label="スコア", color="blue")
        ax2.axhline(0, color="gray", linestyle="--")
        ax2.set_xlabel("年数")
        ax2.set_ylabel("スコア")
        ax2.legend()
        st.pyplot(fig2)

    # 判定テーブル
    st.subheader("成熟スコア 判定基準")
    st.markdown("""
    | スコア範囲 | 判定 |
    |------------|------|
    | > 20       | 🌱 高度に持続可能 |
    | 5〜20      | ✅ 安定的に持続可能 |
    | 0〜5       | ⚠️ 持続可能性に注意 |
    | < 0        | ❌ 持続困難（改善要） |
    """)

    final_score = score_vals[-1]
    if final_score > 20:
        st.success(f"最終スコア {final_score:.2f} → 🌱 高度に持続可能")
    elif final_score > 5:
        st.success(f"最終スコア {final_score:.2f} → ✅ 安定的に持続可能")
    elif final_score > 0:
        st.warning(f"最終スコア {final_score:.2f} → ⚠️ 持続可能性に注意")
    else:
        st.error(f"最終スコア {final_score:.2f} → ❌ 持続困難（改善要）")

# -------------------------------
# 背景ページ
# -------------------------------
elif page == "背景と思想":
    st.title("このモデルの背景と思想")
    st.markdown("""
    ### なぜこのモデルが必要なのか？
    現代社会は「欲望の無限性」と「リソースの有限性」というジレンマを抱えています。

    それを解決する鍵が「文化的成熟度 T(n)」であり、
    社会の内的構造（S(n)）と連動させながら、
    持続性を測るための数理モデルが必要です。

    ### 基本式
    - R(n+1) = R(n) + β × T(n)
    - D(n+1) = D(n) + α × (1 − T(n))
    - スコア = T(n) × (R(n) − D(n))

    ### このモデルが目指すもの
    - 単なる経済成長でなく **人類の繁栄の持続性**
    - **政治や教育、外交政策**の優先順位の見直し
    - 投票行動の判断基準としての **摂理的インフラ**
    """)

# -------------------------------
# S(n)の説明ページ
# -------------------------------
elif page == "S(n) 構造と思想":
    st.title("S(n)：社会構造スコアの構成と思想")
    st.markdown("""
    ### S(n)とは？
    社会を構成する文化的要素の **階層的最小構造**。
    欲望に調和するための構造的成熟度と位置付けられます。

    #### 各要素の意味
    - **t₁（共感性）**：他者と共感し、調和的行動をとる力
    - **t₂（公共心）**：自己中心性から離れ、公共を尊ぶ力
    - **t₃（倫理性）**：社会的正義やルールを守る心
    - **t₄（持続志向）**：未来や他世代を意識する態度

    ### S(n) の計算方法
    - 現段階では `S(n) = min(t₁, t₂, t₃, t₄)` として最も弱い部分がボトルネックになるモデルを採用
    - 将来的には **重みづけ平均** や **論理モデル** との切替可能性あり

    ### なぜ最小値を使うのか？
    文化的未熟さは一部に集中することが多く、
    最も弱い要素が社会の「限界点」になるからです。
    """)
