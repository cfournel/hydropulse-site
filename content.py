# -*- coding: utf-8 -*-
"""Copy for the HydroPulse site, one entry per language.

Adding a language means adding one block here and rerunning `python3 build.py`;
the templates, hreflang alternates and sitemap follow automatically. Keep the
`TOPICS` keys identical across languages — the alternate links are matched on
them, not on the slugs, so a missing key silently breaks that topic's alternate
set.

Note on honesty: the app's own interface is English-only today. The site is
translated because search demand is per-language, but no copy here claims a
localised app UI — `ui["app_lang_note"]` says so explicitly on every page.
"""

SITE = {
    "origin": "https://gethydropulse.com",
    "play": "https://play.google.com/store/apps/details?id=oytaub.hydropulse.app",
    "package": "oytaub.hydropulse.app",
    "email": "support@gethydropulse.com",
    "updated": "2026-08-30",
    # Google Search Console verification token for a "URL prefix" property — the
    # content= value of the google-site-verification meta tag. Leave empty when
    # the property is verified by DNS TXT record instead (preferred: a domain
    # property covers every subdomain and both schemes and cannot be lost by a
    # template change).
    "search_console": "",
}

# Order used for topic cards and the sitemap. Chosen for search intent, not for
# feature coverage: three device/product queries that convert, three
# informational queries with real volume that a hydration app can answer
# honestly, and one that explains the differentiator.
TOPICS = ["wearos", "sport", "heat", "work", "howmuch", "signs", "heartrate"]

# ---------------------------------------------------------------- English ----

