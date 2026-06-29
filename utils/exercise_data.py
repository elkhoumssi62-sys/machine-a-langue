"""Banques de données pour le générateur d'exercices FLE (mode local)."""

from __future__ import annotations

from dataclasses import dataclass

# ── Métadonnées ────────────────────────────────────────────────────────────

LEVEL_LABELS: dict[str, tuple[str, str]] = {
    "A1": ("Débutant", "🌱"),
    "A2": ("Élémentaire", "🌿"),
    "B1": ("Intermédiaire", "🌳"),
    "B2": ("Avancé", "🏆"),
}

THEME_DESCRIPTIONS: dict[str, str] = {
    "Conjugaison": "Temps, modes et accords — fiches progressives",
    "Vocabulaire": "Synonymes, contraires, définitions, champs lexicaux",
    "Phrases à compléter": "Phrases courtes, dialogues, listes de mots",
    "Textes à trous": "Textes authentiques, compréhension et grammaire",
    "QCM Grammaire": "Articles, pronoms, accords, subordonnées…",
}

# ── Vocabulaire ──────────────────────────────────────────────────────────────

SYNONYMS: dict[str, list[tuple[str, str, list[str], str]]] = {
    "A1": [
        ("content", "heureux", ["triste", "fatigué", "fâché"], "Les deux expriment une humeur positive."),
        ("maison", "logement", ["voiture", "jardin", "école"], "Synonyme général pour le lieu où l'on habite."),
        ("beau", "joli", ["laid", "petit", "vieux"], "Adjectifs de beauté courants au quotidien."),
        ("rapide", "vite", ["lent", "lourd", "calme"], "« Vite » est l'adverbe ; « rapide » l'adjectif."),
        ("commencer", "débuter", ["finir", "arrêter", "oublier"], "Verbes de début d'action."),
        ("acheter", "prendre", ["vendre", "donner", "jeter"], "Au magasin, « prendre » peut signifier acheter."),
        ("parler", "dire", ["écouter", "manger", "dormir"], "Verbes de communication orale."),
        ("aimer", "adorer", ["détester", "craindre", "ignorer"], "Nuances d'appréciation."),
    ],
    "A2": [
        ("acheter", "payer", ["vendre", "donner", "perdre"], "Payer = donner de l'argent pour acquérir."),
        ("commencer", "débuter", ["finir", "oublier", "refuser"], "Registre soutenu : débuter."),
        ("important", "essentiel", ["facile", "rare", "inutile"], "Essentiel = indispensable."),
        ("répondre", "répliquer", ["demander", "écouter", "partir"], "Répliquer est plus formel."),
        ("fatigué", "épuisé", ["reposé", "joyeux", "affamé"], "Épuisé = très fatigué."),
        ("voyage", "séjour", ["travail", "repas", "cadeau"], "Séjour = période passée dans un lieu."),
        ("problème", "difficulté", ["solution", "succès", "plaisir"], "Champ lexical de l'obstacle."),
        ("vite", "rapidement", ["lentement", "souvent", "tard"], "Adverbes de manière."),
    ],
    "B1": [
        ("améliorer", "perfectionner", ["détruire", "ignorer", "refuser"], "Perfectionner = améliorer jusqu'à l'excellence."),
        ("évident", "manifeste", ["caché", "douteux", "complexe"], "Registre soutenu : manifeste."),
        ("réussir", "parvenir", ["échouer", "abandonner", "tenter"], "Parvenir à = réussir à."),
        ("néanmoins", "cependant", ["donc", "puis", "ensuite"], "Connecteurs concessifs."),
        ("conséquence", "repercussion", ["cause", "origine", "début"], "Ce qui découle d'une action."),
        ("argument", "raisonnement", ["image", "couleur", "bruit"], "Vocabulaire de l'argumentation."),
        ("nuire", "porter préjudice", ["aider", "soutenir", "guérir"], "Expression figée plus soutenue."),
        ("rare", "peu fréquent", ["courant", "habituel", "banal"], "Nuances de fréquence."),
    ],
    "B2": [
        ("lucide", "clairvoyant", ["naïf", "confus", "distrait"], "Qui voit clair dans une situation."),
        ("pertinent", "approprié", ["absurde", "superficiel", "banal"], "Qui convient au contexte."),
        ("éphémère", "passager", ["éternel", "solide", "permanent"], "Qui dure peu de temps."),
        ("concilier", "harmoniser", ["opposer", "séparer", "rompre"], "Rapprocher des éléments contraires."),
        ("ambigu", "équivoque", ["clair", "explicite", "net"], "Qui peut se comprendre de deux façons."),
        ("prolixe", "bavard", ["concis", "bref", "lacunaire"], "Qui parle ou écrit trop."),
        ("fallacieux", "trompeur", ["honnête", "sincère", "fiable"], "Qui induit en erreur."),
        ("omniprésent", "ubiquitaire", ["absent", "rare", "local"], "Registre très soutenu."),
    ],
}

