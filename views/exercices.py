"""Générateur d'exercices FLE — interface professionnelle."""

from __future__ import annotations

import html

import streamlit as st

from utils.exercise_generator import (
    LEVELS,
    LEVEL_COLORS,
    THEME_ICONS,
    THEMES,
    VOCAB_SUBTYPES,
    Exercise,
    generate_exercise_smart,
    get_level_info,
    get_theme_description,
)
from utils.grok_client import get_model, is_api_configured


def _fmt_html(text: str) -> str:
    return text.replace("\n", "<br>")


def _generate(level: str, theme: str, use_grok: bool) -> None:
    spinner = "Grok génère votre exercice…" if use_grok else "Préparation de votre fiche pédagogique…"
    with st.spinner(spinner):
        exercise, warning = generate_exercise_smart(level, theme, use_grok=use_grok)
    st.session_state["exo_current"] = exercise
    st.session_state["exo_show_corr"] = False
    st.session_state["exo_meta"] = {"level": level, "theme": theme, "use_grok": use_grok}
    st.session_state["exo_warning"] = warning
    st.session_state["exo_count"] = st.session_state.get("exo_count", 0) + 1


def _render_level_track(current: str) -> None:
    steps = []
    for i, lvl in enumerate(LEVELS):
        label, emoji = get_level_info(lvl)
        active = "active" if lvl == current else ""
        done = "done" if LEVELS.index(lvl) < LEVELS.index(current) else ""
        steps.append(
            f'<div class="exo-level-step {active} {done}">'
            f'<span class="exo-level-emoji">{emoji}</span>'
            f'<span class="exo-level-code">{lvl}</span>'
            f'<span class="exo-level-name">{label}</span>'
            f"</div>"
        )
        if i < len(LEVELS) - 1:
            steps.append('<div class="exo-level-connector"></div>')
    st.markdown(
        f'<div class="exo-level-track">{"".join(steps)}</div>',
        unsafe_allow_html=True,
    )


def _source_badge(exercise: Exercise) -> str:
    if exercise.source == "grok":
        return '<span class="exo-source-badge exo-source-grok">🤖 Grok</span>'
    return '<span class="exo-source-badge exo-source-local">📦 Local</span>'