EN = {
    "code": "en",
    "label": "EN",
    "name": "English",
    "base": "",                 # site root
    "topic_dir": "hydration",
    "ui": {
        "home_crumb": "Home",
        "badge_alt": "Get it on Google Play",
        "cta_note": "Wear OS 3.0+. One-time purchase — no subscription, no ads, no account.",
        "app_lang_note": "The app interface is in English.",
        "how_title": "How HydroPulse decides",
        "how_steps": [
            "You enter your weight, age and sweat profile once. That sets your personal baseline loss — the water you lose just by being alive and breathing.",
            "The watch reads your heart rate continuously and converts it into a heart-rate-reserve fraction: how hard you are working relative to your own resting and maximum heart rate, not to an average person's.",
            "Local temperature and humidity are fetched anonymously and turned into a heat-index multiplier, because the same effort costs far more fluid at 33 °C and 70 % humidity than at 18 °C.",
            "Every drink you log is credited back to the ledger. When the running balance crosses your threshold, HydroPulse tells you — with a specific millilitre amount and the reason behind it.",
        ],
        "works_title": "What HydroPulse does here",
        "expect_title": "What to expect",
        "faq_title": "Common questions",
        "features_title": "Why it is not another reminder timer",
        "features": [
            "A running fluid-balance ledger, not a countdown — the interval between nudges changes with your day.",
            "Heart-rate-driven sweat estimate, using your own resting and maximum heart rate.",
            "Live temperature and humidity folded in through a heat-index multiplier.",
            "Every alert carries a millilitre amount and a plain-language reason: heat, exertion or baseline.",
            "Three urgency levels — mild, moderate, urgent — so a nudge and a warning do not look identical.",
            "Native Wear OS tile and watch-face complication: your balance at a glance, no app to open.",
            "One-tap logging straight from the notification, plus a 15-minute snooze.",
            "Quiet hours, so it does not wake you.",
            "mL, fl oz or Imperial units, and your own threshold.",
        ],
        "privacy_title": "Private by design",
        "privacy_body": "Your heart rate, activity and drink log never leave the watch. There is no "
                        "account, no advertising SDK and no product analytics — nothing tracks what "
                        "you do in the app. Two things do leave the device: a pair of coordinates to "
                        "a public weather service, with no identifier attached, and a crash report if "
                        "the app fails. Neither carries your health data.",
        "privacy_link": "Read the full privacy policy",
        "safety_title": "Not a medical device",
        "safety_body": "HydroPulse produces an estimate, not a measurement. It is a wellness tool, not "
                       "a medical device, and it does not diagnose, treat or monitor dehydration or any "
                       "other condition. If you take diuretics, restrict fluid on medical advice, or "
                       "have a kidney, heart or endocrine condition, follow your clinician's intake "
                       "guidance rather than this app's. Seek urgent care for confusion, fainting, or "
                       "heat illness.",
        "related_title": "More on hydration",
        "topics_title": "Hydration, situation by situation",
        "foot_tag": "HydroPulse — adaptive hydration for Wear OS. Estimates, not guesses.",
        "foot_privacy": "Privacy policy",
        "foot_play": "Google Play",
        "foot_terms": "Terms of service",
        "langs_label": "Language",
        "screens_title": "On the watch",
        "sources_title": "Where the model comes from",
        "sources_body": "The baseline draws on IOM and EFSA adequate-intake figures, the sweat-rate "
                        "component on ACSM exercise-hydration guidance, and the environmental "
                        "multiplier on the US National Weather Service heat-index formula. These are "
                        "population references adapted to what a watch can actually sense — a "
                        "well-founded estimate, not a laboratory measurement.",
        # (asset key, alt text, caption)
        "screens": [
            ("home", "HydroPulse home screen showing a 49 % hydration balance and a Log water button",
             "Your balance as a dial, with the amount to drink now."),
            ("notification", "A HydroPulse notification recommending 100 mL with a one-tap log action",
             "One tap to log, one to snooze — the phone stays in your pocket."),
            ("history", "The history screen listing the day's logged drinks",
             "What you actually drank today, not what you meant to."),
            ("settings", "The settings screen with weight, units and threshold options",
             "Your weight, units and threshold — the model fits you."),
        ],
    },
    "home": {
        "title": "HydroPulse — Smart Hydration Reminders for Wear OS",
        "desc": "A Wear OS water reminder that adapts to your heart rate, your activity and the "
                "weather, so it nudges you when your body needs water — not on a fixed timer.",
        "h1": "Hydration reminders that follow your body, not a timer",
        "lede": "Most water reminder apps divide a daily goal by your waking hours and buzz on the "
                "quotient. HydroPulse runs a fluid-balance model on your watch — heart rate, "
                "activity and live weather — and tells you to drink when the balance actually drops.",
        "intro": [
            "An hour at a desk in air conditioning and an hour running in August cost your body wildly "
            "different amounts of water. A fixed interval cannot tell them apart, so it is either "
            "nagging you when you do not need it or silent when you do — and both failures teach you "
            "to ignore it.",
            "HydroPulse keeps a running ledger instead. Passive loss ticks down from your personal "
            "baseline; sweat loss is estimated from how hard your heart is working relative to your "
            "own resting and maximum rate; heat and humidity scale that estimate up. Every drink you "
            "log credits the ledger back. The alert fires on the balance, so on a cool sedentary day "
            "you will barely hear from it, and on a hot training day you will hear from it early.",
            "It was built for the wrist rather than ported to it: a native tile, a watch-face "
            "complication, one-tap logging from the notification, and a recommendation that always "
            "names an amount and a reason instead of just saying “drink water”.",
        ],
    },
    "topics": {
        "wearos": {
            "slug": "water-reminder-wear-os",
            "nav": "On Wear OS",
            "card": "A water reminder built for the watch, not a phone app with a complication.",
            "title": "Water Reminder App for Wear OS — HydroPulse",
            "desc": "A native Wear OS water reminder with a tile, a complication and one-tap logging. "
                    "Works on Pixel Watch, Galaxy Watch and any Wear OS 3.0+ device.",
            "h1": "A water reminder built for Wear OS",
            "lede": "Tile, complication, notification actions and an on-watch model — HydroPulse does "
                    "its thinking on the wrist, so the reminder arrives where your hands already are.",
            "why_title": "Why the watch is the right place for this",
            "why": [
                "Hydration fails on friction. The gap between “I should drink” and a logged "
                "glass is usually a phone in another room, and by the time you find it the moment has "
                "gone. A wrist notification with a Log water button closes that gap to one tap.",
                "The watch is also the only device that knows how hard you are working. Heart rate and "
                "exercise state come from the sensors on your arm, so the estimate is built from live "
                "physiology rather than from a step count synced hours later.",
                "Most hydration apps in the Play Store are phone apps that ship a watch face "
                "complication as an afterthought. HydroPulse is a Wear OS app: the model, the ledger "
                "and the database live on the watch, and it keeps working when your phone is not "
                "nearby.",
            ],
            "works_on": [
                "A swipe-away tile showing your current balance without opening anything.",
                "A watch-face complication, as a ranged value or short text.",
                "Notifications with Log water and Snooze 15 min as direct actions.",
                "Room database and profile stored on the watch, so history survives a lost phone connection.",
                "Wear OS 3.0 and later: Pixel Watch, Galaxy Watch 4 and newer, TicWatch and others.",
            ],
            "expect": "Install it on the watch, set your weight and units once, and grant heart rate, "
                      "activity and coarse location when asked — each one feeds a specific part of "
                      "the model, and the app still works without them using sensible defaults. Battery "
                      "cost is small: passive heart-rate monitoring and a periodic background check, "
                      "with weather cached for 30 minutes.",
            "faq": [
                ("Do I need my phone with me?",
                 "No. The model, the ledger and the water log all run on the watch. A phone is only "
                 "involved in the initial install, and the weather lookup uses whatever connection the "
                 "watch has."),
                ("Which watches does it work on?",
                 "Any Wear OS 3.0 or newer watch with Google Play services — Pixel Watch, Galaxy "
                 "Watch 4 and later, TicWatch and comparable devices. Heart-rate accuracy varies by "
                 "device, and the model degrades gracefully if a sensor is unavailable."),
                ("Is there a phone app?",
                 "No, and that is deliberate. Everything you need is on the watch, which is also why "
                 "there is nothing to sync and no account to create."),
                ("How much battery does it use?",
                 "It uses passive Health Services monitoring rather than a continuous high-rate sensor "
                 "stream, checks in periodically through WorkManager, and caches weather for 30 "
                 "minutes. In normal use it is a background app, not a workout tracker."),
            ],
        },
        "sport": {
            "slug": "hydration-for-running-and-training",
            "nav": "Running & training",
            "card": "Sweat-rate-aware reminders for runs, rides and gym sessions.",
            "title": "Hydration for Running and Training — Sweat Rate",
            "desc": "How much to drink when you train, and how HydroPulse estimates sweat loss from "
                    "your heart-rate reserve and the weather instead of a flat hourly rule.",
            "h1": "Hydration for running and training",
            "lede": "Sweat rate varies from roughly 0.5 to over 2 litres an hour between athletes and "
                    "conditions. A single hourly number cannot cover that range — your heart rate "
                    "and the weather can narrow it.",
            "why_title": "Why a fixed hourly amount fails athletes",
            "why": [
                "Two runners doing the same 10 km can lose amounts of fluid that differ by a factor of "
                "three, depending on body mass, fitness, acclimatisation and the day's heat. Generic "
                "advice has to pick a middle number, which under-serves heavy sweaters and overdoes it "
                "for everyone else.",
                "Effort is the piece a step counter misses entirely. Heart-rate reserve — where "
                "your current heart rate sits between your resting and maximum — tracks metabolic "
                "load far better than pace or cadence, and metabolic load is what drives sweat.",
                "Recovery matters as much as the session. Deficit accumulated during a hard hour does "
                "not disappear at the finish line; HydroPulse keeps the ledger negative afterwards and "
                "keeps asking until it is repaid.",
            ],
            "works_on": [
                "An exertion component driven by heart-rate reserve, so an easy jog and a threshold effort are not treated alike.",
                "A sweat profile setting (light, average, heavy) for personal calibration.",
                "Heat-index scaling, so the same session in July asks for more than in November.",
                "Post-session deficit that carries forward instead of resetting.",
                "Urgency levels, so a mild nudge mid-warm-up does not look like an urgent one at kilometre 15.",
            ],
            "expect": "For best results set your resting and maximum heart rate rather than leaving the "
                      "age-based estimate, and pick the sweat profile that matches your experience of "
                      "yourself. If you have ever weighed yourself before and after a long session, the "
                      "difference in kilograms is roughly your fluid loss in litres — that is the "
                      "single most useful calibration input you can bring.",
            "faq": [
                ("Can it replace a proper sweat-rate test?",
                 "No. Weighing yourself before and after a session under known conditions remains the "
                 "gold standard. HydroPulse estimates continuously from sensors, which is far more "
                 "practical day to day but less precise than a controlled test."),
                ("Does it handle drinking during a race?",
                 "It will keep estimating and keep crediting logged intake, and the notification action "
                 "makes logging fast. Many athletes also snooze it through a race and use the history "
                 "afterwards to see what the deficit looked like."),
                ("What about electrolytes?",
                 "HydroPulse tracks fluid volume, not sodium. For long or very hot sessions, "
                 "electrolyte replacement is a separate question and worth reading up on — drinking "
                 "large volumes of plain water over many hours is not risk-free."),
                ("Does it count coffee and tea?",
                 "You can log any drink. Moderate caffeinated drinks do contribute to daily fluid "
                 "intake for habitual consumers; alcohol is the one that works against you."),
            ],
        },
        "heat": {
            "slug": "drinking-water-in-hot-weather",
            "nav": "Hot weather",
            "card": "When heat and humidity raise your needs, the reminders move first.",
            "title": "Drinking Water in Hot Weather — Heat-Aware Reminders",
            "desc": "Heat and humidity change how much you need to drink long before you feel thirsty. "
                    "How HydroPulse uses live weather and the heat index to move reminders earlier.",
            "h1": "Drinking water in hot weather",
            "lede": "Humidity is the part people underestimate: when sweat cannot evaporate, your body "
                    "produces more of it for less cooling. HydroPulse reads both temperature and "
                    "humidity and shifts your reminders accordingly.",
            "why_title": "Why the thermometer alone is not enough",
            "why": [
                "At 32 °C and 30 % humidity sweat evaporates and does its job. At the same "
                "temperature and 75 % humidity it runs off you instead, so you lose the fluid without "
                "getting the cooling and your body compensates by sweating more. The heat index exists "
                "precisely to capture that difference, and it is what HydroPulse feeds into the model.",
                "Thirst is a lagging indicator in the heat. By the time it is insistent you are often "
                "already a percent or two of body mass down, and in hot conditions that gap opens "
                "faster than the sensation catches up.",
                "Heat also raises your needs while you are doing nothing at all. A still afternoon on a "
                "balcony has a real fluid cost that no activity tracker registers, which is why the "
                "environmental multiplier applies to the baseline and not only to exercise.",
            ],
            "works_on": [
                "Live temperature and humidity, fetched anonymously from a public weather service.",
                "A heat-index multiplier applied to baseline loss, not just to workouts.",
                "Earlier and more frequent alerts on hot days, without you changing a setting.",
                "Coarse location only — enough for local weather, never precise tracking.",
                "A 30-minute weather cache, so the accuracy costs almost no battery.",
            ],
            "expect": "On a genuinely hot day you will notice the app asking sooner and asking for more, "
                      "and on a cool day it will go quiet. That contrast is the feature. Coarse location "
                      "is optional — declined, the app falls back to a temperate default, which is "
                      "safe but blunt in a heatwave.",
            "faq": [
                ("Does it use precise location?",
                 "No. It requests coarse location only, uses it to look up local conditions, and does "
                 "not store it. The request carries coordinates and nothing that identifies you or your "
                 "watch."),
                ("What if I say no to location?",
                 "The app keeps working and uses a temperate default for the environmental component. "
                 "Your heart rate and activity still drive the estimate; only the weather half is "
                 "missing."),
                ("Can drinking too much be a problem?",
                 "Yes. Drinking very large volumes of plain water in a short time can dilute blood "
                 "sodium, which is dangerous. HydroPulse recommends modest amounts spread through the "
                 "day and is not designed to push you toward extremes."),
                ("Is it useful in a sauna or a hot workshop?",
                 "It will register the heart-rate rise, but it reads outdoor weather, so an indoor heat "
                 "source it cannot see will be underestimated. Treat its number as a floor in that case."),
            ],
        },
        "work": {
            "slug": "forgetting-to-drink-water-at-work",
            "nav": "At work",
            "card": "For desk days where six hours vanish between two glasses.",
            "title": "Forgetting to Drink Water at Work — A Reminder That Fits",
            "desc": "Why desk days end in a fluid deficit, and how a wrist reminder with a one-tap log "
                    "and quiet hours survives a calendar full of meetings.",
            "h1": "Forgetting to drink water at work",
            "lede": "Nobody forgets to drink because they do not know they should. They forget because "
                    "focus is a good thing that happens to suppress a weak signal for hours at a time.",
            "why_title": "Why the office is where hydration quietly fails",
            "why": [
                "Deep work and back-to-back meetings both do the same thing to thirst: they push a low "
                "priority signal below the threshold at which you would act on it. The deficit is "
                "gradual, which is exactly why it goes unnoticed until the late-afternoon headache and "
                "the flat feeling that gets blamed on the meeting itself.",
                "Air conditioning and heating both dry the air, and a warm open-plan office sits higher "
                "than you would guess on the environmental scale. None of that is dramatic; all of it "
                "adds up over eight hours.",
                "The reason most reminder apps get uninstalled at work is that they fire during "
                "meetings and at 23:00, so people mute them within a week. Predictable timing is worse "
                "than no timing: the reminder that is always wrong is the one you learn to dismiss "
                "without reading.",
            ],
            "works_on": [
                "Quiet hours, so nothing fires overnight or during the window you block off.",
                "Snooze 15 minutes, for when the nudge lands mid-sentence in a meeting.",
                "One-tap logging on the wrist — no phone, no app switch, no lost train of thought.",
                "Fewer alerts on sedentary days, because the ledger drains slower when you are still.",
                "A tile you can glance at between calls instead of waiting to be interrupted.",
            ],
            "expect": "On a normal indoor day expect a small number of nudges rather than an hourly "
                      "drumbeat, each naming an amount so the decision is already made for you. If it "
                      "feels too frequent or too quiet, the threshold setting moves the trigger point "
                      "instead of forcing you to change your day.",
            "faq": [
                ("Will it buzz during meetings?",
                 "It can, and that is what Snooze 15 min is for. Quiet hours cover recurring blocks; "
                 "for one-off meetings the snooze action on the notification is one tap."),
                ("Do coffee and tea count?",
                 "For habitual consumers, moderate caffeinated drinks do contribute to daily fluid "
                 "intake, and you can log them as drinks. Alcohol is the one that pushes the balance "
                 "the other way."),
                ("Can I make it quieter overall?",
                 "Yes — raise the threshold in settings and the ledger has to drop further before "
                 "an alert fires. Lower it if you would rather be prompted early."),
                ("Does it nag if I ignore it?",
                 "No. It will not re-fire while snoozed, and it respects quiet hours. The urgency level "
                 "rises as the deficit grows, but it does not repeat itself for the sake of repeating."),
            ],
        },
        "howmuch": {
            "slug": "how-much-water-should-you-drink-a-day",
            "nav": "How much per day",
            "card": "Where the 2-litre rule comes from, and why your number is not that.",
            "title": "How Much Water Should You Drink a Day? A Personal Answer",
            "desc": "The eight-glasses rule is a population average, not your target. What actually "
                    "sets your daily fluid need, and how a watch can estimate it hour by hour.",
            "h1": "How much water should you drink a day?",
            "lede": "The honest answer is that a single daily number is the wrong unit. Your need is "
                    "set by your body mass, your effort and your environment, and all three change "
                    "between one day and the next.",
            "why_title": "Where the familiar numbers come from",
            "why": [
                "The figures behind “eight glasses” or “two litres” trace back to "
                "population adequate-intake references — the US Institute of Medicine puts total "
                "daily water at roughly 3.7 L for men and 2.7 L for women, and EFSA gives similar "
                "European figures. Both are totals from all sources, food included, and both are "
                "averages across a whole population rather than prescriptions for one person.",
                "Body mass is the largest single input, which is why the same advice cannot fit a 55 kg "
                "and a 95 kg adult. Age, sex, and pregnancy or nursing shift the baseline further, and "
                "any of those adjustments is bigger than the difference between six and eight glasses.",
                "Then there is the day itself. A hot afternoon and a hard training session can each add "
                "more to your requirement than the entire baseline debate covers — which is why "
                "HydroPulse computes a baseline from your own numbers and then adjusts it continuously "
                "rather than handing you a fixed goal in the morning.",
            ],
            "works_on": [
                "A baseline derived from your weight, age and sex, not from a population average.",
                "Adjustment for pregnancy or nursing, which raise requirements measurably.",
                "Continuous adjustment for effort and weather instead of one morning target.",
                "A recommendation in millilitres or fluid ounces, so “how much now” has an answer.",
                "A history screen showing what the day actually came to, all sources logged by you.",
            ],
            "expect": "Expect a personal daily total that moves — often noticeably below the "
                      "familiar two litres on a cool sedentary day, and well above it on a hot active "
                      "one. Food contributes roughly a fifth of total water intake and HydroPulse does "
                      "not try to estimate it, so its numbers describe what you drink.",
            "faq": [
                ("Is two litres a day wrong?",
                 "It is not wrong, it is generic. It is a reasonable central estimate for total intake "
                 "across a population, and a poor target for a specific person on a specific day."),
                ("Does food count toward the total?",
                 "Yes, roughly 20 % of total water intake comes from food in a typical diet. HydroPulse "
                 "tracks drinks only, so its figures are deliberately about what you drink."),
                ("Should I drink to a schedule or to thirst?",
                 "For most healthy adults in ordinary conditions, thirst is an adequate guide. It "
                 "becomes less reliable with age, in the heat, during hard exercise and when you are "
                 "deeply focused — which is exactly the set of cases this app targets."),
                ("Can I set my own daily goal?",
                 "HydroPulse works from a balance rather than a goal, but the threshold setting lets "
                 "you decide how far the balance may drop before it says something, which is the same "
                 "lever in practice."),
            ],
        },
        "signs": {
            "slug": "signs-of-dehydration",
            "nav": "Signs of dehydration",
            "card": "What mild dehydration actually feels like — and when it stops being mild.",
            "title": "Signs of Dehydration — What to Notice, and When to Worry",
            "desc": "Mild dehydration shows up as fatigue, headache and poor concentration long before "
                    "thirst is urgent. The early signs, the serious ones, and where an app fits.",
            "h1": "Signs of dehydration",
            "lede": "Losing one to two percent of body mass in fluid is enough to blunt concentration "
                    "and mood. It rarely announces itself as thirst — more often as a flat "
                    "afternoon you blame on something else.",
            "why_title": "Early signs, and the ones that matter",
            "why": [
                "The common early markers are dark or infrequent urine, a dull headache, fatigue that "
                "does not match your night's sleep, dry mouth and lips, and a drop in concentration or "
                "mood. Urine colour is the most practical of these: pale straw is the target, and "
                "anything darker than apple juice is worth acting on.",
                "Thirst arrives late and unreliably. It is blunted with age, during intense exercise, "
                "in cold weather and when you are absorbed in something — so “I drink when "
                "I'm thirsty” works better in theory than on an August afternoon or a long meeting.",
                "Some signs are not a hydration problem to solve with a glass of water. Confusion, "
                "fainting, a racing heart at rest, no urine for many hours, or heat exhaustion "
                "progressing to hot dry skin and disorientation need medical attention, not an app. "
                "The same is true for dehydration alongside vomiting or diarrhoea, especially in "
                "children and older adults.",
            ],
            "works_on": [
                "Nudging before the fatigue and the headache, which is the whole point of estimating rather than reacting.",
                "Naming the driver — heat, exertion or baseline — so the signal is interpretable.",
                "Escalating urgency as the estimated deficit grows.",
                "A history you can look back at when an afternoon went badly.",
                "Nothing diagnostic: it estimates fluid balance and makes no claim about your clinical state.",
            ],
            "expect": "Used consistently, the effect people report is not dramatic — it is the "
                      "absence of the four-o'clock slump. What it cannot do is tell you whether you are "
                      "dehydrated: it estimates a balance from sensors and your own logging, and the "
                      "signs above remain the thing to watch.",
            "faq": [
                ("Can a smartwatch detect dehydration?",
                 "No consumer watch measures hydration directly. HydroPulse estimates fluid balance "
                 "from heart rate, activity, weather and what you log — a well-founded estimate, "
                 "not a measurement, and not a diagnosis."),
                ("Is urine colour reliable?",
                 "It is the most practical everyday check. Pale straw suggests you are on track; darker "
                 "suggests you are behind. Some vitamins, medications and foods colour it independently."),
                ("When should I see a doctor?",
                 "Confusion, fainting, a racing heart at rest, no urination for many hours, or signs of "
                 "heat illness need urgent care. So does dehydration with persistent vomiting or "
                 "diarrhoea, particularly in children and older adults."),
                ("Does the app warn me if I am dehydrated?",
                 "It warns you when its estimated balance crosses your threshold. That is a prompt to "
                 "drink, not a clinical assessment, and it should never delay seeking care."),
            ],
        },
        "heartrate": {
            "slug": "heart-rate-and-hydration",
            "nav": "Heart rate & hydration",
            "card": "The link between cardiac drift, effort and fluid loss.",
            "title": "Heart Rate and Hydration — How a Watch Estimates Sweat Loss",
            "desc": "Why heart rate is a better proxy for fluid loss than step count, what heart-rate "
                    "reserve means, and how HydroPulse turns it into millilitres per hour.",
            "h1": "Heart rate and hydration",
            "lede": "Heart rate is the only continuously available signal on a watch that tracks how "
                    "hard your body is actually working. That makes it the best available proxy for "
                    "how fast you are losing fluid.",
            "why_title": "Why heart rate, and not steps",
            "why": [
                "A step count says how much you moved, not how hard it was. Ten thousand flat steps in "
                "the shade and five thousand up a hill in the sun are the same number and nothing like "
                "the same metabolic cost. Heart rate separates them, because it responds to load rather "
                "than to distance.",
                "The useful form is heart-rate reserve: where your current rate sits between your own "
                "resting and maximum. Expressed that way, 140 bpm means something different for a "
                "trained 30-year-old and a sedentary 55-year-old, and the model treats them "
                "differently. Sweat rate scales with metabolic rate, and heart-rate reserve is a "
                "reasonable stand-in for metabolic rate outside a laboratory.",
                "There is a feedback loop worth knowing about. As you lose fluid, plasma volume falls "
                "and heart rate creeps upward at the same effort — cardiac drift. So a rising "
                "heart rate during a long steady session is itself weak evidence of accumulating "
                "deficit, and the estimate leans in the right direction as the session goes on.",
            ],
            "works_on": [
                "Continuous passive heart-rate monitoring through Wear OS Health Services.",
                "Heart-rate reserve computed from your own resting and maximum rate, editable in settings.",
                "Exercise-state detection, so deliberate training is weighted differently from fidgeting.",
                "A sweat multiplier that combines exertion with the heat index rather than treating them separately.",
                "A transparent breakdown — every recommendation says whether heat, exertion or baseline drove it.",
            ],
            "expect": "Set your resting and maximum heart rate if you know them; the age-based default "
                      "— roughly 220 minus your age — is a population formula with a wide "
                      "spread, and correcting it is the single largest accuracy improvement available "
                      "to you. Optical wrist sensors also lose accuracy at high intensity and in the "
                      "cold, so the estimate is only as good as the signal it gets.",
            "faq": [
                ("Does dehydration raise your heart rate?",
                 "Yes. Fluid loss reduces plasma volume, so the heart beats faster to maintain output "
                 "— the effect known as cardiac drift during prolonged exercise. It is one signal "
                 "among several, not a hydration meter."),
                ("Do I have to know my maximum heart rate?",
                 "No. The app falls back to an age-based estimate. But that formula has a standard "
                 "deviation of around ten beats per minute, so entering a real measured value "
                 "meaningfully sharpens the model."),
                ("Does it drain the battery to read heart rate all day?",
                 "It uses passive monitoring rather than a continuous high-rate stream, which is the "
                 "low-power path Wear OS provides for exactly this kind of background use."),
                ("What if my watch's heart-rate sensor is inaccurate?",
                 "Then the exertion component is correspondingly rough. A loose strap, tattoos and cold "
                 "skin all degrade optical readings. Baseline and weather components are unaffected."),
            ],
        },
    },
}

