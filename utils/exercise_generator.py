"""Générateur d'exercices pédagogiques FLE — banque enrichie + génération dynamique."""

from __future__ import annotations

import random
import re
import uuid
from dataclasses import dataclass

from utils.exercise_data import (
    ANTONYMS,
    CLOZE_TEMPLATES,
    CONJ_TENSES,
    CONJ_TIPS,
    CONJ_VERBS,
    DEFINITIONS,
    FILL_TEMPLATES,
    GRAMMAR_QCM_SETS,
    LEVEL_LABELS,
    SYNONYMS,
    THEME_DESCRIPTIONS,
    ClozeTemplate,
    FillTemplate,
    QcmSet,
)

LEVELS = ["A1", "A2", "B1", "B2"]
THEMES = [
    "Conjugaison",
    "Vocabulaire",
    "Phrases à compléter",
    "Textes à trous",
    "QCM Grammaire",
]

THEME_ICONS = {
    "Conjugaison": "✏️",
    "Vocabulaire": "📚",
    "Phrases à compléter": "📝",
    "Textes à trous": "📄",
    "QCM Grammaire": "☑️",
}

VOCAB_SUBTYPES = ["Synonymes", "Contraires", "Définitions"]

LEVEL_COLORS = {
    "A1": "#6db89a",
    "A2": "#5aa88a",
    "B1": "#2d6a8f",
    "B2": "#0f2744",
}

_PERSONS = [
    (0, "je"),
    (1, "tu"),
    (2, "il/elle"),
    (3, "nous"),
    (4, "vous"),
    (5, "ils/elles"),
]


@dataclass
class Exercise:
    id: str
    level: str
    theme: str
    title: str
    instruction: str
    body: str
    correction: str
    tip: str = ""
    subtype: str = ""
    source: str = "local"
    question_count: int = 1
    duration_min: int = 5


# ── Helpers ──────────────────────────────────────────────────────────────────

def _new_id() -> str:
    return str(uuid.uuid4())[:8]


def _clone(ex: Exercise) -> Exercise:
    return Exercise(
        id=_new_id(),
        level=ex.level,
        theme=ex.theme,
        title=ex.title,
        instruction=ex.instruction,
        body=ex.body,
        correction=ex.correction,
        tip=ex.tip,
        subtype=ex.subtype,
        source=ex.source,
        question_count=ex.question_count,
        duration_min=ex.duration_min,
    )


def _format_fill(template: str, answers: list[str], *, reveal: bool = False) -> str:
    result = template
    for i, ans in enumerate(answers):
        placeholder = f"{{{i}}}"
        if reveal:
            result = result.replace(placeholder, f"<b>{ans}</b>", 1)
        else:
            result = result.replace(placeholder, "___", 1)
    return result


def _build_fill_exercise(level: str, tpl: FillTemplate) -> Exercise:
    bank = " · ".join(tpl.word_bank)
    body = _format_fill(tpl.template, tpl.answers, reveal=False)
    correction_lines = [
        f"{i + 1}. <b>{ans}</b> — {exp}"
        for i, (ans, exp) in enumerate(zip(tpl.answers, tpl.explanations))
    ]
    return Exercise(
        id=_new_id(),
        level=level,
        theme="Phrases à compléter",
        title=tpl.title,
        instruction=f"{tpl.instruction}<br><em>Banque : {bank}</em>",
        body=body,
        correction="\n".join(correction_lines),
        tip=tpl.tip,
        question_count=len(tpl.answers),
        duration_min=max(5, len(tpl.answers) + 3),
    )


