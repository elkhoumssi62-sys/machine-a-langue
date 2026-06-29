"""Styles et thème visuel pour Machine à Langue."""

NAVY = "#0f2744"
NAVY_LIGHT = "#1a3a5c"
SOFT_GREEN = "#6db89a"
SOFT_GREEN_LIGHT = "#a8d5c4"
CREAM = "#f8faf9"
ACCENT = "#2d6a8f"


def inject_custom_css() -> None:
    import streamlit as st

    st.markdown(
        f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap');

            :root {{
                --navy: {NAVY};
                --navy-light: {NAVY_LIGHT};
                --soft-green: {SOFT_GREEN};
                --soft-green-light: {SOFT_GREEN_LIGHT};
                --cream: {CREAM};
            }}

            html, body, [class*="css"] {{
                font-family: 'DM Sans', sans-serif;
            }}

            .stApp {{
                background: linear-gradient(160deg, {CREAM} 0%, #eef5f1 45%, #e8f0ec 100%);
            }}

            [data-testid="stSidebar"] {{
                background: linear-gradient(180deg, {NAVY} 0%, {NAVY_LIGHT} 100%);
            }}

            [data-testid="stSidebar"] * {{
                color: #ffffff !important;
            }}

            [data-testid="stSidebar"] .stRadio label {{
                background: rgba(255, 255, 255, 0.06);
                border-radius: 12px;
                padding: 0.55rem 0.85rem;
                margin-bottom: 0.35rem;
                border: 1px solid rgba(255, 255, 255, 0.08);
                transition: all 0.2s ease;
            }}

            [data-testid="stSidebar"] .stRadio label:hover {{
                background: rgba(109, 184, 154, 0.25);
                border-color: {SOFT_GREEN};
            }}

            [data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label[data-baseweb="radio"] {{
                padding: 0.5rem 0.75rem;
            }}

            .hero-card {{
                background: linear-gradient(135deg, {NAVY} 0%, {NAVY_LIGHT} 55%, {ACCENT} 100%);
                border-radius: 24px;
                padding: 2.5rem 2rem;
                color: white;
                box-shadow: 0 20px 50px rgba(15, 39, 68, 0.18);
                margin-bottom: 2rem;
            }}

            .hero-title {{
                font-size: 2.6rem;
                font-weight: 700;
                margin: 0 0 0.5rem 0;
                letter-spacing: -0.02em;
            }}

            .hero-subtitle {{
                font-size: 1.2rem;
                opacity: 0.92;
                margin: 0;
                color: {SOFT_GREEN_LIGHT};
            }}

            .feature-card {{
                background: white;
                border-radius: 18px;
                padding: 1.5rem;
                border: 1px solid rgba(15, 39, 68, 0.08);
                box-shadow: 0 8px 24px rgba(15, 39, 68, 0.06);
                height: 100%;
            }}

            .feature-card h3 {{
                color: {NAVY};
                margin-top: 0;
                font-size: 1.15rem;
            }}

            .feature-card p {{
                color: #4a5568;
                margin-bottom: 0;
                line-height: 1.6;
            }}

            .page-header {{
                color: {NAVY};
                font-size: 2rem;
                font-weight: 700;
                margin-bottom: 0.25rem;
            }}

            .page-subheader {{
                color: #5a6b7d;
                font-size: 1.05rem;
                margin-bottom: 1.5rem;
            }}

            .stButton > button {{
                background: linear-gradient(135deg, {SOFT_GREEN} 0%, #5aa88a 100%);
                color: white;
                border: none;
                border-radius: 12px;
                padding: 0.6rem 1.8rem;
                font-weight: 600;
                box-shadow: 0 4px 14px rgba(109, 184, 154, 0.35);
                transition: transform 0.15s ease, box-shadow 0.15s ease;
            }}

            .stButton > button:hover {{
                transform: translateY(-1px);
                box-shadow: 0 6px 20px rgba(109, 184, 154, 0.45);
                color: white;
                border: none;
            }}

            div[data-testid="stMetric"] {{
                background: white;
                border-radius: 14px;
                padding: 1rem;
                border: 1px solid rgba(15, 39, 68, 0.08);
                box-shadow: 0 4px 12px rgba(15, 39, 68, 0.04);
            }}

            .verb-header-card {{
                background: white;
                border-radius: 20px;
                padding: 1.75rem 2rem;
                border: 1px solid rgba(15, 39, 68, 0.1);
                box-shadow: 0 12px 32px rgba(15, 39, 68, 0.08);
                margin-bottom: 1.5rem;
            }}

            .verb-header-top {{
                display: flex;
                align-items: baseline;
                gap: 1.25rem;
                flex-wrap: wrap;
                margin-bottom: 1rem;
            }}

            .verb-title {{
                color: {NAVY};
                font-size: 2.2rem;
                font-weight: 700;
                margin: 0;
                text-transform: capitalize;
            }}

            .verb-phonetic {{
                color: {SOFT_GREEN};
                font-size: 1.15rem;
                font-style: italic;
                font-weight: 500;
            }}

            .verb-badges {{
                display: flex;
                gap: 0.6rem;
                flex-wrap: wrap;
            }}

            .verb-badge {{
                display: inline-block;
                padding: 0.35rem 0.85rem;
                border-radius: 999px;
                font-size: 0.82rem;
                font-weight: 600;
            }}

            .verb-badge.reflexive {{
                background: rgba(109, 184, 154, 0.18);
                color: #2d6a4f;
            }}

            .verb-badge.aux {{
                background: rgba(45, 106, 143, 0.12);
                color: {ACCENT};
            }}

            .verb-badge.base {{
                background: rgba(15, 39, 68, 0.08);
                color: {NAVY};
            }}

            .tense-hint {{
                color: #5a6b7d;
                font-size: 0.95rem;
                font-style: italic;
                margin: 0 0 1rem 0;
                padding: 0.6rem 1rem;
                background: rgba(109, 184, 154, 0.1);
                border-left: 3px solid {SOFT_GREEN};
                border-radius: 0 8px 8px 0;
            }}

            .conj-table-wrapper {{
                border-radius: 16px;
                overflow: hidden;
                border: 1px solid rgba(15, 39, 68, 0.1);
                box-shadow: 0 6px 20px rgba(15, 39, 68, 0.06);
                margin-bottom: 1.25rem;
            }}

            .conj-table {{
                width: 100%;
                border-collapse: collapse;
                background: white;
            }}

            .conj-table th {{
                background: linear-gradient(135deg, {NAVY} 0%, {NAVY_LIGHT} 100%);
                color: white;
                padding: 0.85rem 1.25rem;
                text-align: left;
                font-weight: 600;
                font-size: 0.9rem;
                letter-spacing: 0.03em;
                text-transform: uppercase;
            }}

            .conj-table td {{
                padding: 0.8rem 1.25rem;
                border-bottom: 1px solid #edf2f7;
            }}

            .conj-pronom {{
                color: {ACCENT};
                font-weight: 600;
                width: 28%;
            }}

            .conj-form {{
                color: {NAVY};
                font-weight: 500;
                font-size: 1.05rem;
            }}

            .conj-row-odd td {{
                background: #ffffff;
            }}

            .conj-row-even td {{
                background: #f7faf9;
            }}

            .conj-table tr:hover td {{
                background: rgba(109, 184, 154, 0.12) !important;
                transition: background 0.15s ease;
            }}

            .conj-table tr:last-child td {{
                border-bottom: none;
            }}

            .example-card {{
                background: linear-gradient(135deg, rgba(15,39,68,0.04) 0%, rgba(109,184,154,0.1) 100%);
                border-radius: 14px;
                padding: 1.1rem 1.35rem;
                border: 1px solid rgba(109, 184, 154, 0.25);
                margin-top: 0.5rem;
            }}

            .example-label {{
                color: {SOFT_GREEN};
                font-weight: 700;
                font-size: 0.82rem;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }}

            .example-text {{
                color: {NAVY};
                font-size: 1.05rem;
                margin: 0.4rem 0 0 0;
                line-height: 1.55;
                font-style: italic;
            }}

            [data-testid="stTabs"] button {{
                font-weight: 600;
            }}

            [data-testid="stTabs"] [aria-selected="true"] {{
                color: {NAVY} !important;
                border-bottom-color: {SOFT_GREEN} !important;
            }}

            .sidebar-brand {{
                text-align: center;
                padding: 1rem 0 1.5rem 0;
                border-bottom: 1px solid rgba(255,255,255,0.12);
                margin-bottom: 1rem;
            }}

            .sidebar-brand-title {{
                font-size: 1.35rem;
                font-weight: 700;
                margin: 0;
            }}

            .sidebar-brand-sub {{
                font-size: 0.8rem;
                opacity: 0.75;
                margin: 0.25rem 0 0 0;
            }}

            .exo-config-card {{
                background: white;
                border-radius: 18px;
                padding: 1.5rem 1.75rem;
                border: 1px solid rgba(15, 39, 68, 0.1);
                box-shadow: 0 8px 24px rgba(15, 39, 68, 0.06);
                margin-bottom: 1.5rem;
            }}

            .exo-card {{
                background: white;
                border-radius: 18px;
                padding: 1.5rem 1.75rem 0.5rem 1.75rem;
                border: 1px solid rgba(15, 39, 68, 0.1);
                box-shadow: 0 8px 28px rgba(15, 39, 68, 0.07);
                margin-bottom: 0.5rem;
            }}

            .exo-card-header {{
                display: flex;
                align-items: center;
                gap: 0.65rem;
                flex-wrap: wrap;
                margin-bottom: 0.75rem;
            }}

            .exo-number {{
                background: {NAVY};
                color: white;
                font-weight: 700;
                font-size: 0.8rem;
                padding: 0.2rem 0.55rem;
                border-radius: 8px;
            }}

            .exo-title {{
                color: {NAVY};
                font-size: 1.2rem;
                font-weight: 700;
                flex: 1;
            }}

            .exo-badge {{
                color: white;
                font-size: 0.75rem;
                font-weight: 700;
                padding: 0.25rem 0.65rem;
                border-radius: 999px;
            }}

            .exo-theme-badge {{
                background: rgba(109, 184, 154, 0.2);
                color: #2d6a4f;
                font-size: 0.75rem;
                font-weight: 600;
                padding: 0.25rem 0.65rem;
                border-radius: 999px;
            }}

            .exo-instruction {{
                color: #5a6b7d;
                font-size: 0.95rem;
                margin: 0 0 1rem 0;
                line-height: 1.5;
            }}

            .exo-body {{
                background: #f7faf9;
                border-radius: 14px;
                padding: 1.25rem 1.5rem;
                color: {NAVY};
                font-size: 1.05rem;
                line-height: 1.75;
                border: 1px solid rgba(109, 184, 154, 0.2);
                margin-bottom: 1rem;
            }}

            .exo-correction {{
                background: linear-gradient(135deg, rgba(109,184,154,0.12) 0%, rgba(45,106,143,0.08) 100%);
                border-radius: 14px;
                padding: 1.15rem 1.4rem;
                border: 1px solid rgba(109, 184, 154, 0.35);
                margin: 0.5rem 0 0.75rem 0;
            }}

            .exo-corr-label {{
                color: {SOFT_GREEN};
                font-weight: 700;
                font-size: 0.85rem;
                text-transform: uppercase;
                letter-spacing: 0.04em;
            }}

            .exo-corr-body {{
                color: {NAVY};
                font-size: 1.02rem;
                line-height: 1.7;
                margin-top: 0.5rem;
            }}

            .exo-tip {{
                color: #5a6b7d;
                font-size: 0.9rem;
                font-style: italic;
                padding: 0.5rem 0;
            }}

            .exo-divider {{
                height: 1px;
                background: rgba(15, 39, 68, 0.08);
                margin: 1.25rem 0;
            }}

            .exo-results-header {{
                background: linear-gradient(135deg, {NAVY} 0%, {NAVY_LIGHT} 100%);
                color: white;
                padding: 0.85rem 1.25rem;
                border-radius: 12px;
                margin-bottom: 1.25rem;
                font-size: 0.95rem;
            }}

            .exo-preview-card {{
                background: white;
                border-radius: 14px;
                padding: 1rem;
                text-align: center;
                border: 1px solid rgba(15, 39, 68, 0.08);
                box-shadow: 0 4px 12px rgba(15, 39, 68, 0.04);
                height: 100%;
            }}

            .exo-preview-card strong {{
                color: {NAVY};
                display: block;
                margin: 0.4rem 0;
                font-size: 0.85rem;
            }}

            .exo-preview-card p {{
                color: #6b7c8d;
                font-size: 0.75rem;
                margin: 0;
                line-height: 1.4;
            }}

            .exo-preview-icon {{
                font-size: 1.5rem;
            }}

            .exo-subtype-badge {{
                background: rgba(45, 106, 143, 0.15);
                color: {ACCENT};
                font-size: 0.72rem;
                font-weight: 600;
                padding: 0.2rem 0.6rem;
                border-radius: 999px;
            }}

            .exo-source-badge {{
                font-size: 0.72rem;
                font-weight: 600;
                padding: 0.2rem 0.6rem;
                border-radius: 999px;
            }}

            .exo-source-grok {{
                background: rgba(15, 39, 68, 0.12);
                color: {NAVY};
            }}

            .exo-source-local {{
                background: rgba(109, 184, 154, 0.2);
                color: #2d6a4f;
            }}

            .exo-level-track {{
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 0;
                margin: 1rem 0 1.25rem 0;
                padding: 0.75rem;
                background: rgba(109, 184, 154, 0.08);
                border-radius: 14px;
            }}

            .exo-level-step {{
                display: flex;
                flex-direction: column;
                align-items: center;
                padding: 0.5rem 1rem;
                border-radius: 12px;
                opacity: 0.45;
                transition: all 0.2s ease;
                min-width: 72px;
            }}

            .exo-level-step.active {{
                opacity: 1;
                background: white;
                box-shadow: 0 4px 14px rgba(15, 39, 68, 0.1);
                border: 2px solid {SOFT_GREEN};
            }}

            .exo-level-step.done {{
                opacity: 0.75;
            }}

            .exo-level-emoji {{
                font-size: 1.2rem;
                line-height: 1;
            }}

            .exo-level-code {{
                font-weight: 800;
                color: {NAVY};
                font-size: 0.95rem;
                margin-top: 0.2rem;
            }}

            .exo-level-name {{
                font-size: 0.65rem;
                color: #6b7c8d;
                text-transform: uppercase;
                letter-spacing: 0.03em;
            }}

            .exo-level-connector {{
                width: 28px;
                height: 3px;
                background: linear-gradient(90deg, {SOFT_GREEN}, {ACCENT});
                border-radius: 2px;
                opacity: 0.35;
            }}

            .exo-meta-bar {{
                display: flex;
                gap: 1.25rem;
                flex-wrap: wrap;
                background: linear-gradient(135deg, {NAVY} 0%, {NAVY_LIGHT} 100%);
                color: white;
                padding: 0.65rem 1.2rem;
                border-radius: 12px 12px 0 0;
                font-size: 0.82rem;
                font-weight: 600;
            }}

            .exo-meta-bar span {{
                opacity: 0.95;
            }}

            .exo-card {{
                border-radius: 0 0 18px 18px !important;
                margin-top: 0 !important;
            }}

            .exo-actions-bar {{
                margin: 0.5rem 0 1.25rem 0;
            }}

            .exo-pedago-note {{
                display: flex;
                gap: 0.85rem;
                align-items: flex-start;
                background: #fffbea;
                border: 1px solid rgba(234, 179, 8, 0.35);
                border-radius: 14px;
                padding: 1rem 1.25rem;
                margin: 0.75rem 0;
            }}

            .exo-pedago-icon {{
                font-size: 1.4rem;
                line-height: 1;
            }}

            .exo-pedago-note strong {{
                color: {NAVY};
                font-size: 0.85rem;
                text-transform: uppercase;
                letter-spacing: 0.03em;
            }}

            .exo-pedago-note p {{
                color: #5a6b7d;
                margin: 0.35rem 0 0 0;
                font-size: 0.92rem;
                line-height: 1.5;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )