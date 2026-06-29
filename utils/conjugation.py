"""Conjugaison française complète (Verbiste + temps composés + pronominaux)."""

from __future__ import annotations

import copy
import json
import re
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

PRONOMS = ["je", "tu", "il/elle", "nous", "vous", "ils/elles"]
IMPERATIF_LABELS = ["tu", "nous", "vous"]
REFLEXIVE_IMP_SUFFIX = ["-toi", "-nous", "-vous"]
PARTICIPE_PASSE_LABELS = ["ms", "mp", "fs", "fp"]

REFLEXIVE_FULL = ["me", "te", "se", "nous", "vous", "se"]
REFLEXIVE_ELIDED = ["m'", "t'", "s'", "nous", "vous", "s'"]

ETRE_VERBS = frozenset({
    "aller", "venir", "arriver", "partir", "entrer", "sortir", "monter", "descendre",
    "rester", "tomber", "naître", "mourir", "devenir", "revenir", "parvenir", "demeurer",
    "retourner", "rester", "échoir", "décéder", "survenir", "intervenir", "prévenir",
    "redevenir", "contrevenir", "apparaître", "disparaître", "reparaître", "transparaître",
    "départir", "émouvoir", "mouvoir", "promouvoir", "repromouvoir",
})

VOWELS = set("aeiouyàâäéèêëïîôùûüœæh")


@dataclass
class TenseResult:
    label: str
    icon: str
    rows: list[dict[str, str]]
    hint: str = ""


@dataclass
class ConjugationResult:
    display_verb: str
    base_verb: str
    reflexive: bool
    auxiliary: str
    pronunciation: str
    examples: list[str]
    tenses: list[TenseResult] = field(default_factory=list)
    participe_passe: list[str] = field(default_factory=list)


def _join_reflexive_aux(reflexive: str, auxiliary: str) -> str:
    if reflexive.endswith("'"):
        return f"{reflexive}{auxiliary}"
    return f"{reflexive} {auxiliary}"


def _join_subject_aux(person_idx: int, auxiliary: str) -> str:
    subjects = ["je", "tu", "il", "nous", "vous", "ils"]
    subject = subjects[person_idx]
    if subject == "je" and auxiliary and auxiliary[0].lower() in VOWELS:
        return f"j'{auxiliary}"
    return f"{subject} {auxiliary}"


def _reflexive_pronoun(idx: int, form: str) -> str:
    if form and form[0].lower() in VOWELS:
        return REFLEXIVE_ELIDED[idx]
    return REFLEXIVE_FULL[idx]


def parse_verb_input(raw: str) -> tuple[str, str, bool]:
    """Retourne (verbe affiché, verbe de base, pronominal)."""
    raw = raw.strip().lower()
    raw = re.sub(r"\s+", " ", raw)

    if raw.startswith("s'"):
        base = raw[2:].strip()
        return f"s'{base}", base, True

    if raw.startswith("se "):
        base = raw[3:].strip()
        display = f"s'{base}" if base and base[0] in VOWELS else f"se {base}"
        return display, base, True

    return raw, raw, False


@lru_cache(maxsize=1)
def _load_data() -> tuple[dict, dict]:
    verbs_path = DATA_DIR / "verbs-fr.json"
    conj_path = DATA_DIR / "conjugation-fr.json"
    if not verbs_path.exists() or not conj_path.exists():
        raise FileNotFoundError("Fichiers de conjugaison introuvables dans data/.")
    with verbs_path.open(encoding="utf-8") as f:
        verbs = json.load(f)
    with conj_path.open(encoding="utf-8") as f:
        conjugations = json.load(f)
    return verbs, conjugations


def _resolve_verb(verbe: str) -> tuple[dict, str, str]:
    verbs, conjugations = _load_data()
    if verbe not in verbs:
        raise ValueError(f"Le verbe « {verbe} » n'a pas été trouvé dans le dictionnaire.")
    info = verbs[verbe]
    template = info["template"]
    if template not in conjugations:
        raise ValueError(f"Modèle de conjugaison introuvable pour « {verbe} ».")
    return info, template, conjugations[template]


def _build_simple_rows(
    persons: list | str,
    root: str,
    mood: str,
    tense: str,
) -> list[str]:
    if isinstance(persons, str):
        return [persons if persons.startswith(root) else root + persons]

    forms: list[str] = []

    if mood == "Imperatif":
        for pers_idx, suffix in persons:
            if suffix is None:
                continue
            forms.append(root + suffix)
        return forms

    if mood == "Participe" and tense == "Participe Passé":
        return [root + suffix for _, suffix in persons if suffix is not None]

    if mood == "Participe" and tense == "Participe Présent":
        suffix = persons if isinstance(persons, str) else persons[0][1]
        return [root + (suffix if isinstance(suffix, str) else str(suffix))]

    for _, suffix in persons:
        if suffix is None:
            continue
        forms.append(root + suffix)
    return forms


def _get_mood_tense_forms(base_verb: str, mood: str, tense: str) -> list[str]:
    info, template, template_data = _resolve_verb(base_verb)
    root = info["root"]
    data = copy.deepcopy(template_data)
    if mood not in data or tense not in data[mood]:
        return []
    return _build_simple_rows(data[mood][tense], root, mood, tense)


def _participe_passe(base_verb: str) -> list[str]:
    forms = _get_mood_tense_forms(base_verb, "Participe", "Participe Passé")
    while len(forms) < 4:
        forms.append(forms[0] if forms else "")
    return forms[:4]