def _build_cloze_exercise(level: str, tpl: ClozeTemplate) -> Exercise:
    n = len(tpl.answers)
    instruction = tpl.instruction.replace("{n}", str(n))
    if tpl.word_bank:
        bank = " · ".join(tpl.word_bank)
        instruction += f"<br><em>Banque : {bank}</em>"
    body = _format_fill(tpl.template, tpl.answers, reveal=False)
    correction_lines = [
        f"Trou {i + 1} : <b>{ans}</b> — {exp}"
        for i, (ans, exp) in enumerate(zip(tpl.answers, tpl.explanations))
    ]
    full_text = _format_fill(tpl.template, tpl.answers, reveal=True)
    return Exercise(
        id=_new_id(),
        level=level,
        theme="Textes à trous",
        title=tpl.title,
        instruction=instruction,
        body=body,
        correction=f"<b>Texte corrigé :</b><br>{full_text}<br><br><b>Détail :</b><br>"
        + "<br>".join(correction_lines),
        tip=tpl.tip,
        question_count=n,
        duration_min=max(8, n + 5),
    )


def _format_qcm_set(qset: QcmSet) -> tuple[str, str, int]:
    letters = ["A", "B", "C", "D"]
    body_parts: list[str] = []
    corr_parts: list[str] = []
    for i, q in enumerate(qset.questions, 1):
        opts = "\n".join(f"   {letters[j]}) {opt}" for j, opt in enumerate(q.options))
        body_parts.append(f"{i}. {q.stem}\n{opts}")
        correct = letters[q.correct_idx]
        answer = q.options[q.correct_idx]
        corr_parts.append(
            f"{i}. <b>{correct}) {answer}</b><br>→ {q.explanation}"
        )
    return "\n\n".join(body_parts), "<br><br>".join(corr_parts), len(qset.questions)


def _build_qcm_exercise(level: str, qset: QcmSet) -> Exercise:
    body, correction, n = _format_qcm_set(qset)
    return Exercise(
        id=_new_id(),
        level=level,
        theme="QCM Grammaire",
        title=qset.title,
        instruction=qset.instruction,
        body=body,
        correction=correction,
        tip=qset.tip,
        subtype=qset.topic,
        question_count=n,
        duration_min=max(5, n * 2),
    )


# ── Générateurs dynamiques ───────────────────────────────────────────────────

def _get_conj_form(result, tense_label: str, person_idx: int) -> str:
    for t in result.tenses:
        if t.label == tense_label and person_idx < len(t.rows):
            return t.rows[person_idx]["Conjugaison"]
    for t in result.tenses:
        if t.rows:
            idx = min(person_idx, len(t.rows) - 1)
            return t.rows[idx]["Conjugaison"]
    return ""


