"""Page d'accueil."""

import streamlit as st


def render() -> None:
    st.markdown(
        """
        <div class="hero-card">
            <p class="hero-title">🇫🇷 Machine à Langue</p>
            <p class="hero-subtitle">Outils intelligents pour apprendre le français</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        Bienvenue sur **Machine à Langue**, votre plateforme dédiée à l'apprentissage
        du français. Que vous soyez élève, enseignant ou passionné de langue,
        nos outils vous accompagnent au quotidien.
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="feature-card">
                <h3>📚 Apprentissage structuré</h3>
                <p>Des ressources adaptées du primaire au lycée, organisées par niveau et par compétence.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="feature-card">
                <h3>✏️ Conjugueur intelligent</h3>
                <p>Conjuguez n'importe quel verbe en un clic et consultez tous les temps de manière claire.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="feature-card">
                <h3>🎯 Générateur d'exercices</h3>
                <p>Créez des fiches par niveau (A1–B2) et par thème : conjugaison, vocabulaire, grammaire, phrases à trous et questions.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    st.markdown("### 🚀 Par où commencer ?")
    st.info(
        "Utilisez le menu de navigation à gauche pour accéder au **Conjugueur** "
        "ou au **Générateur d'exercices**. Chaque outil est conçu pour être simple, "
        "rapide et agréable à utiliser.",
        icon="💡",
    )

    m1, m2, m3 = st.columns(3)
    m1.metric("Outils disponibles", "3", "🛠️")
    m2.metric("Langue", "Français", "🇫🇷")
    m3.metric("Public", "Tous niveaux", "🎓")