def _uses_etre(base_verb: str, reflexive: bool) -> bool:
    if reflexive:
        return True
    return base_verb in ETRE_VERBS


def _pp_for_person(idx: int, participes: list[str], with_etre: bool) -> str:
    if not with_etre:
        return participes[0]
    if idx in (0, 1, 2):
        return f"{participes[0]} / {participes[2]}"
    return f"{participes[1]} / {participes[3]}"


def _compose_rows(
    aux_forms: list[str],
    participes: list[str],
    reflexive: bool,
    with_etre: bool,
) -> list[dict[str, str]]:
    rows = []
    for idx, (pronom, aux) in enumerate(zip(PRONOMS, aux_forms)):
        pp = _pp_for_person(idx, participes, with_etre)
        if reflexive:
            ref = _reflexive_pronoun(idx, aux)
            chunk = f"{_join_reflexive_aux(ref, aux)} {pp}"
        else:
            chunk = f"{_join_subject_aux(idx, aux)} {pp}"
        rows.append({"Pronom": pronom, "Conjugaison": chunk})
    return rows


def _apply_reflexive(simple_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    result = []
    for idx, row in enumerate(simple_rows):
        form = row["Conjugaison"]
        ref = _reflexive_pronoun(idx, form)
        combined = f"{ref}{form}" if ref.endswith("'") else f"{ref} {form}"
        result.append({"Pronom": row["Pronom"], "Conjugaison": combined})
    return result


def _simple_tense_rows(
    base_verb: str,
    mood: str,
    tense: str,
    reflexive: bool,
) -> list[dict[str, str]]:
    forms = _get_mood_tense_forms(base_verb, mood, tense)
    if not forms:
        return []

    if mood == "Imperatif":
        rows = []
        for i, form in enumerate(forms):
            label = IMPERATIF_LABELS[i] if i < len(IMPERATIF_LABELS) else "—"
            conj = (
                f"{form}{REFLEXIVE_IMP_SUFFIX[i]}"
                if reflexive and i < len(REFLEXIVE_IMP_SUFFIX)
                else form
            )
            rows.append({"Pronom": label, "Conjugaison": conj})
        return rows

    rows = [{"Pronom": p, "Conjugaison": f} for p, f in zip(PRONOMS, forms)]
    if reflexive:
        return _apply_reflexive(rows)
    return rows


def _compound_rows(
    base_verb: str,
    aux_tense: str,
    reflexive: bool,
    with_etre: bool,
) -> list[dict[str, str]]:
    auxiliary = "être" if with_etre else "avoir"
    aux_forms = _get_mood_tense_forms(auxiliary, "Indicatif", aux_tense)
    if len(aux_forms) < 6:
        return []
    participes = _participe_passe(base_verb)
    return _compose_rows(aux_forms, participes, reflexive, with_etre)


def conjugate_verb(verbe: str) -> ConjugationResult:
    """Conjugue un verbe (simple ou pronominal) avec tous les temps demandés."""
    if not verbe.strip():
        raise ValueError("Veuillez entrer un verbe.")

    display, base, reflexive = parse_verb_input(verbe)
    _resolve_verb(base)

    with_etre = _uses_etre(base, reflexive)
    auxiliary = "être" if with_etre else "avoir"
    participes = _participe_passe(base)

    from utils.examples import generate_examples
    from utils.pronunciation import get_pronunciation

    tenses = [
        TenseResult(
            "Présent",
            "🟢",
            _simple_tense_rows(base, "Indicatif", "Présent", reflexive),
            "Action habituelle ou en cours.",
        ),
        TenseResult(
            "Imparfait",
            "🕐",
            _simple_tense_rows(base, "Indicatif", "Imparfait", reflexive),
            "Description, habitude ou action en progression dans le passé.",
        ),
        TenseResult(
            "Futur simple",
            "🔮",
            _simple_tense_rows(base, "Indicatif", "Futur", reflexive),
            "Action qui se produira plus tard.",
        ),
        TenseResult(
            "Passé composé",
            "✅",
            _compound_rows(base, "Présent", reflexive, with_etre),
            f"Action passée terminée (auxiliaire : {auxiliary}).",
        ),
        TenseResult(
            "Plus-que-parfait",
            "⏪",
            _compound_rows(base, "Imparfait", reflexive, with_etre),
            "Action passée antérieure à une autre action passée.",
        ),
        TenseResult(
            "Futur antérieur",
            "⏩",
            _compound_rows(base, "Futur", reflexive, with_etre),
            "Action future antérieure à une autre action future.",
        ),
        TenseResult(
            "Subjonctif présent",
            "💫",
            _simple_tense_rows(base, "Subjonctif", "Présent", reflexive),
            "Doute, souhait, émotion ou nécessité.",
        ),
        TenseResult(
            "Conditionnel présent",
            "🤔",
            _simple_tense_rows(base, "Conditionnel", "Présent", reflexive),
            "Hypothèse, politesse ou demande.",
        ),
        TenseResult(
            "Impératif",
            "❗",
            _simple_tense_rows(base, "Imperatif", "Imperatif Présent", reflexive),
            "Ordre, conseil ou invitation.",
        ),
    ]

    tenses = [t for t in tenses if t.rows]

    if not tenses:
        raise ValueError(f"Impossible de conjuguer « {display} ».")

    return ConjugationResult(
        display_verb=display,
        base_verb=base,
        reflexive=reflexive,
        auxiliary=auxiliary,
        pronunciation=get_pronunciation(display, base, reflexive),
        examples=generate_examples(display, base, reflexive, tenses),
        tenses=tenses,
        participe_passe=participes,
    )