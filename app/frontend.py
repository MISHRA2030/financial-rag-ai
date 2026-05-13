import streamlit as st
import requests


# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Financial RAG AI",
    page_icon="📈",
    layout="wide"
)


# =========================================
# SESSION STATE
# =========================================

if "username" not in st.session_state:
    st.session_state.username = ""


# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

.stTextInput input {
    background-color: #262730;
    color: white;
    border-radius: 10px;
    border: 1px solid #00FFAA;
    padding: 12px;
}

.stButton button {
    background: linear-gradient(90deg,#00FFAA,#00BFFF);
    color: black;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
}

.result-box {
    background-color: #1E1E1E;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #00FFAA;
    margin-top: 20px;
}

.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: #00FFAA;
}

.subtitle {
    text-align: center;
    color: #BBBBBB;
    margin-bottom: 30px;
}

.welcome-box {
    background-color:#1E1E1E;
    padding:20px;
    border-radius:15px;
    border:1px solid #00FFAA;
    margin-top:50px;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)


# =========================================
# NAME SCREEN
# =========================================

if st.session_state.username == "":

    st.markdown(
        """
        <div class='welcome-box'>
            <h1 style='color:#00FFAA;'>
                🚀 Welcome to Financial RAG AI
            </h1>

            <p style='color:white;font-size:18px;'>
                AI-Powered Financial Assistant
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    name = st.text_input(
        "👤 Enter Your Name"
    )

    if st.button("Enter System"):

        if name.strip() != "":

            st.session_state.username = name
            st.rerun()

        else:

            st.warning("Please enter your name.")

    st.stop()


# =========================================
# MAIN APP UI
# =========================================

st.markdown(
    "<div class='title'>📈 Financial RAG AI Assistant</div>",
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class='subtitle'>
        🚀 Welcome, {st.session_state.username}
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================
# SIDEBAR
# =========================================

with st.sidebar:

    st.header("⚡ System Info")

    st.success("✅ FastAPI Connected")
    st.success("✅ FAISS Vector DB")
    st.success("✅ HuggingFace Embeddings")
    st.success("✅ Financial Dataset Loaded")

    st.markdown("---")

    st.subheader("💡 Example Questions")

    st.write("- What is revenue growth?")
    st.write("- Explain operating cash flow")
    st.write("- What is net income?")
    st.write("- Explain liabilities")


# =========================================
# QUESTION INPUT
# =========================================

query = st.text_input(
    "🔍 Ask a Financial Question"
)


# =========================================
# BUTTON
# =========================================

if st.button("Generate Answer"):

    if query.strip() != "":

        with st.spinner("🤖 Analyzing financial data..."):

            try:

                url = f"http://127.0.0.1:8000/ask?query={query}"

                response = requests.get(url)

                data = response.json()

                answer = data.get(
                    "answer",
                    "No answer generated."
                )

                st.markdown(
                    f"""
                    <div class='result-box'>
                        <h3>📊 AI Response</h3>
                        <p>{answer}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            except Exception as e:

                st.error(f"Error: {e}")

    else:

        st.warning("⚠️ Please enter a question.")


# =========================================
# FOOTER
# =========================================

st.markdown("---")

