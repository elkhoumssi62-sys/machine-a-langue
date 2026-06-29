"""
Machine à Langue — Application Streamlit
Outils intelligents pour apprendre le français
"""

import streamlit as st

from utils.styles import inject_custom_css
from views import accueil, conjugueur, exercices

PAGES = {
    "🏠 Accueil": accueil,
    "📖 Conjugueur": conjugueur,
    "🎯 Générateur d'exercices": exercices,
}


def render_sidebar() -> str:
    st.sidebar.markdown(
        """
        <div class="sidebar-brand">
            <p class="sidebar-brand-title">🇫🇷 Machine à Langue</p>
            <p class="sidebar-brand-sub">Apprendre le français</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    page = st.sidebar.radio(
        "Navigation",
        list(PAGES.keys()),
        label_visibility="collapsed",
    )

    st.sidebar.divider()
    st.sidebar.caption("© 2026 Machine à Langue")
    st.sidebar.caption("Outils intelligents pour le français 🇫🇷")

    return page


def main() -> None:
    st.set_page_config(
        page_title="Machine à Langue",
        page_icon="🇫🇷",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    inject_custom_css()
    selected = render_sidebar()
    PAGES[selected].render()


if __name__ == "__main__":
    main()