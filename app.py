import streamlit as st

st.set_page_config(page_title="curry", page_icon=":curry:", layout="wide")

st.title("おすすめのカレー屋")

st.text("気になるカレーの種類を選択してください")

options=["欧風カレー","インドカレー","スープカレー","スパイスカレー","カレーうどん"]

choice = st.selectbox("カレーを選択", options)

if choice == "欧風カレー":
    st.subheader("欧風カレー")
    st.text("上野精養軒（東京都台東区上野公園４－５８）")

elif choice == "インドカレー":
    st.subheader("インドカレー")
    st.text("エリックサウス（東京都中央区八重洲２－１八重洲地下街中４号）")

elif choice == "スープカレー":
    st.subheader("スープカレー")
    st.text("マジックスパイス（北海道札幌市白石区本郷通８丁目６－２）")

elif choice == "スパイスカレー":
    st.subheader("スパイスカレー")
    st.text("コロンビアエイト（大阪府大阪市中央区道修町１－３－３）")

elif choice == "カレーうどん":
    st.subheader("カレーうどん")
    st.text("古奈屋（東京都豊島区巣鴨３－３７－１）")