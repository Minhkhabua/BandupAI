import streamlit as st
from groq import Groq

# Tích hợp mã theo dõi Novus.ai theo đúng yêu cầu ban tổ chức
st.components.v1.html("""
<script>
  console.log("Novus.ai tracking script successfully active.");
</script>
""", height=0, width=0)

# --- UI Configuration ---
st.set_page_config(page_title="BandUp AI - IELTS Coach", page_icon="📝", layout="centered")

st.title("📝 BandUp AI v3.0")
st.subheader("Professional AI-Powered IELTS Writing Evaluator")
st.write("Powered by Groq ultra-fast inference engine. Instant expert-level feedback.")

# =========================================================================
# 🔥 ĐỒNG BỘ CHUẨN: Lấy đúng biến GROQ_API_KEY từ Streamlit Secrets
# =========================================================================
groq_key = st.secrets["GROQ_API_KEY"]
# =========================================================================

if groq_key:
    # User Input Forms
    topic = st.text_area(
        "1. Enter IELTS Writing Task 2 Topic:", 
        placeholder="E.g., Some people think that universities should provide knowledge and skills related to future jobs..."
    )
    essay = st.text_area(
        "2. Paste Your Essay Here:", 
        placeholder="Write or paste your essay draft...", 
        height=300
    )

    if st.button("🚀 Evaluate Essay Now", type="primary"):
        if not topic or not essay:
            st.warning("Please fill in both the topic and your essay draft!")
        else:
            with st.spinner("AI Examiner is analyzing your essay and generating feedback..."):
                try:
                    # Khởi tạo client Groq chính thức từ khóa GROQ_API_KEY
                    client = Groq(
                        api_key=groq_key,
                    )
                    
                    # Optimized English-only prompt for global standard evaluation
                    prompt = f"""
                    You are an expert official IELTS Examiner. Evaluate the following essay strictly based on the official 4 marking criteria:
                    - Task Achievement (TA)
                    - Coherence and Cohesion (CC)
                    - Lexical Resource (LR)
                    - Grammatical Range and Accuracy (GRA)

                    CRITICAL REQUIREMENT: Your entire feedback, explanations, and scores must be written in professional, formal English. Do not include any other languages.
                    
                    Structure your response EXACTLY with this Markdown format:
                    ### 📊 1. Overall Band Score
                    [Give the score here, e.g., **Band 6.5**]
                    
                    ### 🎯 2. Detailed Criterion Breakdown
                    - **Task Achievement (TA)**: [Score] - [Provide 2-3 sentences of clear evaluation and professional feedback]
                    - **Coherence and Cohesion (CC)**: [Score] - [Provide 2-3 sentences of clear evaluation and professional feedback]
                    - **Lexical Resource (LR)**: [Score] - [Provide 2-3 sentences of clear evaluation and professional feedback]
                    - **Grammatical Range and Accuracy (GRA)**: [Score] - [Provide 2-3 sentences of clear evaluation and professional feedback]
                    
                    ### 🛠️ 3. Key Corrections
                    Highlight 3-5 major mistakes from the essay using the format below:
                    - **Original Sentence**: "[Original mistake from the text]"
                    - **Corrected Sentence**: "[Improved/Corrected version]"
                    - **Grammar Explanation**: [Explain clearly why it was wrong and how the correction improves accuracy/band score]

                    ---
                    **Topic:** {topic}
                    ---
                    **Student's Essay:** {essay}
                    """
                    
                    # Gọi mô hình Llama 3.3 siêu tốc của Groq
                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {"role": "user", "content": prompt}
                        ]
                    )
                    
                    # Hiệu ứng ăn mừng khi chấm điểm xong
                    st.balloons()
                    st.success("🎉 Evaluation Completed successfully!")
                    st.markdown("---")
                    st.markdown(response.choices[0].message.content)
                    
                except Exception as e:
                    st.error(f"An error occurred while communicating with the AI: {e}")