ANTONYMS: dict[str, list[tuple[str, str, list[str], str]]] = {
    "A1": [
        ("chaud", "froid", ["tiède", "doux", "sec"], "Opposition de température."),
        ("grand", "petit", ["moyen", "beau", "jeune"], "Opposition de taille."),
        ("ouvrir", "fermer", ["casser", "porter", "monter"], "Verbes d'action inverse."),
        ("jour", "nuit", ["matin", "soir", "midi"], "Moments de la journée."),
        ("content", "triste", ["fatigué", "calme", "pressé"], "États d'humeur."),
        ("monter", "descendre", ["entrer", "sortir", "rester"], "Mouvements verticaux."),
        ("beaucoup", "peu", ["assez", "trop", "plus"], "Quantité."),
        ("facile", "difficile", ["simple", "court", "clair"], "Degré de complexité."),
    ],
    "A2": [
        ("facile", "difficile", ["simple", "court", "clair"], "Niveau de difficulté."),
        ("arriver", "partir", ["rester", "entrer", "monter"], "Mouvements opposés."),
        ("augmenter", "diminuer", ["changer", "garder", "mesurer"], "Évolution quantitative."),
        ("optimiste", "pessimiste", ["réaliste", "calme", "sérieux"], "Vision de l'avenir."),
        ("accepte", "refuse", ["demande", "propose", "offre"], "Réponse à une proposition."),
        ("avant", "après", ["pendant", "depuis", "vers"], "Repères temporels."),
        ("plein", "vide", ["grand", "petit", "ouvert"], "État d'un contenant."),
        ("public", "privé", ["ouvert", "fermé", "neuf"], "Accès et espace."),
    ],
    "B1": [
        ("permanent", "temporaire", ["stable", "utile", "public"], "Durée dans le temps."),
        ("sincère", "hypocrite", ["honnête", "direct", "poli"], "Sincérité des propos."),
        ("abondant", "rare", ["suffisant", "léger", "court"], "Fréquence ou quantité."),
        ("prévisible", "imprévisible", ["logique", "normal", "certain"], "Capacité à anticiper."),
        ("théorique", "pratique", ["abstrait", "concret", "réel"], "Rapport à l'action."),
        ("objectif", "subjectif", ["neutre", "personnel", "émotif"], "Point de vue."),
        ("louer", "critiquer", ["décrire", "raconter", "expliquer"], "Jugement sur une œuvre."),
        ("anonyme", "célèbre", ["inconnu", "ordinaire", "discret"], "Notoriété."),
    ],
    "B2": [
        ("équivoque", "explicite", ["ambigu", "complexe", "concis"], "Clarté du message."),
        ("altruiste", "égoïste", ["généreux", "modeste", "sociable"], "Rapport à autrui."),
        ("concis", "prolixe", ["bref", "clair", "précis"], "Longueur du discours."),
        ("fallacieux", "fiable", ["trompeur", "douteux", "fragile"], "Crédibilité."),
        ("lucide", "naïf", ["clairvoyant", "sage", "prudent"], "Lucidité face à la réalité."),
        ("superficiel", "profond", ["léger", "banal", "court"], "Degré d'analyse."),
        ("consensus", "dissensus", ["accord", "harmonie", "unité"], "Vocabulaire du débat."),
        ("austère", "luxueux", ["simple", "sobre", "modeste"], "Style de vie."),
    ],
}

DEFINITIONS: dict[str, list[tuple[str, str, list[str], str]]] = {
    "A1": [
        ("un animal qui miaule", "le chat", ["le chien", "le poisson", "l'oiseau"], "Onomatopée : miauler."),
        ("le repas du matin", "le petit-déjeuner", ["le déjeuner", "le dîner", "le goûter"], "Premier repas de la journée."),
        ("l'endroit où on dort", "la chambre", ["la cuisine", "la salle de bain", "le garage"], "Pièce de la maison."),
        ("la personne qui enseigne", "le professeur", ["l'élève", "le médecin", "le boulanger"], "Métier de l'école."),
        ("le contraire de « non »", "oui", ["peut-être", "jamais", "toujours"], "Réponse affirmative."),
        ("un moyen de transport sur rails", "le train", ["l'avion", "le bateau", "le vélo"], "Transport ferroviaire."),
        ("la saison la plus chaude", "l'été", ["l'hiver", "le printemps", "l'automne"], "Quatre saisons."),
        ("un fruit rouge ou vert, souvent sucré", "la pomme", ["la carotte", "le pain", "le fromage"], "Vocabulaire alimentaire."),
    ],
    "A2": [
        ("une personne qui soigne les malades", "un médecin", ["un professeur", "un boulanger", "un chauffeur"], "Profession de santé."),
        ("le contraire de « toujours »", "jamais", ["souvent", "parfois", "bientôt"], "Fréquence négative."),
        ("un voyage en avion", "un vol", ["un train", "une promenade", "un séjour"], "Transport aérien."),
        ("un document qui prouve l'identité", "une carte d'identité", ["un billet", "un cahier", "un ticket"], "Papiers officiels."),
        ("le lieu où l'on emprunte des livres", "la bibliothèque", ["la boulangerie", "la piscine", "la gare"], "Équipement culturel."),
        ("une période de 24 heures", "un jour", ["une semaine", "un mois", "une heure"], "Temps calendaire."),
        ("qui ne coûte rien", "gratuit", ["cher", "payant", "coûteux"], "Prix."),
        ("le sentiment de vouloir connaître", "la curiosité", ["la colère", "la peur", "la fatigue"], "Émotion / trait."),
    ],
    "B1": [
        ("qui ne peut pas être évité", "inévitable", ["impossible", "improbable", "involontaire"], "Adjectif de certitude."),
        ("le fait de protéger l'environnement", "l'écologie", ["l'économie", "la géologie", "la technologie"], "Champ lexical vert."),
        ("une opinion contraire à la majorité", "une dissidence", ["une assistance", "une coïncidence", "une évidence"], "Vocabulaire du débat."),
        ("qui manque d'expérience", "inexpérimenté", ["compétent", "aguerri", "chevronné"], "Antonyme professionnel."),
        ("un résumé très court d'un texte", "une synthèse", ["une introduction", "une conclusion", "une note"], "Méthodologie écrite."),
        ("le fait de modifier un texte", "une révision", ["une lecture", "une dictée", "une copie"], "Processus d'écriture."),
        ("qui suscite la confiance", "fiable", ["douteux", "fragile", "incertain"], "Qualité d'une source."),
        ("un fait qui contredit une idée", "un contre-exemple", ["un exemple", "une preuve", "un argument"], "Logique argumentative."),
    ],
    "B2": [
        ("qui manque de sincérité", "hypocrite", ["sincère", "humble", "naïf"], "Registre moral."),
        ("une figure de style qui exagère", "l'hyperbole", ["la métaphore", "la litote", "l'euphémisme"], "Stylistique."),
        ("l'ensemble des traditions d'une société", "le patrimoine culturel", ["le patrimoine naturel", "le capital financier", "le marché libre"], "Culture générale."),
        ("qui ne laisse pas de place au doute", "catégorique", ["nuancé", "ambigu", "modeste"], "Ton du locuteur."),
        ("une comparaison sans outil de comparaison", "une métaphore", ["une hyperbole", "une litote", "une anaphore"], "Figure implicite."),
        ("le rejet systématique de toute règle", "l'anarchie", ["la démocratie", "la monarchie", "la république"], "Organisation sociale."),
        ("qui exprime peu de choses en peu de mots", "lacunaire", ["prolixe", "bavard", "ample"], "Style d'écriture."),
        ("un raisonnement qui semble logique mais est faux", "un sophisme", ["un syllogisme", "un axiome", "un théorème"], "Argumentation fallacieuse."),
    ],
}

# ── Conjugaison ──────────────────────────────────────────────────────────────

CONJ_VERBS: dict[str, list[str]] = {
    "A1": ["parler", "aimer", "habiter", "manger", "travailler", "être", "avoir", "aller", "faire", "dire"],
    "A2": ["finir", "choisir", "prendre", "venir", "se lever", "aller", "voir", "pouvoir", "vouloir", "mettre"],
    "B1": ["pouvoir", "vouloir", "devoir", "mettre", "écrire", "prendre", "boire", "croire", "recevoir", "se souvenir"],
    "B2": ["connaître", "croire", "recevoir", "maintenir", "apercevoir", "interdire", "construire", "décevoir", "surprendre", "se méfier"],
}

CONJ_TENSES: dict[str, list[str]] = {
    "A1": ["Présent", "Impératif"],
    "A2": ["Passé composé", "Imparfait", "Futur simple", "Présent"],
    "B1": ["Subjonctif présent", "Conditionnel présent", "Plus-que-parfait", "Passé composé"],
    "B2": ["Futur antérieur", "Plus-que-parfait", "Subjonctif présent", "Conditionnel passé"],
}

