"""Génération d'exemples de phrases par temps."""

from __future__ import annotations

from utils.conjugation import TenseResult

_TEMPLATES: dict[str, list[tuple[int, str]]] = {
    "Présent": [
        (0, "Chaque matin, je {form} avec énergie."),
        (2, "Il {form} toujours à l'heure."),
        (3, "Nous {form} ensemble après les cours."),
    ],
    "Imparfait": [
        (0, "Quand j'étais petit, je {form} souvent."),
        (2, "Il {form} tranquillement sous le soleil."),
        (5, "Ils {form} tous les jours après l'école."),
    ],
    "Futur simple": [
        (0, "Demain, je {form} dès le réveil."),
        (3, "Nous {form} pendant les vacances."),
        (5, "Ils {form} sûrement ce week-end."),
    ],
    "Passé composé": [
        (0, "Ce matin, {form} très tôt."),
        (2, "Hier, {form} avec beaucoup de soin."),
        (4, "Ensemble, {form} hier soir."),
    ],
    "Plus-que-parfait": [
        (0, "Quand il est arrivé, {form} déjà."),
        (2, "Avant la fin du cours, {form} tranquillement."),
        (3, "Nous {form} ensemble plusieurs fois."),
    ],
    "Futur antérieur": [
        (0, "Quand tu arriveras, {form} déjà."),
        (2, "Avant midi, {form} sans doute."),
        (5, "D'ici demain, {form} tous."),
    ],
    "Subjonctif présent": [
        (0, "Il faut que je {form} plus souvent."),
        (2, "Je souhaite qu'il {form} avec nous."),
        (3, "Il est important que nous {form} ensemble."),
    ],
    "Conditionnel présent": [
        (0, "Je {form} volontiers avec toi."),
        (2, "Il voudrait {form} plus tard."),
        (4, "Vous pourriez {form} demain matin."),
    ],
    "Impératif": [
        (1, "{form} tout de suite !"),
        (3, "{form} ensemble, s'il vous plaît !"),
        (4, "{form} maintenant !"),
    ],
}


def _extract_form(rows: list[dict[str, str]], person_idx: int) -> str:
    if person_idx < len(rows):
        return rows[person_idx].get("Conjugaison", "")
    return rows[0].get("Conjugaison", "") if rows else ""


def _example_for_tense(
    display: str,
    tense: TenseResult,
) -> str:
    templates = _TEMPLATES.get(tense.label, [])
    if not templates:
        form = _extract_form(tense.rows, 0)
        return f"Exemple : {form}"

    person_idx, template = templates[0]
    form = _extract_form(tense.rows, person_idx)
    return template.format(form=form)


def get_tense_example(display: str, tense: TenseResult) -> str:
    """Retourne une phrase d'exemple pour un temps donné."""
    return _example_for_tense(display, tense)


def generate_examples(
    display: str,
    base: str,
    reflexive: bool,
    tenses: list[TenseResult],
) -> list[str]:
    """Génère des exemples pour les temps principaux."""
    return [get_tense_example(display, t) for t in tenses[:3]]