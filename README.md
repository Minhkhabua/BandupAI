# Project Story: BandUp AI - IELTS Writing Coach

## 📝 About the project

### What inspired us
Mastering IELTS Writing is one of the most challenging and expensive parts of the English learning journey. Students often have to wait days for human tutors to grade their essays, while traditional automated grammar checkers only catch basic spelling mistakes without evaluating the specific criteria of the official IELTS exam. 

The idea for **BandUp AI** was born to bridge this gap. We wanted to build an instant, on-demand "AI Examiner" that provides accurate band scores and highly detailed pedagogical feedback, empowering students to iterate and improve their writing skills immediately.

### How we built our project
We designed and built the application by combining a clean user interface with a lightning-fast AI inference core:
*   **Frontend UI:** Built using **Streamlit** in Python to deliver a responsive, clutter-free, and intuitive single-page web application where users can effortlessly paste their essay topics and drafts.
*   **Backend AI Engine:** Connected directly to the **Groq API** to leverage state-of-the-art Large Language Models (LLMs) executing at unprecedented inference speeds.

### The challenges we faced
Building this project was an incredible learning experience filled with real-world engineering hurdles:
1.  **Model Deprecation & Migration:** Midway through development, our initial LLM model was decommissioned by the provider. We had to swiftly adapt, refactor our connection logic, and upgrade our backend to Meta's cutting-edge `llama-3.3-70b-versatile` model.
2.  **Prompt Engineering & Structural Constraints:** Instructing a highly complex model to evaluate essays across four distinct parameters while strictly maintaining an exact Markdown output structure required rigorous trial and error. We successfully fine-tuned the system instructions to eliminate multi-language hallucinations and achieve 100% reliable structural formatting.

### What we learned
Through this project, we gained invaluable hands-on engineering skills:
*   Efficient configuration, management, and security of API integration layers using the OpenAI Python SDK standard.
*   Advanced Prompt Engineering techniques to strictly govern LLM output formats and behavioral constraints.
*   Practical debugging methodologies for resolving syntax errors, handling API exceptions, and enhancing UX engagement using interactive UI triggers like `st.balloons()`.

---

## 🛠️ Built with

**BandUp AI** leverages a modern, high-performance tech stack:

*   **Language:** Python 3
*   **Framework:** Streamlit (Rapid Web Application Development)
*   **AI Hardware Acceleration:** Groq Cloud (Ultra-low latency AI inference engine)
*   **LLM Model:** Llama 3.3 70B Versatile (Meta AI)
*   **API Standard:** OpenAI Python SDK

---

## 🚀 "Try it out" links

Explore our codebase or test the live application directly using the links below:

*   **GitHub Repository:** [https://github.com/Minhkhabua/BandupAI](https://github.com/Minhkhabua/BandupAI)
