// ============================
// EXAMS.JS — Logique des examens interactifs
// "Il était une fois un vieux couple heureux"
// Mohammed Khaïr-Eddine
// ============================

// ---- Data: 12 Examens ----
const EXAMS = [
  // EXAMEN 1
  {
    id: 1,
    title: "La vie du vieux couple",
    theme: "La vie quotidienne de Bouchaïb et sa femme dans leur village montagnard",
    meta: { niveau: "1ère année lycée", durée: "45 min", compétence: "Compréhension écrite" },
    textSupport: `Depuis son retour au pays, Bouchaïb n'était plus tenté par le Nord. Il ne voyageait plus que pour se rendre à tel ou tel moussem annuel comme celui de Sidi Hmad Ou Moussa… et il ne ratait jamais le souk hebdomadaire, où il allait à dos d'âne tous les mercredis. Un âne timide et bien mieux traité que les baudets de la région. Son maître y tenait comme à un enfant.`,
    questions: [
      {
        type: "qcm",
        text: "Bouchaïb se rendait au souk :",
        options: ["Tous les lundis", "Tous les mercredis", "Tous les vendredis", "Tous les dimanches"],
        correct: 1,
        feedback: "Le texte précise qu'il allait au souk «tous les mercredis»."
      },
      {
        type: "qcm",
        text: "Quel animal utilisait Bouchaïb pour aller au souk ?",
        options: ["Un cheval", "Un mulet", "Un âne", "Une vache"],
        correct: 2,
        feedback: "Il allait «à dos d'âne» au souk hebdomadaire."
      },
      {
        type: "vf",
        text: "Bouchaïb était encore tenté de repartir travailler dans le Nord.",
        correct: false,
        feedback: "Faux : «Depuis son retour au pays, Bouchaïb n'était plus tenté par le Nord.»"
      },
      {
        type: "vf",
        text: "Bouchaïb traitait son âne comme un enfant.",
        correct: true,
        feedback: "Vrai : «il le disait crûment aux persécuteurs des bêtes [...] il y tenait comme à un enfant»."
      },
      {
        type: "qcm",
        text: "Bouchaïb assistait aux moussems, notamment celui de :",
        options: ["Sidi Allal", "Sidi Hmad Ou Moussa", "Sidi Bourja", "Sidi Brahim"],
        correct: 1,
        feedback: "Le texte mentionne «le moussem annuel de Sidi Hmad Ou Moussa»."
      },
      {
        type: "fill",
        text: "Bouchaïb était un ___ lettré qui possédait des ___ manuscrits relatifs à la région.",
        blanks: ["fin", "vieux"],
        feedback: "«Il était un fin lettré. Il possédait des vieux manuscrits relatifs à la région.»"
      },
      {
        type: "qcm",
        text: "Que faisait Bouchaïb pour la communauté ?",
        options: ["Il était médecin du village", "Il rédigeait les lettres pour les habitants", "Il enseignait à l'école", "Il construisait des maisons"],
        correct: 1,
        feedback: "«Il était l'écrivain public par excellence. Il rédigeait les lettres.»"
      },
      {
        type: "qcm",
        text: "Bouchaïb tenait la comptabilité de quelle institution ?",
        options: ["La mairie", "Le souk", "La mosquée", "L'école"],
        correct: 2,
        feedback: "«Il tenait la comptabilité de la mosquée sur un cahier d'écolier vert.»"
      },
      {
        type: "vf",
        text: "Le vieux couple avait plusieurs enfants.",
        correct: false,
        feedback: "Faux : le texte indique qu'ils n'avaient «aucune descendance»."
      },
      {
        type: "qcm",
        text: "D'où venait le surnom «Bouchaïb» ?",
        options: ["De son prénom berbère", "De son travail à Mazagan", "De sa grande sagesse", "De son âne"],
        correct: 1,
        feedback: "«Un sobriquet lui était resté de cette longue absence, Bouchaïb, car il avait dû travailler à Mazagan.»"
      }
    ],
    production: {
      sujet: "Décrivez la vie quotidienne d'une personne âgée dans votre village ou quartier. Évoquez ses habitudes, ses relations avec la communauté et sa philosophie de vie. (150-200 mots)",
      outils: {
        "Connecteurs temporels": ["d'abord", "ensuite", "chaque jour", "le matin", "le soir", "puis", "enfin"],
        "Verbes d'habitude": ["se lever", "se rendre à", "pratiquer", "partager", "participer", "veiller à"],
        "Adjectifs qualificatifs": ["paisible", "sage", "dévoué(e)", "serein(e)", "généreux/se", "exemplaire"],
        "Expressions utiles": ["il/elle a l'habitude de", "fidèle à sa routine", "au fil du temps", "malgré les années"]
      }
    }
  },

  // EXAMEN 2
  {
    id: 2,
    title: "La vieille voisine Talouqit",
    theme: "La figure de la femme sage et savante dans la communauté villageoise",
    meta: { niveau: "1ère année lycée", durée: "45 min", compétence: "Compréhension & vocabulaire" },
    textSupport: `Cette pauvre vieille vivait dans une immense bâtisse en partie délabrée parmi des multitudes de rats et de chauves-souris. Elle était encore assez vigoureuse pour entretenir une vache. On la surnommait Talouqit sans trop savoir pourquoi. On savait seulement qu'elle était une sainte et qu'elle lisait et écrivait couramment en arabe classique et en berbère. Elle tenait ces connaissances de ses ancêtres, qui étaient des cheiks vénérés.`,
    questions: [
      {
        type: "qcm",
        text: "Que signifie le sobriquet «Talouqit» ?",
        options: ["Vieille femme", "Boîte d'allumettes", "Femme sage", "Sainte du village"],
        correct: 1,
        feedback: "Une note en bas de page précise : «Talouqit : boîte d'allumettes»."
      },
      {
        type: "vf",
        text: "Talouqit savait lire et écrire en arabe classique uniquement.",
        correct: false,
        feedback: "Faux : elle lisait et écrivait «en arabe classique et en berbère»."
      },
      {
        type: "qcm",
        text: "De qui Talouqit tenait-elle ses connaissances ?",
        options: ["D'un imam", "De ses ancêtres cheiks", "D'une école coranique", "Du fqih du village"],
        correct: 1,
        feedback: "«Elle tenait ces connaissances de ses ancêtres, qui étaient des cheiks vénérés.»"
      },
      {
        type: "vf",
        text: "Talouqit exerçait officiellement comme guérisseuse au village.",
        correct: false,
        feedback: "Faux : «elle évitait de passer pour une guérisseuse, même occasionnellement.»"
      },
      {
        type: "qcm",
        text: "Que signifie «Tagourramte» dans le texte ?",
        options: ["Savante", "Sainte", "Guerrière", "Enseignante"],
        correct: 1,
        feedback: "La note précise : «Tagourramte : sainte»."
      },
      {
        type: "fill",
        text: "Talouqit était capable de soigner des enfants atteints de ___ ou de toute autre ___ grave.",
        blanks: ["typhoïde", "maladie"],
        feedback: "«elle dut parfois soigner des enfants atteints de typhoïde ou de toute autre maladie grave.»"
      },
      {
        type: "qcm",
        text: "Pendant les fêtes, que faisait Talouqit pour la communauté ?",
        options: ["Elle préparait du couscous", "Elle faisait le pain communautaire", "Elle récitait des prières", "Elle soignait les malades"],
        correct: 1,
        feedback: "«elle faisait elle-même le pain communautaire» dans son grand four en terre battue."
      },
      {
        type: "vf",
        text: "Les enfants qui venaient chez Talouqit repartaient avec une galette.",
        correct: true,
        feedback: "Vrai : «Les enfants qui venaient là ne repartaient pas sans emporter une galette rembourrée d'un œuf dur.»"
      },
      {
        type: "qcm",
        text: "Que vendait Talouqit de ses connaissances médicinales ?",
        options: ["Elle les vendait cher", "Elle les enseignait gratuitement", "Elle ne les vendait pas", "Elle les réservait aux riches"],
        correct: 2,
        feedback: "«Elle ne vendait donc pas son savoir au premier venu.»"
      },
      {
        type: "qcm",
        text: "Le clan d'où venaient les ancêtres de Talouqit préférait :",
        options: ["La science à la guerre", "La guerre à la science", "La prière à tout", "Le commerce à l'éducation"],
        correct: 1,
        feedback: "«fait rare dans le clan des Aït Al Hassan, qui préféraient la guerre à la science.»"
      }
    ],
    production: {
      sujet: "Rédigez un portrait d'une femme exemplaire de votre entourage ou imaginaire : ses qualités, son rôle dans la communauté, et l'admiration qu'elle inspire. (150-200 mots)",
      outils: {
        "Connecteurs logiques": ["non seulement… mais aussi", "bien que", "malgré", "en outre", "par ailleurs", "en effet"],
        "Verbes de description": ["incarner", "posséder", "transmettre", "inspirer", "mériter", "honorer"],
        "Adjectifs mélioratifs": ["remarquable", "vénérée", "dévouée", "savante", "généreuse", "exemplaire"],
        "Structure du portrait": ["introduction", "qualités morales", "qualités intellectuelles", "rôle social", "conclusion"]
      }
    }
  },

  // EXAMEN 3
  {
    id: 3,
    title: "La terrasse sous les étoiles",
    theme: "La poésie de la vie simple : contemplation, nature et sérénité",
    meta: { niveau: "2ème année lycée", durée: "50 min", compétence: "Compréhension & analyse" },
    textSupport: `En observant cette fantastique chape de joyaux cosmiques, le Vieux louait Dieu de lui avoir permis de vivre des moments de paix avec les seuls êtres qu'il aimât: sa femme, son âne et son chat. De temps en temps, il se remémorait les vieilles légendes, mais sa pensée allait surtout s'égarer parmi ces feux chatoyants à la fois proches et lointains. «Est-ce là que se trouve le fameux Paradis? se demandait-il.»`,
    questions: [
      {
        type: "qcm",
        text: "À quoi le narrateur compare-t-il le ciel étoilé ?",
        options: ["À un tapis de velours", "À un plafond de diamants rayonnants", "À une mer infinie", "À un jardin fleuri"],
        correct: 1,
        feedback: "«on voyait nettement la Voie lactée, qui semblait un plafond de diamants rayonnants.»"
      },
      {
        type: "vf",
        text: "Le Vieux aimait ses trois compagnons : sa femme, son chien et son chat.",
        correct: false,
        feedback: "Faux : il aimait «sa femme, son âne et son chat» — pas un chien."
      },
      {
        type: "qcm",
        text: "Que faisait le Vieux en observant le ciel ?",
        options: ["Il priait en silence", "Il louait Dieu pour sa paix", "Il racontait des histoires", "Il s'endormait"],
        correct: 1,
        feedback: "«le Vieux louait Dieu de lui avoir permis de vivre des moments de paix»."
      },
      {
        type: "qcm",
        text: "Quelle boisson le Vieux appréciait-il en soirée ?",
        options: ["Du café arabe", "Du lait de chèvre", "Du thé vert de Chine", "De l'eau de source"],
        correct: 2,
        feedback: "«ce thé vert de Chine qu'un ami lui envoyait de France»."
      },
      {
        type: "vf",
        text: "La vieille femme parlait beaucoup quand elle rejoignait le Vieux sur la terrasse.",
        correct: false,
        feedback: "Faux : «La vieille s'installait à son tour à côté du Vieux, prenait son thé sans rien dire.»"
      },
      {
        type: "fill",
        text: "Le couple écoutait le ___ lointain du chacal, la plainte du ___, le crissement des insectes.",
        blanks: ["jappement", "hibou"],
        feedback: "«le jappement lointain du chacal, la plainte du hibou, le crissement des insectes»."
      },
      {
        type: "qcm",
        text: "Quelle figure de style est utilisée dans «plafond de diamants rayonnants» ?",
        options: ["Une comparaison", "Une métaphore", "Une personnification", "Une hyperbole"],
        correct: 1,
        feedback: "C'est une métaphore : le ciel étoilé est directement assimilé à un plafond de diamants sans «comme»."
      },
      {
        type: "qcm",
        text: "Quelle question philosophique se posait le Vieux en contemplant les étoiles ?",
        options: ["Pourquoi n'a-t-il pas d'enfants ?", "Où se trouvent le Paradis et l'Enfer ?", "Quand mourra-t-il ?", "Pourquoi a-t-il quitté le Nord ?"],
        correct: 1,
        feedback: "«Est-ce là que se trouve le fameux Paradis ? se demandait-il. Et l'Enfer ?»"
      },
      {
        type: "vf",
        text: "Le couple pouvait dormir sur la terrasse car l'air était doux et agréable.",
        correct: true,
        feedback: "Vrai : «On pouvait manger et passer la nuit sur la terrasse car l'air était agréable.»"
      },
      {
        type: "qcm",
        text: "Comment le Vieux qualifie-t-il le son des mouches dans les toiles d'araignée ?",
        options: ["Un bruit agaçant", "Une musique secrète de la vie", "Un signe de malchance", "Un bruit insignifiant"],
        correct: 1,
        feedback: "«Ce bruit ne le dérangeait pas. Il représentait pour lui l'une des musiques secrètes de la vie.»"
      }
    ],
    production: {
      sujet: "Décrivez un moment de contemplation de la nature que vous avez vécu ou imaginé. Exprimez les émotions ressenties et les réflexions que ce moment a suscitées en vous. (150-200 mots)",
      outils: {
        "Champs lexicaux": ["étoiles / ciel / cosmos", "silence / paix / sérénité", "nuit / crépuscule / aurore"],
        "Figures de style": ["métaphore", "comparaison", "personnification", "hyperbole"],
        "Verbes de perception": ["contempler", "observer", "entendre", "ressentir", "percevoir", "admirer"],
        "Expressions poétiques": ["à la clarté de la lune", "sous la voûte céleste", "dans le silence de la nuit", "au fil des étoiles"]
      }
    }
  },

  // EXAMEN 4
  {
    id: 4,
    title: "Le rêve de l'amandier",
    theme: "Le symbolisme du rêve et la prescience de la mort",
    meta: { niveau: "2ème année lycée", durée: "50 min", compétence: "Analyse littéraire" },
    textSupport: `«Depuis quelque temps, je fais un rêve absurde, toujours le même. Il y a là un grand arbre, un amandier vénérable plus haut que tous les autres… et sur ses branches supérieures beaucoup d'amandes qu'il est impossible de gauler sans grimper. Fasciné par elles, je n'hésite pas, je monte… et c'est au moment où je lève le bras pour gauler que je perds l'équilibre et tombe. Et puis, plus rien. Qu'est-ce que ça veut dire?»`,
    questions: [
      {
        type: "qcm",
        text: "Quel arbre apparaît dans le rêve du Vieux ?",
        options: ["Un olivier", "Un figuier", "Un amandier", "Un noyer"],
        correct: 2,
        feedback: "«Il y a là un grand arbre, un amandier vénérable plus haut que tous les autres.»"
      },
      {
        type: "vf",
        text: "Dans le rêve, le Vieux réussit à cueillir les amandes sans difficulté.",
        correct: false,
        feedback: "Faux : il tombe «au moment où il lève le bras pour gauler» — il n'y parvient pas."
      },
      {
        type: "qcm",
        text: "Comment le Vieux qualifie-t-il lui-même son rêve ?",
        options: ["Merveilleux", "Absurde", "Prophétique", "Inspirant"],
        correct: 1,
        feedback: "«je fais un rêve absurde, toujours le même»."
      },
      {
        type: "vf",
        text: "Le Vieux fait ce rêve une seule fois.",
        correct: false,
        feedback: "Faux : il dit «toujours le même» et «Cette nuit-là encore, il rêva du même arbre.»"
      },
      {
        type: "qcm",
        text: "À qui le Vieux décide-t-il de ne pas parler de son rêve ?",
        options: ["À sa femme", "Au fqih", "Au boucher", "Au Mokhazni"],
        correct: 1,
        feedback: "«Il aurait pu en toucher un mot au fqih, mais il ne le fit pas.»"
      },
      {
        type: "fill",
        text: "Ce qui turlupinait le Vieux, c'était de ne pas pouvoir donner un ___ à ce songe ___.",
        blanks: ["sens", "obsédant"],
        feedback: "«Ce qui le turlupinait, c'était de ne pas pouvoir donner un sens à ce songe obsédant.»"
      },
      {
        type: "qcm",
        text: "Que lui conseille sa femme après ce récit ?",
        options: ["De consulter un marabout", "De ne plus grimper aux arbres", "D'aller voir le médecin", "De prier davantage"],
        correct: 1,
        feedback: "«tu devrais faire attention. À ton âge, on ne grimpe plus aux arbres.»"
      },
      {
        type: "qcm",
        text: "Selon vous, que symbolise la chute dans ce rêve récurrent ?",
        options: ["Un voyage à venir", "La mort prochaine", "Un succès futur", "Un retour au passé"],
        correct: 1,
        feedback: "Dans de nombreuses cultures, rêver de chuter d'un arbre est un présage de mort — ce que le récit confirme symboliquement."
      },
      {
        type: "vf",
        text: "Le rêve trouble la gaieté du Vieux.",
        correct: true,
        feedback: "Vrai : «pourquoi celui-ci fausse-t-il ma gaieté ?»"
      },
      {
        type: "qcm",
        text: "Quelle figure de style est présente dans «un amandier vénérable plus haut que tous les autres» ?",
        options: ["Une antithèse", "Une hyperbole", "Un oxymore", "Une anaphore"],
        correct: 1,
        feedback: "«plus haut que tous les autres» est une hyperbole qui amplifie la grandeur de l'arbre."
      }
    ],
    production: {
      sujet: "Racontez un rêve (réel ou imaginaire) qui vous a marqué(e). Décrivez-le et expliquez quelle signification vous lui accordez. (150-200 mots)",
      outils: {
        "Vocabulaire du rêve": ["rêver de", "songer à", "avoir une vision", "se retrouver dans", "apparaître", "disparaître"],
        "Temps verbaux": ["imparfait (description)", "passé composé (actions)", "conditionnel (interprétation)"],
        "Connecteurs narratifs": ["soudain", "tout à coup", "au moment où", "alors", "c'est alors que"],
        "Verbes de sentiment": ["troubler", "fasciner", "effrayer", "intriguer", "éveiller", "hanter"]
      }
    }
  },

  // EXAMEN 5
  {
    id: 5,
    title: "La cuisine et les repas",
    theme: "La gastronomie traditionnelle comme rituel de vie et de partage",
    meta: { niveau: "1ère année lycée", durée: "45 min", compétence: "Compréhension & vocabulaire" },
    textSupport: `Après avoir mis un énorme quignon à cuire sous la cendre, la vieille femme allumait un brasero et attendait que les braises soient bien rouges pour placer dessus un récipient de terre dans lequel elle préparait soigneusement le mets. Elle obtenait un petit-lait légèrement aigrelet qu'elle parfumait d'une pincée de thym moulu et de quelques gouttes d'huile d'argan. Le couscous d'orge aux légumes de saison passait bien avec cela.`,
    questions: [
      {
        type: "qcm",
        text: "Comment la vieille faisait-elle cuire le pain ?",
        options: ["Dans un four en brique", "Sous la cendre", "Sur une plaque de métal", "Dans un tajine"],
        correct: 1,
        feedback: "«Après avoir mis un énorme quignon à cuire sous la cendre.»"
      },
      {
        type: "vf",
        text: "La vieille utilisait un récipient en métal pour préparer le mets.",
        correct: false,
        feedback: "Faux : «un récipient de terre» — c'est donc de la poterie traditionnelle."
      },
      {
        type: "qcm",
        text: "Comment la vieille parfumait-elle le petit-lait ?",
        options: ["Avec de la cannelle et du miel", "Avec du thym moulu et de l'huile d'argan", "Avec du cumin et de l'ail", "Avec de la menthe fraîche"],
        correct: 1,
        feedback: "«elle parfumait d'une pincée de thym moulu et de quelques gouttes d'huile d'argan»."
      },
      {
        type: "vf",
        text: "Le couscous d'orge était accompagné de viande.",
        correct: false,
        feedback: "Faux : «Un couscous sans viande que le vieux couple appréciait par-dessus tout.»"
      },
      {
        type: "qcm",
        text: "Pour la corvée d'eau, la vieille allait au puits :",
        options: ["Une fois par jour", "Deux fois le matin", "Trois fois par semaine", "Le soir uniquement"],
        correct: 1,
        feedback: "«Pour la corvée d'eau, la vieille allait au puits deux fois le matin.»"
      },
      {
        type: "fill",
        text: "À son retour du puits, la vieille arrosait un massif de ___ et d'___ dont elle découpait quelques tiges pour le thé.",
        blanks: ["menthe", "absinthe"],
        feedback: "«elle ne manquait jamais d'arroser copieusement un massif de menthe et d'absinthe»."
      },
      {
        type: "qcm",
        text: "Que produisait la vache de la vieille femme ?",
        options: ["De la laine", "Un bon lait", "De la viande", "Du fumier uniquement"],
        correct: 1,
        feedback: "«Elle produisait un bon lait que la maîtresse de maison barattait dès la traite matinale.»"
      },
      {
        type: "vf",
        text: "Le couple mangeait de la viande tous les jours.",
        correct: false,
        feedback: "Faux : «le vieux couple mangeait de la viande plusieurs fois par mois» — pas tous les jours."
      },
      {
        type: "qcm",
        text: "Qui assistait au rituel de la préparation du tagine ?",
        options: ["Les voisins", "Le fqih", "Le chat de la maison", "L'âne"],
        correct: 2,
        feedback: "«Seul le chat de la maison y assistait car il était tout aussi intéressé que le vieux couple.»"
      },
      {
        type: "qcm",
        text: "Quel bruit rompait le calme crépusculaire évoqué dans le texte ?",
        options: ["Le chant des voisins", "Le bruit des bêtes par intermittence", "Le son de la radio", "Le vent dans les arbres"],
        correct: 1,
        feedback: "«que seul le bruit des bêtes rompait par intermittence»."
      }
    ],
    production: {
      sujet: "Décrivez la préparation d'un plat traditionnel de votre région. Présentez les ingrédients, les étapes et la signification culturelle de ce mets. (150-200 mots)",
      outils: {
        "Vocabulaire culinaire": ["mélanger", "mijoter", "assaisonner", "parfumer", "cuire", "préparer", "servir"],
        "Connecteurs d'étapes": ["d'abord", "ensuite", "puis", "après avoir", "une fois que", "enfin"],
        "Adjectifs sensoriels": ["savoureux", "parfumé", "doré(e)", "croustillant(e)", "fondant(e)", "généreux/se"],
        "Expressions de tradition": ["de génération en génération", "selon la tradition", "un héritage culinaire", "un rituel familial"]
      }
    }
  },

  // EXAMEN 6
  {
    id: 6,
    title: "La résistance et l'histoire",
    theme: "L'engagement patriotique et la résistance à l'occupation coloniale",
    meta: { niveau: "Terminale", durée: "55 min", compétence: "Compréhension approfondie" },
    textSupport: `Un Mokhazni armé d'un M.A.S. 36 était venu ce jour-là à la mosquée en compagnie du Mokaddem. Il exhibait une liste de noms de gens recherchés à Casablanca pour faits de résistance. Dans toutes les villes du Nord, la résistance à l'occupation était très active. Il y avait des attentats à la bombe, des rafles massives et des exécutions sommaires. Bouchaïb répondit : «Non! On ne les a pas vus ici depuis des années.»`,
    questions: [
      {
        type: "qcm",
        text: "Qu'est-ce qu'un «Mokhazni» dans le contexte du texte ?",
        options: ["Un professeur religieux", "Un soldat ou agent de l'autorité coloniale", "Un chef tribal", "Un commerçant"],
        correct: 1,
        feedback: "Le Mokhazni est un agent armé représentant l'autorité — ici au service du protectorat."
      },
      {
        type: "vf",
        text: "Les personnes recherchées avaient commis des délits criminels de droit commun.",
        correct: false,
        feedback: "Faux : ils étaient recherchés «pour faits de résistance» — c'est une lutte politique."
      },
      {
        type: "qcm",
        text: "Comment Bouchaïb réagit-il face au Mokhazni qui cherchait les résistants ?",
        options: ["Il les dénonce", "Il dit ne pas les avoir vus", "Il fuit le village", "Il appelle les autres habitants"],
        correct: 1,
        feedback: "«Non! On ne les a pas vus ici depuis des années», dit Bouchaïb pour protéger les résistants."
      },
      {
        type: "qcm",
        text: "Quel sobriquet désigne Bouchaïb dans sa fonction sociale ?",
        options: ["Le Cheik", "L'Anflouss", "Le fqih", "Le Mokaddem"],
        correct: 1,
        feedback: "La note précise : «Anflouss : policier de village»."
      },
      {
        type: "vf",
        text: "Le Cheik du village collaborait activement avec les autorités coloniales.",
        correct: false,
        feedback: "Faux : «Le Cheik était lui-même un résistant notoire, il militait pour l'indépendance.»"
      },
      {
        type: "fill",
        text: "Les résistants répondaient : «Quand on est dans la ___, on est ___».",
        blanks: ["montagne", "insaisissable"],
        feedback: "«Quand on est dans la montagne, on est insaisissable», dirent les résistants."
      },
      {
        type: "qcm",
        text: "Qui étaient Zerktouni et Allal ben Abdallah mentionnés dans le texte ?",
        options: ["Des traîtres", "Des feddaïns (résistants) morts en héros", "Des soldats français", "Des marchands"],
        correct: 1,
        feedback: "«les feddaïns payaient de leur vie leurs exploits. Comme Zerktouni ou Allal ben Abdallah.»"
      },
      {
        type: "vf",
        text: "Les commerçants nationalistes qui aidaient la résistance étaient tous arrêtés.",
        correct: false,
        feedback: "Faux : «on ne pouvait pas les arrêter car ils s'étaient fondus dans la nature»."
      },
      {
        type: "qcm",
        text: "Comment Bouchaïb évoque-t-il cette période de résistance par la suite ?",
        options: ["Avec amertume et regret", "Avec enthousiasme, comme une époque d'honneur", "Avec indifférence", "Avec honte"],
        correct: 1,
        feedback: "«Cette époque était celle de l'enthousiasme, du sacrifice et de l'honneur.»"
      },
      {
        type: "qcm",
        text: "Que révèle l'attitude de Bouchaïb face au Mokhazni ?",
        options: ["Sa peur des autorités", "Son courage et sa solidarité patriotique", "Son ignorance de la situation", "Son désintérêt pour la politique"],
        correct: 1,
        feedback: "En protégeant les résistants, Bouchaïb fait preuve de courage civique et de solidarité nationale."
      }
    ],
    production: {
      sujet: "Rédigez un texte sur l'importance de la mémoire collective dans la préservation de l'identité nationale. Appuyez-vous sur des exemples historiques ou personnels. (150-200 mots)",
      outils: {
        "Lexique de la résistance": ["sacrifier", "s'engager", "défendre", "résister", "lutter", "militer", "honorer"],
        "Lexique de la mémoire": ["se souvenir", "commémorer", "transmettre", "perpétuer", "témoigner", "préserver"],
        "Connecteurs argumentatifs": ["en effet", "c'est pourquoi", "or", "cependant", "ainsi", "par conséquent"],
        "Expressions clés": ["la mémoire collective", "un devoir de mémoire", "l'identité nationale", "un héritage historique"]
      }
    }
  },

  // EXAMEN 7
  {
    id: 7,
    title: "Les ruines et la vallée",
    theme: "La disparition d'un monde rural et les transformations sociales",
    meta: { niveau: "Terminale", durée: "55 min", compétence: "Analyse & style" },
    textSupport: `Qu'y a-t-il de plus fascinant et de plus inquiétant que des ruines récentes qui furent des demeures qu'on avait connues? Ces maisons de pierre sèche, bâties sur le flanc du roc, ne sont plus qu'un triste amas de décombres, domaine incontesté des reptiles, des arachnides, des rongeurs et des myriapodes. Une de ces ruines dresse des pans de murs difformes par-dessus un buisson touffus de ronces et de nopals et quelques amandiers vieux et squelettiques.`,
    questions: [
      {
        type: "qcm",
        text: "De quelle nature sont les maisons décrites dans le texte ?",
        options: ["Des villas modernes en béton", "Des maisons de pierre sèche", "Des tentes nomades", "Des demeures en bois"],
        correct: 1,
        feedback: "«Ces maisons de pierre sèche, bâties sur le flanc du roc.»"
      },
      {
        type: "vf",
        text: "Le texte décrit ces ruines avec un sentiment de nostalgie et d'inquiétude.",
        correct: true,
        feedback: "Vrai : «Qu'y a-t-il de plus fascinant et de plus inquiétant que des ruines récentes?»"
      },
      {
        type: "qcm",
        text: "Quels animaux occupent désormais ces ruines ?",
        options: ["Des chats et des chiens errants", "Des reptiles, arachnides, rongeurs et myriapodes", "Des oiseaux migrateurs", "Des chèvres et des moutons"],
        correct: 1,
        feedback: "«domaine incontesté des reptiles, des arachnides, des rongeurs et des myriapodes.»"
      },
      {
        type: "qcm",
        text: "Par quoi les ruines étaient-elles remplacées dans la vallée ?",
        options: ["Par des fermes modernes", "Par des villas somptueuses et complexes ultramodernes", "Par des mosquées neuves", "Par des écoles"],
        correct: 1,
        feedback: "«villas somptueuses, palais et complexes ultramodernes copies conformes des bâtiments riches des grandes mégapoles du Nord.»"
      },
      {
        type: "vf",
        text: "Le narrateur admire sans réserve les nouvelles constructions modernes.",
        correct: false,
        feedback: "Faux : l'expression «copies conformes» est péjorative — le narrateur critique ce mimétisme architectural."
      },
      {
        type: "fill",
        text: "La vallée vivait autrefois au ___ des saisons du labeur des hommes qui ne négligeaient pas la moindre ___ de terre.",
        blanks: ["rythme", "parcelle"],
        feedback: "«la vallée vivait au rythme des saisons du labeur des hommes qui ne négligeaient pas la moindre parcelle de terre.»"
      },
      {
        type: "qcm",
        text: "Quelle figure de style est «amandiers vieux et squelettiques» ?",
        options: ["Une métaphore", "Une personnification", "Une comparaison", "Une métonymie"],
        correct: 1,
        feedback: "«Squelettiques» est une personnification : on attribue aux arbres une caractéristique humaine/animale."
      },
      {
        type: "qcm",
        text: "Que symbolisent les ruines dans le texte ?",
        options: ["La prospérité future", "La fin d'un monde traditionnel", "La victoire des modernistes", "L'abandon des croyances"],
        correct: 1,
        feedback: "Les ruines symbolisent la disparition d'un mode de vie ancestral et communautaire."
      },
      {
        type: "vf",
        text: "Les peuples des montagnes vivaient autrefois dans la paix absolue.",
        correct: false,
        feedback: "Faux : «Ces peuples des montagnes n'avaient connu que des guerres, des vendettas.»"
      },
      {
        type: "qcm",
        text: "Quel procédé stylistique caractérise l'ouverture du roman (question rhétorique) ?",
        options: ["Une exclamation", "Une interrogation rhétorique", "Une interjection", "Une apostrophe"],
        correct: 1,
        feedback: "«Qu'y a-t-il de plus fascinant et de plus inquiétant...» est une interrogation rhétorique pour interpeller le lecteur."
      }
    ],
    production: {
      sujet: "Décrivez les transformations d'un lieu que vous connaissez (village, quartier, ville). Comparez le passé et le présent en exprimant votre sentiment face à ces changements. (150-200 mots)",
      outils: {
        "Vocabulaire de la comparaison": ["autrefois / aujourd'hui", "jadis / désormais", "avant / maintenant", "d'antan / actuel"],
        "Verbes d'évolution": ["disparaître", "remplacer", "transformer", "abandonner", "rénover", "préserver"],
        "Expressions nostalgiques": ["il fut un temps où", "dans ma mémoire", "je me souviens encore", "ce qui reste de"],
        "Registres stylistiques": ["descriptif (imparfait)", "comparatif", "argumentatif (présent)", "nostalgique"]
      }
    }
  },

  // EXAMEN 8
  {
    id: 8,
    title: "La philosophie du vieillard",
    theme: "La sagesse face à la vieillesse, la mort et l'absence d'héritiers",
    meta: { niveau: "Terminale", durée: "55 min", compétence: "Analyse & argumentation" },
    textSupport: `«C'est ailleurs que je recommencerai une autre jeunesse, ailleurs qu'aura lieu le nouveau départ. Ici, c'est fini. Mais est-ce qu'il est permis de se reproduire au Paradis?» Il n'avait donc aucun regret, pas la moindre amertume. Il se sentait en paix avec son âme, heureux et totalement éloigné de certaines vanités terrestres comme de posséder une nichée bruyante et batailleuse.`,
    questions: [
      {
        type: "qcm",
        text: "Comment le Vieux vit-il son absence d'enfants ?",
        options: ["Avec une profonde tristesse", "Avec sérénité et philosophie", "Avec jalousie envers les autres", "Avec colère contre Dieu"],
        correct: 1,
        feedback: "«Il n'avait donc aucun regret, pas la moindre amertume. Il se sentait en paix avec son âme.»"
      },
      {
        type: "vf",
        text: "Le Vieux enviait les pères de famille nombreuse.",
        correct: false,
        feedback: "Faux : «Il n'avait donc jamais envié les pères de famille nombreuse.»"
      },
      {
        type: "qcm",
        text: "Que veut dire «vanités terrestres» dans ce contexte ?",
        options: ["Les richesses matérielles inutiles", "Les ambitions superficielles de ce monde", "Les plaisirs des repas", "Les voyages lointains"],
        correct: 1,
        feedback: "Les «vanités terrestres» désignent les désirs superficiels et passagers de la vie mondaine."
      },
      {
        type: "vf",
        text: "Le Vieux croit en une vie après la mort.",
        correct: true,
        feedback: "Vrai : «C'est ailleurs que je recommencerai une autre jeunesse» — il croit au Paradis."
      },
      {
        type: "qcm",
        text: "Que pense le Vieux du sort des familles nombreuses pauvres ?",
        options: ["Il les admire pour leur courage", "Il pense qu'elles répètent un processus de misère", "Il leur offre son aide", "Il les ignore complètement"],
        correct: 1,
        feedback: "«ils répéteraient fatalement le même processus de misère en ce monde frénétique et dur.»"
      },
      {
        type: "fill",
        text: "Le Vieux dit : «On est venu tout ___, on repart tout ___».",
        blanks: ["nu", "nu"],
        feedback: "«On est venu tout nu, on repart tout nu.» — une phrase qui résume sa philosophie de vie."
      },
      {
        type: "qcm",
        text: "Quelle est la tonalité dominante du discours philosophique du Vieux ?",
        options: ["Tragique et désespérée", "Résignée mais sereine", "Révoltée et rebelle", "Indifférente et froide"],
        correct: 1,
        feedback: "Le Vieux accepte sa situation avec sagesse et sérénité — une résignation positive."
      },
      {
        type: "qcm",
        text: "Où partaient les jeunes des familles nombreuses qui quittaient le village ?",
        options: ["En Europe uniquement", "Dans des bidonvilles du Nord ou en Europe comme mineurs", "Dans d'autres villages marocains", "À La Mecque pour le pèlerinage"],
        correct: 1,
        feedback: "«Beaucoup quittaient le pays et allaient s'échouer dans un quelconque bidonville du Nord. Les plus chanceux étaient engagés en Europe comme mineurs de fond.»"
      },
      {
        type: "vf",
        text: "La vieille femme partage la philosophie sereine de son mari.",
        correct: true,
        feedback: "Vrai : «moi, je suis une grand-mère sans petits-enfants, mais je suis heureuse», dit-elle."
      },
      {
        type: "qcm",
        text: "Quel est le genre littéraire de cette œuvre selon la page de titre ?",
        options: ["Un roman", "Un recueil de poèmes", "Un récit", "Une pièce de théâtre"],
        correct: 2,
        feedback: "La couverture précise : «récit» — ce n'est pas un roman classique."
      }
    ],
    production: {
      sujet: "Que pensez-vous de la sagesse du Vieux face à l'absence d'héritiers et à la mort ? Rédigez un texte argumentatif où vous défendez votre point de vue. (150-200 mots)",
      outils: {
        "Lexique de la sagesse": ["la sérénité", "l'acceptation", "la philosophie", "la résilience", "la paix intérieure"],
        "Verbes d'opinion": ["je pense que", "il me semble que", "j'estime que", "selon moi", "à mon avis"],
        "Connecteurs d'argumentation": ["premièrement", "de plus", "certes", "cependant", "en conclusion"],
        "Expressions philosophiques": ["la condition humaine", "le sens de la vie", "l'essentiel", "les vraies valeurs"]
      }
    }
  },

  // EXAMEN 9
  {
    id: 9,
    title: "La chasse et la nature",
    theme: "La relation de l'homme avec la nature et les animaux sauvages",
    meta: { niveau: "1ère année lycée", durée: "45 min", compétence: "Vocabulaire & compréhension" },
    textSupport: `«Ce soir, j'irai mettre des pièges. On mangera du lièvre demain.» Il avait plusieurs assortiments de pièges et il savait où les tendre pour capturer tel ou tel gibier. Il aimait bien la chair du porc-épic, mais il lui préférait celle du lièvre, qui sentait bon les aromates. Et c'est sans surprise que le lendemain à l'aube il rapporta deux lièvres qu'ils dégustèrent, sa femme et lui, le soir même sur la terrasse.`,
    questions: [
      {
        type: "qcm",
        text: "Quelle viande le Vieux préférait-il entre le porc-épic et le lièvre ?",
        options: ["Le porc-épic", "Le lièvre", "Les deux également", "Ni l'un ni l'autre"],
        correct: 1,
        feedback: "«Il aimait bien la chair du porc-épic, mais il lui préférait celle du lièvre.»"
      },
      {
        type: "vf",
        text: "Le Vieux utilisait une carabine pour chasser.",
        correct: false,
        feedback: "Faux : il utilisait des pièges — «Il avait plusieurs assortiments de pièges.»"
      },
      {
        type: "qcm",
        text: "Combien de lièvres le Vieux rapporta-t-il le lendemain ?",
        options: ["Un", "Deux", "Trois", "Quatre"],
        correct: 1,
        feedback: "«le lendemain à l'aube il rapporta deux lièvres.»"
      },
      {
        type: "vf",
        text: "Le chat de la maison eut aussi une part du gibier.",
        correct: true,
        feedback: "Vrai : «Le chat eut une grosse part.»"
      },
      {
        type: "qcm",
        text: "Pourquoi le piège posé contre le chat sauvage avait-il échoué une fois ?",
        options: ["Le piège était trop petit", "C'est le coq blanc qui avait été pris", "Le chat avait sauté par-dessus", "Le piège s'était cassé"],
        correct: 1,
        feedback: "«Au lieu de ce maudit chat, c'est le coq blanc, ton préféré, qui a été pris.»"
      },
      {
        type: "fill",
        text: "La vieille donna une partie du gibier à la ___, qui ne mangeait de la viande qu'une fois l'an, à l'occasion de l'___.",
        blanks: ["voisine", "Aïd"],
        feedback: "«J'ai donné un peu de ce gibier à la voisine [...] Elle ne mange pratiquement pas de viande. Une fois l'an peut-être, à l'occasion de l'Aïd.»"
      },
      {
        type: "qcm",
        text: "Quel problème causait un chat sauvage au couple ?",
        options: ["Il volait la nourriture", "Il égorgeait les poules pondeuses", "Il effrayait la vache", "Il déchirait le tapis"],
        correct: 1,
        feedback: "«un chat sauvage égorgeait depuis peu» les poules bonnes pondeuses."
      },
      {
        type: "vf",
        text: "Le Vieux connaissait précisément l'endroit où tendre chaque type de piège.",
        correct: true,
        feedback: "Vrai : «il savait où les tendre pour capturer tel ou tel gibier.»"
      },
      {
        type: "qcm",
        text: "Comment le Vieux résout-il le problème du chat sauvage ?",
        options: ["En posant le piège là où la volaille ne peut aller", "En achetant un chien de garde", "En construisant un enclos fermé", "En alertant les voisins"],
        correct: 0,
        feedback: "«Je mettrai le piège où la volaille ne peut pas aller, c'est tout. J'ai mon idée là-dessus.»"
      },
      {
        type: "qcm",
        text: "Le lièvre était apprécié pour son goût car il sentait :",
        options: ["La fumée et le bois", "Les aromates", "L'huile d'argan", "La menthe fraîche"],
        correct: 1,
        feedback: "«il lui préférait celle du lièvre, qui sentait bon les aromates.»"
      }
    ],
    production: {
      sujet: "Décrivez votre relation avec la nature et les animaux. Partagez-vous ou critiquez-vous la pratique de la chasse traditionnelle ? Argumentez votre position. (150-200 mots)",
      outils: {
        "Vocabulaire de la nature": ["la faune", "la flore", "l'écosystème", "la biodiversité", "le gibier", "les prédateurs"],
        "Vocabulaire de la chasse": ["les pièges", "capturer", "chasser", "traquer", "la proie", "le chasseur"],
        "Connecteurs d'opposition": ["certes", "cependant", "néanmoins", "d'un côté… de l'autre", "même si"],
        "Verbes de position": ["défendre", "critiquer", "approuver", "rejeter", "nuancer", "reconnaître"]
      }
    }
  },

  // EXAMEN 10
  {
    id: 10,
    title: "Les dialogues du couple",
    theme: "La communication et la complicité dans un couple âgé",
    meta: { niveau: "2ème année lycée", durée: "50 min", compétence: "Analyse des dialogues" },
    textSupport: `– À quoi penses-tu donc ? dit-elle.\nIl ne répondit pas tout de suite. Il s'écoula un bon moment puis il dit:\n– À quoi je pense ? Eh bien, à tous ces gens qui ont trop d'enfants et qui ne peuvent même pas les nourrir.\n– Eh bien, moi, je suis une grand-mère sans petits-enfants, mais je suis heureuse.\n– C'est ce que je pense moi-même. Sers-nous donc à dîner. Non, attends un peu ! Je dois d'abord faire ma prière.`,
    questions: [
      {
        type: "qcm",
        text: "Qui initie la conversation dans ce passage ?",
        options: ["Le Vieux", "La vieille femme", "Le chat", "Un voisin"],
        correct: 1,
        feedback: "C'est la vieille femme qui pose la première question : «À quoi penses-tu donc ?»"
      },
      {
        type: "vf",
        text: "Le Vieux répond immédiatement à la question de sa femme.",
        correct: false,
        feedback: "Faux : «Il ne répondit pas tout de suite. Il s'écoula un bon moment.»"
      },
      {
        type: "qcm",
        text: "À quoi pensait le Vieux selon sa réponse ?",
        options: ["À sa jeunesse et ses voyages", "Aux gens qui ont trop d'enfants et ne peuvent les nourrir", "À la mort prochaine", "À la récolte annuelle"],
        correct: 1,
        feedback: "«À tous ces gens qui ont trop d'enfants et qui ne peuvent même pas les nourrir.»"
      },
      {
        type: "vf",
        text: "La vieille exprime de la tristesse à propos de son absence d'enfants.",
        correct: false,
        feedback: "Faux : elle dit «je suis heureuse» malgré cette situation."
      },
      {
        type: "qcm",
        text: "Que fait le Vieux avant de dîner ?",
        options: ["Il lave les mains", "Il fait sa prière", "Il donne à manger à l'âne", "Il allume une lampe"],
        correct: 1,
        feedback: "«Non, attends un peu ! Je dois d'abord faire ma prière.»"
      },
      {
        type: "fill",
        text: "La femme dit : «Je suis une ___-___ sans petits-enfants, mais je suis ___».",
        blanks: ["grand", "mère", "heureuse"],
        feedback: "«moi, je suis une grand-mère sans petits-enfants, mais je suis heureuse.»"
      },
      {
        type: "qcm",
        text: "De quoi la vieille entretient-elle son mari après le dîner ?",
        options: ["Des moissons à venir", "De la vache, des poules et du chat sauvage", "Des voisins et du souk", "De la mosquée et du fqih"],
        correct: 1,
        feedback: "«Elle l'entretint de la vache, de ses poules bonnes pondeuses, qu'un chat sauvage égorgeait depuis peu.»"
      },
      {
        type: "vf",
        text: "Les repas du couple sont des moments de silence total.",
        correct: false,
        feedback: "Faux : «Ils mangèrent calmement en devisant» — ils parlaient pendant le repas."
      },
      {
        type: "qcm",
        text: "Quelle image du couple ce dialogue donne-t-il au lecteur ?",
        options: ["Un couple en conflit", "Un couple uni, complice et philosophe", "Un couple indifférent l'un à l'autre", "Un couple séparé par leurs rôles"],
        correct: 1,
        feedback: "Leur échange révèle une profonde complicité, un partage de valeurs et de sérénité."
      },
      {
        type: "qcm",
        text: "Que dit le Vieux du tagine de sa femme ?",
        options: ["«Il est trop salé»", "«Ton tagine est fameux. Et le pain aussi.»", "«Il manque de légumes»", "«C'est le meilleur du village»"],
        correct: 1,
        feedback: "«Ton tagine est fameux. Et le pain aussi.» — il complimente sa femme simplement."
      }
    ],
    production: {
      sujet: "Rédigez un dialogue entre deux personnes âgées qui évoquent leurs souvenirs, leur bonheur simple et leur vision de la vie. Le dialogue doit être naturel et révéler leurs caractères. (150-200 mots)",
      outils: {
        "Verbes introducteurs de dialogue": ["dit-il/elle", "répondit", "demanda", "s'exclama", "murmura", "ajouta"],
        "Ponctuation du dialogue": ["tiret long (–)", "guillemets (« »)", "deux-points (:)", "virgule après le verbe"],
        "Expressions de la complicité": ["nous nous comprenons", "comme tu le sais", "entre nous", "tu as raison"],
        "Thèmes à aborder": ["les souvenirs communs", "les projets futurs", "la gratitude", "l'humour bienveillant"]
      }
    }
  },

  // EXAMEN 11
  {
    id: 11,
    title: "L'auteur et son œuvre",
    theme: "Biographie de Mohammed Khaïr-Eddine et contexte de l'œuvre",
    meta: { niveau: "Terminale", durée: "55 min", compétence: "Culture littéraire" },
    textSupport: `Né en 1941, à Trafraout, dans le Sud marocain. Après des études secondaires à Casablanca, il travailla un temps dans la fonction publique, avant de se consacrer à l'écriture. Il publia ses premiers poèmes dans La Vigie marocaine avant de collaborer dans les années 60 à la revue Souffles. Il s'installa en France en 1966, et publia, l'année suivante, Agadir (Seuil). Mohammed Khaïr-Eddine retourna au Maroc en 1993, où il mourut deux ans plus tard, à Rabat.`,
    questions: [
      {
        type: "qcm",
        text: "Dans quelle ville Mohammed Khaïr-Eddine est-il né ?",
        options: ["Casablanca", "Rabat", "Trafraout", "Agadir"],
        correct: 2,
        feedback: "«Né en 1941, à Trafraout, dans le Sud marocain.»"
      },
      {
        type: "vf",
        text: "Khaïr-Eddine a commencé sa carrière littéraire par des romans.",
        correct: false,
        feedback: "Faux : «Il publia ses premiers poèmes dans La Vigie marocaine» — il a débuté par la poésie."
      },
      {
        type: "qcm",
        text: "À quelle revue marocaine Khaïr-Eddine collabora-t-il dans les années 60 ?",
        options: ["Lamalif", "Souffles", "Anfas", "Al Thaqafa Al Jadida"],
        correct: 1,
        feedback: "«collaborer dans les années 60 à la revue Souffles qu'animait le poète Abdelatif Laabi.»"
      },
      {
        type: "qcm",
        text: "Quel est le premier roman publié par Khaïr-Eddine chez Seuil ?",
        options: ["Moi l'Aigre", "Soleil arachnide", "Agadir", "Le Déterreur"],
        correct: 2,
        feedback: "«Il s'installa en France en 1966, et publia, l'année suivante, Agadir (Seuil).»"
      },
      {
        type: "vf",
        text: "Khaïr-Eddine est mort en France.",
        correct: false,
        feedback: "Faux : «il mourut deux ans plus tard, à Rabat» — il est mort au Maroc."
      },
      {
        type: "fill",
        text: "Son dernier recueil de poèmes, ___, a paru au Cherche-midi éditeur en ___.",
        blanks: ["Mémorial", "1991"],
        feedback: "«Son dernier recueil de poèmes, Mémorial, a paru au Cherche-midi éditeur en 1991.»"
      },
      {
        type: "qcm",
        text: "En quelle année Khaïr-Eddine s'installa-t-il en France ?",
        options: ["1960", "1966", "1970", "1975"],
        correct: 1,
        feedback: "«Il s'installa en France en 1966.»"
      },
      {
        type: "qcm",
        text: "Quel éditeur a publié la plupart des œuvres de Khaïr-Eddine ?",
        options: ["Gallimard", "Le Seuil", "Flammarion", "Albin Michel"],
        correct: 1,
        feedback: "La plupart de ses œuvres sont parues «chez le même éditeur», Le Seuil."
      },
      {
        type: "vf",
        text: "Khaïr-Eddine retourna au Maroc avant sa mort.",
        correct: true,
        feedback: "Vrai : «Mohammed Khaïr-Eddine retourna au Maroc en 1993, où il mourut deux ans plus tard.»"
      },
      {
        type: "qcm",
        text: "«Il était une fois un vieux couple heureux» appartient au genre :",
        options: ["Roman policier", "Récit autobiographique", "Récit littéraire", "Nouvelle fantastique"],
        correct: 2,
        feedback: "La couverture indique «récit» — une forme narrative entre roman et autobiographie."
      }
    ],
    production: {
      sujet: "Rédigez une courte présentation d'un(e) auteur(e) marocain(e) ou maghrébin(e) que vous appréciez : sa biographie, ses œuvres majeures et les thèmes qu'il/elle aborde. (150-200 mots)",
      outils: {
        "Connecteurs chronologiques": ["né(e) en", "en", "après", "puis", "ensuite", "enfin", "jusqu'à sa mort"],
        "Vocabulaire biographique": ["auteur", "écrivain", "romancier/ère", "poète", "œuvre", "publication", "carrière"],
        "Verbes de biographie": ["naître", "étudier", "publier", "s'installer", "mourir", "collaborer", "consacrer"],
        "Structure de présentation": ["introduction (qui?)", "formation", "œuvres principales", "thèmes", "importance littéraire"]
      }
    }
  },

  // EXAMEN 12
  {
    id: 12,
    title: "Bilan général de l'œuvre",
    theme: "Synthèse thématique et stylistique du récit",
    meta: { niveau: "Terminale", durée: "60 min", compétence: "Synthèse & production écrite" },
    textSupport: `Le vieux couple symbolise une sagesse ancestrale face aux transformations du monde moderne. Bouchaïb et sa femme incarnent un art de vivre fondé sur la foi, la simplicité, l'harmonie avec la nature et la communauté. Leur vie quotidienne, leurs dialogues, leurs liens avec les voisins comme Talouqit, et leurs réflexions philosophiques sur la mort, le Paradis et la condition humaine font de ce récit une œuvre à la fois intime et universelle.`,
    questions: [
      {
        type: "qcm",
        text: "Quel est le thème central de l'œuvre ?",
        options: ["La résistance coloniale uniquement", "La vie simple et sage d'un vieux couple dans un village marocain", "Une aventure policière dans le Nord", "Un voyage initiatique en Europe"],
        correct: 1,
        feedback: "L'œuvre tourne autour de la vie quotidienne et philosophique de Bouchaïb et sa femme."
      },
      {
        type: "vf",
        text: "Le récit oppose clairement un monde traditionnel positif à un monde moderne négatif.",
        correct: true,
        feedback: "Vrai : le texte valorise la vie simple et critique le mimétisme des «copies conformes des mégapoles du Nord»."
      },
      {
        type: "qcm",
        text: "Quel animal accompagne symboliquement le couple dans leur vie quotidienne ?",
        options: ["Le coq blanc", "L'âne, la vache et le chat", "Le cheval de labour", "La chèvre laitière"],
        correct: 1,
        feedback: "L'âne (fidèle compagnon), la vache (nourricière) et le chat (compagnon domestique) jouent un rôle central."
      },
      {
        type: "qcm",
        text: "Quelle dimension religieuse traverse tout le récit ?",
        options: ["Une pratique religieuse rigoriste et fermée", "Une foi sereine intégrée naturellement dans la vie quotidienne", "Un conflit entre foi et raison", "Un rejet de la religion traditionnelle"],
        correct: 1,
        feedback: "La prière, la mosquée, le Paradis sont évoqués simplement, naturellement — pas de façon dogmatique."
      },
      {
        type: "vf",
        text: "L'écriture de Khaïr-Eddine dans ce récit est difficile et hermétique.",
        correct: false,
        feedback: "Faux : malgré la richesse du vocabulaire, le style est fluide, narratif et accessible."
      },
      {
        type: "fill",
        text: "Le vieux couple est présenté comme «___ sans descendance qui n'attirait guère l'___ car il vivait en ___».",
        blanks: ["couple âgé", "attention", "silence"],
        feedback: "«Elle avait été la demeure d'un couple âgé sans descendance qui n'attirait guère l'attention car il vivait en silence.»"
      },
      {
        type: "qcm",
        text: "Quel est le rôle de la figure féminine (la vieille) dans le récit ?",
        options: ["Un personnage passif et effacé", "Un pilier de la maison, complice du Vieux, sage et active", "Une figure de conflit conjugal", "Un personnage secondaire sans importance"],
        correct: 1,
        feedback: "Elle gère la maison, participe aux dialogues philosophiques, exprime sa joie de vivre — elle est essentielle."
      },
      {
        type: "qcm",
        text: "Comment Khaïr-Eddine ancre-t-il son récit dans la réalité marocaine ?",
        options: ["Par des références mythologiques grecques", "Par des noms de lieux, personnages historiques et coutumes locales", "Par des allusions à la littérature française", "Par des descriptions géographiques vagues"],
        correct: 1,
        feedback: "Tafraout, Mazagan, les moussems, Sidi Hmad Ou Moussa, l'arabe et le berbère ancrent le récit dans le Maroc réel."
      },
      {
        type: "vf",
        text: "Le récit a une structure linéaire simple sans profondeur philosophique.",
        correct: false,
        feedback: "Faux : les dialogues, le rêve, les réflexions sur la mort et le Paradis donnent au récit une profonde dimension philosophique."
      },
      {
        type: "qcm",
        text: "Quelle est la valeur universelle du récit ?",
        options: ["Il parle uniquement de la culture berbère du Souss", "Il traite de l'exil marocain en France", "Il célèbre la dignité humaine, la sagesse et le bonheur dans la simplicité", "Il critique l'islam traditionnel"],
        correct: 2,
        feedback: "La dignité, la sagesse, l'amour conjugal et le bonheur simple résonnent universellement au-delà du contexte marocain."
      }
    ],
    production: {
      sujet: "Rédigez une synthèse du récit *Il était une fois un vieux couple heureux* en présentant les personnages, les thèmes majeurs et le message de l'œuvre. Donnez votre avis personnel sur le texte. (200-250 mots)",
      outils: {
        "Vocabulaire de synthèse": ["l'œuvre aborde", "l'auteur met en lumière", "le récit illustre", "on peut noter que", "en conclusion"],
        "Présentation de thèmes": ["le thème de", "la question de", "l'enjeu central", "la problématique de"],
        "Verbes d'analyse": ["symboliser", "représenter", "illustrer", "incarner", "révéler", "souligner"],
        "Donner son avis": ["ce qui me frappe", "j'ai particulièrement apprécié", "à mon sens", "ce texte m'a appris que"]
      }
    }
  }
];