# ----------------------------------------------------------------- Français ----

FR = {
    "code": "fr",
    "label": "FR",
    "name": "Français",
    "base": "fr",
    "topic_dir": "hydratation",
    "ui": {
        "home_crumb": "Accueil",
        "badge_alt": "Disponible sur Google Play",
        "cta_note": "Wear OS 3.0+. Achat unique — sans abonnement, sans publicité, sans compte.",
        "app_lang_note": "L'interface de l'application est en anglais.",
        "how_title": "Comment HydroPulse décide",
        "how_steps": [
            "Vous saisissez une fois votre poids, votre âge et votre profil de transpiration. Cela fixe votre perte de base personnelle — l'eau que vous perdez simplement en respirant et en vivant.",
            "La montre lit votre fréquence cardiaque en continu et la convertit en fraction de réserve cardiaque : l'intensité de votre effort par rapport à vos propres fréquences de repos et maximale, pas à celles d'une personne moyenne.",
            "La température et l'humidité locales sont récupérées anonymement et converties en multiplicateur d'indice de chaleur, car le même effort coûte bien plus de liquide à 33 °C avec 70 % d'humidité qu'à 18 °C.",
            "Chaque verre que vous enregistrez est recrédité au bilan. Quand le solde franchit votre seuil, HydroPulse vous prévient — avec une quantité précise en millilitres et la raison qui la motive.",
        ],
        "works_title": "Ce que fait HydroPulse ici",
        "expect_title": "À quoi s'attendre",
        "faq_title": "Questions fréquentes",
        "features_title": "Pourquoi ce n'est pas un minuteur de plus",
        "features": [
            "Un bilan hydrique courant, pas un compte à rebours — l'intervalle entre deux rappels suit votre journée.",
            "Une estimation de sudation pilotée par la fréquence cardiaque, calée sur vos propres valeurs de repos et maximale.",
            "Température et humidité en direct, intégrées via un multiplicateur d'indice de chaleur.",
            "Chaque alerte donne une quantité en millilitres et une raison en clair : chaleur, effort ou métabolisme de base.",
            "Trois niveaux d'urgence — léger, modéré, urgent — pour qu'un simple rappel ne ressemble pas à une alerte sérieuse.",
            "Tuile Wear OS native et complication de cadran : votre solde d'un coup d'œil, sans ouvrir l'application.",
            "Enregistrement en un geste depuis la notification, plus un report de 15 minutes.",
            "Heures silencieuses, pour qu'elle ne vous réveille pas.",
            "Unités en mL, oz liquides ou impériales, et votre propre seuil.",
        ],
        "privacy_title": "Confidentielle par conception",
        "privacy_body": "Votre fréquence cardiaque, votre activité et votre journal de boisson ne "
                        "quittent jamais la montre. Aucun compte, aucun SDK publicitaire, aucune "
                        "mesure d'audience : rien ne piste ce que vous faites dans l'application. Deux "
                        "choses sortent de l'appareil : des coordonnées vers un service météo public, "
                        "sans aucun identifiant, et un rapport de plantage si l'application échoue. "
                        "Ni l'un ni l'autre ne transporte vos données de santé.",
        "privacy_link": "Lire la politique de confidentialité complète",
        "safety_title": "Ce n'est pas un dispositif médical",
        "safety_body": "HydroPulse produit une estimation, pas une mesure. C'est un outil de bien-être, "
                       "pas un dispositif médical : il ne diagnostique, ne traite ni ne surveille la "
                       "déshydratation ou toute autre affection. Si vous prenez des diurétiques, si "
                       "votre apport hydrique est limité sur avis médical, ou si vous souffrez d'une "
                       "affection rénale, cardiaque ou endocrinienne, suivez les consignes de votre "
                       "médecin plutôt que celles de l'application. Consultez en urgence en cas de "
                       "confusion, de malaise ou de coup de chaleur.",
        "related_title": "Autres sujets d'hydratation",
        "topics_title": "L'hydratation, situation par situation",
        "foot_tag": "HydroPulse — hydratation adaptative pour Wear OS. Des estimations, pas des suppositions.",
        "foot_privacy": "Politique de confidentialité",
        "foot_play": "Google Play",
        "foot_terms": "Conditions d'utilisation",
        "langs_label": "Langue",
        "screens_title": "Sur la montre",
        "sources_title": "D'où vient le modèle",
        "sources_body": "La ligne de base s'appuie sur les apports adéquats de l'IOM et de l'EFSA, la "
                        "composante sudation sur les recommandations d'hydratation à l'effort de "
                        "l'ACSM, et le multiplicateur environnemental sur la formule d'indice de "
                        "chaleur du National Weather Service américain. Ce sont des références de "
                        "population adaptées à ce qu'une montre peut réellement percevoir : une "
                        "estimation solidement fondée, pas une mesure de laboratoire.",
        "screens": [
            ("home", "Écran d'accueil HydroPulse affichant un solde d'hydratation de 49 % et un bouton d'enregistrement",
             "Votre solde sous forme de cadran, avec la quantité à boire maintenant."),
            ("notification", "Une notification HydroPulse recommandant 100 mL avec une action d'enregistrement en un geste",
             "Un geste pour enregistrer, un pour reporter — le téléphone reste dans la poche."),
            ("history", "L'écran d'historique listant les boissons enregistrées dans la journée",
             "Ce que vous avez bu aujourd'hui, pas ce que vous comptiez boire."),
            ("settings", "L'écran de réglages avec le poids, les unités et le seuil",
             "Votre poids, vos unités, votre seuil — le modèle s'ajuste à vous."),
        ],
    },
    "home": {
        "title": "HydroPulse — Rappels d'hydratation intelligents pour Wear OS",
        "desc": "Un rappel de boire de l'eau sur Wear OS qui s'adapte à votre fréquence cardiaque, à "
                "votre activité et à la météo : il vous alerte quand votre corps en a besoin.",
        "h1": "Des rappels d'hydratation qui suivent votre corps, pas un minuteur",
        "lede": "La plupart des applications divisent un objectif quotidien par vos heures d'éveil et "
                "vibrent sur le quotient. HydroPulse fait tourner un modèle de bilan hydrique sur "
                "votre montre — cardio, activité et météo — et vous alerte quand le solde baisse "
                "vraiment.",
        "intro": [
            "Une heure au bureau sous climatisation et une heure de course en août ne coûtent pas du "
            "tout la même quantité d'eau. Un intervalle fixe ne sait pas les distinguer : il vous "
            "harcèle quand ce n'est pas utile et se tait quand ça l'est — et ces deux échecs vous "
            "apprennent à l'ignorer.",
            "HydroPulse tient plutôt un bilan courant. La perte passive s'écoule depuis votre ligne de "
            "base personnelle ; la perte par sudation est estimée à partir de l'intensité du travail "
            "cardiaque, rapportée à vos propres fréquences de repos et maximale ; la chaleur et "
            "l'humidité amplifient cette estimation. Chaque boisson enregistrée recrédite le bilan. "
            "L'alerte se déclenche sur le solde : une journée fraîche et sédentaire sera presque "
            "silencieuse, une journée d'entraînement sous la chaleur sera signalée tôt.",
            "L'application a été conçue pour le poignet et non portée sur celui-ci : tuile native, "
            "complication de cadran, enregistrement en un geste depuis la notification, et une "
            "recommandation qui donne toujours une quantité et une raison au lieu de dire simplement "
            "« buvez de l'eau ».",
        ],
    },
    "topics": {
        "wearos": {
            "slug": "rappel-boire-de-l-eau-wear-os",
            "nav": "Sur Wear OS",
            "card": "Un rappel d'hydratation conçu pour la montre, pas une appli mobile avec une complication.",
            "title": "Rappel d'hydratation pour Wear OS — HydroPulse",
            "desc": "Un rappel d'hydratation natif Wear OS avec tuile, complication et enregistrement "
                    "en un geste. Compatible Pixel Watch, Galaxy Watch et Wear OS 3.0+.",
            "h1": "Un rappel d'hydratation conçu pour Wear OS",
            "lede": "Tuile, complication, actions de notification et modèle embarqué : HydroPulse "
                    "calcule au poignet, donc le rappel arrive là où vos mains sont déjà.",
            "why_title": "Pourquoi la montre est le bon endroit",
            "why": [
                "L'hydratation échoue sur la friction. Entre « je devrais boire » et un verre "
                "réellement bu, il y a d'ordinaire un téléphone dans une autre pièce, et le temps de "
                "le retrouver le moment est passé. Une notification au poignet avec un bouton "
                "d'enregistrement ramène cet écart à un seul geste.",
                "La montre est aussi le seul appareil qui sait à quel point vous forcez. La fréquence "
                "cardiaque et l'état d'exercice viennent des capteurs posés sur votre bras : "
                "l'estimation se construit sur une physiologie en direct, pas sur un nombre de pas "
                "synchronisé des heures plus tard.",
                "La plupart des applications d'hydratation du Play Store sont des applications "
                "mobiles qui livrent une complication en supplément. HydroPulse est une application "
                "Wear OS : le modèle, le bilan et la base de données vivent sur la montre, et elle "
                "continue de fonctionner quand le téléphone n'est pas à proximité.",
            ],
            "works_on": [
                "Une tuile accessible d'un balayage, qui affiche votre solde sans rien ouvrir.",
                "Une complication de cadran, en valeur graduée ou en texte court.",
                "Des notifications avec « Log water » et report de 15 min en actions directes.",
                "Base de données et profil stockés sur la montre : l'historique survit à la perte de connexion au téléphone.",
                "Wear OS 3.0 et ultérieur : Pixel Watch, Galaxy Watch 4 et plus récentes, TicWatch et autres.",
            ],
            "expect": "Installez-la sur la montre, réglez une fois votre poids et vos unités, et "
                      "accordez la fréquence cardiaque, l'activité et la localisation approximative "
                      "quand elle les demande — chacune alimente une partie précise du modèle, et "
                      "l'application fonctionne sans elles avec des valeurs par défaut raisonnables. "
                      "Le coût en batterie est faible : suivi cardiaque passif, vérification "
                      "périodique en arrière-plan et météo mise en cache 30 minutes.",
            "faq": [
                ("Ai-je besoin de mon téléphone ?",
                 "Non. Le modèle, le bilan et le journal de boisson tournent sur la montre. Le "
                 "téléphone n'intervient qu'à l'installation, et la requête météo utilise la "
                 "connexion dont dispose la montre."),
                ("Sur quelles montres fonctionne-t-elle ?",
                 "Toute montre Wear OS 3.0 ou ultérieure avec les services Google Play — Pixel "
                 "Watch, Galaxy Watch 4 et suivantes, TicWatch et modèles comparables. La précision "
                 "cardiaque varie selon l'appareil, et le modèle se dégrade proprement si un capteur "
                 "est indisponible."),
                ("Existe-t-il une application téléphone ?",
                 "Non, et c'est délibéré. Tout ce dont vous avez besoin est sur la montre, ce qui "
                 "explique aussi qu'il n'y ait rien à synchroniser ni de compte à créer."),
                ("Quelle consommation de batterie ?",
                 "Elle utilise la surveillance passive de Health Services plutôt qu'un flux capteur "
                 "continu à haute fréquence, se réveille périodiquement via WorkManager et met la "
                 "météo en cache 30 minutes. En usage normal c'est une application d'arrière-plan, "
                 "pas un traqueur d'entraînement."),
            ],
        },
        "sport": {
            "slug": "hydratation-course-a-pied-et-entrainement",
            "nav": "Course & entraînement",
            "card": "Des rappels calés sur votre taux de sudation, pour la course, le vélo et la salle.",
            "title": "Hydratation à la course et à l'entraînement",
            "desc": "Combien boire à l'effort, et comment HydroPulse estime la perte sudorale à partir "
                    "de votre réserve cardiaque et de la météo plutôt que d'une règle horaire fixe.",
            "h1": "Hydratation à la course et à l'entraînement",
            "lede": "Le taux de sudation va d'environ 0,5 à plus de 2 litres par heure selon les "
                    "athlètes et les conditions. Un chiffre horaire unique ne couvre pas cet "
                    "intervalle — votre cardio et la météo, si.",
            "why_title": "Pourquoi une quantité horaire fixe échoue chez les sportifs",
            "why": [
                "Deux coureurs qui font le même 10 km peuvent perdre des volumes de liquide dans un "
                "rapport de un à trois, selon la masse corporelle, la condition physique, "
                "l'acclimatation et la chaleur du jour. Un conseil générique doit choisir un chiffre "
                "médian, qui dessert les gros transpirants et surestime pour tous les autres.",
                "L'intensité est justement ce qu'un podomètre rate entièrement. La réserve cardiaque "
                "— où se situe votre fréquence actuelle entre votre repos et votre maximum — "
                "suit la charge métabolique bien mieux que l'allure ou la cadence, et c'est la charge "
                "métabolique qui pilote la sudation.",
                "La récupération compte autant que la séance. Le déficit accumulé pendant une heure "
                "difficile ne disparaît pas sur la ligne d'arrivée : HydroPulse garde le bilan négatif "
                "ensuite et continue de réclamer jusqu'à ce qu'il soit remboursé.",
            ],
            "works_on": [
                "Une composante d'effort pilotée par la réserve cardiaque : un footing tranquille et un effort au seuil ne sont pas traités pareil.",
                "Un réglage de profil de transpiration (faible, moyen, important) pour l'étalonnage personnel.",
                "Une mise à l'échelle par indice de chaleur : la même séance en juillet demande plus qu'en novembre.",
                "Un déficit post-séance qui se reporte au lieu d'être remis à zéro.",
                "Des niveaux d'urgence, pour qu'un rappel léger à l'échauffement ne ressemble pas à une alerte au 15e kilomètre.",
            ],
            "expect": "Pour de meilleurs résultats, renseignez vos fréquences cardiaques de repos et "
                      "maximale plutôt que de laisser l'estimation par l'âge, et choisissez le profil "
                      "de transpiration qui correspond à ce que vous connaissez de vous. Si vous vous "
                      "êtes déjà pesé avant et après une longue séance, la différence en kilogrammes "
                      "correspond à peu près à votre perte hydrique en litres — c'est l'élément "
                      "d'étalonnage le plus utile que vous puissiez apporter.",
            "faq": [
                ("Peut-elle remplacer un vrai test de sudation ?",
                 "Non. La pesée avant/après une séance dans des conditions connues reste la référence. "
                 "HydroPulse estime en continu à partir des capteurs, ce qui est bien plus praticable "
                 "au quotidien mais moins précis qu'un test contrôlé."),
                ("Gère-t-elle la boisson en course ?",
                 "Elle continue d'estimer et de créditer les apports enregistrés, et l'action de "
                 "notification rend l'enregistrement rapide. Beaucoup d'athlètes la mettent aussi en "
                 "veille pendant une compétition et consultent l'historique ensuite."),
                ("Et les électrolytes ?",
                 "HydroPulse suit le volume de liquide, pas le sodium. Sur les séances longues ou très "
                 "chaudes, le remplacement des électrolytes est une question distincte qui mérite "
                 "d'être creusée : boire de gros volumes d'eau pure pendant des heures n'est pas sans "
                 "risque."),
                ("Le café et le thé comptent-ils ?",
                 "Vous pouvez enregistrer n'importe quelle boisson. Les boissons caféinées consommées "
                 "modérément contribuent bien à l'apport hydrique quotidien chez les consommateurs "
                 "habituels ; c'est l'alcool qui joue contre vous."),
            ],
        },
        "heat": {
            "slug": "boire-de-l-eau-par-forte-chaleur",
            "nav": "Forte chaleur",
            "card": "Quand la chaleur et l'humidité augmentent vos besoins, les rappels bougent d'abord.",
            "title": "Boire de l'eau par forte chaleur | HydroPulse",
            "desc": "La chaleur et l'humidité changent vos besoins bien avant la soif. Comment "
                    "HydroPulse utilise la météo en direct et l'indice de chaleur pour avancer les rappels.",
            "h1": "Boire de l'eau par forte chaleur",
            "lede": "L'humidité est la variable que l'on sous-estime : quand la sueur ne peut pas "
                    "s'évaporer, le corps en produit davantage pour un refroidissement moindre. "
                    "HydroPulse lit la température et l'humidité et décale vos rappels en conséquence.",
            "why_title": "Pourquoi le thermomètre seul ne suffit pas",
            "why": [
                "À 32 °C avec 30 % d'humidité, la sueur s'évapore et fait son travail. À la même "
                "température avec 75 % d'humidité, elle ruisselle : vous perdez le liquide sans "
                "obtenir le refroidissement, et le corps compense en transpirant davantage. L'indice "
                "de chaleur existe précisément pour capturer cette différence, et c'est lui "
                "qu'HydroPulse injecte dans le modèle.",
                "À la chaleur, la soif est un indicateur retardé. Quand elle devient insistante, vous "
                "avez souvent déjà perdu un ou deux pour cent de masse corporelle, et par forte "
                "chaleur cet écart se creuse plus vite que la sensation ne le rattrape.",
                "La chaleur augmente aussi vos besoins alors que vous ne faites rien. Un après-midi "
                "immobile sur un balcon a un coût hydrique réel qu'aucun traqueur d'activité "
                "n'enregistre : c'est pourquoi le multiplicateur environnemental s'applique à la "
                "ligne de base et pas seulement à l'exercice.",
            ],
            "works_on": [
                "Température et humidité en direct, récupérées anonymement auprès d'un service météo public.",
                "Un multiplicateur d'indice de chaleur appliqué à la perte de base, pas seulement aux séances.",
                "Des alertes plus précoces et plus fréquentes les jours chauds, sans changer un réglage.",
                "Localisation approximative uniquement — assez pour la météo locale, jamais du suivi précis.",
                "Un cache météo de 30 minutes : la précision ne coûte presque pas de batterie.",
            ],
            "expect": "Un jour vraiment chaud, vous remarquerez qu'elle demande plus tôt et davantage ; "
                      "un jour frais, elle se taira. Ce contraste est la fonctionnalité. La "
                      "localisation approximative est facultative : refusée, l'application retombe sur "
                      "un climat tempéré par défaut, ce qui est prudent mais grossier en pleine canicule.",
            "faq": [
                ("Utilise-t-elle la localisation précise ?",
                 "Non. Elle demande uniquement la localisation approximative, s'en sert pour consulter "
                 "les conditions locales et ne la stocke pas. La requête contient des coordonnées et "
                 "rien qui vous identifie, vous ou votre montre."),
                ("Et si je refuse la localisation ?",
                 "L'application continue de fonctionner avec un climat tempéré par défaut pour la "
                 "composante environnementale. Votre fréquence cardiaque et votre activité alimentent "
                 "toujours l'estimation ; seule la moitié météo manque."),
                ("Peut-on boire trop ?",
                 "Oui. Ingérer de très grands volumes d'eau pure en peu de temps peut diluer le sodium "
                 "sanguin, ce qui est dangereux. HydroPulse recommande des quantités modestes réparties "
                 "dans la journée et n'est pas conçue pour vous pousser aux extrêmes."),
                ("Est-elle utile en sauna ou en atelier chaud ?",
                 "Elle enregistrera la hausse de fréquence cardiaque, mais elle lit la météo "
                 "extérieure : une source de chaleur intérieure qu'elle ne voit pas sera "
                 "sous-estimée. Considérez alors son chiffre comme un plancher."),
            ],
        },
        "work": {
            "slug": "oublier-de-boire-au-bureau",
            "nav": "Au bureau",
            "card": "Pour les journées de bureau où six heures passent entre deux verres.",
            "title": "Oublier de boire au bureau — un rappel qui tient la journée",
            "desc": "Pourquoi les journées de bureau finissent en déficit hydrique, et comment un "
                    "rappel au poignet avec enregistrement en un geste survit à un agenda chargé.",
            "h1": "Oublier de boire au bureau",
            "lede": "Personne n'oublie de boire par ignorance. On oublie parce que la concentration, "
                    "qui est une bonne chose, étouffe un signal faible pendant des heures d'affilée.",
            "why_title": "Pourquoi l'hydratation déraille discrètement au travail",
            "why": [
                "Le travail en profondeur et les réunions en cascade font la même chose à la soif : "
                "ils poussent un signal de faible priorité sous le seuil où vous agiriez. Le déficit "
                "est progressif, et c'est exactement pour cela qu'il passe inaperçu jusqu'au mal de "
                "tête de fin d'après-midi et à la sensation de plat qu'on met sur le dos de la réunion.",
                "La climatisation comme le chauffage assèchent l'air, et un open space chaud se situe "
                "plus haut qu'on ne le croit sur l'échelle environnementale. Rien de spectaculaire ; "
                "tout cela s'additionne sur huit heures.",
                "Si la plupart des applications de rappel finissent désinstallées au bureau, c'est "
                "qu'elles se déclenchent en pleine réunion et à 23 h, et qu'on les coupe en une "
                "semaine. Une régularité prévisible est pire que rien : le rappel qui a toujours tort "
                "est celui qu'on apprend à écarter sans le lire.",
            ],
            "works_on": [
                "Heures silencieuses : rien ne se déclenche la nuit ni pendant la plage que vous réservez.",
                "Report de 15 minutes, quand le rappel tombe au milieu d'une phrase en réunion.",
                "Enregistrement en un geste au poignet — pas de téléphone, pas de changement d'application, pas de fil perdu.",
                "Moins d'alertes les jours sédentaires, parce que le bilan se vide plus lentement à l'arrêt.",
                "Une tuile à consulter entre deux appels au lieu d'attendre d'être interrompu.",
            ],
            "expect": "Une journée normale en intérieur, attendez-vous à un petit nombre de rappels "
                      "plutôt qu'à un battement horaire, chacun donnant une quantité pour que la "
                      "décision soit déjà prise. Si c'est trop fréquent ou trop discret, le réglage "
                      "de seuil déplace le point de déclenchement sans vous obliger à changer votre "
                      "journée.",
            "faq": [
                ("Va-t-elle vibrer pendant les réunions ?",
                 "C'est possible, et c'est à cela que sert le report de 15 min. Les heures silencieuses "
                 "couvrent les plages récurrentes ; pour une réunion ponctuelle, l'action de report sur "
                 "la notification tient en un geste."),
                ("Le café et le thé comptent-ils ?",
                 "Chez les consommateurs habituels, les boissons caféinées prises modérément "
                 "contribuent à l'apport hydrique quotidien, et vous pouvez les enregistrer. C'est "
                 "l'alcool qui pousse le bilan dans l'autre sens."),
                ("Puis-je la rendre plus discrète ?",
                 "Oui — augmentez le seuil dans les réglages et le bilan devra descendre plus bas "
                 "avant qu'une alerte parte. Baissez-le si vous préférez être sollicité tôt."),
                ("Insiste-t-elle si je l'ignore ?",
                 "Non. Elle ne se redéclenche pas pendant un report et respecte les heures "
                 "silencieuses. Le niveau d'urgence monte à mesure que le déficit grandit, mais elle "
                 "ne se répète pas pour le plaisir."),
            ],
        },
        "howmuch": {
            "slug": "combien-d-eau-boire-par-jour",
            "nav": "Combien par jour",
            "card": "D'où vient la règle des 2 litres, et pourquoi votre chiffre n'est pas celui-là.",
            "title": "Combien d'eau boire par jour ? Une réponse personnelle",
            "desc": "La règle des huit verres est une moyenne de population, pas votre objectif. Ce qui "
                    "détermine vos besoins, et comment une montre peut les estimer.",
            "h1": "Combien d'eau faut-il boire par jour ?",
            "lede": "La réponse honnête, c'est qu'un chiffre quotidien unique est la mauvaise unité. "
                    "Votre besoin dépend de votre masse corporelle, de votre effort et de votre "
                    "environnement — et les trois changent d'un jour à l'autre.",
            "why_title": "D'où viennent les chiffres habituels",
            "why": [
                "Les valeurs derrière « huit verres » ou « deux litres » remontent à des références "
                "d'apport adéquat de population : l'Institute of Medicine américain situe l'eau totale "
                "quotidienne autour de 3,7 L pour les hommes et 2,7 L pour les femmes, et l'EFSA donne "
                "des chiffres européens comparables. Ce sont des totaux toutes sources confondues, "
                "alimentation incluse, et des moyennes de population plutôt que des prescriptions "
                "individuelles.",
                "La masse corporelle est le premier facteur, ce qui explique qu'un même conseil ne "
                "puisse convenir à un adulte de 55 kg et à un autre de 95 kg. L'âge, le sexe, la "
                "grossesse et l'allaitement déplacent encore la ligne de base, et chacun de ces "
                "ajustements pèse plus lourd que le débat entre six et huit verres.",
                "Reste la journée elle-même. Un après-midi de canicule ou une séance difficile peuvent "
                "chacun ajouter davantage à vos besoins que tout le débat sur la ligne de base — "
                "c'est pourquoi HydroPulse calcule une base à partir de vos propres chiffres puis "
                "l'ajuste en continu, au lieu de vous remettre un objectif fixe le matin.",
            ],
            "works_on": [
                "Une ligne de base dérivée de votre poids, de votre âge et de votre sexe, pas d'une moyenne de population.",
                "Un ajustement pour la grossesse ou l'allaitement, qui augmentent mesurablement les besoins.",
                "Un ajustement continu selon l'effort et la météo plutôt qu'une cible unique le matin.",
                "Une recommandation en millilitres ou en onces liquides, pour que « combien maintenant » ait une réponse.",
                "Un écran d'historique montrant ce que la journée a réellement donné, sources enregistrées par vous.",
            ],
            "expect": "Attendez-vous à un total quotidien personnel qui bouge — souvent nettement "
                      "sous les deux litres habituels un jour frais et sédentaire, et bien au-dessus un "
                      "jour chaud et actif. L'alimentation fournit environ un cinquième de l'apport "
                      "hydrique total et HydroPulse n'essaie pas de l'estimer : ses chiffres décrivent "
                      "ce que vous buvez.",
            "faq": [
                ("Deux litres par jour, c'est faux ?",
                 "Ce n'est pas faux, c'est générique. C'est une estimation centrale raisonnable pour "
                 "l'apport total d'une population, et un mauvais objectif pour une personne donnée un "
                 "jour donné."),
                ("L'alimentation compte-t-elle dans le total ?",
                 "Oui, environ 20 % de l'apport hydrique total vient des aliments dans un régime "
                 "courant. HydroPulse ne suit que les boissons : ses chiffres portent délibérément sur "
                 "ce que vous buvez."),
                ("Faut-il boire selon un horaire ou à la soif ?",
                 "Pour la plupart des adultes en bonne santé dans des conditions ordinaires, la soif "
                 "est un guide suffisant. Elle devient moins fiable avec l'âge, à la chaleur, à "
                 "l'effort intense et en pleine concentration — précisément les cas que vise cette "
                 "application."),
                ("Puis-je fixer mon propre objectif quotidien ?",
                 "HydroPulse raisonne en bilan plutôt qu'en objectif, mais le réglage de seuil vous "
                 "laisse décider jusqu'où le solde peut descendre avant qu'elle intervienne, ce qui "
                 "revient au même levier en pratique."),
            ],
        },
        "signs": {
            "slug": "signes-de-deshydratation",
            "nav": "Signes de déshydratation",
            "card": "À quoi ressemble vraiment une déshydratation légère — et quand elle cesse de l'être.",
            "title": "Signes de déshydratation : quoi surveiller, quand agir",
            "desc": "La déshydratation légère se manifeste par la fatigue, les maux de tête et la perte "
                    "de concentration bien avant la soif. Les signes précoces, les signes graves.",
            "h1": "Les signes de déshydratation",
            "lede": "Perdre un à deux pour cent de sa masse corporelle en liquide suffit à émousser la "
                    "concentration et l'humeur. Cela s'annonce rarement comme une soif — plutôt "
                    "comme un après-midi plat que l'on met sur le compte d'autre chose.",
            "why_title": "Les signes précoces, et ceux qui comptent",
            "why": [
                "Les marqueurs précoces courants sont des urines foncées ou peu fréquentes, un mal de "
                "tête sourd, une fatigue sans rapport avec votre nuit, une bouche et des lèvres sèches, "
                "et une baisse de concentration ou d'humeur. La couleur des urines est le plus "
                "pratique : le jaune paille clair est la cible, et tout ce qui est plus foncé qu'un "
                "jus de pomme mérite d'agir.",
                "La soif arrive tard et de façon peu fiable. Elle s'émousse avec l'âge, pendant "
                "l'effort intense, par temps froid et quand vous êtes absorbé — « je bois quand "
                "j'ai soif » marche donc mieux en théorie qu'un après-midi d'août ou en longue réunion.",
                "Certains signes ne se règlent pas avec un verre d'eau. Confusion, malaise, cœur qui "
                "s'emballe au repos, absence d'urines pendant de longues heures, ou épuisement dû à la "
                "chaleur évoluant vers une peau chaude et sèche et une désorientation exigent un avis "
                "médical, pas une application. Il en va de même en cas de déshydratation avec "
                "vomissements ou diarrhée, surtout chez l'enfant et la personne âgée.",
            ],
            "works_on": [
                "Alerter avant la fatigue et le mal de tête : c'est tout l'intérêt d'estimer plutôt que de réagir.",
                "Nommer le facteur — chaleur, effort ou métabolisme de base — pour que le signal soit interprétable.",
                "Faire monter l'urgence à mesure que le déficit estimé grandit.",
                "Un historique à relire quand un après-midi s'est mal passé.",
                "Rien de diagnostique : elle estime un bilan hydrique et ne prétend rien sur votre état clinique.",
            ],
            "expect": "Utilisée régulièrement, l'effet rapporté n'a rien de spectaculaire : c'est "
                      "l'absence du coup de mou de seize heures. Ce qu'elle ne peut pas faire, c'est "
                      "vous dire si vous êtes déshydraté : elle estime un bilan à partir des capteurs "
                      "et de vos enregistrements, et les signes ci-dessus restent ce qu'il faut "
                      "surveiller.",
            "faq": [
                ("Une montre connectée peut-elle détecter la déshydratation ?",
                 "Aucune montre grand public ne mesure directement l'hydratation. HydroPulse estime un "
                 "bilan hydrique à partir du cardio, de l'activité, de la météo et de vos "
                 "enregistrements : une estimation fondée, pas une mesure ni un diagnostic."),
                ("La couleur des urines est-elle fiable ?",
                 "C'est le contrôle quotidien le plus pratique. Jaune paille clair suggère que vous "
                 "êtes dans les clous, plus foncé que vous êtes en retard. Certaines vitamines, "
                 "médicaments et aliments la colorent indépendamment."),
                ("Quand consulter un médecin ?",
                 "Confusion, malaise, cœur qui s'emballe au repos, absence d'urines pendant de longues "
                 "heures ou signes de coup de chaleur imposent une prise en charge urgente. De même "
                 "pour une déshydratation avec vomissements ou diarrhée persistants, en particulier "
                 "chez l'enfant et la personne âgée."),
                ("L'application me prévient-elle si je suis déshydraté ?",
                 "Elle vous prévient quand son bilan estimé franchit votre seuil. C'est une invitation "
                 "à boire, pas une évaluation clinique, et cela ne doit jamais retarder une consultation."),
            ],
        },
        "heartrate": {
            "slug": "frequence-cardiaque-et-hydratation",
            "nav": "Cardio & hydratation",
            "card": "Le lien entre dérive cardiaque, intensité et perte hydrique.",
            "title": "Fréquence cardiaque et hydratation | HydroPulse",
            "desc": "Pourquoi la fréquence cardiaque prédit mieux la perte hydrique que le nombre de "
                    "pas, ce qu'est la réserve cardiaque, et comment HydroPulse la convertit en mL/h.",
            "h1": "Fréquence cardiaque et hydratation",
            "lede": "La fréquence cardiaque est le seul signal disponible en continu sur une montre qui "
                    "suive l'intensité réelle du travail de votre corps. C'est donc le meilleur "
                    "indicateur indirect de votre vitesse de perte hydrique.",
            "why_title": "Pourquoi le cardio plutôt que les pas",
            "why": [
                "Un nombre de pas dit combien vous avez bougé, pas à quel point c'était difficile. Dix "
                "mille pas à plat à l'ombre et cinq mille en montée au soleil affichent des chiffres "
                "sans rapport avec leur coût métabolique. La fréquence cardiaque les sépare, parce "
                "qu'elle répond à la charge et non à la distance.",
                "La forme utile est la réserve cardiaque : où se situe votre fréquence actuelle entre "
                "votre repos et votre maximum. Exprimé ainsi, 140 bpm ne signifie pas la même chose "
                "pour un trentenaire entraîné et pour un sédentaire de 55 ans, et le modèle les traite "
                "différemment. Le taux de sudation suit le métabolisme, et la réserve cardiaque en est "
                "un substitut raisonnable hors laboratoire.",
                "Il existe une boucle de rétroaction utile à connaître. À mesure que vous perdez du "
                "liquide, le volume plasmatique baisse et la fréquence cardiaque monte à effort "
                "constant : c'est la dérive cardiaque. Une fréquence qui grimpe pendant une longue "
                "séance régulière est donc en soi un indice de déficit qui s'accumule, et l'estimation "
                "penche dans le bon sens au fil de la séance.",
            ],
            "works_on": [
                "Suivi cardiaque passif continu via Health Services de Wear OS.",
                "Réserve cardiaque calculée à partir de vos propres fréquences de repos et maximale, modifiables dans les réglages.",
                "Détection de l'état d'exercice, pour pondérer autrement un entraînement délibéré.",
                "Un multiplicateur de sudation qui combine effort et indice de chaleur au lieu de les traiter séparément.",
                "Une décomposition transparente : chaque recommandation indique si c'est la chaleur, l'effort ou la base qui domine.",
            ],
            "expect": "Renseignez vos fréquences de repos et maximale si vous les connaissez ; la valeur "
                      "par défaut fondée sur l'âge — environ 220 moins votre âge — est une "
                      "formule de population à forte dispersion, et la corriger est le plus grand gain "
                      "de précision à votre portée. Les capteurs optiques au poignet perdent aussi en "
                      "précision à haute intensité et par temps froid : l'estimation vaut ce que vaut "
                      "le signal reçu.",
            "faq": [
                ("La déshydratation augmente-t-elle la fréquence cardiaque ?",
                 "Oui. La perte de liquide réduit le volume plasmatique, donc le cœur bat plus vite "
                 "pour maintenir le débit — c'est la dérive cardiaque à l'effort prolongé. C'est "
                 "un signal parmi d'autres, pas un hydratomètre."),
                ("Dois-je connaître ma fréquence cardiaque maximale ?",
                 "Non, l'application retombe sur une estimation par l'âge. Mais cette formule a un "
                 "écart-type d'une dizaine de battements par minute : saisir une valeur réellement "
                 "mesurée affine sensiblement le modèle."),
                ("Lire le cardio toute la journée vide-t-il la batterie ?",
                 "Elle utilise la surveillance passive plutôt qu'un flux continu à haute fréquence, "
                 "c'est-à-dire la voie basse consommation prévue par Wear OS pour ce type d'usage en "
                 "arrière-plan."),
                ("Et si le capteur cardiaque de ma montre est imprécis ?",
                 "La composante effort le sera d'autant. Un bracelet lâche, les tatouages et une peau "
                 "froide dégradent tous la lecture optique. Les composantes de base et météo ne sont "
                 "pas affectées."),
            ],
        },
    },
}

