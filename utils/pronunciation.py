"""Prononciation : transcription phonétique + synthèse vocale."""

from __future__ import annotations

import asyncio
import hashlib
import re
import tempfile
from pathlib import Path

_CACHE_DIR = Path(tempfile.gettempdir()) / "machine_a_langue_tts"
_CACHE_DIR.mkdir(exist_ok=True)

_PHONETIC_MAP = {
    "ai": "è", "ei": "è", "oi": "wa", "ou": "ou", "au": "o",
    "eau": "o", "an": "an", "en": "an", "in": "in", "on": "on",
    "un": "œ̃", "ien": "yèn", "tion": "sion", "ille": "iy",
    "ph": "f", "ch": "ch", "gn": "gn", "qu": "k",
}

_COMMON_VERBS = {
    "parler": "par-lé",
    "être": "ètre",
    "avoir": "a-vwar",
    "aller": "a-lé",
    "faire": "fèr",
    "venir": "və-nir",
    "pouvoir": "pou-vwar",
    "vouloir": "vou-vwar",
    "devoir": "də-vwar",
    "prendre": "prandr",
    "mettre": "mètre",
    "dire": "dir",
    "voir": "vwar",
    "savoir": "sa-vwar",
    "falloir": "fa-lwar",
    "lever": "lə-vé",
    "appeler": "a-pə-lé",
    "finir": "fi-nir",
    "choisir": "shwa-zir",
    "manger": "man-jé",
    "commencer": "ko-man-sé",
}


def get_pronunciation(display: str, base: str, reflexive: bool) -> str:
    """Retourne une transcription phonétique simplifiée."""
    if base in _COMMON_VERBS:
        phon = _COMMON_VERBS[base]
    else:
        phon = _approximate_phonetic(base)

    if reflexive:
        prefix = "sə" if display.startswith("s'") else "sə"
        return f"[ {prefix} {phon} ]"
    return f"[ {phon} ]"


def _approximate_phonetic(word: str) -> str:
    w = word.lower()
    if w.endswith("er"):
        stem = w[:-2]
        return f"{_simplify(stem)}-é"
    if w.endswith("ir"):
        stem = w[:-2]
        return f"{_simplify(stem)}-ir"
    if w.endswith("re"):
        stem = w[:-2]
        return f"{_simplify(stem)}-r"
    return _simplify(w)


def _simplify(text: str) -> str:
    for pattern, repl in sorted(_PHONETIC_MAP.items(), key=lambda x: -len(x[0])):
        text = text.replace(pattern, repl)
    return text


def _cache_path(text: str) -> Path:
    digest = hashlib.md5(text.encode("utf-8")).hexdigest()
    return _CACHE_DIR / f"{digest}.mp3"


def synthesize_speech(text: str) -> Path | None:
    """Génère un fichier audio via edge-tts (API Microsoft gratuite)."""
    cached = _cache_path(text)
    if cached.exists():
        return cached

    try:
        import edge_tts
    except ImportError:
        return None

    async def _run() -> None:
        communicate = edge_tts.Communicate(text, "fr-FR-DeniseNeural")
        await communicate.save(str(cached))

    try:
        asyncio.run(_run())
        return cached if cached.exists() else None
    except Exception:
        return None


def speakable_form(display: str, form: str) -> str:
    """Nettoie une forme conjuguée pour la synthèse vocale."""
    clean = re.sub(r"\s*/\s*.*", "", form)
    clean = clean.replace("(", "").replace(")", "")
    return clean.strip()