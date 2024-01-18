import streamlit as st
import pandas as pd

st.set_page_config(
  
    page_title="Your App Title",
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(
    """
    <style>
        body {
            background-color: #080707;
            color: #f4fbfb;
            font-family: serif;
            primaryColor=#7b2828;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url('https://scontent.fkhi21-1.fna.fbcdn.net/v/t39.30808-6/302424089_549936696883486_6803970556109482786_n.png?_nc_cat=101&ccb=1-7&_nc_sid=efb6e6&_nc_ohc=e_SxF0pGy4QAX_Se-wS&_nc_ht=scontent.fkhi21-1.fna&oh=00_AfAiX2AcKzaUBArx7z3foEyZgvJMvfVvKXetVCXlR3Hsig&oe=65AE4A60');
                background-repeat: no-repeat;
               background-size: 120px;
                padding-top: 120px;
                background-position: 20px 20px;
            }
           
           
        </style>
        """,
        unsafe_allow_html=True,
    )

st.subheader("Update Parts Master list")
# Create a DataFrame with the given data
data1 = {
   
    'Part discription<br>(father)': ['PICKUP FRAME', 'PICKUP FRAME', 'PICKUP FRAME','V6 TAIL GATE<br> <br>V6 TAIL GATE','HD TAIL GATE','HD TAIL GATE'],
    'item name(childern)': ['FANCANTINE-A40-ST1', 'COCLE-A-40-ST1', 'RACCOGLITORE_V6_DX-K56790', 'item 1<br><br>item 2','item 1','item 2'],
    'QUANTITY per order': ['1', '1', '1','1','1','1'],
   # 'program ': ['Welding part 1', 'welding part 2', 'welding part3','','',''],
     #'Detail': ['Diameter:12<br>lenght:120', 'Diameter:19<br>lenght:130', 'Diameter:15<br>lenght:170','','',''],
}
df1 = pd.DataFrame(data1)

styled_df = df1.style.hide(axis="index").set_table_styles([
  {'selector': '', 'props': [('background-color', '#FFFFFF'), ('color', 'black')]},
        {'selector': 'th', 'props': [('background-color', '#FFFFFF'), ('color', 'black')]},
])

st.markdown(styled_df.to_html(escape=False), unsafe_allow_html=True)