# ----------------------------------------------------------------- Español ----

ES = {
    "code": "es",
    "label": "ES",
    "name": "Español",
    "base": "es",
    "topic_dir": "hidratacion",
    "ui": {
        "home_crumb": "Inicio",
        "badge_alt": "Disponible en Google Play",
        "cta_note": "Wear OS 3.0+. Pago único: sin suscripción, sin anuncios, sin cuenta.",
        "app_lang_note": "La interfaz de la aplicación está en inglés.",
        "how_title": "Cómo decide HydroPulse",
        "how_steps": [
            "Introduces una sola vez tu peso, tu edad y tu perfil de sudoración. Eso fija tu pérdida basal personal: el agua que pierdes simplemente por respirar y estar vivo.",
            "El reloj lee tu frecuencia cardíaca de forma continua y la convierte en una fracción de reserva cardíaca: cuánto esfuerzo haces respecto a tus propias frecuencias de reposo y máxima, no a las de una persona media.",
            "La temperatura y la humedad locales se consultan de forma anónima y se traducen en un multiplicador de índice de calor, porque el mismo esfuerzo cuesta mucho más líquido a 33 °C con 70 % de humedad que a 18 °C.",
            "Cada bebida que registras se abona al balance. Cuando el saldo cruza tu umbral, HydroPulse te avisa: con una cantidad concreta en mililitros y el motivo que hay detrás.",
        ],
        "works_title": "Qué hace HydroPulse aquí",
        "expect_title": "Qué esperar",
        "faq_title": "Preguntas frecuentes",
        "features_title": "Por qué no es otro temporizador",
        "features": [
            "Un balance hídrico continuo, no una cuenta atrás: el intervalo entre avisos cambia con tu día.",
            "Estimación de sudoración guiada por la frecuencia cardíaca, con tus propias cifras de reposo y máxima.",
            "Temperatura y humedad en directo, integradas mediante un multiplicador de índice de calor.",
            "Cada aviso trae una cantidad en mililitros y un motivo en lenguaje claro: calor, esfuerzo o metabolismo basal.",
            "Tres niveles de urgencia —leve, moderado, urgente— para que un recordatorio no se confunda con una alerta seria.",
            "Tile nativo de Wear OS y complicación de esfera: tu saldo de un vistazo, sin abrir nada.",
            "Registro con un toque desde la notificación, más un aplazamiento de 15 minutos.",
            "Horas de silencio, para que no te despierte.",
            "Unidades en mL, onzas líquidas o imperiales, y tu propio umbral.",
        ],
        "privacy_title": "Privada por diseño",
        "privacy_body": "Tu frecuencia cardíaca, tu actividad y tu registro de bebidas nunca salen del "
                        "reloj. No hay cuenta, ni SDK publicitario, ni analítica de producto: nada "
                        "rastrea lo que haces en la aplicación. Dos cosas sí salen del dispositivo: un "
                        "par de coordenadas a un servicio meteorológico público, sin identificador "
                        "alguno, y un informe de fallo si la aplicación se cae. Ninguno lleva tus "
                        "datos de salud.",
        "privacy_link": "Leer la política de privacidad completa",
        "safety_title": "No es un dispositivo médico",
        "safety_body": "HydroPulse produce una estimación, no una medición. Es una herramienta de "
                       "bienestar, no un dispositivo médico: no diagnostica, no trata ni monitoriza la "
                       "deshidratación ni ninguna otra afección. Si tomas diuréticos, si tienes el "
                       "aporte de líquidos restringido por indicación médica, o si padeces una "
                       "enfermedad renal, cardíaca o endocrina, sigue las pautas de tu médico antes "
                       "que las de la aplicación. Busca atención urgente ante confusión, desmayo o "
                       "golpe de calor.",
        "related_title": "Más sobre hidratación",
        "topics_title": "La hidratación, situación por situación",
        "foot_tag": "HydroPulse — hidratación adaptativa para Wear OS. Estimaciones, no conjeturas.",
        "foot_privacy": "Política de privacidad",
        "foot_play": "Google Play",
        "foot_terms": "Condiciones del servicio",
        "langs_label": "Idioma",
        "screens_title": "En el reloj",
        "sources_title": "De dónde sale el modelo",
        "sources_body": "La línea base se apoya en las ingestas adecuadas del IOM y la EFSA, el "
                        "componente de sudoración en las recomendaciones de hidratación en el ejercicio "
                        "del ACSM, y el multiplicador ambiental en la fórmula del índice de calor del "
                        "Servicio Meteorológico Nacional de EE. UU. Son referencias poblacionales "
                        "adaptadas a lo que un reloj puede percibir realmente: una estimación bien "
                        "fundada, no una medición de laboratorio.",
        "screens": [
            ("home", "Pantalla principal de HydroPulse con un saldo de hidratación del 49 % y un botón de registro",
             "Tu saldo como un dial, con la cantidad que toca beber ahora."),
            ("notification", "Una notificación de HydroPulse que recomienda 100 mL con registro de un toque",
             "Un toque para registrar, otro para aplazar: el móvil se queda en el bolsillo."),
            ("history", "La pantalla de historial con las bebidas registradas del día",
             "Lo que has bebido hoy, no lo que pensabas beber."),
            ("settings", "La pantalla de ajustes con peso, unidades y umbral",
             "Tu peso, tus unidades, tu umbral: el modelo se ajusta a ti."),
        ],
    },
    "home": {
        "title": "HydroPulse — Recordatorios de hidratación para Wear OS",
        "desc": "Un recordatorio de beber agua para Wear OS que se adapta a tu pulso, tu actividad y "
                "el tiempo: te avisa cuando tu cuerpo lo necesita, no por reloj.",
        "h1": "Recordatorios de hidratación que siguen a tu cuerpo, no a un temporizador",
        "lede": "La mayoría de las apps divide un objetivo diario entre tus horas de vigilia y vibra "
                "con el cociente. HydroPulse ejecuta un modelo de balance hídrico en tu reloj "
                "—pulso, actividad y clima— y te avisa cuando el saldo baja de verdad.",
        "intro": [
            "Una hora de escritorio con aire acondicionado y una hora corriendo en agosto le cuestan a "
            "tu cuerpo cantidades de agua muy distintas. Un intervalo fijo no sabe distinguirlas: o te "
            "molesta cuando no hace falta o calla cuando sí, y ambos fallos te enseñan a ignorarlo.",
            "HydroPulse lleva en cambio un balance continuo. La pérdida pasiva desciende desde tu línea "
            "base personal; la pérdida por sudor se estima según cuánto trabaja tu corazón respecto a "
            "tus propias frecuencias de reposo y máxima; el calor y la humedad amplifican esa "
            "estimación. Cada bebida registrada abona el balance. La alerta salta según el saldo: un "
            "día fresco y sedentario apenas la oirás, y un día de entrenamiento con calor la oirás "
            "pronto.",
            "Está hecha para la muñeca, no portada a ella: tile nativo, complicación de esfera, "
            "registro de un toque desde la notificación y una recomendación que siempre dice una "
            "cantidad y un motivo en lugar de limitarse a «bebe agua».",
        ],
    },
    "topics": {
        "wearos": {
            "slug": "recordatorio-de-agua-wear-os",
            "nav": "En Wear OS",
            "card": "Un recordatorio de agua hecho para el reloj, no una app de móvil con complicación.",
            "title": "App de recordatorio de agua para Wear OS — HydroPulse",
            "desc": "Un recordatorio de hidratación nativo de Wear OS con tile, complicación y registro "
                    "de un toque. Compatible con Pixel Watch, Galaxy Watch y Wear OS 3.0+.",
            "h1": "Un recordatorio de agua hecho para Wear OS",
            "lede": "Tile, complicación, acciones de notificación y modelo a bordo: HydroPulse calcula "
                    "en la muñeca, así que el aviso llega donde ya están tus manos.",
            "why_title": "Por qué el reloj es el sitio adecuado",
            "why": [
                "La hidratación falla por fricción. Entre «debería beber» y un vaso realmente bebido "
                "suele haber un móvil en otra habitación, y para cuando lo encuentras el momento ha "
                "pasado. Una notificación en la muñeca con un botón de registro reduce esa distancia a "
                "un solo toque.",
                "El reloj es además el único aparato que sabe cuánto estás esforzándote. La frecuencia "
                "cardíaca y el estado de ejercicio salen de los sensores apoyados en tu brazo, así que "
                "la estimación se construye sobre fisiología en directo y no sobre un recuento de "
                "pasos sincronizado horas después.",
                "La mayoría de las apps de hidratación de Play Store son apps de móvil que añaden una "
                "complicación como extra. HydroPulse es una app de Wear OS: el modelo, el balance y la "
                "base de datos viven en el reloj, y sigue funcionando cuando el móvil no está cerca.",
            ],
            "works_on": [
                "Un tile a un deslizamiento que muestra tu saldo sin abrir nada.",
                "Una complicación de esfera, como valor graduado o texto corto.",
                "Notificaciones con «Log water» y aplazar 15 min como acciones directas.",
                "Base de datos y perfil guardados en el reloj: el historial sobrevive a la pérdida de conexión con el móvil.",
                "Wear OS 3.0 en adelante: Pixel Watch, Galaxy Watch 4 y posteriores, TicWatch y otros.",
            ],
            "expect": "Instálala en el reloj, ajusta una vez tu peso y tus unidades y concede "
                      "frecuencia cardíaca, actividad y ubicación aproximada cuando las pida: cada una "
                      "alimenta una parte concreta del modelo, y la app funciona sin ellas con valores "
                      "por defecto razonables. El coste de batería es bajo: monitorización cardíaca "
                      "pasiva, una comprobación periódica en segundo plano y clima en caché 30 minutos.",
            "faq": [
                ("¿Necesito llevar el móvil?",
                 "No. El modelo, el balance y el registro de bebidas funcionan en el reloj. El móvil "
                 "solo interviene en la instalación inicial, y la consulta del clima usa la conexión "
                 "que tenga el reloj."),
                ("¿En qué relojes funciona?",
                 "En cualquier reloj con Wear OS 3.0 o posterior y servicios de Google Play: Pixel "
                 "Watch, Galaxy Watch 4 y siguientes, TicWatch y equivalentes. La precisión cardíaca "
                 "varía según el aparato, y el modelo se degrada con elegancia si falta un sensor."),
                ("¿Hay app para el móvil?",
                 "No, y es deliberado. Todo lo que necesitas está en el reloj, y por eso tampoco hay "
                 "nada que sincronizar ni una cuenta que crear."),
                ("¿Cuánta batería consume?",
                 "Usa la monitorización pasiva de Health Services en lugar de un flujo continuo de "
                 "sensor a alta frecuencia, se despierta periódicamente con WorkManager y cachea el "
                 "clima 30 minutos. En uso normal es una app de segundo plano, no un registrador de "
                 "entrenamientos."),
            ],
        },
        "sport": {
            "slug": "hidratacion-para-correr-y-entrenar",
            "nav": "Correr y entrenar",
            "card": "Avisos ajustados a tu tasa de sudoración, para carrera, bici y gimnasio.",
            "title": "Hidratación para correr y entrenar | HydroPulse",
            "desc": "Cuánto beber al entrenar y cómo HydroPulse estima la pérdida por sudor a partir de "
                    "tu reserva cardíaca y del clima, en vez de una regla fija por hora.",
            "h1": "Hidratación para correr y entrenar",
            "lede": "La tasa de sudoración va de unos 0,5 a más de 2 litros por hora según el atleta y "
                    "las condiciones. Una única cifra por hora no cubre ese rango; tu pulso y el "
                    "clima sí lo estrechan.",
            "why_title": "Por qué una cantidad fija por hora falla con los deportistas",
            "why": [
                "Dos corredores que hacen los mismos 10 km pueden perder volúmenes de líquido que "
                "difieren en un factor de tres, según masa corporal, forma física, aclimatación y el "
                "calor del día. Un consejo genérico tiene que elegir una cifra intermedia, que se "
                "queda corta con quien suda mucho y sobra para el resto.",
                "El esfuerzo es justo lo que un podómetro no ve. La reserva cardíaca —dónde está "
                "tu pulso actual entre tu reposo y tu máximo— sigue la carga metabólica mucho mejor "
                "que el ritmo o la cadencia, y es la carga metabólica la que impulsa la sudoración.",
                "La recuperación importa tanto como la sesión. El déficit acumulado en una hora dura "
                "no desaparece en la meta: HydroPulse mantiene el balance en negativo después y sigue "
                "pidiendo hasta que se salda.",
            ],
            "works_on": [
                "Un componente de esfuerzo guiado por la reserva cardíaca: un trote suave y un esfuerzo en umbral no se tratan igual.",
                "Un ajuste de perfil de sudoración (baja, media, alta) para calibrar en personal.",
                "Escalado por índice de calor: la misma sesión en julio pide más que en noviembre.",
                "Déficit posterior a la sesión que se arrastra en lugar de reiniciarse.",
                "Niveles de urgencia, para que un aviso leve en el calentamiento no se parezca a uno urgente en el kilómetro 15.",
            ],
            "expect": "Para mejores resultados introduce tus frecuencias de reposo y máxima en lugar de "
                      "dejar la estimación por edad, y elige el perfil de sudoración que coincida con "
                      "lo que sabes de ti. Si alguna vez te has pesado antes y después de una sesión "
                      "larga, la diferencia en kilogramos equivale más o menos a tu pérdida de líquido "
                      "en litros: es el dato de calibración más útil que puedes aportar.",
            "faq": [
                ("¿Puede sustituir una prueba de sudoración real?",
                 "No. Pesarse antes y después de una sesión en condiciones conocidas sigue siendo el "
                 "patrón de referencia. HydroPulse estima de forma continua con sensores, mucho más "
                 "práctico a diario pero menos preciso que una prueba controlada."),
                ("¿Sirve para beber en competición?",
                 "Seguirá estimando y abonando lo que registres, y la acción de la notificación hace "
                 "que registrar sea rápido. Muchos atletas también la aplazan durante la carrera y "
                 "revisan luego el historial."),
                ("¿Y los electrolitos?",
                 "HydroPulse sigue el volumen de líquido, no el sodio. En sesiones largas o muy "
                 "calurosas la reposición de electrolitos es una cuestión aparte que conviene mirar: "
                 "beber grandes volúmenes de agua pura durante horas no está libre de riesgo."),
                ("¿Cuentan el café y el té?",
                 "Puedes registrar cualquier bebida. En consumidores habituales, las bebidas con "
                 "cafeína en cantidad moderada sí contribuyen al aporte diario de líquido; el alcohol "
                 "es el que juega en contra."),
            ],
        },
        "heat": {
            "slug": "beber-agua-con-mucho-calor",
            "nav": "Mucho calor",
            "card": "Cuando el calor y la humedad suben tus necesidades, los avisos se mueven primero.",
            "title": "Beber agua con mucho calor — avisos que siguen al clima",
            "desc": "El calor y la humedad cambian cuánto necesitas beber antes de la sed. Cómo HydroPulse "
                    "usa el clima y el índice de calor para adelantar los avisos.",
            "h1": "Beber agua con mucho calor",
            "lede": "La humedad es lo que más se subestima: cuando el sudor no puede evaporarse, el "
                    "cuerpo produce más para enfriar menos. HydroPulse lee temperatura y humedad y "
                    "desplaza tus avisos en consecuencia.",
            "why_title": "Por qué el termómetro solo no basta",
            "why": [
                "A 32 °C con 30 % de humedad el sudor se evapora y cumple su función. A la misma "
                "temperatura con 75 % de humedad te resbala: pierdes el líquido sin obtener el "
                "enfriamiento, y el cuerpo compensa sudando más. El índice de calor existe "
                "precisamente para capturar esa diferencia, y es lo que HydroPulse introduce en el "
                "modelo.",
                "Con calor, la sed es un indicador tardío. Cuando aprieta, con frecuencia ya has "
                "perdido un uno o dos por ciento de masa corporal, y en condiciones calurosas esa "
                "brecha se abre más rápido de lo que la sensación tarda en alcanzarla.",
                "El calor también sube tus necesidades mientras no haces nada. Una tarde quieta en un "
                "balcón tiene un coste hídrico real que ningún medidor de actividad registra: por eso "
                "el multiplicador ambiental se aplica a la línea base y no solo al ejercicio.",
            ],
            "works_on": [
                "Temperatura y humedad en directo, consultadas de forma anónima a un servicio meteorológico público.",
                "Un multiplicador de índice de calor aplicado a la pérdida basal, no solo a los entrenamientos.",
                "Avisos más tempranos y frecuentes los días calurosos, sin que cambies ningún ajuste.",
                "Solo ubicación aproximada: lo justo para el clima local, nunca seguimiento preciso.",
                "Una caché de clima de 30 minutos: la precisión casi no cuesta batería.",
            ],
            "expect": "Un día realmente caluroso notarás que pide antes y pide más; un día fresco se "
                      "quedará callada. Ese contraste es la función. La ubicación aproximada es "
                      "opcional: si la rechazas, la app recurre a un valor templado por defecto, "
                      "prudente pero tosco en plena ola de calor.",
            "faq": [
                ("¿Usa la ubicación precisa?",
                 "No. Pide solo ubicación aproximada, la usa para consultar las condiciones locales y "
                 "no la almacena. La petición lleva coordenadas y nada que te identifique a ti o a tu "
                 "reloj."),
                ("¿Y si deniego la ubicación?",
                 "La app sigue funcionando con un valor templado por defecto para el componente "
                 "ambiental. Tu frecuencia cardíaca y tu actividad siguen alimentando la estimación; "
                 "solo falta la mitad meteorológica."),
                ("¿Se puede beber demasiado?",
                 "Sí. Ingerir volúmenes muy grandes de agua pura en poco tiempo puede diluir el sodio "
                 "en sangre, lo cual es peligroso. HydroPulse recomienda cantidades modestas repartidas "
                 "por el día y no está diseñada para empujarte a los extremos."),
                ("¿Sirve en una sauna o un taller caluroso?",
                 "Registrará la subida de pulso, pero lee el clima exterior: una fuente de calor "
                 "interior que no ve quedará infraestimada. Toma entonces su cifra como un mínimo."),
            ],
        },
        "work": {
            "slug": "olvidarse-de-beber-agua-en-el-trabajo",
            "nav": "En el trabajo",
            "card": "Para jornadas de escritorio en las que seis horas pasan entre dos vasos.",
            "title": "Olvidarse de beber agua en el trabajo | HydroPulse",
            "desc": "Por qué las jornadas de oficina acaban en déficit hídrico, y cómo un aviso en la "
                    "muñeca con registro de un toque sobrevive a una agenda llena.",
            "h1": "Olvidarse de beber agua en el trabajo",
            "lede": "Nadie olvida beber por desconocimiento. Se olvida porque la concentración, que es "
                    "algo bueno, silencia una señal débil durante horas seguidas.",
            "why_title": "Por qué la hidratación se tuerce en silencio en la oficina",
            "why": [
                "El trabajo profundo y las reuniones encadenadas hacen lo mismo con la sed: empujan una "
                "señal de baja prioridad por debajo del umbral en el que actuarías. El déficit es "
                "gradual, y justo por eso pasa desapercibido hasta el dolor de cabeza de media tarde y "
                "esa sensación plana que se le achaca a la reunión.",
                "El aire acondicionado y la calefacción resecan el aire, y una oficina diáfana y cálida "
                "está más arriba de lo que crees en la escala ambiental. Nada de esto es dramático; "
                "todo suma a lo largo de ocho horas.",
                "Si la mayoría de las apps de recordatorio acaban desinstaladas en el trabajo es porque "
                "saltan en plena reunión y a las 23:00, y la gente las silencia en una semana. Un "
                "horario previsible es peor que ninguno: el aviso que siempre se equivoca es el que "
                "aprendes a descartar sin leerlo.",
            ],
            "works_on": [
                "Horas de silencio: nada salta de noche ni en la franja que bloquees.",
                "Aplazar 15 minutos, para cuando el aviso cae a mitad de frase en una reunión.",
                "Registro de un toque en la muñeca: sin móvil, sin cambiar de app, sin perder el hilo.",
                "Menos avisos en días sedentarios, porque el balance se vacía más despacio en reposo.",
                "Un tile que puedes mirar entre llamadas en vez de esperar a que te interrumpan.",
            ],
            "expect": "En un día normal de interior espera unos pocos avisos en lugar de un tamborileo "
                      "cada hora, cada uno con una cantidad para que la decisión ya esté tomada. Si te "
                      "parece demasiado frecuente o demasiado callada, el ajuste de umbral mueve el "
                      "punto de disparo sin obligarte a cambiar tu jornada.",
            "faq": [
                ("¿Vibrará durante las reuniones?",
                 "Puede, y para eso está aplazar 15 min. Las horas de silencio cubren las franjas "
                 "recurrentes; para una reunión puntual, la acción de aplazar en la notificación es un "
                 "solo toque."),
                ("¿Cuentan el café y el té?",
                 "En consumidores habituales, las bebidas con cafeína en cantidad moderada contribuyen "
                 "al aporte diario de líquido, y puedes registrarlas. El alcohol es el que empuja el "
                 "balance en sentido contrario."),
                ("¿Puedo hacerla más discreta?",
                 "Sí: sube el umbral en los ajustes y el balance tendrá que bajar más antes de que "
                 "salte un aviso. Bájalo si prefieres que te avise pronto."),
                ("¿Insiste si la ignoro?",
                 "No. No vuelve a saltar mientras está aplazada y respeta las horas de silencio. El "
                 "nivel de urgencia sube según crece el déficit, pero no se repite por repetirse."),
            ],
        },
        "howmuch": {
            "slug": "cuanta-agua-hay-que-beber-al-dia",
            "nav": "Cuánta al día",
            "card": "De dónde sale la regla de los 2 litros y por qué tu cifra no es esa.",
            "title": "¿Cuánta agua hay que beber al día? Una respuesta personal",
            "desc": "La regla de los ocho vasos es una media poblacional, no tu objetivo. Qué determina "
                    "de verdad tu necesidad diaria y cómo un reloj puede estimarla hora a hora.",
            "h1": "¿Cuánta agua hay que beber al día?",
            "lede": "La respuesta honesta es que una cifra diaria única es la unidad equivocada. Tu "
                    "necesidad la fijan tu masa corporal, tu esfuerzo y tu entorno, y los tres cambian "
                    "de un día para otro.",
            "why_title": "De dónde vienen las cifras habituales",
            "why": [
                "Los números detrás de «ocho vasos» o «dos litros» proceden de referencias "
                "poblacionales de ingesta adecuada: el Institute of Medicine estadounidense sitúa el "
                "agua total diaria en torno a 3,7 L en hombres y 2,7 L en mujeres, y la EFSA da cifras "
                "europeas similares. Ambas son totales de todas las fuentes, comida incluida, y medias "
                "de una población entera más que prescripciones para una persona.",
                "La masa corporal es el mayor factor individual, y por eso el mismo consejo no puede "
                "servir a un adulto de 55 kg y a otro de 95 kg. La edad, el sexo y el embarazo o la "
                "lactancia desplazan más la línea base, y cualquiera de esos ajustes pesa más que la "
                "diferencia entre seis y ocho vasos.",
                "Luego está el día en sí. Una tarde de calor o una sesión dura pueden añadir cada una "
                "más a tu requerimiento que todo el debate sobre la línea base: por eso HydroPulse "
                "calcula una base con tus propias cifras y luego la ajusta continuamente, en vez de "
                "entregarte un objetivo fijo por la mañana.",
            ],
            "works_on": [
                "Una línea base derivada de tu peso, tu edad y tu sexo, no de una media poblacional.",
                "Ajuste por embarazo o lactancia, que elevan las necesidades de forma medible.",
                "Ajuste continuo por esfuerzo y clima en lugar de un único objetivo matutino.",
                "Una recomendación en mililitros u onzas líquidas, para que «cuánto ahora» tenga respuesta.",
                "Una pantalla de historial que muestra en qué quedó realmente el día, con lo que tú registres.",
            ],
            "expect": "Espera un total diario personal que se mueve: a menudo bastante por debajo de "
                      "los dos litros habituales en un día fresco y sedentario, y bastante por encima "
                      "en uno caluroso y activo. La comida aporta aproximadamente una quinta parte del "
                      "agua total y HydroPulse no intenta estimarla, así que sus cifras describen lo "
                      "que bebes.",
            "faq": [
                ("¿Está mal lo de dos litros al día?",
                 "No está mal, es genérico. Es una estimación central razonable para el aporte total de "
                 "una población y un mal objetivo para una persona concreta en un día concreto."),
                ("¿Cuenta la comida en el total?",
                 "Sí, alrededor del 20 % del agua total procede de los alimentos en una dieta típica. "
                 "HydroPulse solo registra bebidas, así que sus cifras tratan deliberadamente de lo que "
                 "bebes."),
                ("¿Hay que beber por horario o a demanda de sed?",
                 "Para la mayoría de adultos sanos en condiciones normales, la sed es una guía "
                 "suficiente. Pierde fiabilidad con la edad, con calor, en ejercicio intenso y en plena "
                 "concentración: justo los casos a los que apunta esta app."),
                ("¿Puedo fijar mi propio objetivo diario?",
                 "HydroPulse razona con un balance más que con un objetivo, pero el ajuste de umbral te "
                 "deja decidir cuánto puede caer el saldo antes de que diga algo, que en la práctica es "
                 "la misma palanca."),
            ],
        },
        "signs": {
            "slug": "senales-de-deshidratacion",
            "nav": "Señales de deshidratación",
            "card": "Cómo se siente de verdad una deshidratación leve, y cuándo deja de ser leve.",
            "title": "Señales de deshidratación — qué mirar y cuándo preocuparse",
            "desc": "La deshidratación leve aparece como fatiga, dolor de cabeza y falta de "
                    "concentración mucho antes que la sed. Las señales tempranas y las graves.",
            "h1": "Señales de deshidratación",
            "lede": "Perder entre uno y dos por ciento de masa corporal en líquido basta para embotar la "
                    "concentración y el ánimo. Rara vez se anuncia como sed: más bien como una tarde "
                    "plana que achacas a otra cosa.",
            "why_title": "Señales tempranas y las que importan",
            "why": [
                "Los marcadores tempranos habituales son orina oscura o poco frecuente, dolor de cabeza "
                "sordo, fatiga que no encaja con lo que dormiste, boca y labios secos, y una caída de "
                "concentración o de ánimo. El color de la orina es el más práctico: amarillo pajizo "
                "claro es el objetivo, y cualquier tono más oscuro que un zumo de manzana merece que "
                "actúes.",
                "La sed llega tarde y de forma poco fiable. Se embota con la edad, durante el ejercicio "
                "intenso, con frío y cuando estás absorto: «bebo cuando tengo sed» funciona mejor en "
                "teoría que una tarde de agosto o en una reunión larga.",
                "Algunas señales no se resuelven con un vaso de agua. Confusión, desmayo, corazón "
                "acelerado en reposo, ausencia de orina durante muchas horas, o un agotamiento por "
                "calor que progresa a piel caliente y seca y desorientación requieren atención médica, "
                "no una app. Lo mismo vale para la deshidratación con vómitos o diarrea, sobre todo en "
                "niños y personas mayores.",
            ],
            "works_on": [
                "Avisar antes de la fatiga y el dolor de cabeza: ese es todo el sentido de estimar en vez de reaccionar.",
                "Nombrar el motivo —calor, esfuerzo o metabolismo basal— para que la señal sea interpretable.",
                "Escalar la urgencia según crece el déficit estimado.",
                "Un historial que puedes repasar cuando una tarde ha ido mal.",
                "Nada diagnóstico: estima un balance hídrico y no afirma nada sobre tu estado clínico.",
            ],
            "expect": "Usada con constancia, el efecto que la gente describe no es espectacular: es la "
                      "ausencia del bajón de las cuatro de la tarde. Lo que no puede hacer es decirte si "
                      "estás deshidratado: estima un balance a partir de los sensores y de lo que "
                      "registras, y las señales de arriba siguen siendo lo que hay que vigilar.",
            "faq": [
                ("¿Puede un reloj detectar la deshidratación?",
                 "Ningún reloj de consumo mide la hidratación directamente. HydroPulse estima un "
                 "balance hídrico con pulso, actividad, clima y lo que registras: una estimación bien "
                 "fundada, no una medición ni un diagnóstico."),
                ("¿Es fiable el color de la orina?",
                 "Es la comprobación diaria más práctica. Amarillo pajizo claro sugiere que vas bien; "
                 "más oscuro, que vas por detrás. Algunas vitaminas, medicamentos y alimentos la tiñen "
                 "por su cuenta."),
                ("¿Cuándo debo ir al médico?",
                 "Confusión, desmayo, corazón acelerado en reposo, ausencia de orina durante muchas "
                 "horas o señales de golpe de calor requieren atención urgente. También la "
                 "deshidratación con vómitos o diarrea persistentes, sobre todo en niños y mayores."),
                ("¿La app me avisa si estoy deshidratado?",
                 "Te avisa cuando su balance estimado cruza tu umbral. Es una invitación a beber, no "
                 "una valoración clínica, y nunca debe retrasar la búsqueda de atención médica."),
            ],
        },
        "heartrate": {
            "slug": "frecuencia-cardiaca-e-hidratacion",
            "nav": "Pulso e hidratación",
            "card": "La relación entre deriva cardíaca, esfuerzo y pérdida de líquido.",
            "title": "Frecuencia cardíaca e hidratación: estimar el sudor",
            "desc": "Por qué el pulso predice la pérdida de líquido mejor que los pasos, qué es la "
                    "reserva cardíaca y cómo HydroPulse la convierte en mililitros por hora.",
            "h1": "Frecuencia cardíaca e hidratación",
            "lede": "La frecuencia cardíaca es la única señal disponible de forma continua en un reloj "
                    "que sigue cuánto trabaja realmente tu cuerpo. Eso la convierte en el mejor "
                    "indicador indirecto de a qué velocidad pierdes líquido.",
            "why_title": "Por qué el pulso y no los pasos",
            "why": [
                "Un recuento de pasos dice cuánto te moviste, no cuánto costó. Diez mil pasos en llano "
                "a la sombra y cinco mil cuesta arriba al sol son cifras sin relación con su coste "
                "metabólico. La frecuencia cardíaca las separa, porque responde a la carga y no a la "
                "distancia.",
                "La forma útil es la reserva cardíaca: dónde está tu pulso actual entre tu reposo y tu "
                "máximo. Expresado así, 140 lpm significa algo distinto para alguien entrenado de 30 "
                "años y para un sedentario de 55, y el modelo los trata distinto. La tasa de sudoración "
                "escala con la tasa metabólica, y la reserva cardíaca es un sustituto razonable de esta "
                "fuera del laboratorio.",
                "Hay un bucle de retroalimentación que conviene conocer. A medida que pierdes líquido, "
                "el volumen plasmático baja y el pulso sube al mismo esfuerzo: es la deriva cardíaca. "
                "Un pulso que trepa durante una sesión larga y constante es en sí mismo un indicio "
                "débil de déficit acumulándose, y la estimación se inclina en la dirección correcta "
                "conforme avanza la sesión.",
            ],
            "works_on": [
                "Monitorización cardíaca pasiva continua mediante Health Services de Wear OS.",
                "Reserva cardíaca calculada con tus propias frecuencias de reposo y máxima, editables en ajustes.",
                "Detección del estado de ejercicio, para ponderar distinto un entrenamiento deliberado.",
                "Un multiplicador de sudoración que combina esfuerzo e índice de calor en vez de tratarlos por separado.",
                "Un desglose transparente: cada recomendación dice si mandó el calor, el esfuerzo o la base.",
            ],
            "expect": "Introduce tus frecuencias de reposo y máxima si las conoces; el valor por defecto "
                      "basado en la edad —unos 220 menos tu edad— es una fórmula poblacional con "
                      "mucha dispersión, y corregirla es la mayor mejora de precisión a tu alcance. Los "
                      "sensores ópticos de muñeca además pierden precisión a alta intensidad y con "
                      "frío: la estimación vale lo que valga la señal que recibe.",
            "faq": [
                ("¿La deshidratación sube el pulso?",
                 "Sí. La pérdida de líquido reduce el volumen plasmático, así que el corazón late más "
                 "rápido para mantener el gasto: es la deriva cardíaca en ejercicio prolongado. Es una "
                 "señal entre varias, no un medidor de hidratación."),
                ("¿Tengo que saber mi frecuencia cardíaca máxima?",
                 "No, la app recurre a una estimación por edad. Pero esa fórmula tiene una desviación "
                 "típica de unos diez latidos por minuto, así que introducir un valor medido de verdad "
                 "afina el modelo de forma apreciable."),
                ("¿Leer el pulso todo el día gasta batería?",
                 "Usa monitorización pasiva en lugar de un flujo continuo a alta frecuencia, que es la "
                 "vía de bajo consumo que Wear OS ofrece precisamente para este uso en segundo plano."),
                ("¿Y si el sensor de pulso de mi reloj es impreciso?",
                 "El componente de esfuerzo será igual de tosco. Una correa floja, los tatuajes y la "
                 "piel fría degradan la lectura óptica. Los componentes basal y meteorológico no se ven "
                 "afectados."),
            ],
        },
    },
}

LANGS = [EN, FR, ES]