CONJ_TIPS: dict[str, str] = {
    "Présent": "Le présent exprime un fait actuel, une habitude ou une vérité générale.",
    "Passé composé": "Action terminée dans le passé. Auxiliaire être pour mouvement/pronominal.",
    "Imparfait": "Description, habitude ou action en cours dans le passé.",
    "Futur simple": "Action future ou promesse. Radical souvent identique à l'infinitif.",
    "Subjonctif présent": "Après il faut que, bien que, je doute que, pour que…",
    "Conditionnel présent": "Hypothèse, politesse, futur dans le passé.",
    "Plus-que-parfait": "Action antérieure à une autre action passée.",
    "Futur antérieur": "Action future antérieure à une autre action future.",
    "Impératif": "Ordre, conseil ou invitation. Pas de pronom sujet.",
}

# ── Phrases à compléter (courtes) ───────────────────────────────────────────

@dataclass
class FillTemplate:
    title: str
    instruction: str
    word_bank: list[str]
    template: str
    answers: list[str]
    tip: str
    explanations: list[str]


FILL_TEMPLATES: dict[str, list[FillTemplate]] = {
    "A1": [
        FillTemplate(
            "Se présenter en classe",
            "Complétez le dialogue avec les mots proposés.",
            ["je m'appelle", "j'ai", "ans", "habite", "viens"],
            "— Bonjour ! Comment tu t'appelles ?\n— Bonjour ! {0} Sophie. {1} 22 {2}. J'{3} à Lyon et je {4} de Belgique.",
            ["Je m'appelle", "J'ai", "ans", "habite", "viens"],
            "Modèle DELF A1 — entraînez la prononciation en binômes.",
            ["Présentation nominale.", "Avoir + âge.", "Nom masculin invariable.", "Habiter + lieu.", "Venir de + pays."],
        ),
        FillTemplate(
            "À la boulangerie",
            "Utilisez la banque de mots pour compléter la scène.",
            ["bonjour", "baguette", "euros", "merci", "revoir"],
            "— {0}, je voudrais une {1}, s'il vous plaît.\n— Voilà, ça fait deux {2}.\n— {3} ! Au {4} !",
            ["Bonjour", "baguette", "euros", "Merci", "revoir"],
            "Scène communicative A1 — insister sur la politesse.",
            ["Formule d'accueil.", "Produit courant.", "Monnaie.", "Remerciement.", "Au revoir."],
        ),
        FillTemplate(
            "Ma famille",
            "Complétez les phrases sur la famille.",
            ["frère", "sœur", "parents", "grands-parents", "oncle"],
            "J'ai un {0} et une {1}. Mes {2} habitent à Marseille. Mes {3} ont 70 ans. Mon {4} est médecin.",
            ["frère", "sœur", "parents", "grands-parents", "oncle"],
            "Prolongement : dessiner un arbre généalogique.",
            ["Membre masculin.", "Membre féminin.", "Père et mère.", "Pluriel.", "Frère du père ou de la mère."],
        ),
    ],
    "A2": [
        FillTemplate(
            "Raconter ses vacances",
            "Complétez le récit au passé composé et à l'imparfait.",
            ["été", "avons passé", "plage", "faisait", "avons nagé", "photos"],
            "L'{0} dernier, nous {1} une semaine à la {2}. Il {3} beau chaque jour. Nous {4} et avons pris des {5}.",
            ["été", "avons passé", "plage", "faisait", "avons nagé", "photos"],
            "Contraste imparfait (description) / passé composé (actions).",
            ["Saison.", "Passé composé.", "Lieu.", "Imparfait météo.", "Action terminée.", "Objets souvenirs."],
        ),
        FillTemplate(
            "Prendre rendez-vous",
            "Complétez l'appel téléphonique.",
            ["bonjour", "rendez-vous", "mardi", "14 heures", "confirmer", "merci"],
            "— {0}, je voudrais un {1} chez le médecin.\n— Nous avons une place {2} à {3}.\n— Parfait, je vous appelle pour {4}. {5} beaucoup !",
            ["Bonjour", "rendez-vous", "mardi", "14 heures", "confirmer", "merci"],
            "Situation administrative courante — reformuler à l'oral.",
            ["Salutation.", "Nom de l'action.", "Jour.", "Heure.", "Verbe à l'infinitif.", "Politesse."],
        ),
        FillTemplate(
            "Au restaurant",
            "Complétez la commande.",
            ["carte", "entrée", "plat", "dessert", "addition", "pourboire"],
            "Le serveur apporte la {0}. Je choisis une {1} et un {2}. Pour finir, un {3}. À la fin, je demande l'{4} et je laisse un {5}.",
            ["carte", "entrée", "plat", "dessert", "addition", "pourboire"],
            "Champ lexical restaurant — jeu de rôle possible.",
            ["Menu.", "Premier service.", "Service principal.", "Fin du repas.", "Note à payer.", "Pour le serveur."],
        ),
    ],
    "B1": [
        FillTemplate(
            "Lettre de motivation",
            "Complétez avec les connecteurs et expressions formelles.",
            ["Madame, Monsieur", "actuellement", "compétences", "candidature", "restant", "salutations"],
            "{0},\nJe suis {1} étudiant en lettres et je souhaite développer mes {2}. Je vous prie de bien vouloir examiner ma {3} pour le poste {4} à votre disposition.\nVeuillez agréer mes {5} distinguées.",
            ["Madame, Monsieur", "actuellement", "compétences", "candidature", "restant", "salutations"],
            "Production écrite B1 — formules de politesse.",
            ["Formule d'appel.", "Temps présent.", "Nom pluriel.", "Nom féminin.", "Participe présent.", "Formule de clôture."],
        ),
        FillTemplate(
            "Débat en classe",
            "Complétez l'argumentation.",
            ["D'une part", "cependant", "en effet", "par conséquent", "En conclusion"],
            "{0}, les réseaux sociaux facilitent la communication. {1}, ils peuvent nuire à la concentration. {2}, de nombreuses études le montrent. {3}, un usage modéré est recommandé. {4}, il faut apprendre à les utiliser avec discernement.",
            ["D'une part", "cependant", "en effet", "par conséquent", "En conclusion"],
            "Connecteurs logiques — carte mentale conseillée.",
            ["Premier argument.", "Opposition.", "Justification.", "Conséquence.", "Synthèse."],
        ),
    ],
    "B2": [
        FillTemplate(
            "Analyse littéraire",
            "Complétez le paragraphe d'analyse.",
            ["néanmoins", "symbolise", "progressivement", "suggère", "en définitive"],
            "L'auteur décrit un paysage désolé qui {0} l'isolement du personnage. La lumière diminue {1}, ce qui {2} un malaise croissant. Le lexique choisi {3} une critique sociale voilée. {4}, ce passage prépare le dénouement tragique.",
            ["symbolise", "progressivement", "suggère", "néanmoins", "En définitive"],
            "Vocabulaire d'analyse — préparation bac/DALF.",
            ["Verbe d'interprétation.", "Adverbe de manière.", "Verbe d'implication.", "Concession (ici repositionné).", "Formule conclusive."],
        ),
        FillTemplate(
            "Article de presse",
            "Complétez l'éditorial.",
            ["En outre", "subséquemment", "il convient", "dès lors", "Force est de constater"],
            "{0} que la crise économique frappe les plus fragiles. {1}, les mesures annoncées tardent. {2} de noter que les inégalités se creusent. {3}, une réponse collective s'impose. {4}, l'urgence est réelle.",
            ["Force est de constater", "En outre", "il convient", "Dès lors", "subséquemment"],
            "Registre journalistique soutenu.",
            ["Tournure impersonnelle.", "Ajout d'argument.", "Formule prescriptive.", "Conséquence logique.", "Succession temporelle."],
        ),
    ],
}