// ============================
// APP STATE
// ============================
let currentExam = null;
let answers = {};
let corrected = false;

// ============================
// RENDER ENGINE
// ============================

function showWelcome() {
  document.getElementById('welcome-screen').style.display = 'block';
  document.querySelectorAll('.exam-panel').forEach(p => p.classList.remove('active'));
  currentExam = null;
  corrected = false;
  answers = {};
  document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
}

function loadExam(id) {
  const exam = EXAMS.find(e => e.id === id);
  if (!exam) return;

  currentExam = exam;
  corrected = false;
  answers = {};

  // Update nav
  document.querySelectorAll('.nav-btn').forEach(b => {
    b.classList.toggle('active', parseInt(b.dataset.id) === id);
  });

  // Hide welcome
  document.getElementById('welcome-screen').style.display = 'none';

  // Hide all panels, show correct one
  document.querySelectorAll('.exam-panel').forEach(p => p.classList.remove('active'));
  const panel = document.getElementById(`exam-${id}`);
  if (!panel) {
    renderExamPanel(exam);
    document.getElementById(`exam-${id}`).classList.add('active');
  } else {
    resetExamPanel(panel, exam);
    panel.classList.add('active');
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function renderExamPanel(exam) {
  const container = document.getElementById('exams-container');

  const panel = document.createElement('div');
  panel.id = `exam-${exam.id}`;
  panel.className = 'exam-panel active';
  panel.innerHTML = buildExamHTML(exam);
  container.appendChild(panel);

  attachExamEvents(panel, exam);
}

function buildExamHTML(exam) {
  return `
    <div class="exam-header">
      <div class="exam-num">Examen ${exam.id} / 12</div>
      <div class="exam-title">${exam.title}</div>
      <div class="exam-meta">
        <span>📚 ${exam.meta.niveau}</span>
        <span>⏱ ${exam.meta.durée}</span>
        <span>🎯 ${exam.meta.compétence}</span>
      </div>
    </div>

    <div class="student-name-bar">
      <label class="student-name-label" for="student-name-${exam.id}">
        <span class="student-name-icon">👤</span> Nom et prénom de l'élève
      </label>
      <input
        type="text"
        id="student-name-${exam.id}"
        class="student-name-input"
        placeholder="Entrez votre nom complet ici…"
        autocomplete="name"
      >
    </div>

    <div class="text-support">
      <div class="text-support-label">Texte support</div>
      <p>${exam.textSupport.replace(/\n/g, '<br>')}</p>
    </div>

    <div class="questions-section">
      <div class="section-title">
        <span class="icon">?</span>
        Questions de compréhension (10 questions)
      </div>
      ${exam.questions.map((q, i) => buildQuestionHTML(q, i, exam.id)).join('')}

      <div class="actions">
        <button class="btn btn-primary" onclick="correctExam(${exam.id})">✓ Corriger l'examen</button>
        <button class="btn btn-secondary" onclick="resetExam(${exam.id})">↺ Réinitialiser</button>
      </div>

      <div class="score-banner" id="score-${exam.id}"></div>
      <div class="whatsapp-bar" id="wa-bar-${exam.id}" style="display:none;">
        <button class="btn btn-whatsapp" onclick="sendWhatsApp(${exam.id})">
          <svg viewBox="0 0 24 24" fill="currentColor" width="18" height="18" style="flex-shrink:0"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
          Envoyer mes réponses via WhatsApp
        </button>
        <p class="whatsapp-hint">Votre nom, score et production écrite seront envoyés au professeur.</p>
      </div>
    </div>

    <div class="production-section">
      <div class="section-title">
        <span class="icon">✍</span>
        Production écrite
      </div>
      <div class="production-theme">
        <h3>Sujet</h3>
        <p>${exam.production.sujet}</p>
      </div>
      ${buildToolboxHTML(exam.production.outils)}
      <textarea class="writing-area" id="writing-${exam.id}"
        placeholder="Rédigez votre texte ici…&#10;&#10;Pensez à structurer votre réponse : introduction, développement, conclusion."
        oninput="countWords(${exam.id})"></textarea>
      <div class="word-counter" id="wc-${exam.id}">0 mots</div>
    </div>
  `;
}

function buildQuestionHTML(q, i, examId) {
  const num = i + 1;
  let inputHTML = '';

  if (q.type === 'qcm') {
    inputHTML = `<ul class="options-list">
      ${q.options.map((opt, j) => `
        <li>
          <label class="option-label" id="opt-${examId}-${i}-${j}">
            <input type="radio" name="q-${examId}-${i}" value="${j}" onchange="recordAnswer(${examId},${i},'${j}')">
            <span>${String.fromCharCode(65+j)}) ${opt}</span>
          </label>
        </li>
      `).join('')}
    </ul>`;
  } else if (q.type === 'vf') {
    inputHTML = `<div class="tf-group">
      <button class="tf-btn" id="tf-${examId}-${i}-true" onclick="selectTF(${examId},${i},true)">✓ Vrai</button>
      <button class="tf-btn" id="tf-${examId}-${i}-false" onclick="selectTF(${examId},${i},false)">✗ Faux</button>
    </div>`;
  } else if (q.type === 'fill') {
    const parts = q.text.split('___');
    let html = '<div class="fill-blank">';
    parts.forEach((part, idx) => {
      html += `<span>${part}</span>`;
      if (idx < parts.length - 1) {
        html += `<input type="text" class="blank-input" id="fill-${examId}-${i}-${idx}"
          onchange="recordFill(${examId},${i},${idx},this.value)"
          placeholder="…">`;
      }
    });
    html += '</div>';
    inputHTML = html;
  }

  return `
    <div class="question-item" id="qi-${examId}-${i}">
      <div class="question-text"><span class="question-num">${num}</span> ${q.type === 'fill' ? '' : q.text}</div>
      ${inputHTML}
      <div class="feedback" id="fb-${examId}-${i}"></div>
    </div>
  `;
}

function buildToolboxHTML(outils) {
  const cats = Object.entries(outils);
  return `
    <div class="toolbox">
      <div class="toolbox-title">🧰 Boîte à outils</div>
      <div class="toolbox-grid">
        ${cats.map(([cat, items]) => `
          <div class="tool-category">
            <h4>${cat}</h4>
            <ul>${items.map(it => `<li>${it}</li>`).join('')}</ul>
          </div>
        `).join('')}
      </div>
    </div>
  `;
}

// ============================
// INTERACTION HANDLERS
// ============================

function recordAnswer(examId, qIndex, value) {
  if (!answers[examId]) answers[examId] = {};
  answers[examId][qIndex] = parseInt(value);
}

function selectTF(examId, qIndex, value) {
  if (!answers[examId]) answers[examId] = {};
  answers[examId][qIndex] = value;

  // Update button styles
  document.getElementById(`tf-${examId}-${qIndex}-true`).classList.toggle('selected', value === true);
  document.getElementById(`tf-${examId}-${qIndex}-false`).classList.toggle('selected', value === false);
}

function recordFill(examId, qIndex, blankIdx, value) {
  if (!answers[examId]) answers[examId] = {};
  if (!answers[examId][qIndex]) answers[examId][qIndex] = {};
  answers[examId][qIndex][blankIdx] = value.trim().toLowerCase();
}

function countWords(examId) {
  const ta = document.getElementById(`writing-${examId}`);
  const wc = document.getElementById(`wc-${examId}`);
  const text = ta.value.trim();
  const count = text === '' ? 0 : text.split(/\s+/).length;
  wc.textContent = count + (count > 1 ? ' mots' : ' mot');
  wc.style.color = count >= 150 ? 'var(--correct)' : 'var(--neutral)';
}

// ============================
// CORRECTION ENGINE
// ============================

function correctExam(examId) {
  const exam = EXAMS.find(e => e.id === examId);
  if (!exam) return;

  corrected = true;
  let score = 0;

  exam.questions.forEach((q, i) => {
    const fb = document.getElementById(`fb-${examId}-${i}`);
    fb.className = 'feedback show';

    if (q.type === 'qcm') {
      const userAns = answers[examId] && answers[examId][i] !== undefined ? answers[examId][i] : null;
      const correct = userAns === q.correct;

      q.options.forEach((_, j) => {
        const lbl = document.getElementById(`opt-${examId}-${i}-${j}`);
        if (!lbl) return;
        if (j === q.correct) lbl.classList.add(userAns === j ? 'correct' : 'missed');
        else if (j === userAns && !correct) lbl.classList.add('wrong');
      });

      if (correct) score++;
      fb.classList.add(correct ? 'correct-fb' : 'wrong-fb');
      fb.innerHTML = (correct ? '✓ Bonne réponse ! ' : '✗ Mauvaise réponse. ') + q.feedback;

    } else if (q.type === 'vf') {
      const userAns = answers[examId] && answers[examId][i] !== undefined ? answers[examId][i] : null;
      const correct = userAns === q.correct;

      const trueBtn  = document.getElementById(`tf-${examId}-${i}-true`);
      const falseBtn = document.getElementById(`tf-${examId}-${i}-false`);

      trueBtn.classList.remove('selected');
      falseBtn.classList.remove('selected');

      if (q.correct === true)  trueBtn.classList.add('correct');
      else                     falseBtn.classList.add('correct');

      if (userAns !== null && userAns !== q.correct) {
        if (userAns === true)  trueBtn.classList.add('wrong');
        else                   falseBtn.classList.add('wrong');
      }

      if (correct && userAns !== null) score++;
      fb.classList.add((correct && userAns !== null) ? 'correct-fb' : 'wrong-fb');
      fb.innerHTML = ((correct && userAns !== null) ? '✓ Bonne réponse ! ' : '✗ Mauvaise réponse. ') + q.feedback;

    } else if (q.type === 'fill') {
      const blankCount = q.blanks.length;
      let allCorrect = true;
      const userFills = (answers[examId] && answers[examId][i]) ? answers[examId][i] : {};

      for (let b = 0; b < blankCount; b++) {
        const input = document.getElementById(`fill-${examId}-${i}-${b}`);
        const userVal = (userFills[b] || '').toLowerCase().trim();
        const correctVal = q.blanks[b].toLowerCase().trim();
        const isCorrect = userVal === correctVal;

        if (input) {
          input.classList.remove('correct', 'wrong');
          input.classList.add(isCorrect ? 'correct' : 'wrong');
          if (!isCorrect) {
            input.value = input.value + ' → ' + q.blanks[b];
          }
        }
        if (!isCorrect) allCorrect = false;
      }

      if (allCorrect) score++;
      fb.classList.add(allCorrect ? 'correct-fb' : 'wrong-fb');
      fb.innerHTML = (allCorrect ? '✓ Bonne réponse ! ' : '✗ Mauvaise réponse. ') + q.feedback;
    }
  });

  // Show score
  const scoreBanner = document.getElementById(`score-${examId}`);
  scoreBanner.classList.add('show');
  const pct = Math.round((score / 10) * 100);
  const mention = pct >= 85 ? 'Excellent !' : pct >= 70 ? 'Bien !' : pct >= 50 ? 'Assez bien.' : 'À retravailler.';
  scoreBanner.innerHTML = `Note : ${score} / 10 — ${pct}%
    <div class="score-detail">${mention}</div>`;

  // Show WhatsApp send button
  const waBar = document.getElementById(`wa-bar-${examId}`);
  if (waBar) waBar.style.display = 'block';
}

function resetExam(examId) {
  const exam = EXAMS.find(e => e.id === examId);
  if (!exam) return;

  if (answers[examId]) answers[examId] = {};
  corrected = false;

  // Re-render the panel
  const panel = document.getElementById(`exam-${examId}`);
  if (panel) {
    panel.innerHTML = buildExamHTML(exam);
    attachExamEvents(panel, exam);
  }
}

function resetExamPanel(panel, exam) {
  if (answers[exam.id]) answers[exam.id] = {};
  corrected = false;
  // No full re-render needed — just reset the existing panel if desired
}

function attachExamEvents(panel, exam) {
  // Events are handled via inline onclick — no additional attachment needed
}

// ============================
// WHATSAPP SENDER
// ============================

function sendWhatsApp(examId) {
  const exam = EXAMS.find(e => e.id === examId);
  if (!exam) return;

  // Get student name
  const nameInput = document.getElementById(`student-name-${examId}`);
  const studentName = nameInput ? nameInput.value.trim() : '';
  if (!studentName) {
    nameInput && nameInput.focus();
    nameInput && (nameInput.style.borderColor = 'var(--wrong)');
    alert('⚠️ Veuillez entrer votre nom et prénom avant d\'envoyer.');
    return;
  }

  // Get score from banner
  const scoreBanner = document.getElementById(`score-${examId}`);
  const scoreText = scoreBanner ? scoreBanner.innerText.split('\n')[0] : '—';

  // Get writing
  const writingTA = document.getElementById(`writing-${examId}`);
  const writingText = writingTA ? writingTA.value.trim() : '';

  // Build detail of answers
  let answerLines = '';
  if (exam.questions) {
    exam.questions.forEach((q, i) => {
      const ans = answers[examId] && answers[examId][i] !== undefined ? answers[examId][i] : null;
      let answerStr = '—';
      if (q.type === 'qcm' && ans !== null) {
        answerStr = `${String.fromCharCode(65 + ans)}) ${q.options[ans]}`;
      } else if (q.type === 'vf' && ans !== null) {
        answerStr = ans ? 'Vrai' : 'Faux';
      } else if (q.type === 'fill' && ans !== null) {
        answerStr = Object.values(ans).join(', ');
      }
      const correct = (() => {
        if (q.type === 'qcm') return ans === q.correct;
        if (q.type === 'vf') return ans === q.correct;
        if (q.type === 'fill') {
          const fills = (answers[examId] && answers[examId][i]) ? answers[examId][i] : {};
          return q.blanks.every((b, idx) => (fills[idx] || '').toLowerCase().trim() === b.toLowerCase().trim());
        }
        return false;
      })();
      answerLines += `Q${i + 1}: ${answerStr} ${correct ? '✓' : '✗'}\n`;
    });
  }

  // Compose message
  const msg =
`📝 EXAMEN ${examId} — ${exam.title}
👤 Élève : ${studentName}
🏆 Score : ${scoreText}

📋 Réponses :
${answerLines}
✍️ Production écrite :
${writingText || '(non rédigée)'}`;

  const phone = '212630749641';
  const url = `https://wa.me/${phone}?text=${encodeURIComponent(msg)}`;
  window.open(url, '_blank');
}

// ============================
// INIT
// ============================

document.addEventListener('DOMContentLoaded', () => {
  // Build nav buttons
  const navList = document.getElementById('nav-exams-list');
  EXAMS.forEach(exam => {
    const li = document.createElement('li');
    li.className = 'nav-exams';
    const btn = document.createElement('button');
    btn.className = 'nav-btn';
    btn.dataset.id = exam.id;
    btn.textContent = `Ex. ${exam.id}`;
    btn.addEventListener('click', () => loadExam(exam.id));
    li.appendChild(btn);
    navList.appendChild(li);
  });

  // Build exam cards in welcome screen
  const grid = document.getElementById('exam-grid');
  EXAMS.forEach(exam => {
    const card = document.createElement('div');
    card.className = 'exam-card';
    card.innerHTML = `
      <div class="exam-card-num">Examen ${exam.id}</div>
      <div class="exam-card-title">${exam.title}</div>
    `;
    card.addEventListener('click', () => loadExam(exam.id));
    grid.appendChild(card);
  });
});