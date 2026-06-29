"""Client xAI Grok pour la génération d'exercices FLE."""

from __future__ import annotations

import json
import os
import uuid
from typing import Any

import httpx

from utils.exercise_generator import (
    LEVELS,
    THEMES,
    VOCAB_SUBTYPES,
    Exercise,
)

XAI_API_BASE = "https://api.x.ai/v1"
DEFAULT_MODEL = "grok-4.3"

_EXERCISE_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "description": "Titre court et accrocheur de l'exercice"},
        "instruction": {
            "type": "string",
            "description": "Consigne claire pour l'élève, peut contenir du HTML simple (<b>, <em>)",
        },
        "body": {
            "type": "string",
            "description": "Énoncé de l'exercice (questions, texte à trous, QCM…), HTML simple autorisé",
        },
        "correction": {
            "type": "string",
            "description": "Correction détaillée et pédagogique, réponses en gras avec <b>",
        },
        "tip": {
            "type": "string",
            "description": "Note pédagogique pour le professeur (règle, piège, prolongement)",
        },
        "subtype": {
            "type": "string",
            "description": "Sous-type pour Vocabulaire : Synonymes, Contraires ou Définitions ; sinon chaîne vide",
        },
    },
    "required": ["title", "instruction", "body", "correction", "tip", "subtype"],
    "additionalProperties": False,
}

_LEVEL_GUIDANCE = {
    "A1": "Débutant absolu. Vocabulaire concret, phrases courtes, présent de l'indicatif, articles, genre.",
    "A2": "Élémentaire. Passé composé, imparfait, futur simple, pronoms COD/COI, négation, vie quotidienne.",
    "B1": "Intermédiaire. Subjonctif, conditionnel, connecteurs logiques, argumentation simple, accords avancés.",
    "B2": "Avancé. Concordance des temps, registres de langue, subordonnées, voix passive, analyse stylistique.",
}

_THEME_GUIDANCE = {
    "Conjugaison": "Exercice de conjugaison : temps et modes adaptés au niveau, verbes variés (réguliers et irréguliers).",
    "Vocabulaire": (
        "Exercice de vocabulaire en QCM (4 options A-D). Choisir un sous-type : "
        f"{', '.join(VOCAB_SUBTYPES)}. Indiquer le subtype correspondant."
    ),
    "Phrases à compléter": "Texte à trous cohérent (dialogue, récit, description) avec liste de mots ou choix contextuels.",
    "Textes à trous": "Texte authentique de 80 à 150 mots avec 6 à 10 trous grammaticaux ou lexicaux, correction détaillée.",
    "QCM Grammaire": "QCM de grammaire (2 à 4 questions), options A/B/C/D, point grammatical précis du niveau.",
}

_SYSTEM_PROMPT = """Tu es un professeur expert de FLE (Français Langue Étrangère) avec 20 ans d'expérience.
Tu conçois des exercices pour des professeurs qui les projettent en classe ou les impriment.

Règles impératives :
- Langue : français standard, adapté au niveau CECRL demandé.
- Qualité pédagogique : consigne claire, énoncé progressif, correction exhaustive.
- Format HTML léger dans instruction, body et correction : <b>gras</b>, <em>italique</em> uniquement.
- Pas de markdown (pas de **, pas de #).
- Les QCM utilisent le format « A) … B) … C) … D) … » avec retours à la ligne.
- La correction explique le « pourquoi » quand c'est utile pour le professeur.
- Contenu original à chaque génération — pas de copier des manuels connus.
- Éviter les sujets sensibles (politique, religion, violence).
"""


def get_api_key() -> str | None:
    """Résout la clé API depuis Streamlit secrets ou variable d'environnement."""
    try:
        import streamlit as st

        key = st.secrets.get("XAI_API_KEY")
        if key:
            return str(key).strip()
    except Exception:
        pass
    key = os.environ.get("XAI_API_KEY", "").strip()
    return key or None


def get_model() -> str:
    """Modèle xAI configurable via secrets ou XAI_MODEL."""
    try:
        import streamlit as st

        model = st.secrets.get("XAI_MODEL")
        if model:
            return str(model).strip()
    except Exception:
        pass
    return os.environ.get("XAI_MODEL", DEFAULT_MODEL).strip() or DEFAULT_MODEL


def is_api_configured() -> bool:
    return bool(get_api_key())


def _build_user_prompt(level: str, theme: str) -> str:
    if level not in LEVELS:
        level = "A1"
    if theme not in THEMES:
        theme = "Conjugaison"
    return (
        f"Génère UN exercice de FLE.\n\n"
        f"Niveau CECRL : {level}\n"
        f"Profil niveau : {_LEVEL_GUIDANCE[level]}\n\n"
        f"Type d'exercice : {theme}\n"
        f"Consignes type : {_THEME_GUIDANCE[theme]}\n\n"
        f"Réponds uniquement avec le JSON structuré demandé."
    )


def _parse_exercise_payload(data: dict[str, Any], level: str, theme: str) -> Exercise:
    subtype = str(data.get("subtype", "")).strip()
    if theme == "Vocabulaire" and subtype not in VOCAB_SUBTYPES:
        subtype = ""

    return Exercise(
        id=str(uuid.uuid4())[:8],
        level=level,
        theme=theme,
        title=str(data.get("title", "Exercice")).strip() or "Exercice",
        instruction=str(data.get("instruction", "")).strip(),
        body=str(data.get("body", "")).strip(),
        correction=str(data.get("correction", "")).strip(),
        tip=str(data.get("tip", "")).strip(),
        subtype=subtype,
        source="grok",
    )


def generate_exercise_grok(level: str, theme: str, *, timeout: float = 60.0) -> Exercise:
    """Génère un exercice via l'API xAI Grok. Lève une exception en cas d'échec."""
    api_key = get_api_key()
    if not api_key:
        raise RuntimeError(
            "Clé API xAI non configurée. Ajoutez XAI_API_KEY dans "
            ".streamlit/secrets.toml ou en variable d'environnement."
        )

    model = get_model()
    payload = {
        "model": model,
        "temperature": 0.85,
        "messages": [
            {"role": "system", "content": _SYSTEM_PROMPT},
            {"role": "user", "content": _build_user_prompt(level, theme)},
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "fle_exercise",
                "strict": True,
                "schema": _EXERCISE_SCHEMA,
            },
        },
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    with httpx.Client(timeout=timeout) as client:
        response = client.post(
            f"{XAI_API_BASE}/chat/completions",
            headers=headers,
            json=payload,
        )

    if response.status_code != 200:
        detail = response.text[:500]
        raise RuntimeError(f"API xAI ({response.status_code}) : {detail}")

    result = response.json()
    try:
        content = result["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError("Réponse API xAI invalide.") from exc

    if isinstance(content, str):
        data = json.loads(content)
    elif isinstance(content, dict):
        data = content
    else:
        raise RuntimeError("Format de contenu API inattendu.")

    exercise = _parse_exercise_payload(data, level, theme)
    if not exercise.body or not exercise.correction:
        raise RuntimeError("Exercice généré incomplet (body ou correction manquant).")
    return exercise