# ── Textes à trous (longs) ────────────────────────────────────────────────────

@dataclass
class ClozeTemplate:
    title: str
    instruction: str
    word_bank: list[str] | None
    template: str
    answers: list[str]
    tip: str
    explanations: list[str]


CLOZE_TEMPLATES: dict[str, list[ClozeTemplate]] = {
    "A1": [
        ClozeTemplate(
            "Une journée typique",
            "Lisez le texte et complétez les {n} trous. Banque de mots disponible.",
            ["se lève", "petit-déjeuner", "travail", "midi", "soir", "dort"],
            "Luc {0} à 7 heures. Il prend son {1} avec sa famille. Il va au {2} en bus. À {3}, il mange à la cantine. Le {4}, il regarde la télé. Il {5} à 22 heures.",
            ["se lève", "petit-déjeuner", "travail", "midi", "soir", "dort"],
            "Routine quotidienne — support pour présent de l'indicatif.",
            ["Verbe pronominal.", "Repas du matin.", "Lieu professionnel.", "Moment de la journée.", "Fin de journée.", "3e personne singulier."],
        ),
        ClozeTemplate(
            "Les saisons",
            "Complétez le texte sur les saisons (articles et adjectifs).",
            ["Le", "chaud", "Les", "froid", "colorés", "neige"],
            "{0} printemps est doux. L'été est très {1}. {2} feuilles d'automne sont {3}. En hiver, il y a de la {4} et les arbres ne sont plus {5}.",
            ["Le", "chaud", "Les", "colorées", "neige", "verts"],
            "Réviser articles définis et accords de base.",
            ["Article devant saison.", "Adjectif masculin.", "Article pluriel.", "Accord fém. plur.", "Nom féminin.", "Adjectif masc. plur."],
        ),
    ],
    "A2": [
        ClozeTemplate(
            "Week-end à la montagne",
            "Complétez ce récit au passé (passé composé / imparfait).",
            None,
            "Samedi dernier, nous {0} en train jusqu'à Chamonix. Il {1} beau et les sommets {2} magnifiques. Nous {3} une randonnée de trois heures. Le soir, nous {4} dans un petit restaurant typique. C'{5} une expérience inoubliable !",
            ["sommes allés", "faisait", "étaient", "avons fait", "avons dîné", "était"],
            "Alternance imparfait (cadre) / passé composé (actions).",
            ["Mouvement → être.", "Description météo.", "Description état.", "Action ponctuelle.", "Action terminée.", "Imparfait de description."],
        ),
        ClozeTemplate(
            "Courriel professionnel",
            "Complétez l'e-mail avec les formules adaptées.",
            ["Madame", "sujet", "disponibilité", "ci-joint", "salutations"],
            "Bonjour {0} Dupont,\nJe vous écris au {1} de ma candidature. Je reste à votre disposition pour préciser mes {2}. Vous trouverez {3} mon CV.\nCordialement,\nMarc Leroy",
            ["Madame", "sujet", "disponibilités", "ci-joint", "salutations"],
            "Écriture professionnelle A2/B1 — modèle réutilisable.",
            ["Civilité.", "Nom du champ.", "Pluriel requis.", "Locution figée.", "Formule finale."],
        ),
    ],
    "B1": [
        ClozeTemplate(
            "L'impact des écrans",
            "Complétez ce texte argumentatif (connecteurs et temps verbaux).",
            None,
            "Aujourd'hui, les écrans {0} une place centrale dans la vie des adolescents. {1} certains estiment qu'ils favorisent l'apprentissage, {2} soulignent leurs effets négatifs. Les parents {3} s'inquiéter de l'addiction possible. {4}, il serait pertinent d'encadrer le temps d'utilisation. Chaque famille {5} trouver un équilibre adapté.",
            ["occupent", "Si", "d'autres", "commencent à", "Ainsi", "doit"],
            "Texte dialectique — préparation production écrite B1.",
            ["Présent descriptif.", "Concession.", "Sujet pluriel.", "Périphrase progressive.", "Connecteur conclusif.", "Modalité devoir."],
        ),
        ClozeTemplate(
            "Biographie d'un artiste",
            "Complétez la biographie (temps du récit).",
            None,
            "Marie Curie {0} née en Pologne en 1867. Elle {1} en France à l'âge de 24 ans. En 1903, elle {2} le prix Nobel de physique. Elle {3} la première femme à recevoir cette distinction. Sa carrière {4} encore aujourd'hui des millions de jeunes filles.",
            ["est", "est arrivée", "a reçu", "est devenue", "inspire"],
            "Biographie : passé composé pour les faits, présent pour l'impact.",
            ["État passé → être.", "Mouvement → être.", "Action ponctuelle.", "Changement d'état.", "Vérité actuelle."],
        ),
    ],
    "B2": [
        ClozeTemplate(
            "Éditorial — la laïcité",
            "Complétez cet éditorial (registre soutenu, subordonnées).",
            None,
            "La laïcité, {0} certains voudraient réduire à un simple principe administratif, {1} en réalité un pilier de notre vivre-ensemble. {2} l'État garantisse la liberté de conscience, chacun doit pouvoir exprimer ses convictions {3} respecter celles d'autrui. {4} nous oublions cette exigence, le dialogue civique {5} compromis.",
            ["que", "constitue", "Bien que", "tout en", "Si", "serait"],
            "Subordonnées concessives et conditionnelles — analyse de presse.",
            ["Pronom relatif complément.", "Registre soutenu.", "Concession + subjonctif.", "Locution complexe.", "Condition irréelle.", "Conditionnel de conséquence."],
        ),
        ClozeTemplate(
            "Extrait romanesque",
            "Complétez ce passage littéraire.",
            ["pénombre", "surgit", "immobile", "bruissement", "contemplait"],
            "Dans la {0} du crépuscule, le héros {1} la mer, {2} comme une statue. Un léger {3} dans les roseaux {4} une silhouette. Le temps {5} suspendu.",
            ["pénombre", "contemplait", "immobile", "bruissement", "surgit", "semblait"],
            "Lexique littéraire — préparation commentaire composé.",
            ["Nom poétique.", "Imparfait description.", "Adjectif attribut.", "Onomatopée poétique.", "Verbe de mouvement soudain.", "Imparfait d'atmosphère."],
        ),
    ],
}

