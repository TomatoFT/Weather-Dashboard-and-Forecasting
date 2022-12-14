import streamlit as st

st.set_page_config(
    page_title='Weather Dashboard and Forecast App',
    page_icon="chart_with_upwards_trend",
    layout='wide',
)
st.title('Welcome you to our Apps')
st.sidebar.success('Select an application below to use')

st.markdown(
    """
<style>
.css-1aumxhk {
    background-color: #D4AF37;
}
</style>
""",
    unsafe_allow_html=True,
)