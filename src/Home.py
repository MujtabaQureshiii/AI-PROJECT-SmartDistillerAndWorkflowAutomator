import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from fa_icons import inject_fa, fa
from utils import email_configured,sheets_configured
from config import GROQ_API_KEY

st.set_page_config(
    page_title="AI Smart-Distiller",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

if "exited" not in st.session_state:
    st.session_state.exited = False

inject_fa()

with st.sidebar:
    st.markdown("""
    <style>
    .exit-spacer { flex: 1; }
    .exit-section { padding: 1rem 0.5rem 0.5rem; border-top: 1px solid rgba(255,255,255,0.08); margin-top: 1rem; }
    div[data-testid="stSidebar"] button[kind="secondary"] {
        background: rgba(220,38,38,0.08) !important;
        border: 1px solid rgba(220,38,38,0.35) !important;
        color: #f87171 !important; font-size: 0.85rem !important; border-radius: 8px !important;
    }
    div[data-testid="stSidebar"] button[kind="secondary"]:hover {
        background: rgba(220,38,38,0.18) !important; color: #fca5a5 !important;
    }
    </style>
    <div class="exit-spacer"></div><div class="exit-section"></div>
    """, unsafe_allow_html=True)

    if st.button("  ⇥  Exit Application", key="exit_btn_sidebar", use_container_width=True):
        st.session_state.exited = True
        st.rerun()

if st.session_state.exited:
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;500&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
section.main > div { background: #07071a !important; }
.ty-wrapper { display:flex; flex-direction:column; align-items:center; justify-content:center; min-height:82vh; text-align:center; padding:2rem; }
.ty-title { font-family:'Playfair Display',serif; font-size:3.2rem; font-weight:700; color:#e8d5b7; margin:1rem 0 0.4rem; letter-spacing:-1px; }
.ty-subtitle { font-size:1rem; color:#8899bb; font-weight:300; margin-bottom:0.4rem; }
.ty-course { font-size:0.78rem; color:#445566; letter-spacing:1.2px; text-transform:uppercase; margin-bottom:2.5rem; }
.ty-divider { width:60px; height:2px; background:linear-gradient(90deg,transparent,#e8d5b7,transparent); margin:0 auto 2.5rem; }
.ty-badges { display:flex; flex-wrap:wrap; justify-content:center; gap:1rem; max-width:780px; }
.ty-badge { background:linear-gradient(135deg,#0f0f23,#1a1a3e); border:1px solid rgba(232,213,183,0.2); border-radius:14px; padding:1.1rem 1.4rem; min-width:210px; text-align:left; position:relative; overflow:hidden; transition:border-color 0.2s,transform 0.2s; }
.ty-badge:hover { border-color:rgba(232,213,183,0.45); transform:translateY(-2px); }
.ty-badge::before { content:''; position:absolute; top:0; left:0; width:3px; height:100%; background:linear-gradient(180deg,#e8d5b7,#c8a882); border-radius:12px 0 0 12px; }
.badge-avatar { width:40px; height:40px; border-radius:50%; background:linear-gradient(135deg,#e8d5b7,#c8a882); display:flex; align-items:center; justify-content:center; font-weight:700; font-size:0.85rem; color:#1a1a2e; margin-bottom:0.65rem; }
.badge-name { font-size:0.93rem; font-weight:500; color:#e8d5b7; margin-bottom:2px; }
.badge-roll { font-size:0.76rem; color:#8899bb; font-family:monospace; margin-bottom:5px; }
.badge-role { display:inline-flex; align-items:center; gap:5px; font-size:0.68rem; color:#7788aa; background:rgba(232,213,183,0.07); border:1px solid rgba(232,213,183,0.13); padding:2px 9px; border-radius:20px; }
.ty-footer { margin-top:2.5rem; font-size:0.76rem; color:#334455; letter-spacing:0.5px; }
</style>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="ty-wrapper">
  <div style="font-size:3.5rem;color:#e8d5b7;opacity:0.85;"><i class="fas fa-brain"></i></div>
  <div class="ty-title">Thank You</div>
  <div class="ty-subtitle">AI Smart-Distiller</div>
  <div class="ty-course">FAST-NUCES &nbsp;&middot;&nbsp; Artificial Intelligence &nbsp;&middot;&nbsp; Spring 2026</div>
  <div class="ty-divider"></div>
  <div class="ty-badges">
    <div class="ty-badge">
      <div class="badge-avatar">SM</div>
      <div class="badge-name">Muzammil Zaidi</div>
      <div class="badge-roll">24K-0887</div>
      <div class="badge-role">Automation &amp; Workflows</div>
    </div>
    <div class="ty-badge">
      <div class="badge-avatar">MA</div>
      <div class="badge-name">Muzamil Ali</div>
      <div class="badge-roll">24K-1023</div>
      <div class="badge-role">Backend &amp; API Integration</div>
    </div>
    <div class="ty-badge">
      <div class="badge-avatar">GM</div>
      <div class="badge-name">Ghulam Mujtaba</div>
      <div class="badge-roll">24K-0535</div>
      <div class="badge-role">UI Design &amp; Project Lead</div>
    </div>
  </div>
  <div class="ty-footer">© 2026 FAST-NUCES Karachi · All rights reserved.</div>
</div>
""", unsafe_allow_html=True)
    st.stop()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;500&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.hero { background: linear-gradient(135deg, #0f0f23 0%, #1a1a3e 50%, #0d1b2a 100%); border-radius: 16px; padding: 3rem 3.5rem; margin-bottom: 2rem; position: relative; overflow: hidden; }
.hero::before { content: ''; position: absolute; top: -60px; right: -60px; width: 280px; height: 280px; background: radial-gradient(circle, rgba(232,213,183,0.08) 0%, transparent 70%); border-radius: 50%; }
.hero-title { font-family: 'Playfair Display', serif; font-size: 3rem; font-weight: 700; color: #e8d5b7; margin: 0; line-height: 1.1; letter-spacing: -1px; }
.hero-sub { font-size: 1.05rem; color: #8899bb; margin: 0.75rem 0 0; font-weight: 300; }
.badge-tag { display: inline-block; background: rgba(232,213,183,0.12); color: #e8d5b7; font-size: 0.72rem; padding: 3px 10px; border-radius: 20px; border: 1px solid rgba(232,213,183,0.25); margin-bottom: 1rem; letter-spacing: 0.8px; text-transform: uppercase; }
.feature-card { background: #ffffff08; border: 1px solid #ffffff14; border-radius: 12px; padding: 1.5rem; height: 100%; transition: border-color 0.2s, transform 0.2s; }
.feature-card:hover { border-color: #e8d5b730; transform: translateY(-2px); }
.feature-icon { font-size: 1.6rem; margin-bottom: 0.75rem; color: #e8d5b7; }
.feature-title { font-weight: 500; font-size: 1rem; color: #e8d5b7; margin-bottom: 0.4rem; }
.feature-desc { font-size: 0.85rem; color: #8899bb; line-height: 1.6; }
.stat-card { background: #ffffff08; border: 1px solid #ffffff14; border-radius: 10px; padding: 1rem 1.25rem; }
.stat-ok   { color: #28a745; font-weight: 600; }
.stat-warn { color: #e8d5b7; font-weight: 600; }
.stat-msg  { font-size: 0.78rem; color: #5a6a8a; margin-top: 3px; }
section.main > div { background: #0a0a1a; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div class="badge-tag">AI Project</div>
  <div class="hero-title">AI Smart-Distiller</div>
  <p class="hero-sub">Extract insights from long-form text — automatically route them to Google Sheets &amp; Email</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### What this system does")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"""<div class="feature-card"><div class="feature-icon">{fa("fa-robot")}</div><div class="feature-title">AI Extraction</div><div class="feature-desc">Uses Gemini to intelligently extract summaries, action items, and deadlines from any long-form text.</div></div>""", unsafe_allow_html=True)
with c2:
    st.markdown(f"""<div class="feature-card"><div class="feature-icon">{fa("fa-table-cells")}</div><div class="feature-title">Google Sheets</div><div class="feature-desc">Automatically appends extracted data as a new row — timestamp, summary, tasks, and deadlines organized for you.</div></div>""", unsafe_allow_html=True)
with c3:
    st.markdown(f"""<div class="feature-card"><div class="feature-icon">{fa("fa-envelope")}</div><div class="feature-title">Email Reports</div><div class="feature-desc">Sends a beautifully formatted HTML email report with all extracted insights via Gmail SMTP.</div></div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### Navigate to")
st.markdown("""
<div style="display:flex; gap:16px; margin-bottom:1rem;">
  <a href="/Distiller" style="flex:1; text-decoration:none;">
    <div style="background:linear-gradient(135deg,#1a1a3e,#0d1b2a); border:1px solid rgba(255,255,255,0.12); border-radius:12px; padding:1.25rem 1.5rem; transition:all 0.2s; height:100%;">
      <div style="display:flex; align-items:center; gap:10px; margin-bottom:6px;">
        <span style="width:36px;height:36px;background:rgba(139,124,248,0.15);border-radius:8px;display:flex;align-items:center;justify-content:center;"><i class="fas fa-brain" style="color:#8b7cf8;font-size:15px;"></i></span>
        <span style="font-size:1rem;font-weight:600;color:#e8d5b7;">Distiller</span>
      </div>
      <div style="font-size:0.82rem;color:#6677aa;padding-left:46px;">Paste text and extract AI insights</div>
    </div>
  </a>
  <a href="/Automation" style="flex:1; text-decoration:none;">
    <div style="background:linear-gradient(135deg,#1a1a3e,#0d1b2a); border:1px solid rgba(255,255,255,0.12); border-radius:12px; padding:1.25rem 1.5rem; transition:all 0.2s; height:100%;">
      <div style="display:flex; align-items:center; gap:10px; margin-bottom:6px;">
        <span style="width:36px;height:36px;background:rgba(61,220,132,0.12);border-radius:8px;display:flex;align-items:center;justify-content:center;"><i class="fas fa-bolt" style="color:#3ddc84;font-size:15px;"></i></span>
        <span style="font-size:1rem;font-weight:600;color:#e8d5b7;">Automation</span>
      </div>
      <div style="font-size:0.82rem;color:#6677aa;padding-left:46px;">Push data to Sheets &amp; Email</div>
    </div>
  </a>
  <a href="/About" style="flex:1; text-decoration:none;">
    <div style="background:linear-gradient(135deg,#1a1a3e,#0d1b2a); border:1px solid rgba(255,255,255,0.12); border-radius:12px; padding:1.25rem 1.5rem; transition:all 0.2s; height:100%;">
      <div style="display:flex; align-items:center; gap:10px; margin-bottom:6px;">
        <span style="width:36px;height:36px;background:rgba(91,192,235,0.12);border-radius:8px;display:flex;align-items:center;justify-content:center;"><i class="fas fa-book-open" style="color:#5bc0eb;font-size:15px;"></i></span>
        <span style="font-size:1rem;font-weight:600;color:#e8d5b7;">About</span>
      </div>
      <div style="font-size:0.82rem;color:#6677aa;padding-left:46px;">Project details &amp; setup guide</div>
    </div>
  </a>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### System status")
s1, s2, s3 = st.columns(3)

def status_card(col, label, ok, ok_msg, fail_msg):
    status = "✅ Live" if ok else "⚙️ Not configured"
    msg    = ok_msg if ok else fail_msg
    col.markdown(f"""<div class="stat-card"><div class="{'stat-ok' if ok else 'stat-warn'}">{status}</div><div style="font-size:0.85rem;color:#c8d0e8;margin-top:4px;">{label}</div><div class="stat-msg">{msg}</div></div>""", unsafe_allow_html=True)

with s1: status_card(s1, "Groq API", bool(GROQ_API_KEY.strip()), "llama-3.3-70b connected", "Add GROQ_API_KEY in config.py")
with s2: status_card(s2, "Google Sheets", sheets_configured(), "Service account linked", "Add GOOGLE_SERVICE_ACCOUNT_JSON")
with s3: status_card(s3, "Email (Gmail)", email_configured(), "SMTP configured", "Add EMAIL_SENDER + EMAIL_PASSWORD")