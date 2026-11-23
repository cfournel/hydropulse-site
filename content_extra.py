# -*- coding: utf-8 -*-
"""Pages added on 2026-11-23: Galaxy Watch, Pixel Watch and a "best water reminder apps for
Wear OS" comparison (EN/FR/ES), plus German and Portuguese with the product pages only.

Search data behind the choice (Brave, 2026-11-23): the site already ranks on "pixel watch
hydration app" and "best water reminder app wear os", is absent on "galaxy watch water reminder
app", and absent in every non-English query. Facts about other apps are limited to what their
own makers publish; anything we could not check is not claimed.
"""

# ------------------------------------------------------------------ English ----

EN_TOPICS = {
    "galaxy": {
        "slug": "water-reminder-galaxy-watch",
        "nav": "Galaxy Watch",
        "card": "A water reminder for Galaxy Watch 4 and later that follows your heart rate and the heat.",
        "title": "Water Reminder for Samsung Galaxy Watch — HydroPulse",
        "desc": "A water reminder app for Galaxy Watch 4, 5, 6, 7 and Ultra that reacts to your "
                "heart rate, your workouts and the weather, with a tile and one-tap logging.",
        "h1": "A water reminder for Samsung Galaxy Watch",
        "lede": "Galaxy Watch 4 and every model since run Wear OS, so HydroPulse installs straight "
                "from Google Play on the watch. It adds what Samsung Health's water counter does "
                "not do: telling you when to drink, and how much, from what your body is doing.",
        "why_title": "What it adds to Samsung Health",
        "why": [
            "Samsung Health counts the glasses you log against a daily target. That is useful, but "
            "it waits for you to remember. HydroPulse runs the other half: it estimates what you are "
            "losing from your heart rate, your activity and the local heat, and nudges you when the "
            "balance actually drops.",
            "On a cool day at a desk you will barely hear from it; on a hot afternoon or during a "
            "long ride it speaks up early, with an amount in millilitres and the reason.",
            "Every drink you log in HydroPulse can also be written to Health Connect, so it is not "
            "trapped in one app.",
        ],
        "works_on": [
            "Galaxy Watch 4, 5, 6, 7, Ultra and later Wear OS models; not the older Tizen watches (Galaxy Watch 3, Active 2).",
            "Install from Google Play on the watch, or from the phone's Play Store with the watch selected.",
            "A tile to add to your tile carousel, and a complication for watch faces that accept third-party data.",
            "Log water and Snooze 15 min right from the notification.",
        ],
        "expect": "Grant heart rate, activity and approximate location when asked: each feeds one part "
                  "of the model, and the app still works without them. Samsung's battery settings "
                  "can put rarely used apps to sleep; if reminders stop, exclude HydroPulse from "
                  "\"sleeping apps\" in the watch's battery settings.",
        "faq": [
            ("Does HydroPulse work on Galaxy Watch?",
             "Yes, on Galaxy Watch 4 and every later model, which run Wear OS 3 or newer. The older "
             "Tizen-based Galaxy watches cannot install Wear OS apps."),
            ("Do I still need Samsung Health?",
             "No. HydroPulse works on its own. If you use Health Connect, your logged drinks are "
             "written there too."),
            ("Can I log water from the watch face?",
             "Yes, from the tile, the notification or the app, in one tap; a complication shows your "
             "hydration percentage on faces that accept third-party data."),
        ],
    },
    "pixel": {
        "slug": "water-reminder-pixel-watch",
        "nav": "Pixel Watch",
        "card": "Water reminders and one-tap logging on Google Pixel Watch.",
        "title": "Water Reminder for Google Pixel Watch — HydroPulse",
        "desc": "A water reminder for Pixel Watch 1, 2, 3 and 4: it reads your heart rate and the "
                "weather to tell you when to drink, with a tile and one-tap logging.",
        "h1": "A water reminder for Google Pixel Watch",
        "lede": "Pixel Watch owners often ask how to log water and get reminders from the watch "
                "itself. HydroPulse does both on the wrist, and decides when to remind you from your "
                "heart rate and the heat rather than a fixed hour.",
        "why_title": "Why use it on a Pixel Watch",
        "why": [
            "Water tracking in the Fitbit ecosystem has mostly lived in the phone app. HydroPulse "
            "keeps it on the watch: a tile with your balance, a notification with a Log water "
            "button, and a history of the day.",
            "Its reminders are not hourly. They follow a running estimate of your losses, built from "
            "the watch's heart-rate sensor, your activity and the local weather, so they come early "
            "on a hot workout day and stay quiet on a calm one.",
            "Drinks can be written to Health Connect, where other health apps can read them.",
        ],
        "works_on": [
            "Pixel Watch, Pixel Watch 2, 3 and 4 (Wear OS 3 or newer).",
            "A tile, a complication and notification actions.",
            "Works without the phone nearby: the model and the log live on the watch.",
        ],
        "expect": "Install it from Google Play on the watch, set your weight and units once, and "
                  "allow heart rate, activity and approximate location. Battery use is small: "
                  "passive heart-rate data and a periodic check, with the weather cached.",
        "faq": [
            ("Can I log water on Pixel Watch?",
             "Yes, with HydroPulse: from its tile, its notification or the app, in one tap."),
            ("Does it sync with Fitbit?",
             "HydroPulse writes your drinks to Health Connect. Whether the Fitbit app shows them "
             "depends on Fitbit's own Health Connect support on your phone."),
            ("Does it need the phone?",
             "No. Everything runs on the watch; only the weather lookup needs a connection."),
        ],
    },
    "best": {
        "slug": "best-water-reminder-apps-wear-os",
        "nav": "Best apps for Wear OS",
        "card": "Built-in trackers, timer apps and adaptive reminders on Wear OS, compared honestly.",
        "title": "Best Water Reminder Apps for Wear OS (2026)",
        "desc": "Samsung Health, Fitbit, timer-based reminder apps and HydroPulse compared for Wear "
                "OS watches: what each one does on the wrist, and who it suits.",
        "h1": "Water reminder apps for Wear OS, compared",
        "lede": "Three kinds of tools can remind you to drink on a Wear OS watch: the tracker that "
                "came with it, an app that buzzes on a timer, and an app that estimates your need. "
                "This page is written by the makers of HydroPulse; we say what each kind is good at.",
        "why_title": "The three approaches",
        "why": [
            "Built-in trackers. Samsung Health on Galaxy Watch counts glasses against a daily goal; "
            "Fitbit lets you log water, mostly from the phone. Free and already there, but they "
            "count rather than remind.",
            "Timer reminder apps. Most \"drink water\" apps on Google Play split a daily goal into "
            "fixed intervals and buzz every hour or so. Simple and often free with ads; the catch is "
            "that the timer cannot tell a desk morning from a hot run, so many people mute it.",
            "Adaptive reminders. HydroPulse runs a fluid-balance model on the watch from your heart "
            "rate, your activity and the local weather, and reminds you when the balance drops, "
            "with an amount and a reason. It is a paid app, one-time purchase, no ads.",
        ],
        "works_on": [
            "Pick a built-in tracker if you only want to count glasses and never be nudged.",
            "Pick a timer app if your days are regular and an hourly buzz suits you.",
            "Pick HydroPulse if you train, work in the heat or ignored timers before: it speaks up when your body loses more.",
            "Whatever you use, logging from the wrist in one tap is what makes the habit stick.",
        ],
        "expect": "HydroPulse needs a Wear OS 3+ watch (Galaxy Watch 4 or later, Pixel Watch, recent "
                  "TicWatch, Fossil, OnePlus and Xiaomi models). Its reminders are estimates, not "
                  "measurements, and it is not a medical device.",
        "faq": [
            ("What is the best water reminder app for Wear OS?",
             "It depends on what you want: Samsung Health or Fitbit to count glasses, a timer app for "
             "regular hourly nudges, HydroPulse for reminders that follow your heart rate, activity "
             "and the weather."),
            ("Is there a free option?",
             "Yes: the built-in trackers and many timer apps are free, often with ads. HydroPulse is "
             "a one-time purchase with no ads and no subscription."),
            ("Which apps work without a phone?",
             "HydroPulse runs entirely on the watch. Built-in trackers and timer apps vary: check "
             "that the app has a real Wear OS version, not only a phone app with a watch face."),
        ],
    },
}

FR_TOPICS = {
    "galaxy": {
        "slug": "rappel-boire-de-l-eau-galaxy-watch",
        "nav": "Galaxy Watch",
        "card": "Un rappel d'hydratation pour Galaxy Watch 4 et plus, qui suit votre pouls et la chaleur.",
        "title": "Rappel pour boire de l'eau sur Galaxy Watch — HydroPulse",
        "desc": "Une appli de rappel d'eau pour Galaxy Watch 4, 5, 6, 7 et Ultra qui suit votre "
                "pouls, vos séances et la météo, avec une tuile et un ajout en un geste.",
        "h1": "Un rappel pour boire de l'eau sur Samsung Galaxy Watch",
        "lede": "Les Galaxy Watch 4 et tous les modèles suivants tournent sous Wear OS : HydroPulse "
                "s'installe directement depuis Google Play sur la montre. Elle ajoute ce que le "
                "compteur d'eau de Samsung Health ne fait pas : vous dire quand boire, et combien.",
        "why_title": "Ce qu'elle ajoute à Samsung Health",
        "why": [
            "Samsung Health compte les verres que vous notez par rapport à un objectif du jour. "
            "C'est utile, mais il attend que vous y pensiez. HydroPulse fait l'autre moitié : elle "
            "estime ce que vous perdez à partir de votre pouls, de votre activité et de la chaleur, "
            "et vous prévient quand le bilan baisse vraiment.",
            "Un jour frais au bureau, elle se fait discrète ; un après-midi chaud ou pendant une "
            "longue sortie vélo, elle vous parle tôt, avec une quantité en millilitres et la raison.",
            "Chaque verre noté peut aussi être écrit dans Health Connect, pour ne pas rester "
            "enfermé dans une seule appli.",
        ],
        "works_on": [
            "Galaxy Watch 4, 5, 6, 7, Ultra et suivantes ; pas les anciennes montres Tizen (Galaxy Watch 3, Active 2).",
            "Installation depuis Google Play sur la montre, ou depuis le Play Store du téléphone en choisissant la montre.",
            "Une tuile à ajouter au carrousel et une complication pour les cadrans qui acceptent les données d'autres applis.",
            "Noter un verre ou reporter de 15 minutes directement depuis la notification.",
        ],
        "expect": "Acceptez le pouls, l'activité et la position approximative quand ils sont demandés : "
                  "chacun alimente une partie du modèle, et l'appli marche aussi sans eux. Les "
                  "réglages de batterie Samsung peuvent mettre en veille les applis peu ouvertes ; si "
                  "les rappels s'arrêtent, excluez HydroPulse des « applis en veille ».",
        "faq": [
            ("HydroPulse fonctionne-t-elle sur Galaxy Watch ?",
             "Oui, sur les Galaxy Watch 4 et tous les modèles suivants, qui tournent sous Wear OS 3 "
             "ou plus. Les anciennes Galaxy sous Tizen ne peuvent pas installer d'applis Wear OS."),
            ("Faut-il encore Samsung Health ?",
             "Non, HydroPulse fonctionne seule. Si vous utilisez Health Connect, vos verres y sont "
             "aussi enregistrés."),
            ("Peut-on noter un verre depuis le cadran ?",
             "Oui, depuis la tuile, la notification ou l'appli, en un geste ; une complication affiche "
             "votre pourcentage d'hydratation sur les cadrans compatibles."),
        ],
    },
    "pixel": {
        "slug": "rappel-boire-de-l-eau-pixel-watch",
        "nav": "Pixel Watch",
        "card": "Rappels d'hydratation et ajout d'un verre en un geste sur Google Pixel Watch.",
        "title": "Rappel pour boire de l'eau sur Pixel Watch — HydroPulse",
        "desc": "Un rappel d'eau pour Pixel Watch 1, 2, 3 et 4 : il lit votre pouls et la météo "
                "pour vous dire quand boire, avec une tuile et un ajout en un geste.",
        "h1": "Un rappel pour boire de l'eau sur Google Pixel Watch",
        "lede": "Beaucoup de possesseurs de Pixel Watch cherchent comment noter leur eau et recevoir "
                "des rappels depuis la montre. HydroPulse fait les deux au poignet, et choisit le "
                "moment du rappel selon votre pouls et la chaleur, pas selon l'heure.",
        "why_title": "Pourquoi l'utiliser sur une Pixel Watch",
        "why": [
            "Chez Fitbit, le suivi de l'eau se fait surtout dans l'appli du téléphone. HydroPulse le "
            "garde sur la montre : une tuile avec votre bilan, une notification avec un bouton pour "
            "noter un verre, et l'historique du jour.",
            "Ses rappels ne sont pas horaires. Ils suivent une estimation continue de vos pertes, "
            "tirée du capteur cardiaque, de votre activité et de la météo locale : tôt un jour de "
            "séance au chaud, discrets un jour calme.",
            "Les verres peuvent être écrits dans Health Connect, où d'autres applis santé les lisent.",
        ],
        "works_on": [
            "Pixel Watch, Pixel Watch 2, 3 et 4 (Wear OS 3 ou plus).",
            "Une tuile, une complication et des actions dans la notification.",
            "Fonctionne sans le téléphone à proximité : le modèle et le journal sont sur la montre.",
        ],
        "expect": "Installez-la depuis Google Play sur la montre, réglez une fois votre poids et vos "
                  "unités, puis autorisez le pouls, l'activité et la position approximative. "
                  "Consommation de batterie faible : données cardiaques passives et vérification "
                  "périodique, météo mise en cache.",
        "faq": [
            ("Peut-on noter son eau sur Pixel Watch ?",
             "Oui, avec HydroPulse : depuis sa tuile, sa notification ou l'appli, en un geste."),
            ("Est-ce synchronisé avec Fitbit ?",
             "HydroPulse écrit vos verres dans Health Connect. Leur affichage dans Fitbit dépend de "
             "la prise en charge de Health Connect par l'appli Fitbit sur votre téléphone."),
            ("Faut-il le téléphone ?",
             "Non. Tout tourne sur la montre ; seule la météo demande une connexion."),
        ],
    },
    "best": {
        "slug": "meilleures-applis-rappel-eau-wear-os",
        "nav": "Meilleures applis Wear OS",
        "card": "Suivi intégré, applis minuteur et rappels adaptatifs sur Wear OS, comparés honnêtement.",
        "title": "Meilleures applis pour boire de l'eau sur Wear OS (2026)",
        "desc": "Samsung Health, Fitbit, applis de rappel à minuteur et HydroPulse comparés sur "
                "montre Wear OS : ce que chacun fait au poignet, et pour qui.",
        "h1": "Applis de rappel d'eau pour Wear OS : le comparatif",
        "lede": "Trois sortes d'outils peuvent vous rappeler de boire sur une montre Wear OS : le "
                "suivi livré avec la montre, une appli qui vibre à heure fixe, et une appli qui "
                "estime votre besoin. Cette page est écrite par l'éditeur de HydroPulse.",
        "why_title": "Les trois approches",
        "why": [
            "Le suivi intégré. Samsung Health sur Galaxy Watch compte les verres face à un objectif ; "
            "Fitbit permet de noter son eau, surtout depuis le téléphone. Gratuit et déjà là, mais "
            "cela compte plus que cela ne rappelle.",
            "Les applis minuteur. La plupart des applis « boire de l'eau » de Google Play découpent "
            "un objectif en intervalles fixes et vibrent toutes les heures environ. Simples, souvent "
            "gratuites avec publicité ; mais le minuteur ne distingue pas une matinée au bureau d'une "
            "course au soleil, alors beaucoup finissent par le couper.",
            "Les rappels adaptatifs. HydroPulse calcule un bilan hydrique sur la montre à partir de "
            "votre pouls, de votre activité et de la météo, et vous prévient quand il baisse, avec "
            "une quantité et une raison. Appli payante, achat unique, sans publicité.",
        ],
        "works_on": [
            "Un suivi intégré si vous voulez seulement compter vos verres, sans rappel.",
            "Une appli minuteur si vos journées sont régulières et qu'une vibration par heure vous convient.",
            "HydroPulse si vous faites du sport, travaillez au chaud ou avez déjà coupé des minuteurs : elle parle quand vous perdez plus.",
            "Dans tous les cas, noter un verre en un geste au poignet est ce qui fait tenir l'habitude.",
        ],
        "expect": "HydroPulse demande une montre Wear OS 3 ou plus (Galaxy Watch 4 et suivantes, Pixel "
                  "Watch, TicWatch, Fossil, OnePlus et Xiaomi récentes). Ses rappels sont des "
                  "estimations, pas des mesures, et ce n'est pas un dispositif médical.",
        "faq": [
            ("Quelle est la meilleure appli pour boire de l'eau sur Wear OS ?",
             "Tout dépend de ce que vous cherchez : Samsung Health ou Fitbit pour compter les verres, "
             "une appli minuteur pour des rappels réguliers, HydroPulse pour des rappels qui suivent "
             "votre pouls, votre activité et la météo."),
            ("Existe-t-il une option gratuite ?",
             "Oui : le suivi intégré et beaucoup d'applis minuteur sont gratuits, souvent avec "
             "publicité. HydroPulse est un achat unique, sans publicité ni abonnement."),
            ("Quelles applis marchent sans téléphone ?",
             "HydroPulse tourne entièrement sur la montre. Pour les autres, vérifiez qu'il existe une "
             "vraie version Wear OS, pas seulement une appli téléphone avec un cadran."),
        ],
    },
}

ES_TOPICS = {
    "galaxy": {
        "slug": "recordatorio-de-agua-galaxy-watch",
        "nav": "Galaxy Watch",
        "card": "Un recordatorio de agua para Galaxy Watch 4 y posteriores que sigue tu pulso y el calor.",
        "title": "Recordatorio de agua para Galaxy Watch — HydroPulse",
        "desc": "Una app de recordatorio de agua para Galaxy Watch 4, 5, 6, 7 y Ultra que sigue tu "
                "pulso, tus entrenamientos y el clima, con tarjeta y registro en un toque.",
        "h1": "Un recordatorio para beber agua en Samsung Galaxy Watch",
        "lede": "Los Galaxy Watch 4 y todos los modelos posteriores usan Wear OS, así que HydroPulse "
                "se instala desde Google Play en el propio reloj. Añade lo que el contador de agua de "
                "Samsung Health no hace: decirte cuándo beber y cuánto.",
        "why_title": "Qué añade a Samsung Health",
        "why": [
            "Samsung Health cuenta los vasos que anotas frente a un objetivo diario. Es útil, pero "
            "espera a que te acuerdes. HydroPulse hace la otra mitad: estima lo que pierdes a partir "
            "de tu pulso, tu actividad y el calor, y te avisa cuando el balance baja de verdad.",
            "Un día fresco en la oficina apenas la notarás; una tarde de calor o en una salida larga "
            "en bici te avisa pronto, con una cantidad en mililitros y el motivo.",
            "Cada vaso anotado puede escribirse también en Health Connect.",
        ],
        "works_on": [
            "Galaxy Watch 4, 5, 6, 7, Ultra y posteriores; no los antiguos relojes Tizen (Galaxy Watch 3, Active 2).",
            "Se instala desde Google Play en el reloj, o desde el Play Store del móvil eligiendo el reloj.",
            "Una tarjeta para el carrusel y una complicación para las esferas que aceptan datos de otras apps.",
            "Anotar agua o posponer 15 minutos desde la notificación.",
        ],
        "expect": "Concede pulso, actividad y ubicación aproximada cuando te lo pida: cada uno alimenta "
                  "una parte del modelo, y la app funciona también sin ellos. Los ajustes de batería "
                  "de Samsung pueden dormir las apps poco usadas; si los avisos se detienen, excluye "
                  "HydroPulse de las «apps en suspensión».",
        "faq": [
            ("¿HydroPulse funciona en Galaxy Watch?",
             "Sí, en los Galaxy Watch 4 y todos los modelos posteriores, con Wear OS 3 o superior. Los "
             "antiguos Galaxy con Tizen no pueden instalar apps de Wear OS."),
            ("¿Sigo necesitando Samsung Health?",
             "No, HydroPulse funciona por sí sola. Si usas Health Connect, tus vasos se guardan allí "
             "también."),
            ("¿Puedo anotar agua desde la esfera?",
             "Sí, desde la tarjeta, la notificación o la app, en un toque; una complicación muestra tu "
             "porcentaje de hidratación en las esferas compatibles."),
        ],
    },
    "pixel": {
        "slug": "recordatorio-de-agua-pixel-watch",
        "nav": "Pixel Watch",
        "card": "Recordatorios de agua y registro en un toque en Google Pixel Watch.",
        "title": "Recordatorio de agua para Pixel Watch — HydroPulse",
        "desc": "Un recordatorio de agua para Pixel Watch 1, 2, 3 y 4: lee tu pulso y el clima "
                "para decirte cuándo beber, con tarjeta y registro en un toque.",
        "h1": "Un recordatorio para beber agua en Google Pixel Watch",
        "lede": "Muchos usuarios de Pixel Watch buscan cómo anotar agua y recibir avisos desde el "
                "reloj. HydroPulse hace las dos cosas en la muñeca, y decide cuándo avisarte según tu "
                "pulso y el calor, no según la hora.",
        "why_title": "Por qué usarla en un Pixel Watch",
        "why": [
            "En Fitbit, el registro de agua se hace sobre todo en la app del móvil. HydroPulse lo "
            "mantiene en el reloj: una tarjeta con tu balance, una notificación con botón para anotar "
            "agua y el historial del día.",
            "Sus avisos no son cada hora. Siguen una estimación continua de tus pérdidas, a partir "
            "del sensor de pulso, tu actividad y el clima local.",
            "Los vasos pueden escribirse en Health Connect, donde otras apps de salud los leen.",
        ],
        "works_on": [
            "Pixel Watch, Pixel Watch 2, 3 y 4 (Wear OS 3 o superior).",
            "Una tarjeta, una complicación y acciones en la notificación.",
            "Funciona sin el móvil cerca: el modelo y el registro están en el reloj.",
        ],
        "expect": "Instálala desde Google Play en el reloj, ajusta una vez tu peso y tus unidades y "
                  "permite pulso, actividad y ubicación aproximada. Gasta poca batería: datos de "
                  "pulso pasivos y una comprobación periódica, con el clima en caché.",
        "faq": [
            ("¿Se puede anotar agua en Pixel Watch?",
             "Sí, con HydroPulse: desde su tarjeta, su notificación o la app, en un toque."),
            ("¿Se sincroniza con Fitbit?",
             "HydroPulse escribe tus vasos en Health Connect. Que Fitbit los muestre depende del "
             "soporte de Health Connect en la app de Fitbit de tu móvil."),
            ("¿Necesita el móvil?",
             "No. Todo funciona en el reloj; solo el clima necesita conexión."),
        ],
    },
    "best": {
        "slug": "mejores-apps-recordatorio-agua-wear-os",
        "nav": "Mejores apps Wear OS",
        "card": "Seguimiento integrado, apps con temporizador y avisos adaptativos en Wear OS, comparados.",
        "title": "Mejores apps para beber agua en Wear OS (2026)",
        "desc": "Samsung Health, Fitbit, apps de recordatorio con temporizador y HydroPulse "
                "comparadas en relojes Wear OS: qué hace cada una en la muñeca y para quién.",
        "h1": "Apps de recordatorio de agua para Wear OS, comparadas",
        "lede": "Tres tipos de herramientas pueden recordarte beber en un reloj Wear OS: el "
                "seguimiento que trae el reloj, una app que vibra a horas fijas y una app que estima "
                "tu necesidad. Esta página la escribe el editor de HydroPulse.",
        "why_title": "Los tres enfoques",
        "why": [
            "El seguimiento integrado. Samsung Health en Galaxy Watch cuenta vasos frente a un "
            "objetivo; Fitbit permite anotar agua, sobre todo desde el móvil. Gratis y ya instalado, "
            "pero cuenta más que recuerda.",
            "Las apps con temporizador. La mayoría de apps de «beber agua» en Google Play reparten un "
            "objetivo en intervalos fijos y vibran cada hora. Sencillas y a menudo gratis con "
            "anuncios; pero el temporizador no distingue una mañana en la oficina de una carrera al "
            "sol, y mucha gente acaba silenciándolo.",
            "Los avisos adaptativos. HydroPulse calcula un balance hídrico en el reloj con tu pulso, "
            "tu actividad y el clima, y te avisa cuando baja, con una cantidad y un motivo. App de "
            "pago, compra única, sin anuncios.",
        ],
        "works_on": [
            "Un seguimiento integrado si solo quieres contar vasos, sin avisos.",
            "Una app con temporizador si tus días son regulares y te basta un aviso por hora.",
            "HydroPulse si entrenas, trabajas con calor o ya silenciaste temporizadores: avisa cuando pierdes más.",
            "Sea cual sea, anotar agua en un toque desde la muñeca es lo que hace durar el hábito.",
        ],
        "expect": "HydroPulse necesita un reloj con Wear OS 3 o superior (Galaxy Watch 4 y posteriores, "
                  "Pixel Watch, TicWatch, Fossil, OnePlus y Xiaomi recientes). Sus avisos son "
                  "estimaciones, no mediciones, y no es un producto sanitario.",
        "faq": [
            ("¿Cuál es la mejor app para beber agua en Wear OS?",
             "Depende de lo que busques: Samsung Health o Fitbit para contar vasos, una app con "
             "temporizador para avisos regulares, HydroPulse para avisos que siguen tu pulso, tu "
             "actividad y el clima."),
            ("¿Hay una opción gratis?",
             "Sí: el seguimiento integrado y muchas apps con temporizador son gratis, a menudo con "
             "anuncios. HydroPulse es una compra única, sin anuncios ni suscripción."),
            ("¿Qué apps funcionan sin móvil?",
             "HydroPulse funciona entera en el reloj. Para las demás, comprueba que tengan una versión "
             "real de Wear OS y no solo una app de móvil con una esfera."),
        ],
    },
}

