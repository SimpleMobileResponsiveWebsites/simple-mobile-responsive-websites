import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Safe Websites — Leave PHP Behind",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom styling adapted from the boilerplate
st.markdown("""
<style>
    .hero {
        background: linear-gradient(135deg, #1e3a5f 0%, #c0392b 100%);
        padding: 4rem 2rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .hero h1 { font-size: 3.0rem; margin-bottom: 0.5rem; font-weight: 700; color: white; }
    .hero p { font-size: 1.35rem; opacity: 0.95; color: white; }
    .peace { font-size: 1.5rem; font-weight: 500; color: #fadbd8; margin-top: 1rem; }

    .service-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #c0392b;
        height: 100%;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        color: #000000 !important;
    }
    .service-card h4 { 
        margin-top: 0; 
        color: #1e3a5f !important; 
    }
    .service-card p { 
        color: #000000 !important; 
    }

    .highlight { 
        background-color: #fdecea; 
        padding: 1.5rem; 
        border-radius: 10px; 
        color: #000000 !important;
    }
    .highlight h3, 
    .highlight p, 
    .highlight li, 
    .highlight ul,
    .highlight strong {
        color: #000000 !important;
    }
    .highlight strong {
        color: #c0392b !important;
    }

    .cta-box {
        background: linear-gradient(135deg, #1e3a5f 0%, #c0392b 100%);
        padding: 3rem 2rem;
        border-radius: 12px;
        text-align: center;
        color: white;
        margin-top: 2rem;
    }
    .cta-box h2 { color: white; margin-bottom: 0.5rem; }
    .cta-box p { color: #fadbd8; font-size: 1.15rem; margin-bottom: 1.5rem; }
    .book-btn {
        display: inline-block;
        background-color: #ffffff;
        color: #1e3a5f !important;
        font-weight: 700;
        font-size: 1.15rem;
        padding: 0.9rem 2.2rem;
        border-radius: 8px;
        text-decoration: none;
        transition: all 0.2s ease;
    }
    .book-btn:hover {
        background-color: #fdecea;
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

# HERO
st.markdown("""
<div class="hero">
    <h1>Your Website & the PHP Problem</h1>
    <p>A big bug just hit the engine many WordPress sites still use.</p>
    <p class="peace">You do not have to stay on PHP.<br>Move to a platform that handles the hard stuff for you.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### Simple facts for business owners running WordPress.")

# CORE MESSAGE
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="highlight">
    <h3>What happened</h3>
    <p>PHP is the engine under most WordPress sites. A new problem called <strong>PHP2Shell</strong> was found in that engine.</p>
    <ul>
        <li>It is two serious bugs (CVE-2026-109618 and CVE-2026-109619).</li>
        <li>Hackers can run their own code on the server.</li>
        <li>They do not need a weak plugin or open admin page.</li>
        <li>Updating WordPress, themes, or plugins does <strong>not</strong> fix it.</li>
        <li>The PHP engine on the server must be updated.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight">
    <h3>What you can do</h3>
    <p><strong>Leave the PHP headaches behind.</strong></p>
    <p>Platforms like Wix, Shopify, and Square do not make you manage PHP.</p>
    <p>They handle the engine, security, and updates. Your site stays simpler and safer.</p>
    <p>Fixed PHP versions exist (8.5.12, 8.4.27, 8.3.36, 8.2.35), but many owners prefer not to deal with this again.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.subheader("Better platforms that do not use PHP")

# Service cards — alternatives
services = [
    ("Wix", "Easy drag-and-drop builder. Managed hosting. No PHP for you to patch or update."),
    ("Shopify", "Built for selling. Handles security and updates. You focus on products, not servers."),
    ("Square App / Website", "Simple websites and payments in one place. Managed platform, no PHP runtime for you to maintain."),
    ("Why switch?", "No emergency PHP patches. No server restarts. No risk from engine-level bugs like PHP2Shell."),
]

cols = st.columns(4)
for i, (title, desc) in enumerate(services):
    with cols[i % 4]:
        st.markdown(f"""
        <div class="service-card">
            <h4>{title}</h4>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")  # spacing

st.markdown("---")
st.markdown("""
### Designed to be simple
- **Business owners** get a clear explanation and a path forward.  
- **No technical jargon required.**  
- Talk through options in plain language.

**Core idea:** Stop managing the PHP engine yourself. Move to a platform where the hard security work is already handled.
""")

# Slick CTA
st.markdown("""
<div class="cta-box">
    <h2>Free 15-Minute Consultation</h2>
    <p>Want to talk about moving your site away from PHP risks?<br>Email us and we’ll set up a short, no-pressure call.</p>
    <a class="book-btn" href="mailto:simplemobileresponsivewebsites@gmail.com?subject=Free%2015-min%20consultation%20-%20moving%20off%20PHP">
        Email for Free Consultation
    </a>
    <p style="margin-top: 1rem; font-size: 1rem;">simplemobileresponsivewebsites@gmail.com</p>
</div>
""", unsafe_allow_html=True)

st.caption(f"PHP Security Info • Simple alternatives for business owners • {datetime.now().year}")