def _generate_conj_drill(level: str) -> Exercise:
    """Fiche de conjugaison multi-questions (4 à 6 items)."""
    from utils.conjugation import conjugate_verb, parse_verb_input

    mode = random.choice(["paradigm", "mixed", "sentences"])
    verbs = CONJ_VERBS.get(level, CONJ_VERBS["A1"])
    tenses = CONJ_TENSES.get(level, CONJ_TENSES["A1"])

    if mode == "paradigm":
        verb = random.choice([v for v in verbs if v not in ("être", "avoir")])
        tense = random.choice([t for t in tenses if t != "Impératif"] or tenses)
        result = conjugate_verb(verb)
        display, _, reflexive = parse_verb_input(verb)
        persons = _PERSONS[:6] if level == "A1" else random.sample(_PERSONS, min(5, len(_PERSONS)))
        lines, corrs = [], []
        for i, (idx, label) in enumerate(persons, 1):
            form = _get_conj_form(result, tense, idx)
            if not form:
                continue
            lines.append(f"{i}. {label} ___ ({display})")
            corrs.append(f"{i}. {label} <b>{form}</b>")
        tip = CONJ_TIPS.get(tense, "") + f" Auxiliaire : {result.auxiliary}."
        if reflexive:
            tip += " Verbe pronominal."
        return Exercise(
            id=_new_id(), level=level, theme="Conjugaison",
            title=f"Paradigme — {display}",
            instruction=f"Conjuguez <em>{display}</em> au <b>{tense}</b> pour chaque personne.",
            body="\n".join(lines), correction="\n".join(corrs), tip=tip,
            question_count=len(lines), duration_min=max(6, len(lines)),
        )

    if mode == "mixed":
        count = random.randint(4, 5)
        lines, corrs, used = [], [], set()
        for i in range(count):
            verb = random.choice(verbs)
            tense = random.choice(tenses)
            person_idx, person_label = random.choice(_PERSONS)
            key = (verb, tense, person_idx)
            if key in used:
                continue
            used.add(key)
            result = conjugate_verb(verb)
            display, _, _ = parse_verb_input(verb)
            form = _get_conj_form(result, tense, person_idx)
            if not form:
                continue
            lines.append(f"{len(lines) + 1}. {person_label} ___ ({display}, {tense})")
            corrs.append(f"{len(corrs) + 1}. {person_label} <b>{form}</b>")
        return Exercise(
            id=_new_id(), level=level, theme="Conjugaison",
            title="Conjugaison mixte",
            instruction="Conjuguez chaque verbe au temps indiqué entre parenthèses.",
            body="\n".join(lines), correction="\n".join(corrs),
            tip="Lisez d'abord le temps demandé, puis identifiez la personne.",
            question_count=len(lines), duration_min=max(6, len(lines)),
        )

    # sentences — phrases à trous contextuelles
    verb = random.choice(verbs)
    tense = random.choice([t for t in tenses if t != "Impératif"] or tenses)
    result = conjugate_verb(verb)
    display, _, reflexive = parse_verb_input(verb)
    contexts = {
        "A1": [
            ("Chaque matin, je ___ à 7 heures.", 0),
            ("Tu ___ avec tes amis ?", 1),
            ("Nous ___ en français en classe.", 3),
        ],
        "A2": [
            ("Hier, elle ___ tard.", 2),
            ("Quand j'étais enfant, je ___ souvent.", 0),
            ("Demain, nous ___ à Lyon.", 3),
        ],
        "B1": [
            ("Il faut que tu ___ avant midi.", 1),
            ("Si j'avais su, je ___ plus tôt.", 0),
            ("Bien qu'il ___ demain, nous partirons.", 2),
        ],
        "B2": [
            ("Quand il aura fini, nous ___ .", 3),
            ("Il doutait qu'elle ___ venir.", 2),
            ("J'aurais préféré que vous ___ plus tôt.", 4),
        ],
    }
    pool = contexts.get(level, contexts["A1"])
    chosen = random.sample(pool, min(3, len(pool)))
    lines, corrs = [], []
    for i, (sentence, person_idx) in enumerate(chosen, 1):
        form = _get_conj_form(result, tense, person_idx)
        if not form:
            form = _get_conj_form(result, tense, 0)
        blanked = re.sub(r"___", "___", sentence, count=1)
        lines.append(f"{i}. {blanked} ({display})")
        filled = sentence.replace("___", f"<b>{form}</b>")
        corrs.append(f"{i}. {filled}")
    return Exercise(
        id=_new_id(), level=level, theme="Conjugaison",
        title=f"Conjugaison en contexte — {display}",
        instruction=f"Complétez au <b>{tense}</b> avec le verbe <em>{display}</em>.",
        body="\n".join(lines), correction="\n".join(corrs),
        tip=CONJ_TIPS.get(tense, ""),
        question_count=len(lines), duration_min=7,
    )