# ── QCM Grammaire dynamiques ─────────────────────────────────────────────────

@dataclass
class QcmQuestion:
    stem: str
    options: list[str]
    correct_idx: int
    explanation: str


@dataclass
class QcmSet:
    title: str
    instruction: str
    topic: str
    questions: list[QcmQuestion]
    tip: str


GRAMMAR_QCM_SETS: dict[str, list[QcmSet]] = {
    "A1": [
        QcmSet(
            "Les articles définis",
            "Choisissez la bonne réponse.",
            "Articles",
            [
                QcmQuestion("___ maison est grande.", ["le", "la", "les", "des"], 1, "« Maison » est féminin → la."),
                QcmQuestion("___ enfants jouent dehors.", ["le", "la", "les", "l'"], 2, "Pluriel → les."),
                QcmQuestion("___ homme arrive.", ["le", "la", "les", "l'"], 3, "Devant h muet → l'."),
            ],
            "Les articles définis s'accordent en genre et en nombre avec le nom.",
        ),
        QcmSet(
            "Présent des verbes en -er",
            "Quelle forme est correcte ?",
            "Conjugaison",
            [
                QcmQuestion("Nous ___ (parler) français.", ["parle", "parles", "parlons", "parlez"], 2, "1er groupe : nous → -ons."),
                QcmQuestion("Tu ___ (habiter) où ?", ["habite", "habites", "habitons", "habitent"], 1, "Tu → -es."),
                QcmQuestion("Ils ___ (manger) à la cantine.", ["mange", "manges", "mangeons", "mangent"], 3, "Ils → -ent."),
            ],
            "Terminaisons du 1er groupe : -e, -es, -e, -ons, -ez, -ent.",
        ),
        QcmSet(
            "Masculin et féminin",
            "Quelle forme convient ?",
            "Genre",
            [
                QcmQuestion("C'est une ___ (ami)", ["ami", "amie", "amies", "amis"], 1, "Féminin : amie."),
                QcmQuestion("Une ___ (professeur)", ["professeur", "professeure", "professeuse", "professeurée"], 1, "Forme féminine courante."),
                QcmQuestion("Un ___ (acteur) célèbre", ["acteur", "acteure", "actrice", "acteuse"], 2, "Féminin : actrice."),
            ],
            "Certains féminins sont irréguliers : acteur/actrice, chanteur/chanteuse.",
        ),
    ],
    "A2": [
        QcmSet(
            "Passé composé ou imparfait ?",
            "Choisissez le temps adapté.",
            "Temps du passé",
            [
                QcmQuestion("Quand j'étais petit, je ___ (jouer) dehors.", ["j'ai joué", "je jouais", "je jouerai", "je joue"], 1, "Habitude passée → imparfait."),
                QcmQuestion("Hier, nous ___ (visiter) le musée.", ["visitions", "avons visité", "visitons", "visiterons"], 1, "Action ponctuelle → passé composé."),
                QcmQuestion("Il ___ (pleuvoir) quand nous sommes sortis.", ["a plu", "pleuvait", "pleut", "pleuvra"], 1, "Contexte en cours → imparfait."),
            ],
            "Imparfait = toile de fond. Passé composé = action ponctuelle.",
        ),
        QcmSet(
            "Pronoms COD et COI",
            "Quel pronom convient ?",
            "Pronoms",
            [
                QcmQuestion("Je vois Marie. Je ___ vois.", ["le", "la", "lui", "leur"], 1, "COD féminin → la."),
                QcmQuestion("Il parle à ses parents. Il ___ parle.", ["le", "la", "lui", "leur"], 3, "COI pluriel → leur."),
                QcmQuestion("Tu écoutes les enfants. Tu ___ écoutes.", ["le", "la", "les", "leur"], 2, "COD pluriel → les."),
            ],
            "COD : le/la/les — COI : lui/leur. Ne pas confondre !",
        ),
        QcmSet(
            "La négation",
            "Quelle phrase est correcte ?",
            "Négation",
            [
                QcmQuestion("Je mange des fruits → négation", ["Je mange pas des fruits.", "Je ne mange pas de fruits.", "Je ne mange jamais des fruits.", "B et C possibles"], 3, "Ne…pas et ne…jamais ; « des » → « de »."),
                QcmQuestion("Elle a quelque chose → négation", ["Elle n'a pas quelque chose.", "Elle n'a rien.", "Elle ne a rien.", "Elle a rien."], 1, "Quelque chose → rien."),
            ],
            "La négation est en deux parties : ne … pas / plus / jamais / rien.",
        ),
    ],
    "B1": [
        QcmSet(
            "Accord du participe passé",
            "Quelle forme est correcte ?",
            "Accords",
            [
                QcmQuestion("Les fleurs que j'ai ___ (cueillir)", ["cueilli", "cueillie", "cueillies", "cueillit"], 2, "COD « fleurs » avant l'auxiliaire → accord fém. plur."),
                QcmQuestion("Elles sont ___ (arriver) hier.", ["arrivé", "arrivée", "arrivées", "arrivés"], 2, "Être → accord avec le sujet « elles »."),
                QcmQuestion("Les livres que nous avons ___ (lire)", ["lu", "lus", "lues", "lues"], 1, "COD masculin pluriel antéposé → lus."),
            ],
            "Avoir + COD antéposé → accord. Être → accord avec le sujet.",
        ),
        QcmSet(
            "Pronoms relatifs",
            "Choisissez le pronom relatif correct.",
            "Relatifs",
            [
                QcmQuestion("La femme ___ parle est ma tante.", ["que", "qui", "dont", "où"], 1, "Sujet du verbe → qui."),
                QcmQuestion("Le livre ___ je lis est passionnant.", ["qui", "que", "dont", "lequel"], 1, "COD → que."),
                QcmQuestion("La ville ___ je suis né est Lyon.", ["que", "qui", "dont", "où"], 3, "Lieu → où."),
            ],
            "Qui = sujet, que = COD, dont = complément de, où = lieu/temps.",
        ),
        QcmSet(
            "Subjonctif ou indicatif ?",
            "Quelle forme convient ?",
            "Subjonctif",
            [
                QcmQuestion("Il faut que tu ___ (venir).", ["viens", "viennes", "venais", "viendras"], 1, "Après « il faut que » → subjonctif."),
                QcmQuestion("Je pense qu'il ___ (être) en retard.", ["soit", "est", "serait", "fût"], 1, "Après « je pense que » → indicatif."),
                QcmQuestion("Bien qu'il ___ (pleuvoir), nous sortons.", ["pleut", "pleuve", "pleuvait", "pleuvra"], 1, "Après « bien que » → subjonctif."),
            ],
            "Subjonctif après doute, volonté, sentiment ; indicatif après certitude.",
        ),
    ],
    "B2": [
        QcmSet(
            "Subordonnées et ponctuation",
            "Quelle phrase est correcte ?",
            "Syntaxe",
            [
                QcmQuestion("Bien qu'il pleuve…", ["Bien qu'il pleuve nous sortons.", "Bien qu'il pleuve, nous sortons.", "Bien qu'il pleut, nous sortons."], 1, "Virgule + subjonctif après bien que."),
                QcmQuestion("Je ne sais pas ___ il viendra.", ["si", "s'il", "que", "qu'il"], 1, "Si + il → s'il (élision)."),
                QcmQuestion("Quoiqu'il ___ (faire) son possible…", ["fait", "fasse", "ferait", "fera"], 1, "Quoique → subjonctif."),
            ],
            "Subordonnée en tête de phrase → virgule de séparation.",
        ),
        QcmSet(
            "Voix passive et formes composées",
            "Quelle transformation est correcte ?",
            "Voix passive",
            [
                QcmQuestion("Le directeur signe les contrats.", ["Les contrats sont signés par le directeur.", "Les contrats ont signé par le directeur.", "Les contrats sont signé par le directeur."], 0, "Être + participe passé + par + agent."),
                QcmQuestion("On a construit ce pont en 1990.", ["Ce pont a été construit en 1990.", "Ce pont est construit en 1990.", "Ce pont a construit en 1990."], 0, "Passé composé passif : a été + participe."),
            ],
            "Voix passive : être + participe passé (accord avec le sujet).",
        ),
        QcmSet(
            "Concordance des temps",
            "Quelle forme respecte la concordance ?",
            "Concordance",
            [
                QcmQuestion("Il a dit qu'il ___ (venir) le lendemain.", ["vient", "viendrait", "viendra", "venait"], 1, "Futur du discours direct → conditionnel au rapporté."),
                QcmQuestion("Je pensais qu'elle ___ (déjà / finir).", ["a déjà fini", "avait déjà fini", "finirait", "finissait"], 1, "Passé composé → plus-que-parfait."),
                QcmQuestion("S'il ___ (savoir), il serait resté.", ["sait", "savait", "avait su", "aurait su"], 2, "Conditionnel → plus-que-parfait dans la subordonnée."),
            ],
            "Concordance : présent→imparfait, futur→conditionnel, passé composé→plus-que-parfait.",
        ),
    ],
}