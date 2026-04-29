import streamlit as st
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from webhook import send_to_n8n
from fa_icons import inject_fa, fa

st.set_page_config(page_title="Automation — AI Smart-Distiller", page_icon="⚡", layout="wide")
inject_fa()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;500&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.page-header { background: linear-gradient(135deg, #0d1f0d, #1a3a1a); border-radius: 12px; padding: 1.75rem 2rem; margin-bottom: 1.5rem; }
.page-header h1 { font-family:'Playfair Display',serif; color:#c8f0c8; font-size:2rem; margin:0; display:flex; align-items:center; gap:0.6rem; }
.page-header p  { color:#7aaa7a; margin:0.4rem 0 0; font-size:0.9rem; }
.dest-card { border: 1.5px solid #e0e0e0; border-radius: 12px; padding: 1.5rem; background: #fafafa; transition: border-color 0.2s; }
.dest-card.active { border-color: #2563eb; background: #f0f6ff; }
.dest-title { font-size: 1.05rem; font-weight: 500; color: #1a1a2e; display: flex; align-items: center; gap: 0.5rem; }
.dest-desc  { font-size: 0.83rem; color: #666; margin-top: 4px; line-height: 1.5; }
.result-preview { background: #f8f9ff; border: 1px solid #dde3f5; border-radius: 8px; padding: 1rem 1.25rem; font-size: 0.88rem; color: #3a3a6a; line-height: 1.7; max-height: 180px; overflow-y: auto; }
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="page-header">
  <h1>{fa("fa-bolt")} Automation</h1>
  <p>Push extracted insights to Google Sheets and Email via n8n</p>
</div>
""", unsafe_allow_html=True)

result = st.session_state.get("last_result", None)
if not result:
    st.warning("No extracted data yet. Go to **Distiller** first and run the pipeline.")
    st.stop()

with st.expander("Preview: data that will be sent", expanded=True):
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("**Summary**")
        st.markdown(f'<div class="result-preview">{result.get("summary","—")}</div>', unsafe_allow_html=True)
        st.markdown("**Tasks**")
        tasks_html = "".join(f'<div>{fa("fa-check-circle","color:#2563eb;")} {t}</div>' for t in result.get("tasks",[])) or "<i>None found</i>"
        st.markdown(f'<div class="result-preview">{tasks_html}</div>', unsafe_allow_html=True)
    with col_b:
        st.markdown("**Deadlines**")
        dl_html = "".join(f'<div>{fa("fa-calendar-days","color:#ca8a04;")} <b>{d["date"]}</b> — {d["context"]}</div>' for d in result.get("deadlines",[])) or "<i>None found</i>"
        st.markdown(f'<div class="result-preview">{dl_html}</div>', unsafe_allow_html=True)

st.markdown("---")
st.subheader("Choose destinations")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="dest-card active">
      <div class="dest-title">{fa("fa-table-cells")} Google Sheets</div>
      <div class="dest-desc">Appends one row via n8n webhook<br>Sheet: <strong>AI Distiller Output</strong></div>
    </div>""", unsafe_allow_html=True)
    send_sheets = st.checkbox("Send to Google Sheets", value=True)

with col2:
    st.markdown(f"""
    <div class="dest-card active">
      <div class="dest-title">{fa("fa-envelope")} Email Report</div>
      <div class="dest-desc">Sends formatted HTML email via n8n webhook<br>Via Gmail integration</div>
    </div>""", unsafe_allow_html=True)
    send_mail = st.checkbox("Send Email Report", value=True)

st.markdown("<br>", unsafe_allow_html=True)
run_auto = st.button("Run Automation", type="primary")

if run_auto:
    if not send_sheets and not send_mail:
        st.error("Select at least one destination.")
    else:
        targets = []
        if send_sheets: targets.append("Google Sheets")
        if send_mail:   targets.append("Email")

        with st.status("Sending to n8n…", expanded=True) as status:
            st.write(f"Firing webhook → {', '.join(targets)}…")
            log = send_to_n8n(result, targets)
            all_ok = all(v["status_code"] == 200 for v in log.values())
            status.update(
                label="Automation complete!" if all_ok else "Completed with errors.",
                state="complete" if all_ok else "error"
            )

        st.markdown("---")
        for dest, res in log.items():
            if res["status_code"] == 200:
                st.success(f"**{dest}** — {res['message']}")
            else:
                st.error(f"**{dest}** — {res['message']}")