import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from extractor import extract_insights
from fa_icons import inject_fa, fa

st.set_page_config(page_title="Distiller — AI Smart-Distiller", page_icon="🧠", layout="wide")
inject_fa()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;500&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.page-header { background: linear-gradient(135deg, #0f0f23, #1a1a3e); border-radius: 12px; padding: 1.75rem 2rem; margin-bottom: 1.5rem; }
.page-header h1 { font-family:'Playfair Display',serif; color:#e8d5b7; font-size:2rem; margin:0; display:flex; align-items:center; gap:0.6rem; }
.page-header p  { color:#8899bb; margin:0.4rem 0 0; font-size:0.9rem; }
.result-card { background: #f0fdf4; border-left: 4px solid #16a34a; padding: 1rem 1.25rem; border-radius: 8px; margin: 0.5rem 0; font-size: 0.95rem; line-height: 1.7; color: #1a1a2e; }
.task-item { background: #eff6ff; border-left: 3px solid #2563eb; padding: 0.55rem 1rem; border-radius: 6px; margin: 0.4rem 0; font-size: 0.9rem; color: #1a1a2e; display: flex; align-items: flex-start; gap: 0.5rem; }
.date-item { background: #fefce8; border-left: 3px solid #ca8a04; padding: 0.55rem 1rem; border-radius: 6px; margin: 0.4rem 0; font-size: 0.9rem; color: #1a1a2e; display: flex; align-items: flex-start; gap: 0.5rem; }
.tip-box { background: #f8f9ff; border: 1px solid #dde3f5; border-radius: 8px; padding: 1rem 1.25rem; font-size: 0.85rem; color: #3a3a6a; line-height: 1.7; }
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="page-header">
  <h1>{fa("fa-brain")} Distiller</h1>
  <p>Paste any long-form text and extract structured insights using Gemini</p>
</div>
""", unsafe_allow_html=True)

if "last_result" not in st.session_state: st.session_state.last_result = None
if "last_input"  not in st.session_state: st.session_state.last_input  = ""

sample = """Meeting Minutes — Project Kickoff
Date: April 5, 2026

Attendees: Ali, Sara, Mujtaba, Muzammil

Tasks for this sprint:
1. Sara will complete the UI wireframes by April 28, 2026.
2. Mujtaba must finish the API integration before May 3, 2026.
3. Ali is responsible for writing the final report, due May 10, 2026.

The client presentation deadline is May 15, 2026.
Budget approved: PKR 0 (free-tier APIs only).
Next sync meeting scheduled for April 29, 2026 at 10:00 AM."""

col_in, col_tip = st.columns([2, 1])

with col_in:
    st.subheader("Input Text", anchor=False)
    input_text = st.text_area(
        "Paste meeting notes, articles, project briefs, transcripts…",
        value=sample, height=300, placeholder="Paste any long-form text here…"
    )

with col_tip:
    st.markdown(f"""
    <div class="tip-box">
    <strong>{fa("fa-lightbulb")} What gets extracted</strong><br><br>
    <b>{fa("fa-list-check")} Summary</b> — core message in 2–3 sentences<br><br>
    <b>{fa("fa-check-circle")} Tasks</b> — every action item &amp; responsibility<br><br>
    <b>{fa("fa-calendar-days")} Deadlines</b> — dates with context<br><br>
    <hr style="border:none;border-top:1px solid #dde3f5;margin:0.75rem 0;">
    <strong>{fa("fa-rotate")} Next step</strong><br><br>
    Go to <b>Automation</b> to push results to Google Sheets and Email.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
run_btn = st.button("Run Distiller", type="primary")

if run_btn:
    if not input_text.strip():
        st.error("Please paste some text before processing.")
    else:
        with st.status("Running AI extraction pipeline…", expanded=True) as status:
            st.write("Sending text to Gemini API…")
            result = extract_insights(input_text)
            st.session_state.last_result = result
            st.session_state.last_input  = input_text[:300]
            status.update(label="Done — results ready below.", state="complete")

        if "error" in result:
            st.error(f"Extraction failed: {result['summary']}")
        else:
            st.markdown("---")
            st.subheader("Extracted Insights")
            tab1, tab2, tab3, tab4 = st.tabs(["Summary", "Tasks", "Deadlines", "Raw JSON"])

            with tab1:
                st.markdown(f'<div class="result-card">{result.get("summary","N/A")}</div>', unsafe_allow_html=True)

            with tab2:
                tasks = result.get("tasks", [])
                if tasks:
                    for i, t in enumerate(tasks, 1):
                        st.markdown(f'<div class="task-item"><span style="color:#2563eb">{fa("fa-check-circle")}</span><span><strong>{i}.</strong> {t}</span></div>', unsafe_allow_html=True)
                else:
                    st.info("No tasks found.")

            with tab3:
                dates = result.get("deadlines", [])
                if dates:
                    for d in dates:
                        st.markdown(f'<div class="date-item"><span style="color:#ca8a04">{fa("fa-calendar-days")}</span><span><strong>{d.get("date","")}</strong> — {d.get("context","")}</span></div>', unsafe_allow_html=True)
                else:
                    st.info("No deadlines found.")

            with tab4:
                st.json(result)

            st.success("Results saved. Go to **Automation** to push them to Google Sheets & Email.")