"""Page du conjugueur — version complète et professionnelle."""

from __future__ import annotations

import streamlit as st

from utils.conjugation import ConjugationResult, conjugate_verb
from utils.examples import get_tense_example
from utils.pronunciation import speakable_form, synthesize_speech


def _render_table(rows: list[dict[str, str]], tense_label: str) -> None:
    if not rows:
        st.caption("Aucune forme disponible.")
        return

    body_html = ""
    for i, row in enumerate(rows):
        pronom = row.get("Pronom", row.get("Genre / Nombre", "—"))
        form = row.get("Conjugaison", row.get("Forme", ""))
        alt = "conj-row-even" if i % 2 else "conj-row-odd"
        body_html += f"""
        <tr class="{alt}">
            <td class="conj-pronom">{pronom}</td>
            <td class="conj-form">{form}</td>
        </tr>
        """

    st.markdown(
        f"""
        <div class="conj-table-wrapper">
            <table class="conj-table">
                <thead>
                    <tr>
                        <th>Pronom</th>
                        <th>Conjugaison</th>
                    </tr>
                </thead>
                <tbody>{body_html}</tbody>
            </table>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_verb_header(result: ConjugationResult) -> None:
    badges = []
    if result.reflexive:
        badges.append('<span class="verb-badge reflexive">🔄 Pronominal</span>')
    badges.append(f'<span class="verb-badge aux">⚙️ Auxiliaire : {result.auxiliary}</span>')
    badges.append(f'<span class="verb-badge base">📌 Base : {result.base_verb}</span>')

    st.markdown(
        f"""
        <div class="verb-header-card">
            <div class="verb-header-top">
                <h2 class="verb-title">{result.display_verb}</h2>
                <span class="verb-phonetic">{result.pronunciation}</span>
            </div>
            <div class="verb-badges">{"".join(badges)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _play_audio(label: str, text: str) -> None:
    audio_path = synthesize_speech(text)
    if audio_path:
        st.audio(str(audio_path), format="audio/mp3")
    else:
        st.caption(f"🔊 Prononciation simulée : *{label}* → {text}")


def render() -> None:
    st.markdown('<p class="page-header">📖 Conjugueur</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="page-subheader">'
        "Conjuguez un verbe simple ou pronominal — "
        "<em>parler</em>, <em>être</em>, <em>se lever</em>, <em>s'appeler</em>…"
        "</p>",
        unsafe_allow_html=True,
    )

    col_input, col_btn, col_hint = st.columns([3, 1, 1])
    with col_input:
        verbe = st.text_input(
            "Verbe à conjuguer",
            placeholder="Ex. : parler, se lever, s'appeler, finir…",
            label_visibility="collapsed",
            key="conj_input",
        )
    with col_btn:
        conjuguer = st.button("✨ Conjuguer", use_container_width=True, type="primary")
    with col_hint:
        st.caption("💡 Essayez *se lever*")

    if conjuguer:
        if not verbe.strip():
            st.warning("⚠️ Veuillez entrer un verbe avant de conjuguer.")
            return
        try:
            with st.spinner(f"Conjugaison de « {verbe.strip()} » en cours…"):
                result = conjugate_verb(verbe)
            st.session_state["conjugation_result"] = result
        except ValueError as exc:
            st.error(f"❌ {exc}")
        except Exception:
            st.error("❌ Une erreur est survenue. Réessayez avec un autre verbe.")

    result: ConjugationResult | None = st.session_state.get("conjugation_result")
    if not result:
        st.info(
            "💬 Saisissez un verbe puis cliquez sur **Conjuguer** pour explorer tous les temps.",
            icon="ℹ️",
        )
        _render_suggestions()
        return

    _render_verb_header(result)

    audio_col1, audio_col2 = st.columns([1, 3])
    with audio_col1:
        if st.button("🔊 Écouter l'infinitif", use_container_width=True):
            st.session_state["play_infinitif"] = result.display_verb
    with audio_col2:
        if result.participe_passe:
            st.caption(
                f"Participe passé : **{result.participe_passe[0]}** "
                f"(fém. {result.participe_passe[2]}, pl. {result.participe_passe[1]})"
            )

    if st.session_state.get("play_infinitif"):
        _play_audio("infinitif", st.session_state["play_infinitif"])

    tab_labels = [f"{t.icon} {t.label}" for t in result.tenses]
    tabs = st.tabs(tab_labels)

    for tab, tense in zip(tabs, result.tenses):
        with tab:
            if tense.hint:
                st.markdown(f'<p class="tense-hint">{tense.hint}</p>', unsafe_allow_html=True)

            _render_table(tense.rows, tense.label)

            example = get_tense_example(result.display_verb, tense)
            st.markdown(
                f"""
                <div class="example-card">
                    <span class="example-label">💬 Exemple</span>
                    <p class="example-text">{example}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            if tense.rows:
                sample_form = tense.rows[min(1, len(tense.rows) - 1)]["Conjugaison"]
                speak = speakable_form(result.display_verb, sample_form)
                if st.button(f"🔊 Prononcer un exemple", key=f"audio_{tense.label}"):
                    _play_audio(tense.label, speak)


def _render_suggestions() -> None:
    st.markdown("##### 🌟 Verbes suggérés")
    suggestions = ["parler", "être", "avoir", "finir", "se lever", "s'appeler", "aller", "faire"]
    cols = st.columns(4)
    for i, sug in enumerate(suggestions):
        with cols[i % 4]:
            if st.button(sug, key=f"sug_{sug}", use_container_width=True):
                st.session_state["conj_input"] = sug
                try:
                    st.session_state["conjugation_result"] = conjugate_verb(sug)
                    st.rerun()
                except ValueError as exc:
                    st.error(str(exc))