def _render_exercise(exercise: Exercise) -> None:
    icon = THEME_ICONS.get(exercise.theme, "📋")
    color = LEVEL_COLORS.get(exercise.level, "#0f2744")
    subtype_badge = (
        f'<span class="exo-subtype-badge">{html.escape(exercise.subtype)}</span>'
        if exercise.subtype else ""
    )
    count = st.session_state.get("exo_count", 1)

    st.markdown(
        f"""
        <div class="exo-meta-bar">
            <span>📋 Fiche n°{count}</span>
            <span>❓ {exercise.question_count} question{"s" if exercise.question_count > 1 else ""}</span>
            <span>⏱️ ~{exercise.duration_min} min</span>
        </div>
        <div class="exo-card">
            <div class="exo-card-header">
                <span class="exo-title">{icon} {html.escape(exercise.title)}</span>
                <span class="exo-badge" style="background:{color}">{exercise.level}</span>
                <span class="exo-theme-badge">{html.escape(exercise.theme)}</span>
                {subtype_badge}
                {_source_badge(exercise)}
            </div>
            <p class="exo-instruction">{_fmt_html(exercise.instruction)}</p>
            <div class="exo-body">{_fmt_html(exercise.body)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_api_status(use_grok: bool) -> None:
    if not use_grok:
        st.caption(
            "📦 **Mode local** — banque enrichie, génération dynamique, "
            "prêt pour la classe (aucune clé API requise)."
        )
        return
    if is_api_configured():
        st.success(f"🤖 Mode Grok actif — modèle `{get_model()}`.", icon="✅")
    else:
        st.warning("Clé API absente — repli automatique sur le mode local.", icon="⚠️")


def render() -> None:
    st.markdown('<p class="page-header">🎯 Générateur d\'exercices</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="page-subheader">'
        "Fiches pédagogiques prêtes à projeter — conjugaison, vocabulaire, "
        "phrases à trous, textes à trous et QCM de grammaire."
        "</p>",
        unsafe_allow_html=True,
    )

    with st.expander("⚙️ Options avancées (API Grok)", expanded=False):
        mode_col1, mode_col2 = st.columns([1, 2])
        with mode_col1:
            st.toggle(
                "Activer Grok API",
                value=st.session_state.get("exo_use_grok", False),
                key="exo_use_grok",
            )
        with mode_col2:
            _render_api_status(st.session_state.get("exo_use_grok", False))

    use_grok = st.session_state.get("exo_use_grok", False)

    st.markdown('<div class="exo-config-card">', unsafe_allow_html=True)

    st.markdown("##### 🎓 Niveau CECRL")
    level = st.radio(
        "Niveau",
        LEVELS,
        horizontal=True,
        format_func=lambda x: f"{get_level_info(x)[1]} {x} · {get_level_info(x)[0]}",
        label_visibility="collapsed",
        key="exo_level",
    )
    _render_level_track(level)

    st.markdown("##### 📂 Type d'exercice")
    theme_cols = st.columns(len(THEMES))
    theme = st.session_state.get("exo_theme_pick", THEMES[0])
    for col, t in zip(theme_cols, THEMES):
        with col:
            selected = theme == t
            btn_type = "primary" if selected else "secondary"
            if st.button(
                f"{THEME_ICONS.get(t, '📋')} {t}",
                key=f"theme_btn_{t}",
                use_container_width=True,
                type=btn_type,
            ):
                st.session_state["exo_theme_pick"] = t
                theme = t
    theme = st.session_state.get("exo_theme_pick", THEMES[0])

    st.caption(f"ℹ️ {get_theme_description(theme)}")
    if theme == "Vocabulaire":
        st.caption(f"📚 Sous-types : {', '.join(VOCAB_SUBTYPES)}")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="exo-actions-bar">', unsafe_allow_html=True)
    btn1, btn2, btn3 = st.columns(3)
    with btn1:
        if st.button("✨ Générer", type="primary", use_container_width=True):
            _generate(level, theme, use_grok)
    with btn2:
        if st.button("👁️ Voir la correction", use_container_width=True):
            st.session_state["exo_show_corr"] = True
    with btn3:
        if st.button("🔀 Nouvel exercice", use_container_width=True):
            _generate(level, theme, use_grok)
    st.markdown("</div>", unsafe_allow_html=True)

    warning = st.session_state.pop("exo_warning", None)
    if warning:
        st.info(warning, icon="ℹ️")

    exercise: Exercise | None = st.session_state.get("exo_current")

    if not exercise:
        _render_welcome()
        return

    _render_exercise(exercise)

    if st.session_state.get("exo_show_corr", False):
        st.markdown(
            f"""
            <div class="exo-correction">
                <span class="exo-corr-label">📗 Correction détaillée</span>
                <div class="exo-corr-body">{_fmt_html(exercise.correction)}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if exercise.tip:
            st.markdown(
                f"""
                <div class="exo-pedago-note">
                    <span class="exo-pedago-icon">💡</span>
                    <div>
                        <strong>Note pédagogique</strong>
                        <p>{html.escape(exercise.tip)}</p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        st.caption("👆 Cliquez sur **Voir la correction** une fois le travail terminé.")

    st.divider()
    ideas = [
        "📽️ Projeter la fiche et chronométrer 10–15 min de travail.",
        "👥 Binômes : l'un répond, l'autre corrige à l'oral.",
        "📋 Révéler la correction question par question pour l'interactivité.",
    ]
    for idea in ideas:
        st.caption(idea)


def _render_welcome() -> None:
    st.info(
        "👆 Choisissez un **niveau** et un **type**, puis cliquez sur **Générer** "
        "pour obtenir une fiche prête à l'emploi.",
        icon="ℹ️",
    )

    row1 = st.columns(3)
    row2 = st.columns(2)
    cards = [
        ("Conjugaison", "Paradigmes, phrases en contexte, temps adaptés"),
        ("Vocabulaire", "3 QCM par fiche : synonymes, contraires, définitions"),
        ("Phrases à compléter", "Dialogues, scènes, listes de mots"),
        ("Textes à trous", "Textes longs avec correction ligne par ligne"),
        ("QCM Grammaire", "2 à 3 questions avec explications détaillées"),
    ]
    all_cols = list(row1) + list(row2)
    for col, (title, desc) in zip(all_cols, cards):
        with col:
            icon = THEME_ICONS.get(title, "📋")
            st.markdown(
                f"""
                <div class="exo-preview-card">
                    <span class="exo-preview-icon">{icon}</span>
                    <strong>{title}</strong>
                    <p>{desc}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )