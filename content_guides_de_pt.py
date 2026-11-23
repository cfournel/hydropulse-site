# -*- coding: utf-8 -*-
"""German and Portuguese versions of the six background guides (sport, heat, work, howmuch,
signs, heartrate), added 2026-11-23 so DE and PT carry the same topics as EN/FR/ES.
Translated from the English copy in content.py; keep the facts aligned when one changes."""

DE_GUIDES = {
    "sport": {
        "slug": "trinken-beim-laufen-und-training",
        "nav": "Laufen & Training",
        "card": "Erinnerungen nach Schweißrate für Läufe, Radtouren und das Fitnessstudio.",
        "title": "Richtig trinken beim Laufen und Training — Schweißrate",
        "desc": "Wie viel du beim Training trinken solltest und wie HydroPulse den Schweißverlust "
                "aus Herzfrequenzreserve und Wetter schätzt statt nach fester Stundenregel.",
        "h1": "Trinken beim Laufen und Training",
        "lede": "Die Schweißrate reicht je nach Mensch und Bedingungen von etwa 0,5 bis über 2 Liter "
                "pro Stunde. Eine einzige Stundenmenge kann das nicht abdecken — Puls und Wetter "
                "können es eingrenzen.",
        "why_title": "Warum eine feste Stundenmenge bei Sport versagt",
        "why": [
            "Zwei Läufer auf denselben 10 km können sich im Flüssigkeitsverlust um den Faktor drei "
            "unterscheiden, je nach Körpermasse, Fitness, Hitzegewöhnung und Tagestemperatur. "
            "Allgemeine Ratschläge müssen einen Mittelwert wählen: zu wenig für starke Schwitzer, zu "
            "viel für alle anderen.",
            "Die Anstrengung entgeht einem Schrittzähler völlig. Die Herzfrequenzreserve — wo dein "
            "aktueller Puls zwischen Ruhe- und Maximalpuls liegt — bildet die Stoffwechsellast viel "
            "besser ab als Tempo oder Schrittfrequenz, und diese Last treibt das Schwitzen an.",
            "Die Erholung zählt so viel wie die Einheit. Ein Defizit aus einer harten Stunde "
            "verschwindet nicht an der Ziellinie; HydroPulse hält die Bilanz danach im Minus und "
            "erinnert weiter, bis es ausgeglichen ist.",
        ],
        "works_on": [
            "Ein Anstrengungsanteil aus der Herzfrequenzreserve: lockerer Dauerlauf und Schwellenlauf werden nicht gleich behandelt.",
            "Ein Schweißprofil (wenig, mittel, stark) zur persönlichen Kalibrierung.",
            "Hitzeindex-Skalierung: dieselbe Einheit im Juli verlangt mehr als im November.",
            "Ein Defizit nach dem Training, das weiterläuft statt zurückgesetzt zu werden.",
            "Dringlichkeitsstufen: ein leichter Hinweis beim Aufwärmen sieht anders aus als ein dringender bei Kilometer 15.",
        ],
        "expect": "Am genauesten wird es, wenn du deinen Ruhe- und Maximalpuls einträgst statt der "
                  "Altersschätzung, und das Schweißprofil wählst, das zu dir passt. Wer sich schon "
                  "einmal vor und nach einer langen Einheit gewogen hat: Die Differenz in Kilogramm "
                  "entspricht etwa dem Verlust in Litern — die wertvollste Angabe zur Kalibrierung.",
        "faq": [
            ("Ersetzt das einen echten Schweißtest?",
             "Nein. Sich vor und nach einer Einheit unter bekannten Bedingungen zu wiegen bleibt der "
             "Goldstandard. HydroPulse schätzt laufend aus Sensordaten: im Alltag viel praktischer, "
             "aber weniger genau als ein kontrollierter Test."),
            ("Kommt es mit dem Trinken im Wettkampf klar?",
             "Es schätzt weiter und rechnet eingetragene Getränke an; das Eintragen aus der "
             "Benachrichtigung geht schnell. Viele schlummern es im Rennen und schauen danach im "
             "Verlauf, wie groß das Defizit war."),
            ("Und Elektrolyte?",
             "HydroPulse verfolgt die Flüssigkeitsmenge, nicht Natrium. Bei langen oder sehr heißen "
             "Einheiten ist der Elektrolytersatz eine eigene Frage — viel reines Wasser über viele "
             "Stunden ist nicht risikofrei."),
            ("Zählen Kaffee und Tee?",
             "Du kannst jedes Getränk eintragen. Mäßig koffeinhaltige Getränke tragen bei "
             "Gewohnheitstrinkern zur Tagesmenge bei; Alkohol wirkt dagegen."),
        ],
    },
    "heat": {
        "slug": "trinken-bei-hitze",
        "nav": "Hitze",
        "card": "Wenn Hitze und Luftfeuchte den Bedarf erhöhen, kommen die Erinnerungen früher.",
        "title": "Trinken bei Hitze — Erinnerungen, die das Wetter kennen",
        "desc": "Hitze und Luftfeuchte ändern deinen Bedarf lange bevor du Durst spürst. Wie "
                "HydroPulse Live-Wetter und den Hitzeindex nutzt, um früher zu erinnern.",
        "h1": "Trinken bei Hitze",
        "lede": "Die Luftfeuchte wird unterschätzt: Wenn Schweiß nicht verdunsten kann, produziert "
                "der Körper mehr davon bei weniger Kühlung. HydroPulse liest Temperatur und "
                "Luftfeuchte und verschiebt deine Erinnerungen entsprechend.",
        "why_title": "Warum das Thermometer allein nicht reicht",
        "why": [
            "Bei 32 °C und 30 % Luftfeuchte verdunstet Schweiß und kühlt. Bei gleicher Temperatur und "
            "75 % läuft er ab, du verlierst die Flüssigkeit ohne Kühlung, und der Körper schwitzt "
            "mehr. Genau diesen Unterschied erfasst der Hitzeindex, und den nutzt HydroPulse.",
            "Durst kommt bei Hitze zu spät. Wenn er drängt, fehlen oft schon ein bis zwei Prozent "
            "des Körpergewichts, und bei Hitze öffnet sich diese Lücke schneller, als das Gefühl "
            "nachkommt.",
            "Hitze erhöht den Bedarf auch, wenn du gar nichts tust. Ein ruhiger Nachmittag auf dem "
            "Balkon kostet echte Flüssigkeit, die kein Aktivitätstracker sieht; deshalb gilt der "
            "Umweltfaktor für den Grundbedarf, nicht nur für Training.",
        ],
        "works_on": [
            "Live-Temperatur und Luftfeuchte, anonym von einem öffentlichen Wetterdienst.",
            "Ein Hitzeindex-Faktor auf den Grundverlust, nicht nur aufs Training.",
            "Frühere und häufigere Hinweise an heißen Tagen, ohne dass du etwas einstellst.",
            "Nur ungefährer Standort — genug fürs Wetter, nie genaue Ortung.",
            "Wetter 30 Minuten zwischengespeichert, also kaum Akkuverbrauch.",
        ],
        "expect": "An einem richtig heißen Tag fragt die App früher und nach mehr, an einem kühlen "
                  "wird sie still. Dieser Kontrast ist die Funktion. Der ungefähre Standort ist "
                  "optional; ohne ihn nimmt die App gemäßigtes Wetter an — sicher, aber grob bei "
                  "einer Hitzewelle.",
        "faq": [
            ("Nutzt sie den genauen Standort?",
             "Nein. Sie fragt nur nach dem ungefähren Standort, nutzt ihn für das Wetter vor Ort und "
             "speichert ihn nicht. Die Anfrage enthält Koordinaten, nichts, was dich identifiziert."),
            ("Und wenn ich den Standort ablehne?",
             "Die App funktioniert weiter mit einem gemäßigten Standardwert. Puls und Aktivität "
             "steuern die Schätzung weiterhin; nur der Wetteranteil fehlt."),
            ("Kann zu viel Trinken ein Problem sein?",
             "Ja. Sehr große Mengen reines Wasser in kurzer Zeit können das Natrium im Blut "
             "verdünnen, was gefährlich ist. HydroPulse empfiehlt maßvolle, über den Tag verteilte "
             "Mengen."),
        ],
    },
    "work": {
        "slug": "trinken-vergessen-bei-der-arbeit",
        "nav": "Bei der Arbeit",
        "card": "Für Bürotage, an denen sechs Stunden zwischen zwei Gläsern verschwinden.",
        "title": "Trinken vergessen bei der Arbeit — eine passende Erinnerung",
        "desc": "Warum Bürotage im Flüssigkeitsdefizit enden und wie eine Erinnerung am Handgelenk "
                "mit Eintragen per Tipp und Ruhezeiten einen vollen Kalender übersteht.",
        "h1": "Trinken vergessen bei der Arbeit",
        "lede": "Niemand vergisst zu trinken, weil er nicht weiß, dass er sollte. Man vergisst es, "
                "weil Konzentration ein schwaches Signal stundenlang unterdrückt.",
        "why_title": "Warum es im Büro leise schiefgeht",
        "why": [
            "Konzentriertes Arbeiten und Meetings am Stück tun dasselbe mit dem Durst: Sie drücken "
            "ein schwaches Signal unter die Schwelle, ab der du handeln würdest. Das Defizit wächst "
            "langsam und fällt erst mit den Kopfschmerzen am späten Nachmittag auf.",
            "Klimaanlage und Heizung trocknen die Luft, und ein warmes Großraumbüro liegt höher auf "
            "der Umweltskala als gedacht. Nichts davon ist dramatisch; über acht Stunden summiert "
            "es sich.",
            "Die meisten Erinnerungs-Apps fliegen bei der Arbeit raus, weil sie in Meetings und um "
            "23 Uhr vibrieren. Eine Erinnerung, die immer falsch liegt, lernt man ungelesen "
            "wegzuwischen.",
        ],
        "works_on": [
            "Ruhezeiten: nachts oder im gesperrten Zeitraum kommt nichts.",
            "15 Minuten schlummern, wenn der Hinweis mitten im Meeting kommt.",
            "Eintragen mit einem Tipp am Handgelenk — kein Handy, kein App-Wechsel.",
            "Weniger Hinweise an ruhigen Tagen, weil die Bilanz dann langsamer sinkt.",
            "Eine Kachel für einen Blick zwischen zwei Calls.",
        ],
        "expect": "An einem normalen Bürotag kommen wenige Hinweise statt eines Stundentakts, jeder "
                  "mit einer Menge, damit die Entscheidung schon getroffen ist. Zu oft oder zu "
                  "selten? Die Schwelle in den Einstellungen verschiebt den Auslöser.",
        "faq": [
            ("Vibriert sie in Meetings?",
             "Das kann passieren, dafür gibt es „15 Min. später“. Ruhezeiten decken wiederkehrende "
             "Blöcke ab; für einzelne Meetings reicht ein Tipp auf der Benachrichtigung."),
            ("Kann ich sie insgesamt leiser stellen?",
             "Ja — erhöhe die Schwelle in den Einstellungen, dann muss die Bilanz weiter sinken, bevor "
             "ein Hinweis kommt. Senke sie, wenn du früher erinnert werden willst."),
            ("Nervt sie, wenn ich sie ignoriere?",
             "Nein. Beim Schlummern und in Ruhezeiten bleibt sie still. Die Dringlichkeit steigt mit "
             "dem Defizit, aber sie wiederholt sich nicht um der Wiederholung willen."),
        ],
    },
    "howmuch": {
        "slug": "wie-viel-wasser-am-tag-trinken",
        "nav": "Wie viel pro Tag",
        "card": "Woher die 2-Liter-Regel kommt und warum deine Zahl eine andere ist.",
        "title": "Wie viel Wasser am Tag trinken? Eine persönliche Antwort",
        "desc": "Die Acht-Gläser-Regel ist ein Durchschnitt, nicht dein Ziel. Was deinen täglichen "
                "Bedarf bestimmt und wie eine Uhr ihn Stunde für Stunde schätzen kann.",
        "h1": "Wie viel Wasser sollte man am Tag trinken?",
        "lede": "Ehrlich gesagt ist eine einzige Tageszahl die falsche Einheit. Dein Bedarf hängt von "
                "Körpermasse, Anstrengung und Umgebung ab, und alle drei ändern sich von Tag zu Tag.",
        "why_title": "Woher die bekannten Zahlen kommen",
        "why": [
            "„Acht Gläser“ oder „zwei Liter“ gehen auf Referenzwerte für die Bevölkerung zurück: Das "
            "US Institute of Medicine nennt rund 3,7 L Wasser am Tag für Männer und 2,7 L für Frauen, "
            "die EFSA ähnliche Werte. Beides sind Gesamtmengen aus allen Quellen, Essen inklusive, und "
            "Durchschnitte, keine Vorgaben für eine Person.",
            "Die Körpermasse ist der größte Einzelfaktor, deshalb passt derselbe Rat nicht für 55 kg "
            "und 95 kg. Alter, Geschlecht, Schwangerschaft oder Stillzeit verschieben den Grundbedarf "
            "weiter — jeweils mehr als der Unterschied zwischen sechs und acht Gläsern.",
            "Dazu kommt der Tag selbst. Ein heißer Nachmittag oder ein hartes Training können mehr "
            "ausmachen als die ganze Debatte um den Grundbedarf. Deshalb berechnet HydroPulse einen "
            "Grundbedarf aus deinen Werten und passt ihn laufend an, statt dir morgens ein festes "
            "Ziel zu geben.",
        ],
        "works_on": [
            "Ein Grundbedarf aus Gewicht, Alter und Geschlecht, nicht aus einem Durchschnitt.",
            "Anpassung für Schwangerschaft oder Stillzeit, die den Bedarf messbar erhöhen.",
            "Laufende Anpassung an Anstrengung und Wetter statt eines Morgenziels.",
            "Eine Empfehlung in mL oder fl oz, damit „wie viel jetzt“ eine Antwort hat.",
            "Ein Verlauf, der zeigt, was der Tag wirklich ergeben hat.",
        ],
        "expect": "Rechne mit einer persönlichen Tagesmenge, die sich bewegt — an einem kühlen, "
                  "ruhigen Tag oft deutlich unter zwei Litern, an einem heißen, aktiven Tag weit "
                  "darüber. Essen liefert etwa ein Fünftel des Wassers; HydroPulse schätzt das nicht, "
                  "seine Zahlen beschreiben, was du trinkst.",
        "faq": [
            ("Sind zwei Liter am Tag falsch?",
             "Nicht falsch, nur allgemein. Ein vernünftiger Mittelwert für eine Bevölkerung, aber ein "
             "schlechtes Ziel für eine bestimmte Person an einem bestimmten Tag."),
            ("Zählt Essen mit?",
             "Ja, etwa 20 % des Wassers kommen bei normaler Ernährung aus dem Essen. HydroPulse "
             "erfasst nur Getränke."),
            ("Nach Plan oder nach Durst trinken?",
             "Für die meisten gesunden Erwachsenen reicht der Durst im Alltag. Weniger zuverlässig "
             "wird er im Alter, bei Hitze, bei hartem Training und bei starker Konzentration — genau "
             "die Fälle, für die diese App gedacht ist."),
        ],
    },
    "signs": {
        "slug": "anzeichen-von-dehydrierung",
        "nav": "Anzeichen von Dehydrierung",
        "card": "Wie sich leichte Dehydrierung anfühlt — und wann sie nicht mehr leicht ist.",
        "title": "Anzeichen von Dehydrierung — worauf achten, wann handeln",
        "desc": "Leichte Dehydrierung zeigt sich als Müdigkeit, Kopfschmerz und Konzentrationsmangel, "
                "lange bevor Durst drängt. Frühe und ernste Zeichen, und wo eine App passt.",
        "h1": "Anzeichen von Dehydrierung",
        "lede": "Ein bis zwei Prozent des Körpergewichts an Flüssigkeit zu verlieren reicht, um "
                "Konzentration und Stimmung zu dämpfen. Selten als Durst — öfter als matter "
                "Nachmittag, den man etwas anderem zuschreibt.",
        "why_title": "Frühe Zeichen und die, die wirklich zählen",
        "why": [
            "Typische frühe Zeichen: dunkler oder seltener Urin, dumpfer Kopfschmerz, Müdigkeit, die "
            "nicht zur Nacht passt, trockener Mund und trockene Lippen, nachlassende Konzentration oder "
            "Laune. Die Urinfarbe ist am praktischsten: hellgelb ist das Ziel, dunkler als Apfelsaft "
            "ein Grund zu handeln.",
            "Durst kommt spät und unzuverlässig. Er ist im Alter, bei intensivem Sport, bei Kälte und "
            "bei Vertiefung abgeschwächt — „ich trinke, wenn ich Durst habe“ klappt in der Theorie "
            "besser als an einem Augustnachmittag.",
            "Manche Zeichen löst kein Glas Wasser. Verwirrtheit, Ohnmacht, Herzrasen in Ruhe, viele "
            "Stunden ohne Urin oder heiße, trockene Haut mit Desorientierung brauchen ärztliche Hilfe, "
            "keine App. Ebenso Dehydrierung mit Erbrechen oder Durchfall, besonders bei Kindern und "
            "älteren Menschen.",
        ],
        "works_on": [
            "Ein Hinweis vor Müdigkeit und Kopfschmerz: genau dafür wird geschätzt statt reagiert.",
            "Der Grund wird genannt — Hitze, Anstrengung oder Grundbedarf —, damit das Signal verständlich ist.",
            "Steigende Dringlichkeit mit wachsendem geschätztem Defizit.",
            "Ein Verlauf, in den du schauen kannst, wenn ein Nachmittag schlecht lief.",
            "Keine Diagnose: Die App schätzt eine Bilanz und sagt nichts über deinen Gesundheitszustand.",
        ],
        "expect": "Regelmäßig genutzt ist der Effekt unspektakulär — das Tief um 16 Uhr bleibt aus. "
                  "Ob du dehydriert bist, kann sie nicht sagen: Sie schätzt eine Bilanz aus Sensoren "
                  "und deinen Einträgen, und die Zeichen oben bleiben das, worauf du achten solltest.",
        "faq": [
            ("Kann eine Smartwatch Dehydrierung erkennen?",
             "Keine Verbraucheruhr misst den Wasserhaushalt direkt. HydroPulse schätzt die Bilanz aus "
             "Puls, Aktivität, Wetter und Einträgen — eine begründete Schätzung, keine Messung und "
             "keine Diagnose."),
            ("Ist die Urinfarbe zuverlässig?",
             "Sie ist die praktischste Alltagsprüfung. Hellgelb heißt im Plan, dunkler heißt im "
             "Rückstand. Manche Vitamine, Medikamente und Lebensmittel färben ihn unabhängig davon."),
            ("Wann zum Arzt?",
             "Verwirrtheit, Ohnmacht, Herzrasen in Ruhe, viele Stunden ohne Urin oder Zeichen eines "
             "Hitzeschadens brauchen dringend Hilfe, ebenso Dehydrierung mit anhaltendem Erbrechen oder "
             "Durchfall, besonders bei Kindern und Älteren."),
        ],
    },
    "heartrate": {
        "slug": "puls-und-trinken",
        "nav": "Puls & Trinken",
        "card": "Der Zusammenhang zwischen kardialem Drift, Anstrengung und Flüssigkeitsverlust.",
        "title": "Puls und Trinken — wie eine Uhr den Schweißverlust schätzt",
        "desc": "Warum der Puls ein besserer Hinweis auf Flüssigkeitsverlust ist als Schritte, was die "
                "Herzfrequenzreserve ist und wie HydroPulse daraus mL pro Stunde macht.",
        "h1": "Puls und Trinken",
        "lede": "Der Puls ist das einzige ständig verfügbare Signal an der Uhr, das zeigt, wie hart "
                "dein Körper arbeitet. Damit ist er der beste verfügbare Hinweis darauf, wie schnell "
                "du Flüssigkeit verlierst.",
        "why_title": "Warum Puls und nicht Schritte",
        "why": [
            "Schritte sagen, wie viel du dich bewegt hast, nicht wie anstrengend es war. Zehntausend "
            "flache Schritte im Schatten und fünftausend bergauf in der Sonne ergeben dieselbe Zahl "
            "und ganz andere Kosten. Der Puls trennt sie, weil er auf Last reagiert, nicht auf Strecke.",
            "Die nützliche Form ist die Herzfrequenzreserve: wo dein Puls zwischen deinem eigenen Ruhe- "
            "und Maximalpuls liegt. So bedeuten 140 Schläge für eine trainierte 30-Jährige etwas "
            "anderes als für einen untrainierten 55-Jährigen. Die Schweißrate folgt dem Stoffwechsel, "
            "und die Herzfrequenzreserve ist außerhalb des Labors ein guter Stellvertreter dafür.",
            "Es gibt eine Rückkopplung: Mit dem Flüssigkeitsverlust sinkt das Plasmavolumen, und der "
            "Puls steigt bei gleicher Leistung — der kardiale Drift. Ein steigender Puls in einer "
            "langen, gleichmäßigen Einheit ist selbst ein schwacher Hinweis auf ein wachsendes Defizit.",
        ],
        "works_on": [
            "Laufende passive Pulsmessung über Wear OS Health Services.",
            "Herzfrequenzreserve aus deinem eigenen Ruhe- und Maximalpuls, in den Einstellungen änderbar.",
            "Trainingserkennung: echtes Training wird anders gewichtet als Zappeln.",
            "Ein Schweißfaktor, der Anstrengung und Hitzeindex zusammen betrachtet.",
            "Transparenz: Jede Empfehlung sagt, ob Hitze, Anstrengung oder Grundbedarf sie ausgelöst hat.",
        ],
        "expect": "Trage Ruhe- und Maximalpuls ein, wenn du sie kennst; die Altersformel (etwa 220 "
                  "minus Alter) streut stark, und sie zu korrigieren bringt die größte Verbesserung. "
                  "Optische Sensoren werden bei hoher Intensität und Kälte ungenauer — die Schätzung "
                  "ist nur so gut wie das Signal.",
        "faq": [
            ("Erhöht Dehydrierung den Puls?",
             "Ja. Flüssigkeitsverlust senkt das Plasmavolumen, also schlägt das Herz schneller — der "
             "kardiale Drift bei langer Belastung. Ein Signal unter mehreren, kein Wassermessgerät."),
            ("Muss ich meinen Maximalpuls kennen?",
             "Nein, die App nimmt sonst eine Altersschätzung. Diese Formel streut aber um rund zehn "
             "Schläge pro Minute, ein gemessener Wert schärft das Modell deutlich."),
            ("Kostet die Pulsmessung den ganzen Tag viel Akku?",
             "Sie nutzt passive Messung statt eines dauernden schnellen Datenstroms — den sparsamen "
             "Weg, den Wear OS genau dafür bietet."),
        ],
    },
}

PT_GUIDES = {
    "sport": {
        "slug": "hidratacao-para-corrida-e-treino",
        "nav": "Corrida e treino",
        "card": "Lembretes que consideram o suor em corridas, pedais e academia.",
        "title": "Hidratação na corrida e no treino — taxa de suor",
        "desc": "Quanto beber quando você treina e como o HydroPulse estima a perda de suor pela "
                "reserva cardíaca e pelo clima, em vez de uma regra fixa por hora.",
        "h1": "Hidratação para corrida e treino",
        "lede": "A taxa de suor varia de cerca de 0,5 a mais de 2 litros por hora entre pessoas e "
                "condições. Um único número por hora não cobre essa faixa — o pulso e o clima ajudam "
                "a estreitá-la.",
        "why_title": "Por que uma quantidade fixa por hora falha no esporte",
        "why": [
            "Dois corredores nos mesmos 10 km podem perder quantidades de líquido que variam três "
            "vezes, conforme massa corporal, condicionamento, aclimatação e calor do dia. Um conselho "
            "genérico escolhe um meio-termo: pouco para quem sua muito, demais para os outros.",
            "O esforço é o que o contador de passos não vê. A reserva cardíaca — onde o seu pulso "
            "atual fica entre o de repouso e o máximo — acompanha a carga metabólica muito melhor do "
            "que ritmo ou cadência, e é essa carga que faz você suar.",
            "A recuperação conta tanto quanto o treino. O déficit de uma hora puxada não some na linha "
            "de chegada; o HydroPulse mantém o balanço negativo depois e continua lembrando até ele "
            "ser reposto.",
        ],
        "works_on": [
            "Um componente de esforço pela reserva cardíaca: trote leve e limiar não são tratados igual.",
            "Um perfil de suor (pouco, médio, muito) para calibrar.",
            "Escala pelo índice de calor: o mesmo treino em janeiro pede mais do que em julho.",
            "Déficit pós-treino que continua em vez de zerar.",
            "Níveis de urgência: um aviso leve no aquecimento não parece um urgente no km 15.",
        ],
        "expect": "Para melhores resultados, informe o seu pulso de repouso e máximo em vez da "
                  "estimativa por idade, e escolha o perfil de suor que combina com você. Se já se "
                  "pesou antes e depois de um treino longo, a diferença em quilos é mais ou menos a "
                  "perda em litros — a calibração mais útil que existe.",
        "faq": [
            ("Substitui um teste de taxa de suor?",
             "Não. Pesar-se antes e depois de um treino em condições conhecidas continua sendo o "
             "padrão-ouro. O HydroPulse estima continuamente por sensores: mais prático no dia a dia, "
             "menos preciso que um teste controlado."),
            ("Funciona para beber durante uma prova?",
             "Ele continua estimando e creditando o que você registra, e o registro pela notificação é "
             "rápido. Muitos atletas adiam os avisos na prova e olham o histórico depois."),
            ("E os eletrólitos?",
             "O HydroPulse acompanha o volume de líquido, não o sódio. Em treinos longos ou muito "
             "quentes, repor eletrólitos é outra questão — beber muita água pura por horas não é "
             "isento de risco."),
            ("Café e chá contam?",
             "Você pode registrar qualquer bebida. Bebidas com cafeína moderada contam para quem as "
             "consome com frequência; o álcool é o que joga contra."),
        ],
    },
    "heat": {
        "slug": "beber-agua-no-calor",
        "nav": "Calor",
        "card": "Quando calor e umidade aumentam a necessidade, os lembretes chegam antes.",
        "title": "Beber água no calor — lembretes que conhecem o clima",
        "desc": "Calor e umidade mudam quanto você precisa beber muito antes da sede. Como o "
                "HydroPulse usa o clima ao vivo e o índice de calor para lembrar mais cedo.",
        "h1": "Beber água no calor",
        "lede": "A umidade é a parte subestimada: quando o suor não evapora, o corpo produz mais suor "
                "para resfriar menos. O HydroPulse lê temperatura e umidade e ajusta os lembretes.",
        "why_title": "Por que só o termômetro não basta",
        "why": [
            "A 32 °C e 30 % de umidade o suor evapora e resfria. Na mesma temperatura com 75 % ele "
            "escorre, você perde o líquido sem o resfriamento, e o corpo sua mais. O índice de calor "
            "existe para captar essa diferença, e é ele que entra no modelo.",
            "No calor, a sede chega atrasada. Quando ela insiste, muitas vezes já falta um ou dois por "
            "cento do peso corporal, e no calor essa diferença abre mais rápido do que a sensação.",
            "O calor aumenta a necessidade mesmo parado. Uma tarde quente na varanda tem um custo real "
            "que nenhum rastreador de atividade registra; por isso o fator ambiental vale para a "
            "necessidade básica, não só para o exercício.",
        ],
        "works_on": [
            "Temperatura e umidade ao vivo, de um serviço público de clima, de forma anônima.",
            "Um multiplicador de índice de calor sobre a perda básica, não só nos treinos.",
            "Avisos mais cedo e mais frequentes em dias quentes, sem mudar nenhum ajuste.",
            "Só localização aproximada — o bastante para o clima, nunca rastreamento preciso.",
            "Clima guardado por 30 minutos, quase sem gasto de bateria.",
        ],
        "expect": "Num dia realmente quente o app pede antes e pede mais; num dia fresco fica quieto. "
                  "Esse contraste é a função. A localização aproximada é opcional; sem ela o app usa "
                  "um clima ameno padrão — seguro, mas impreciso numa onda de calor.",
        "faq": [
            ("Usa a localização precisa?",
             "Não. Pede só a localização aproximada, usa para o clima local e não a guarda. A "
             "consulta leva coordenadas e nada que identifique você."),
            ("E se eu recusar a localização?",
             "O app continua funcionando com um clima ameno padrão. Pulso e atividade seguem guiando "
             "a estimativa; só falta a parte do clima."),
            ("Beber demais pode ser um problema?",
             "Sim. Beber volumes muito grandes de água pura em pouco tempo pode diluir o sódio do "
             "sangue, o que é perigoso. O HydroPulse recomenda quantidades moderadas ao longo do dia."),
        ],
    },
    "work": {
        "slug": "esquecer-de-beber-agua-no-trabalho",
        "nav": "No trabalho",
        "card": "Para dias de escritório em que seis horas somem entre dois copos.",
        "title": "Esquecer de beber água no trabalho — um lembrete que serve",
        "desc": "Por que dias de escritório terminam com déficit de líquido e como um lembrete no "
                "pulso, com registro em um toque e horário silencioso, sobrevive à agenda cheia.",
        "h1": "Esquecer de beber água no trabalho",
        "lede": "Ninguém esquece de beber por não saber que deveria. Esquece porque a concentração "
                "abafa um sinal fraco durante horas.",
        "why_title": "Por que o escritório é onde a hidratação falha em silêncio",
        "why": [
            "Trabalho focado e reuniões seguidas fazem o mesmo com a sede: empurram um sinal fraco "
            "para baixo do ponto em que você agiria. O déficit cresce devagar e só aparece com a dor "
            "de cabeça no fim da tarde.",
            "Ar-condicionado e aquecimento secam o ar, e um escritório aberto e quente fica mais alto "
            "na escala ambiental do que parece. Nada dramático; em oito horas, soma.",
            "A maioria dos apps de lembrete é desinstalada no trabalho porque vibra em reuniões e às "
            "23h. O lembrete que sempre erra é aquele que você aprende a dispensar sem ler.",
        ],
        "works_on": [
            "Horário silencioso: nada à noite nem no período que você bloquear.",
            "Adiar 15 minutos quando o aviso chega no meio de uma reunião.",
            "Registro com um toque no pulso — sem celular, sem trocar de app.",
            "Menos avisos em dias parados, porque o balanço cai mais devagar.",
            "Um Bloco para olhar entre duas chamadas.",
        ],
        "expect": "Num dia normal de escritório, espere poucos avisos em vez de um a cada hora, cada "
                  "um com uma quantidade. Frequente demais ou de menos? O limite nos ajustes muda o "
                  "ponto de disparo.",
        "faq": [
            ("Ele vibra durante reuniões?",
             "Pode acontecer, e para isso existe “Adiar 15 min”. O horário silencioso cobre blocos "
             "recorrentes; para uma reunião avulsa, basta um toque na notificação."),
            ("Posso deixá-lo mais discreto?",
             "Sim — aumente o limite nos ajustes e o balanço precisa cair mais antes de um aviso. "
             "Diminua se preferir ser lembrado antes."),
            ("Ele insiste se eu ignorar?",
             "Não. Fica quieto quando adiado e no horário silencioso. A urgência sobe com o déficit, "
             "mas ele não se repete à toa."),
        ],
    },
    "howmuch": {
        "slug": "quanta-agua-beber-por-dia",
        "nav": "Quanto por dia",
        "card": "De onde vem a regra dos 2 litros, e por que o seu número é outro.",
        "title": "Quanta água beber por dia? Uma resposta pessoal",
        "desc": "A regra dos oito copos é uma média, não a sua meta. O que define a sua necessidade "
                "diária e como um relógio pode estimá-la hora a hora.",
        "h1": "Quanta água você deve beber por dia?",
        "lede": "A resposta honesta é que um único número diário é a unidade errada. A sua necessidade "
                "depende da massa corporal, do esforço e do ambiente, e os três mudam de um dia para "
                "o outro.",
        "why_title": "De onde vêm os números conhecidos",
        "why": [
            "“Oito copos” ou “dois litros” vêm de valores de referência populacionais: o Institute "
            "of Medicine dos EUA indica cerca de 3,7 L de água por dia para homens e 2,7 L para "
            "mulheres, e a EFSA dá valores parecidos. São totais de todas as fontes, alimentos "
            "incluídos, e médias de uma população, não receitas para uma pessoa.",
            "A massa corporal é o maior fator isolado, por isso o mesmo conselho não serve para 55 kg "
            "e 95 kg. Idade, sexo, gravidez ou amamentação mudam ainda mais a base — cada um mais do "
            "que a diferença entre seis e oito copos.",
            "E há o próprio dia. Uma tarde quente ou um treino pesado podem somar mais do que todo o "
            "debate sobre a base. Por isso o HydroPulse calcula uma base com os seus dados e a ajusta "
            "continuamente, em vez de dar uma meta fixa pela manhã.",
        ],
        "works_on": [
            "Uma base calculada pelo seu peso, idade e sexo, não por uma média.",
            "Ajuste para gravidez ou amamentação, que aumentam a necessidade.",
            "Ajuste contínuo ao esforço e ao clima em vez de uma meta matinal.",
            "Uma recomendação em mL ou fl oz, para que “quanto agora” tenha resposta.",
            "Um histórico que mostra quanto o dia realmente somou.",
        ],
        "expect": "Espere um total diário pessoal que varia — muitas vezes bem abaixo de dois litros "
                  "num dia fresco e parado, e bem acima num dia quente e ativo. A comida dá cerca de um "
                  "quinto da água total; o HydroPulse não estima isso, os números dele falam do que "
                  "você bebe.",
        "faq": [
            ("Dois litros por dia está errado?",
             "Não está errado, é genérico. É uma boa média para uma população e uma meta ruim para uma "
             "pessoa num dia específico."),
            ("A comida entra na conta?",
             "Sim, cerca de 20 % da água vem dos alimentos numa dieta comum. O HydroPulse registra "
             "apenas bebidas."),
            ("Beber por horário ou por sede?",
             "Para a maioria dos adultos saudáveis, a sede basta no dia a dia. Ela é menos confiável "
             "com a idade, no calor, em treinos intensos e com muita concentração — justamente os "
             "casos para os quais este app foi feito."),
        ],
    },
    "signs": {
        "slug": "sinais-de-desidratacao",
        "nav": "Sinais de desidratação",
        "card": "Como é a desidratação leve — e quando ela deixa de ser leve.",
        "title": "Sinais de desidratação — o que notar e quando se preocupar",
        "desc": "A desidratação leve aparece como cansaço, dor de cabeça e falta de concentração "
                "muito antes da sede. Os sinais iniciais, os graves, e onde um app entra.",
        "h1": "Sinais de desidratação",
        "lede": "Perder um a dois por cento do peso corporal em líquido já basta para diminuir a "
                "concentração e o humor. Raramente aparece como sede — mais como uma tarde sem "
                "energia que você atribui a outra coisa.",
        "why_title": "Sinais iniciais, e os que importam",
        "why": [
            "Os sinais iniciais comuns: urina escura ou pouca urina, dor de cabeça leve, cansaço que "
            "não combina com a noite de sono, boca e lábios secos, queda de concentração ou de humor. "
            "A cor da urina é o mais prático: amarelo-claro é o alvo, mais escuro que suco de maçã é "
            "motivo para agir.",
            "A sede chega tarde e sem garantia. Ela diminui com a idade, em exercício intenso, no frio "
            "e quando você está absorto — “bebo quando tenho sede” funciona melhor na teoria do que "
            "numa tarde de verão.",
            "Alguns sinais não se resolvem com um copo d'água. Confusão, desmaio, coração acelerado em "
            "repouso, muitas horas sem urinar ou pele quente e seca com desorientação precisam de "
            "atendimento médico, não de um app. O mesmo vale para desidratação com vômito ou diarreia, "
            "sobretudo em crianças e idosos.",
        ],
        "works_on": [
            "Avisar antes do cansaço e da dor de cabeça: é para isso que ele estima em vez de reagir.",
            "Dizer o motivo — calor, esforço ou base — para que o sinal faça sentido.",
            "Urgência crescente conforme o déficit estimado aumenta.",
            "Um histórico para consultar quando uma tarde foi ruim.",
            "Nada de diagnóstico: ele estima um balanço e não diz nada sobre o seu estado de saúde.",
        ],
        "expect": "Usado com regularidade, o efeito não é espetacular — é a ausência da queda das "
                  "quatro da tarde. Ele não pode dizer se você está desidratado: estima um balanço por "
                  "sensores e pelos seus registros, e os sinais acima continuam sendo o que observar.",
        "faq": [
            ("Um smartwatch detecta desidratação?",
             "Nenhum relógio comum mede a hidratação diretamente. O HydroPulse estima o balanço pelo "
             "pulso, pela atividade, pelo clima e pelos registros — uma estimativa fundamentada, não "
             "uma medição nem um diagnóstico."),
            ("A cor da urina é confiável?",
             "É a verificação diária mais prática. Amarelo-claro indica que está em dia; mais escuro, "
             "que está atrasado. Algumas vitaminas, remédios e alimentos alteram a cor."),
            ("Quando procurar um médico?",
             "Confusão, desmaio, coração acelerado em repouso, muitas horas sem urinar ou sinais de "
             "insolação pedem atendimento urgente, assim como desidratação com vômito ou diarreia "
             "persistentes, sobretudo em crianças e idosos."),
        ],
    },
    "heartrate": {
        "slug": "frequencia-cardiaca-e-hidratacao",
        "nav": "Pulso e hidratação",
        "card": "A relação entre deriva cardíaca, esforço e perda de líquido.",
        "title": "Frequência cardíaca e hidratação: o relógio e o suor",
        "desc": "Por que o pulso indica melhor a perda de líquido do que os passos, o que é a reserva "
                "cardíaca e como o HydroPulse a transforma em mililitros por hora.",
        "h1": "Frequência cardíaca e hidratação",
        "lede": "O pulso é o único sinal sempre disponível no relógio que mostra o quanto o seu corpo "
                "está trabalhando. Por isso é o melhor indicador disponível da velocidade com que "
                "você perde líquido.",
        "why_title": "Por que o pulso, e não os passos",
        "why": [
            "Passos dizem quanto você se mexeu, não o quanto custou. Dez mil passos planos na sombra e "
            "cinco mil morro acima no sol dão o mesmo número e custos muito diferentes. O pulso separa "
            "os dois, porque responde à carga, não à distância.",
            "A forma útil é a reserva cardíaca: onde o seu pulso atual fica entre o seu próprio pulso "
            "de repouso e o máximo. Assim, 140 bpm significam coisas diferentes para uma pessoa treinada "
            "de 30 anos e uma sedentária de 55. O suor acompanha o metabolismo, e a reserva cardíaca é "
            "um bom substituto para ele fora do laboratório.",
            "Há um efeito de retorno: ao perder líquido, o volume de plasma cai e o pulso sobe no mesmo "
            "esforço — a deriva cardíaca. Um pulso subindo num treino longo e constante já é um "
            "indício fraco de déficit crescente.",
        ],
        "works_on": [
            "Monitoramento passivo e contínuo do pulso pelo Wear OS Health Services.",
            "Reserva cardíaca a partir do seu pulso de repouso e máximo, editável nos ajustes.",
            "Detecção de treino: exercício de verdade pesa diferente de se mexer na cadeira.",
            "Um multiplicador de suor que combina esforço e índice de calor.",
            "Transparência: cada recomendação diz se veio do calor, do esforço ou da base.",
        ],
        "expect": "Informe o seu pulso de repouso e máximo se os conhecer; a fórmula por idade (cerca "
                  "de 220 menos a idade) varia muito, e corrigi-la é a maior melhoria possível. "
                  "Sensores ópticos perdem precisão em alta intensidade e no frio — a estimativa é tão "
                  "boa quanto o sinal.",
        "faq": [
            ("A desidratação aumenta o pulso?",
             "Sim. A perda de líquido reduz o volume de plasma, e o coração bate mais rápido — a deriva "
             "cardíaca em esforços longos. É um sinal entre vários, não um medidor de hidratação."),
            ("Preciso saber o meu pulso máximo?",
             "Não, o app usa uma estimativa por idade. Mas essa fórmula varia cerca de dez batimentos "
             "por minuto, então um valor medido melhora bastante o modelo."),
            ("Medir o pulso o dia todo gasta muita bateria?",
             "Ele usa monitoramento passivo em vez de um fluxo contínuo rápido — o caminho econômico "
             "que o Wear OS oferece exatamente para isso."),
        ],
    },
}