# ------------------------------------------------------------------- German ----

DE = {
    "code": "de",
    "label": "DE",
    "name": "Deutsch",
    "base": "de",
    "topic_dir": "trinken",
    "ui": {
        "home_crumb": "Start",
        "badge_alt": "Jetzt bei Google Play",
        "cta_note": "Wear OS 3.0+. Einmalkauf — kein Abo, keine Werbung, kein Konto.",
        "app_lang_note": "Die App ist auf Deutsch, Englisch, Französisch, Spanisch und Portugiesisch.",
        "how_title": "Wie HydroPulse entscheidet",
        "how_steps": [
            "Du gibst einmal Gewicht, Alter und Schweißprofil ein. Daraus ergibt sich dein persönlicher Grundverlust — das Wasser, das du allein durch Atmen und Leben verlierst.",
            "Die Uhr misst laufend deinen Puls und rechnet ihn in einen Anteil deiner Herzfrequenzreserve um: wie stark du dich anstrengst, gemessen an deinem eigenen Ruhe- und Maximalpuls.",
            "Temperatur und Luftfeuchtigkeit vor Ort werden anonym abgerufen und in einen Hitzeindex-Faktor umgerechnet, denn dieselbe Anstrengung kostet bei 33 °C und 70 % Luftfeuchte viel mehr Flüssigkeit als bei 18 °C.",
            "Jedes eingetragene Getränk wird der Bilanz gutgeschrieben. Fällt der Stand unter deine Schwelle, meldet sich HydroPulse — mit einer Menge in Millilitern und dem Grund.",
        ],
        "works_title": "Was HydroPulse hier macht",
        "expect_title": "Was dich erwartet",
        "faq_title": "Häufige Fragen",
        "features_title": "Warum es kein weiterer Timer ist",
        "features": [
            "Eine laufende Flüssigkeitsbilanz statt eines Countdowns — der Abstand zwischen Erinnerungen folgt deinem Tag.",
            "Schweißschätzung aus dem Puls, bezogen auf deinen eigenen Ruhe- und Maximalpuls.",
            "Live-Temperatur und Luftfeuchte über einen Hitzeindex-Faktor.",
            "Jede Erinnerung nennt eine Menge in mL und einen Grund: Hitze, Anstrengung oder Grundbedarf.",
            "Drei Dringlichkeitsstufen, damit ein Hinweis nicht wie eine Warnung aussieht.",
            "Native Wear-OS-Kachel und Zifferblatt-Komplikation: deine Bilanz auf einen Blick.",
            "Eintragen mit einem Tipp aus der Benachrichtigung, dazu 15 Minuten Schlummern.",
            "Ruhezeiten, damit sie dich nicht weckt.",
            "Einheiten in mL, fl oz oder Schlucken, und deine eigene Schwelle.",
        ],
        "privacy_title": "Privat von Grund auf",
        "privacy_body": "Puls, Aktivität und Trinkprotokoll verlassen nie die Uhr. Kein Konto, kein "
                        "Werbe-SDK, keine Nutzungsanalyse. Nur zwei Dinge gehen hinaus: Koordinaten "
                        "an einen öffentlichen Wetterdienst, ohne Kennung, und ein Absturzbericht, "
                        "falls die App abstürzt. Keines davon enthält Gesundheitsdaten.",
        "privacy_link": "Datenschutzerklärung lesen (Englisch)",
        "safety_title": "Kein Medizinprodukt",
        "safety_body": "HydroPulse liefert eine Schätzung, keine Messung. Es ist ein Wellness-Werkzeug, "
                       "kein Medizinprodukt, und diagnostiziert, behandelt oder überwacht weder "
                       "Dehydrierung noch eine andere Erkrankung. Wenn du Entwässerungsmittel nimmst, "
                       "ärztlich die Trinkmenge begrenzen sollst oder eine Nieren-, Herz- oder "
                       "Hormonerkrankung hast, folge den Vorgaben deiner Ärztin oder deines Arztes. "
                       "Bei Verwirrtheit, Ohnmacht oder Hitzschlag sofort Hilfe holen.",
        "related_title": "Mehr zum Trinken",
        "topics_title": "Trinken auf deiner Uhr",
        "foot_tag": "HydroPulse — Trinkerinnerung für Wear OS, die sich anpasst.",
        "foot_privacy": "Datenschutz",
        "foot_play": "Google Play",
        "foot_terms": "Nutzungsbedingungen",
        "langs_label": "Sprache",
        "screens_title": "Auf der Uhr",
        "sources_title": "Woher das Modell kommt",
        "sources_body": "Der Grundbedarf stützt sich auf Referenzwerte von IOM und EFSA, der "
                        "Schweißanteil auf die Trinkempfehlungen des ACSM für Sport, der Umgebungsfaktor "
                        "auf die Hitzeindex-Formel des US-Wetterdienstes. Bevölkerungswerte, angepasst "
                        "an das, was eine Uhr messen kann — eine begründete Schätzung, keine "
                        "Labormessung.",
        "screens": [
            ("home", "HydroPulse-Startbildschirm mit 49 % Trinkbilanz und Eintragen-Taste",
             "Deine Bilanz als Ring, mit der Menge für jetzt."),
            ("notification", "Eine HydroPulse-Benachrichtigung mit 100 mL und Eintragen mit einem Tipp",
             "Ein Tipp zum Eintragen, einer zum Schlummern."),
            ("history", "Der Verlauf mit den Getränken des Tages",
             "Was du heute wirklich getrunken hast."),
            ("settings", "Die Einstellungen mit Gewicht, Einheiten und Schwelle",
             "Gewicht, Einheiten, Schwelle — das Modell passt sich an."),
        ],
    },
    "home": {
        "title": "HydroPulse — Trinkerinnerung für Wear OS",
        "desc": "Eine Trinkerinnerung für Wear OS, die sich nach Puls, Aktivität und Wetter richtet "
                "und dich erinnert, wenn dein Körper Wasser braucht — nicht nach Timer.",
        "h1": "Trinkerinnerungen, die deinem Körper folgen, nicht einer Uhrzeit",
        "lede": "Die meisten Trink-Apps teilen ein Tagesziel durch deine Wachstunden und vibrieren "
                "danach. HydroPulse rechnet auf der Uhr eine Flüssigkeitsbilanz aus Puls, Aktivität "
                "und Wetter und sagt dir, wann die Bilanz wirklich sinkt.",
        "intro": [
            "Eine Stunde am Schreibtisch mit Klimaanlage und eine Stunde Laufen im August kosten deinen "
            "Körper völlig unterschiedlich viel Wasser. Ein fester Takt kann das nicht unterscheiden: "
            "Er nervt, wenn du nichts brauchst, und schweigt, wenn du etwas brauchst.",
            "HydroPulse führt stattdessen eine laufende Bilanz. Sie sinkt mit deinem Grundbedarf, mit "
            "dem Schweiß, den dein Puls verrät, und mit der Hitze; jedes Getränk füllt sie wieder auf. "
            "An einem kühlen, ruhigen Tag hörst du kaum etwas, an einem heißen Trainingstag früh.",
            "Gebaut für das Handgelenk: eine Kachel, eine Komplikation, Eintragen mit einem Tipp und "
            "eine Empfehlung, die immer eine Menge und einen Grund nennt.",
        ],
    },
    "topics": {
        "wearos": {
            "slug": "trinkerinnerung-wear-os",
            "nav": "Wear OS",
            "card": "Eine Trinkerinnerung für die Uhr, keine Handy-App mit Komplikation.",
            "title": "Trinkerinnerung App für Wear OS — HydroPulse",
            "desc": "Eine native Trinkerinnerung für Wear OS mit Kachel, Komplikation und Eintragen "
                    "mit einem Tipp. Für Pixel Watch, Galaxy Watch und alle Wear OS 3.0+ Uhren.",
            "h1": "Eine Trinkerinnerung für Wear OS",
            "lede": "Kachel, Komplikation, Aktionen in der Benachrichtigung und ein Modell auf der "
                    "Uhr: HydroPulse rechnet am Handgelenk, also kommt die Erinnerung dort an, wo "
                    "deine Hände schon sind.",
            "why_title": "Warum die Uhr der richtige Ort ist",
            "why": [
                "Trinkgewohnheiten scheitern an Hürden. Zwischen „ich sollte trinken“ und einem "
                "eingetragenen Glas liegt meist ein Handy im anderen Zimmer. Eine Benachrichtigung am "
                "Handgelenk mit Eintragen-Taste macht daraus einen Tipp.",
                "Nur die Uhr weiß, wie sehr du dich anstrengst. Puls und Training kommen vom Sensor am "
                "Arm, die Schätzung beruht also auf deinem Körper, nicht auf einer Schrittzahl.",
                "Viele Trink-Apps sind Handy-Apps mit einer Komplikation als Zugabe. HydroPulse ist eine "
                "Wear-OS-App: Modell, Bilanz und Daten liegen auf der Uhr.",
            ],
            "works_on": [
                "Eine Kachel mit deiner aktuellen Bilanz, ohne etwas zu öffnen.",
                "Eine Komplikation fürs Zifferblatt.",
                "Benachrichtigungen mit „Wasser eintragen“ und „15 Min. später“.",
                "Wear OS 3.0 und neuer: Pixel Watch, Galaxy Watch 4 und neuer, TicWatch und andere.",
            ],
            "expect": "Installiere sie auf der Uhr, stelle Gewicht und Einheiten einmal ein und erlaube "
                      "Puls, Aktivität und ungefähren Standort. Jede Berechtigung speist einen Teil des "
                      "Modells; ohne sie arbeitet die App mit sinnvollen Standardwerten. Der Akkuverbrauch "
                      "ist gering.",
            "faq": [
                ("Brauche ich mein Handy?",
                 "Nein. Modell, Bilanz und Protokoll laufen auf der Uhr. Nur das Wetter braucht eine "
                 "Verbindung."),
                ("Auf welchen Uhren läuft sie?",
                 "Auf jeder Uhr mit Wear OS 3.0 oder neuer und Google Play: Pixel Watch, Galaxy Watch 4 "
                 "und neuer, TicWatch und vergleichbare Modelle."),
                ("Gibt es eine Handy-App?",
                 "Nein, mit Absicht. Alles Nötige ist auf der Uhr, also gibt es nichts zu "
                 "synchronisieren und kein Konto."),
            ],
        },
        "galaxy": {
            "slug": "trinkerinnerung-galaxy-watch",
            "nav": "Galaxy Watch",
            "card": "Eine Trinkerinnerung für Galaxy Watch 4 und neuer, die Puls und Hitze folgt.",
            "title": "Trinkerinnerung für Samsung Galaxy Watch — HydroPulse",
            "desc": "Eine Trinkerinnerung für Galaxy Watch 4, 5, 6, 7 und Ultra, die Puls, Training "
                    "und Wetter berücksichtigt, mit Kachel und Eintragen mit einem Tipp.",
            "h1": "Eine Trinkerinnerung für die Samsung Galaxy Watch",
            "lede": "Seit der Galaxy Watch 4 laufen alle Modelle mit Wear OS, HydroPulse kommt also "
                    "direkt aus Google Play auf die Uhr. Sie ergänzt, was der Wasserzähler von Samsung "
                    "Health nicht kann: dir sagen, wann und wie viel du trinken solltest.",
            "why_title": "Was sie zu Samsung Health hinzufügt",
            "why": [
                "Samsung Health zählt eingetragene Gläser gegen ein Tagesziel, wartet aber darauf, dass "
                "du daran denkst. HydroPulse schätzt deinen Verlust aus Puls, Aktivität und Hitze und "
                "meldet sich, wenn die Bilanz wirklich sinkt.",
                "An einem kühlen Bürotag hörst du kaum etwas, an einem heißen Nachmittag oder auf einer "
                "langen Radtour früh, mit Menge und Grund.",
                "Jedes Getränk kann auch in Health Connect geschrieben werden.",
            ],
            "works_on": [
                "Galaxy Watch 4, 5, 6, 7, Ultra und neuer; nicht die älteren Tizen-Uhren (Galaxy Watch 3, Active 2).",
                "Installation aus Google Play auf der Uhr oder im Play Store des Handys mit ausgewählter Uhr.",
                "Eine Kachel und eine Komplikation für Zifferblätter, die Daten anderer Apps zeigen.",
                "Wasser eintragen oder 15 Minuten schlummern direkt aus der Benachrichtigung.",
            ],
            "expect": "Erlaube Puls, Aktivität und ungefähren Standort. Samsungs Akku-Einstellungen "
                      "können selten genutzte Apps schlafen legen; wenn keine Erinnerungen mehr kommen, "
                      "nimm HydroPulse von den „Apps im Standby“ aus.",
            "faq": [
                ("Läuft HydroPulse auf der Galaxy Watch?",
                 "Ja, auf der Galaxy Watch 4 und allen neueren Modellen mit Wear OS 3 oder neuer. Die "
                 "älteren Tizen-Modelle können keine Wear-OS-Apps installieren."),
                ("Brauche ich Samsung Health noch?",
                 "Nein, HydroPulse funktioniert allein. Mit Health Connect landen deine Getränke auch "
                 "dort."),
            ],
        },
        "pixel": {
            "slug": "trinkerinnerung-pixel-watch",
            "nav": "Pixel Watch",
            "card": "Trinkerinnerungen und Eintragen mit einem Tipp auf der Google Pixel Watch.",
            "title": "Trinkerinnerung für Google Pixel Watch — HydroPulse",
            "desc": "Eine Trinkerinnerung für Pixel Watch 1, 2, 3 und 4: Sie liest Puls und Wetter, "
                    "sagt dir, wann du trinken solltest, und trägt mit einem Tipp ein.",
            "h1": "Eine Trinkerinnerung für die Google Pixel Watch",
            "lede": "Viele suchen nach einer Möglichkeit, Wasser direkt auf der Pixel Watch "
                    "einzutragen und erinnert zu werden. HydroPulse macht beides am Handgelenk und "
                    "richtet die Erinnerung nach Puls und Hitze, nicht nach der Uhrzeit.",
            "why_title": "Warum auf der Pixel Watch",
            "why": [
                "Bei Fitbit läuft das Wassertracking vor allem in der Handy-App. HydroPulse bleibt auf "
                "der Uhr: Kachel mit Bilanz, Benachrichtigung mit Eintragen-Taste, Tagesverlauf.",
                "Die Erinnerungen kommen nicht stündlich, sondern folgen einer laufenden Schätzung aus "
                "Pulssensor, Aktivität und Wetter.",
                "Getränke können in Health Connect geschrieben werden.",
            ],
            "works_on": [
                "Pixel Watch, Pixel Watch 2, 3 und 4 (Wear OS 3 oder neuer).",
                "Kachel, Komplikation und Aktionen in der Benachrichtigung.",
                "Läuft ohne Handy in der Nähe.",
            ],
            "expect": "Aus Google Play auf der Uhr installieren, Gewicht und Einheiten einmal "
                      "einstellen, Puls, Aktivität und ungefähren Standort erlauben. Geringer "
                      "Akkuverbrauch.",
            "faq": [
                ("Kann ich auf der Pixel Watch Wasser eintragen?",
                 "Ja, mit HydroPulse: über Kachel, Benachrichtigung oder App, mit einem Tipp."),
                ("Synchronisiert sie mit Fitbit?",
                 "HydroPulse schreibt deine Getränke in Health Connect. Ob Fitbit sie anzeigt, hängt "
                 "von der Health-Connect-Unterstützung der Fitbit-App ab."),
            ],
        },
        "best": {
            "slug": "beste-trinkerinnerung-apps-wear-os",
            "nav": "Beste Apps für Wear OS",
            "card": "Eingebaute Tracker, Timer-Apps und anpassende Erinnerungen auf Wear OS im Vergleich.",
            "title": "Beste Trinkerinnerung-Apps für Wear OS (2026)",
            "desc": "Samsung Health, Fitbit, Timer-Apps und HydroPulse auf Wear-OS-Uhren im Vergleich: "
                    "was jede Lösung am Handgelenk kann und für wen sie passt.",
            "h1": "Trinkerinnerung-Apps für Wear OS im Vergleich",
            "lede": "Drei Arten von Werkzeugen erinnern dich auf einer Wear-OS-Uhr ans Trinken: der "
                    "eingebaute Tracker, eine App mit Timer und eine App, die deinen Bedarf schätzt. "
                    "Diese Seite stammt von den Machern von HydroPulse.",
            "why_title": "Die drei Ansätze",
            "why": [
                "Eingebaute Tracker. Samsung Health zählt Gläser gegen ein Tagesziel, Fitbit lässt dich "
                "Wasser eintragen, meist auf dem Handy. Kostenlos und schon da, aber sie zählen eher, "
                "als dass sie erinnern.",
                "Timer-Apps. Die meisten Trink-Apps bei Google Play teilen ein Ziel in feste Abstände "
                "und vibrieren etwa stündlich. Einfach, oft kostenlos mit Werbung; der Timer kennt aber "
                "keinen Unterschied zwischen Büro und Lauf in der Sonne.",
                "Anpassende Erinnerungen. HydroPulse rechnet auf der Uhr eine Bilanz aus Puls, "
                "Aktivität und Wetter und meldet sich, wenn sie sinkt, mit Menge und Grund. "
                "Kostenpflichtig, Einmalkauf, ohne Werbung.",
            ],
            "works_on": [
                "Eingebauter Tracker, wenn du nur zählen und nie erinnert werden willst.",
                "Timer-App, wenn deine Tage regelmäßig sind.",
                "HydroPulse, wenn du trainierst, in der Hitze arbeitest oder Timer schon stummgeschaltet hast.",
            ],
            "expect": "HydroPulse braucht eine Uhr mit Wear OS 3 oder neuer. Die Erinnerungen sind "
                      "Schätzungen, keine Messungen, und es ist kein Medizinprodukt.",
            "faq": [
                ("Welche Trinkerinnerung-App ist die beste für Wear OS?",
                 "Das hängt davon ab, was du willst: Samsung Health oder Fitbit zum Zählen, eine "
                 "Timer-App für regelmäßige Hinweise, HydroPulse für Erinnerungen nach Puls, "
                 "Aktivität und Wetter."),
                ("Gibt es eine kostenlose Option?",
                 "Ja, eingebaute Tracker und viele Timer-Apps sind kostenlos, oft mit Werbung. "
                 "HydroPulse ist ein Einmalkauf ohne Werbung und ohne Abo."),
            ],
        },
    },
}