def _generate_vocab_multi(level: str, subtype: str) -> Exercise:
    pool_map = {
        "Synonymes": SYNONYMS,
        "Contraires": ANTONYMS,
        "Définitions": DEFINITIONS,
    }
    pool = list(pool_map[subtype].get(level, pool_map[subtype]["A1"]))
    random.shuffle(pool)
    count = min(3, len(pool))
    selected = pool[:count]
    letters = ["A", "B", "C", "D"]
    body_parts, corr_parts = [], []

    for i, item in enumerate(selected, 1):
        if subtype == "Définitions":
            definition, answer, distractors, explain = item
            prompt = f"« {definition} »"
            label = definition[:30]
        elif subtype == "Synonymes":
            word, answer, distractors, explain = item
            prompt = f"Synonyme de « <b>{word}</b> » ?"
            label = word
        else:
            word, answer, distractors, explain = item
            prompt = f"Contraire de « <b>{word}</b> » ?"
            label = word

        options = [answer] + list(distractors[:3])
        random.shuffle(options)
        opts_text = "\n".join(f"   {letters[j]}) {opt}" for j, opt in enumerate(options))
        correct_letter = letters[options.index(answer)]
        body_parts.append(f"{i}. {prompt}\n{opts_text}")
        corr_parts.append(
            f"{i}. <b>{correct_letter}) {answer}</b> — {explain}"
        )

    return Exercise(
        id=_new_id(), level=level, theme="Vocabulaire",
        title=f"{subtype} — fiche {count} questions",
        instruction=f"Exercice de <b>{subtype}</b> : choisissez la bonne réponse (A, B, C ou D) pour chaque question.",
        body="\n\n".join(body_parts),
        correction="<br>".join(corr_parts),
        tip=f"Faites justifier chaque réponse à l'oral. Type : {subtype}.",
        subtype=subtype,
        question_count=count,
        duration_min=max(5, count * 2),
    )


# ── Point d'entrée ───────────────────────────────────────────────────────────

_GENERATORS = {
    "Conjugaison": lambda lvl: _generate_conj_drill(lvl),
    "Vocabulaire": lambda lvl: _generate_vocab_multi(lvl, random.choice(VOCAB_SUBTYPES)),
    "Phrases à compléter": lambda lvl: _build_fill_exercise(
        lvl, random.choice(FILL_TEMPLATES.get(lvl, FILL_TEMPLATES["A1"]))
    ),
    "Textes à trous": lambda lvl: _build_cloze_exercise(
        lvl, random.choice(CLOZE_TEMPLATES.get(lvl, CLOZE_TEMPLATES["A1"]))
    ),
    "QCM Grammaire": lambda lvl: _build_qcm_exercise(
        lvl, random.choice(GRAMMAR_QCM_SETS.get(lvl, GRAMMAR_QCM_SETS["A1"]))
    ),
}


def generate_exercise(level: str, theme: str) -> Exercise:
    """Génère un exercice unique pour le niveau et le type donnés."""
    if level not in LEVELS:
        level = "A1"
    if theme not in THEMES:
        theme = "Conjugaison"
    return _GENERATORS[theme](level)


def generate_exercises(level: str, theme: str, count: int = 1) -> list[Exercise]:
    """Génère plusieurs exercices distincts."""
    count = max(1, min(count, 5))
    results: list[Exercise] = []
    seen: set[str] = set()
    for _ in range(count * 5):
        if len(results) >= count:
            break
        ex = generate_exercise(level, theme)
        key = f"{ex.title}:{ex.body[:80]}"
        if key not in seen:
            seen.add(key)
            results.append(ex)
    return results[:count]


def generate_exercise_smart(
    level: str,
    theme: str,
    *,
    use_grok: bool = True,
    fallback_on_error: bool = True,
) -> tuple[Exercise, str | None]:
    """Génère via Grok si demandé, sinon localement."""
    if not use_grok:
        return generate_exercise(level, theme), None

    from utils.grok_client import generate_exercise_grok, is_api_configured

    if not is_api_configured():
        if fallback_on_error:
            return generate_exercise(level, theme), "Clé API absente — exercice généré en mode local."
        raise RuntimeError("Clé API xAI non configurée.")

    try:
        return generate_exercise_grok(level, theme), None
    except Exception as exc:
        if fallback_on_error:
            return generate_exercise(level, theme), f"Grok indisponible — repli sur le mode local."
        raise


def get_level_info(level: str) -> tuple[str, str]:
    return LEVEL_LABELS.get(level, ("", ""))


def get_theme_description(theme: str) -> str:
    return THEME_DESCRIPTIONS.get(theme, "")