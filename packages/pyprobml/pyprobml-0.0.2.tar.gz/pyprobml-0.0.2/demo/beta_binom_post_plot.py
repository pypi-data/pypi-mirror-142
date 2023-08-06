import sys
import streamlit as st

from pyprobml.scripts.beta_binom_post_plot import make_graph

st.subheader("Bayesian Coin Toss")
column = st.columns(1)[0]

num_heads = st.slider("Number of Heads", min_value=2, max_value=20, value=4, step=1)
num_tails = st.slider("Number of Tails", min_value=2, max_value=20, value=1, step=1)

alpha = st.slider("Alpha", min_value=0.5, max_value=5.0, value=2.0, step=0.1)
beta = st.slider("Beta", min_value=0.5, max_value=5.0, value=2.0, step=0.1)

data = {
    "prior": {"a": alpha, "b": beta},
    "likelihood": {"n_0": num_tails, "n_1": num_heads},
    "posterior": {"a": alpha + num_heads, "b": beta + num_tails},
}

fig = make_graph(data, save_name="")
fig.set_size_inches(10, 4)

with column:
    st.pyplot(fig)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown(
    """
            The above visualization shows the joint effect of data and prior on the posterior. There are some interesting observations here:
            * When prior is $Beta(1, 1)$, it becomes Uniform prior and thus **uninformative**. In this case, posterior matches with likelihood.
            * With an increase in the number of samples, the posterior gets closer to the likelihood. Thus, when the number of samples is less, prior plays an important role.
            """
)