# --------------------------------------------------------------- Portuguese ----

PT = {
    "code": "pt",
    "label": "PT",
    "name": "Português",
    "base": "pt",
    "topic_dir": "hidratacao",
    "ui": {
        "home_crumb": "Início",
        "badge_alt": "Disponível no Google Play",
        "cta_note": "Wear OS 3.0+. Compra única — sem assinatura, sem anúncios, sem conta.",
        "app_lang_note": "O app está em português, inglês, francês, espanhol e alemão.",
        "how_title": "Como o HydroPulse decide",
        "how_steps": [
            "Você informa uma vez o peso, a idade e o perfil de transpiração. Isso define a sua perda básica pessoal — a água que você perde só por respirar e viver.",
            "O relógio lê o seu pulso continuamente e o converte em fração da reserva cardíaca: o quanto você se esforça em relação ao seu próprio pulso de repouso e máximo.",
            "A temperatura e a umidade locais são obtidas de forma anônima e viram um multiplicador de índice de calor, porque o mesmo esforço custa muito mais líquido a 33 °C e 70 % de umidade do que a 18 °C.",
            "Cada bebida registrada volta para o balanço. Quando o saldo passa do seu limite, o HydroPulse avisa — com uma quantidade em mililitros e o motivo.",
        ],
        "works_title": "O que o HydroPulse faz aqui",
        "expect_title": "O que esperar",
        "faq_title": "Perguntas frequentes",
        "features_title": "Por que não é mais um cronômetro",
        "features": [
            "Um balanço hídrico contínuo, não uma contagem regressiva — o intervalo entre lembretes segue o seu dia.",
            "Estimativa de suor pelo pulso, com base no seu próprio pulso de repouso e máximo.",
            "Temperatura e umidade ao vivo, por um multiplicador de índice de calor.",
            "Cada alerta traz uma quantidade em mL e um motivo: calor, esforço ou necessidade básica.",
            "Três níveis de urgência, para um lembrete não parecer um alarme.",
            "Bloco (Tile) nativo do Wear OS e complicação de mostrador: o seu saldo num relance.",
            "Registro com um toque na notificação, e adiar 15 minutos.",
            "Horário silencioso, para não acordar você.",
            "Unidades em mL, fl oz ou goles, e o seu próprio limite.",
        ],
        "privacy_title": "Privado por padrão",
        "privacy_body": "O seu pulso, a sua atividade e o seu registro de bebidas nunca saem do relógio. "
                        "Sem conta, sem SDK de anúncios, sem análise de uso. Só duas coisas saem: "
                        "coordenadas para um serviço público de clima, sem identificador, e um relatório "
                        "de falha se o app travar. Nenhuma leva dados de saúde.",
        "privacy_link": "Ler a política de privacidade (em inglês)",
        "safety_title": "Não é um dispositivo médico",
        "safety_body": "O HydroPulse produz uma estimativa, não uma medição. É uma ferramenta de "
                       "bem-estar, não um dispositivo médico, e não diagnostica, trata nem monitora "
                       "desidratação ou outra condição. Se você toma diuréticos, tem restrição de "
                       "líquidos por orientação médica ou uma doença renal, cardíaca ou endócrina, siga "
                       "a orientação do seu médico. Em caso de confusão, desmaio ou insolação, procure "
                       "atendimento urgente.",
        "related_title": "Mais sobre hidratação",
        "topics_title": "Hidratação no seu relógio",
        "foot_tag": "HydroPulse — lembrete de água para Wear OS que se adapta a você.",
        "foot_privacy": "Privacidade",
        "foot_play": "Google Play",
        "foot_terms": "Termos de uso",
        "langs_label": "Idioma",
        "screens_title": "No relógio",
        "sources_title": "De onde vem o modelo",
        "sources_body": "A necessidade básica se apoia nos valores de referência do IOM e da EFSA, o "
                        "suor nas recomendações de hidratação esportiva do ACSM, e o fator ambiental na "
                        "fórmula de índice de calor do serviço meteorológico dos EUA. Referências "
                        "populacionais adaptadas ao que um relógio consegue medir — uma estimativa "
                        "fundamentada, não uma medição de laboratório.",
        "screens": [
            ("home", "Tela inicial do HydroPulse com balanço de 49 % e botão para registrar água",
             "O seu saldo num anel, com a quantidade para agora."),
            ("notification", "Notificação do HydroPulse sugerindo 100 mL com registro em um toque",
             "Um toque para registrar, outro para adiar."),
            ("history", "O histórico com as bebidas do dia",
             "O que você realmente bebeu hoje."),
            ("settings", "Ajustes com peso, unidades e limite",
             "Peso, unidades, limite — o modelo se ajusta a você."),
        ],
    },
    "home": {
        "title": "HydroPulse — Lembrete de água para Wear OS",
        "desc": "Um lembrete de água para Wear OS que se adapta ao seu pulso, à sua atividade e ao "
                "clima, e avisa quando o seu corpo precisa de água — não num horário fixo.",
        "h1": "Lembretes de água que seguem o seu corpo, não o relógio",
        "lede": "A maioria dos apps de beber água divide uma meta pelas horas acordado e vibra no "
                "cronômetro. O HydroPulse calcula no relógio um balanço hídrico com pulso, atividade e "
                "clima, e avisa quando o balanço realmente cai.",
        "intro": [
            "Uma hora sentado no escritório com ar-condicionado e uma hora correndo em pleno verão "
            "custam quantidades de água muito diferentes. Um intervalo fixo não vê a diferença: "
            "incomoda quando você não precisa e fica em silêncio quando precisa.",
            "O HydroPulse mantém um balanço contínuo. Ele cai com a sua necessidade básica, com o suor "
            "que o seu pulso revela e com o calor; cada bebida o recarrega. Num dia fresco e calmo "
            "você quase não ouve falar dele; num dia quente de treino, ele avisa cedo.",
            "Feito para o pulso: um Bloco, uma complicação, registro com um toque e uma recomendação "
            "que sempre diz quanto e por quê.",
        ],
    },
    "topics": {
        "wearos": {
            "slug": "lembrete-de-agua-wear-os",
            "nav": "Wear OS",
            "card": "Um lembrete de água feito para o relógio, não um app de celular com complicação.",
            "title": "App lembrete de água para Wear OS — HydroPulse",
            "desc": "Um lembrete de água nativo para Wear OS com Bloco, complicação e registro em um "
                    "toque. Funciona em Pixel Watch, Galaxy Watch e relógios Wear OS 3.0+.",
            "h1": "Um lembrete de água feito para Wear OS",
            "lede": "Bloco, complicação, ações na notificação e um modelo no relógio: o HydroPulse "
                    "pensa no pulso, então o lembrete chega onde as suas mãos já estão.",
            "why_title": "Por que o relógio é o lugar certo",
            "why": [
                "O hábito de beber água falha por atrito. Entre “preciso beber” e um copo registrado "
                "costuma haver um celular em outro cômodo. Uma notificação no pulso com botão de "
                "registro reduz isso a um toque.",
                "Só o relógio sabe o quanto você está se esforçando. Pulso e treino vêm do sensor no "
                "braço, então a estimativa vem do seu corpo, não de uma contagem de passos.",
                "Muitos apps de hidratação são apps de celular com uma complicação de brinde. O "
                "HydroPulse é um app Wear OS: o modelo, o balanço e os dados ficam no relógio.",
            ],
            "works_on": [
                "Um Bloco com o seu saldo atual, sem abrir nada.",
                "Uma complicação para o mostrador.",
                "Notificações com “Registrar água” e “Adiar 15 min”.",
                "Wear OS 3.0 ou superior: Pixel Watch, Galaxy Watch 4 e posteriores, TicWatch e outros.",
            ],
            "expect": "Instale no relógio, ajuste o peso e as unidades uma vez e permita pulso, atividade "
                      "e localização aproximada. Cada permissão alimenta uma parte do modelo; sem elas o "
                      "app usa valores padrão razoáveis. Consumo de bateria baixo.",
            "faq": [
                ("Preciso do celular?",
                 "Não. O modelo, o balanço e o registro rodam no relógio. Só o clima precisa de conexão."),
                ("Em quais relógios funciona?",
                 "Em qualquer relógio com Wear OS 3.0 ou superior e Google Play: Pixel Watch, Galaxy "
                 "Watch 4 e posteriores, TicWatch e modelos semelhantes."),
                ("Existe app para celular?",
                 "Não, de propósito. Tudo o que você precisa está no relógio: nada para sincronizar, "
                 "nenhuma conta."),
            ],
        },
        "galaxy": {
            "slug": "lembrete-de-agua-galaxy-watch",
            "nav": "Galaxy Watch",
            "card": "Um lembrete de água para Galaxy Watch 4 e posteriores que segue o pulso e o calor.",
            "title": "Lembrete de água para Samsung Galaxy Watch — HydroPulse",
            "desc": "Um lembrete de água para Galaxy Watch 4, 5, 6, 7 e Ultra que considera o pulso, "
                    "os treinos e o clima, com Bloco e registro em um toque.",
            "h1": "Um lembrete para beber água no Samsung Galaxy Watch",
            "lede": "Desde o Galaxy Watch 4, todos os modelos usam Wear OS, então o HydroPulse é "
                    "instalado direto do Google Play no relógio. Ele faz o que o contador de água do "
                    "Samsung Health não faz: dizer quando beber e quanto.",
            "why_title": "O que ele acrescenta ao Samsung Health",
            "why": [
                "O Samsung Health conta os copos registrados contra uma meta diária, mas espera você "
                "lembrar. O HydroPulse estima a sua perda pelo pulso, pela atividade e pelo calor, e "
                "avisa quando o balanço realmente cai.",
                "Num dia fresco no escritório você quase não ouve falar dele; numa tarde quente ou num "
                "pedal longo, ele avisa cedo, com quantidade e motivo.",
                "Cada bebida pode ser gravada também no Health Connect.",
            ],
            "works_on": [
                "Galaxy Watch 4, 5, 6, 7, Ultra e posteriores; não os antigos relógios Tizen (Galaxy Watch 3, Active 2).",
                "Instalação pelo Google Play no relógio, ou pela Play Store do celular escolhendo o relógio.",
                "Um Bloco e uma complicação para mostradores que aceitam dados de outros apps.",
                "Registrar água ou adiar 15 minutos direto na notificação.",
            ],
            "expect": "Permita pulso, atividade e localização aproximada. As configurações de bateria da "
                      "Samsung podem colocar apps pouco usados para dormir; se os lembretes pararem, "
                      "tire o HydroPulse dos “apps em suspensão”.",
            "faq": [
                ("O HydroPulse funciona no Galaxy Watch?",
                 "Sim, no Galaxy Watch 4 e em todos os modelos posteriores, com Wear OS 3 ou superior. "
                 "Os antigos Galaxy com Tizen não instalam apps Wear OS."),
                ("Ainda preciso do Samsung Health?",
                 "Não, o HydroPulse funciona sozinho. Com o Health Connect, as suas bebidas também vão "
                 "para lá."),
            ],
        },
        "pixel": {
            "slug": "lembrete-de-agua-pixel-watch",
            "nav": "Pixel Watch",
            "card": "Lembretes de água e registro em um toque no Google Pixel Watch.",
            "title": "Lembrete de água para Google Pixel Watch — HydroPulse",
            "desc": "Um lembrete de água para Pixel Watch 1, 2, 3 e 4: lê o pulso e o clima para "
                    "dizer quando beber, com Bloco e registro em um toque.",
            "h1": "Um lembrete para beber água no Google Pixel Watch",
            "lede": "Muita gente procura como registrar água e receber lembretes direto no Pixel "
                    "Watch. O HydroPulse faz as duas coisas no pulso, e escolhe a hora do lembrete "
                    "pelo pulso e pelo calor, não pelo relógio.",
            "why_title": "Por que usar no Pixel Watch",
            "why": [
                "No Fitbit, o registro de água fica sobretudo no app do celular. O HydroPulse mantém "
                "tudo no relógio: Bloco com o saldo, notificação com botão de registro e histórico do dia.",
                "Os lembretes não são de hora em hora: seguem uma estimativa contínua do sensor de "
                "pulso, da atividade e do clima.",
                "As bebidas podem ser gravadas no Health Connect.",
            ],
            "works_on": [
                "Pixel Watch, Pixel Watch 2, 3 e 4 (Wear OS 3 ou superior).",
                "Bloco, complicação e ações na notificação.",
                "Funciona sem o celular por perto.",
            ],
            "expect": "Instale pelo Google Play no relógio, ajuste peso e unidades uma vez e permita "
                      "pulso, atividade e localização aproximada. Consumo de bateria baixo.",
            "faq": [
                ("Dá para registrar água no Pixel Watch?",
                 "Sim, com o HydroPulse: pelo Bloco, pela notificação ou pelo app, com um toque."),
                ("Sincroniza com o Fitbit?",
                 "O HydroPulse grava as bebidas no Health Connect. Se o Fitbit as mostra depende do "
                 "suporte ao Health Connect no app do Fitbit."),
            ],
        },
        "best": {
            "slug": "melhores-apps-lembrete-de-agua-wear-os",
            "nav": "Melhores apps Wear OS",
            "card": "Rastreadores integrados, apps de cronômetro e lembretes adaptativos no Wear OS.",
            "title": "Melhores apps de lembrete de água para Wear OS (2026)",
            "desc": "Samsung Health, Fitbit, apps de cronômetro e HydroPulse comparados em relógios "
                    "Wear OS: o que cada um faz no pulso e para quem serve.",
            "h1": "Apps de lembrete de água para Wear OS, comparados",
            "lede": "Três tipos de ferramenta podem lembrar você de beber água num relógio Wear OS: o "
                    "rastreador que vem com ele, um app que vibra em horários fixos e um app que "
                    "estima a sua necessidade. Esta página é escrita pelos criadores do HydroPulse.",
            "why_title": "As três abordagens",
            "why": [
                "Rastreadores integrados. O Samsung Health conta copos contra uma meta; o Fitbit permite "
                "registrar água, mais pelo celular. Grátis e já instalados, mas contam mais do que "
                "lembram.",
                "Apps de cronômetro. A maioria dos apps de beber água no Google Play divide uma meta em "
                "intervalos fixos e vibra a cada hora. Simples, muitas vezes grátis com anúncios; mas o "
                "cronômetro não diferencia o escritório de uma corrida no sol.",
                "Lembretes adaptativos. O HydroPulse calcula no relógio um balanço com pulso, atividade "
                "e clima, e avisa quando ele cai, com quantidade e motivo. App pago, compra única, sem "
                "anúncios.",
            ],
            "works_on": [
                "Rastreador integrado se você só quer contar copos, sem lembretes.",
                "App de cronômetro se os seus dias são regulares.",
                "HydroPulse se você treina, trabalha no calor ou já silenciou cronômetros antes.",
            ],
            "expect": "O HydroPulse precisa de um relógio com Wear OS 3 ou superior. Os lembretes são "
                      "estimativas, não medições, e não é um dispositivo médico.",
            "faq": [
                ("Qual é o melhor app de lembrete de água para Wear OS?",
                 "Depende do que você quer: Samsung Health ou Fitbit para contar copos, um app de "
                 "cronômetro para avisos regulares, HydroPulse para lembretes que seguem pulso, "
                 "atividade e clima."),
                ("Existe opção grátis?",
                 "Sim, os rastreadores integrados e muitos apps de cronômetro são grátis, muitas vezes "
                 "com anúncios. O HydroPulse é compra única, sem anúncios e sem assinatura."),
            ],
        },
    },
}
