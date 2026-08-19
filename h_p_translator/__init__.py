"""
Translate H and P codes to human-readable text.
"""

# H codes dictionary
H_CODES = {
    "H200": "Unstable explosive",
    "H201": "Explosive; mass explosion hazard",
    "H202": "Explosive; severe fragmentation hazard",
    "H203": "Explosive; fire blast or projection hazard",
    "H204": "Fire or projection hazard",
    "H205": "May mass explode in fire",
    "H206": "Fire blast or projection hazard; increased risk of explosion if desensitizing agent is reduced",
    "H207": "Fire or projection hazard; increased risk of explosion if desensitizing agent is reduced",
    "H208": "Fire hazard; increased risk of explosion if desensitizing agent is reduced",
    "H220": "Extremely flammable gas",
    "H221": "Flammable gas",
    "H222": "Extremely flammable aerosol",
    "H223": "Flammable aerosol",
    "H224": "Extremely flammable liquid and vapour",
    "H225": "Highly flammable liquid and vapour",
    "H226": "Flammable liquid and vapour",
    "H227": "Combustible liquid",
    "H228": "Flammable solid",
    "H229": "Pressurised container: may burst if heated",
    "H230": "May react explosively even in the absence of air",
    "H231": "May react explosively even in the absence of air at elevated pressure and/or temperature",
    "H232": "May ignite spontaneously if exposed to air",
    "H240": "Heating may cause an explosion",
    "H241": "Heating may cause a fire or explosion",
    "H242": "Heating may cause a fire",
    "H250": "Self-heating; may catch fire",
    "H251": "Self-heating; may catch fire",
    "H252": "Self-heating in large quantities; may catch fire",
    "H260": "In contact with water releases flammable gases which may ignite spontaneously",
    "H261": "In contact with water releases flammable gases",
    "H270": "May cause or intensify fire; oxidizer",
    "H271": "May cause fire or explosion; strong oxidizer",
    "H272": "May intensify fire; oxidizer",
    "H280": "Contains gas under pressure; may explode if heated",
    "H281": "Contains refrigerated gas; may cause cryogenic burns or injury",
    "H290": "May be corrosive to metals",
    "H300": "Fatal if swallowed",
    "H301": "Toxic if swallowed",
    "H302": "Harmful if swallowed",
    "H303": "May be harmful if swallowed",
    "H304": "May be fatal if swallowed and enters airways",
    "H305": "May be harmful if swallowed and enters airways",
    "H310": "Fatal in contact with skin",
    "H311": "Toxic in contact with skin",
    "H312": "Harmful in contact with skin",
    "H313": "May be harmful in contact with skin",
    "H314": "Causes severe skin burns and eye damage",
    "H315": "Causes skin irritation",
    "H316": "Causes mild skin irritation",
    "H317": "May cause an allergic skin reaction",
    "H318": "Causes serious eye damage",
    "H319": "Causes serious eye irritation",
    "H320": "Causes eye irritation",
    "H330": "Fatal if inhaled",
    "H331": "Toxic if inhaled",
    "H332": "Harmful if inhaled",
    "H333": "May be harmful if inhaled",
    "H334": "May cause allergy or asthma symptoms or breathing difficulties if inhaled",
    "H335": "May cause respiratory irritation",
    "H336": "May cause drowsiness or dizziness",
    "H340": "May cause genetic defects",
    "H341": "Suspected of causing genetic defects",
    "H342": "May cause heritable genetic defects",
    "H350": "May cause cancer",
    "H351": "Suspected of causing cancer",
    "H360": "May damage fertility or the unborn child",
    "H361": "Suspected of damaging fertility or the unborn child",
    "H362": "May cause harm to breast-fed children",
    "H370": "Causes damage to organs",
    "H371": "May cause damage to organs",
    "H372": "Causes damage to organs through prolonged or repeated exposure",
    "H373": "May cause damage to organs through prolonged or repeated exposure",
    "H400": "Very toxic to aquatic life",
    "H401": "Toxic to aquatic life",
    "H402": "Harmful to aquatic life",
    "H410": "Very toxic to aquatic life with long lasting effects",
    "H411": "Toxic to aquatic life with long lasting effects",
    "H412": "Harmful to aquatic life with long lasting effects",
    "H413": "May cause long lasting harmful effects to aquatic life",
    "H420": "Harms public health and the environment by destroying ozone in the upper atmosphere",
}

# H codes arabic dictionary
H_CODES_AR = {
    # Explosives
    "H200": "مادة متفجرة غير مستقرة",
    "H201": "متفجرة؛ خطر انفجار جماعي",
    "H202": "متفجرة؛ خطر تطاير شديد",
    "H203": "متفجرة؛ خطر حريق أو انفجار أو تطاير",
    "H204": "خطر حريق أو تطاير",
    "H205": "قد تنفجر بكميات كبيرة في الحريق",
    # Flammable gases, liquids, solids
    "H220": "غاز شديد الاشتعال",
    "H221": "غاز قابل للاشتعال",
    "H222": "هباء جوي شديد الاشتعال",
    "H223": "هباء جوي قابل للاشتعال",
    "H224": "سائل وبخاره شديدا الاشتعال",
    "H225": "سائل وبخاره شديدا الاشتعال",
    "H226": "سائل وبخاره قابلان للاشتعال",
    "H227": "سائل قابل للاحتراق",
    "H228": "مادة صلبة قابلة للاشتعال",
    "H229": "وعاء مضغوط: قد ينفجر إذا سخن",
    "H230": "قد يتفاعل بشكل متفجر حتى في غياب الهواء",
    "H231": "قد يتفاعل بشكل متفجر حتى في غياب الهواء عند ضغط و/أو درجة حرارة مرتفعة",
    "H232": "قد يشتعل تلقائياً إذا تعرض للهواء",
    # Self-reactive / Self-heating
    "H240": "التسخين قد يسبب انفجاراً",
    "H241": "التسخين قد يسبب حريقاً أو انفجاراً",
    "H242": "التسخين قد يسبب حريقاً",
    "H250": "يشتعل تلقائياً إذا تعرض للهواء",
    "H251": "مادة ذاتية التسخين؛ قد تشتعل",
    "H252": "مادة ذاتية التسخين بكميات كبيرة؛ قد تشتعل",
    # Contact with water
    "H260": "عند ملامسته للماء يطلق غازات قابلة للاشتعال قد تشتعل تلقائياً",
    "H261": "عند ملامسته للماء يطلق غازات قابلة للاشتعال",
    # Oxidizing
    "H270": "قد يسبب أو يشعل حريقاً؛ مؤكسد",
    "H271": "قد يسبب حريقاً أو انفجاراً؛ مؤكسد قوي",
    "H272": "قد يشعل حريقاً؛ مؤكسد",
    # Gases under pressure
    "H280": "يحوي غازاً تحت ضغط؛ قد ينفجر إذا سخن",
    "H281": "يحوي غازاً مبرداً؛ قد يسبب حروقاً أو إصابات بالبرودة الشديدة",
    # Corrosive to metals
    "H290": "قد يكون أكالاً للمعادن",
    # Acute toxicity - oral
    "H300": "قاتل إذا تم ابتلاعه",
    "H301": "سام إذا تم ابتلاعه",
    "H302": "ضار إذا تم ابتلاعه",
    "H303": "قد يكون ضاراً إذا تم ابتلاعه",
    "H304": "قد يكون قاتلاً إذا تم ابتلاعه ودخل إلى المجاري التنفسية",
    "H305": "قد يكون ضاراً إذا تم ابتلاعه ودخل إلى المجاري التنفسية",
    # Acute toxicity - dermal
    "H310": "قاتل عند ملامسته للجلد",
    "H311": "سام عند ملامسته للجلد",
    "H312": "ضار عند ملامسته للجلد",
    "H313": "قد يكون ضاراً عند ملامسته للجلد",
    # Skin corrosion/irritation
    "H314": "يسبب حروقاً شديدة في الجلد وأضراراً في العينين",
    "H315": "يسبب تهيج الجلد",
    "H316": "يسبب تهيجاً خفيفاً للجلد",
    "H317": "قد يسبب حساسية جلدية",
    # Serious eye damage/eye irritation
    "H318": "يسبب أضراراً جسيمة في العينين",
    "H319": "يسبب تهيجاً شديداً للعينين",
    "H320": "يسبب تهيج العينين",
    # Acute toxicity - inhalation
    "H330": "قاتل إذا تم استنشاقه",
    "H331": "سام إذا تم استنشاقه",
    "H332": "ضار إذا تم استنشاقه",
    "H333": "قد يكون ضاراً إذا تم استنشاقه",
    "H334": "قد يسبب أعراض حساسية أو ربو أو صعوبات في التنفس إذا تم استنشاقه",
    # Specific target organ toxicity
    "H335": "قد يسبب تهيج الجهاز التنفسي",
    "H336": "قد يسبب النعاس أو الدوار",
    # Germ cell mutagenicity
    "H340": "قد يسبب عيوباً وراثية",
    "H341": "يشتبه في أنه يسبب عيوباً وراثية",
    "H342": "قد يسبب عيوباً وراثية",
    # Carcinogenicity
    "H350": "قد يسبب السرطان",
    "H351": "يشتبه في أنه يسبب السرطان",
    # Reproductive toxicity
    "H360": "قد يضر بالخصوبة أو الجنين",
    "H361": "يشتبه في أنه يضر بالخصوبة أو الجنين",
    "H362": "قد يسبب ضرراً للأطفال الذين يرضعون من الثدي",
    # Specific target organ toxicity - single exposure
    "H370": "يسبب ضرراً للأعضاء",
    "H371": "قد يسبب ضرراً للأعضاء",
    # Specific target organ toxicity - repeated exposure
    "H372": "يسبب ضرراً للأعضاء نتيجة التعرض المطول أو المتكرر",
    "H373": "قد يسبب ضرراً للأعضاء نتيجة التعرض المطول أو المتكرر",
    # Hazardous to the aquatic environment
    "H400": "سام جداً للكائنات المائية",
    "H401": "سام للكائنات المائية",
    "H402": "ضار للكائنات المائية",
    "H410": "سام جداً للكائنات المائية مع تأثيرات طويلة الأمد",
    "H411": "سام للكائنات المائية مع تأثيرات طويلة الأمد",
    "H412": "ضار للكائنات المائية مع تأثيرات طويلة الأمد",
    "H413": "قد يسبب تأثيرات ضارة طويلة الأمد للكائنات المائية",
    # Hazardous to the ozone layer
    "H420": "يضر بالصحة العامة والبيئة عن طريق تدمير الأوزون في الغلاف الجوي العلوي",
}

# H codes french dictionary

H_CODES_FR = {
    # Explosives
    "H200": "Explosif instable",
    "H201": "Explosif; danger d'explosion en masse",
    "H202": "Explosif; danger de projection sévère",
    "H203": "Explosif; danger d'incendie, d'effet de souffle ou de projection",
    "H204": "Danger d'incendie ou de projection",
    "H205": "Peut exploser en masse en cas d'incendie",
    # Flammable gases, liquids, solids
    "H220": "Gaz extrêmement inflammable",
    "H221": "Gaz inflammable",
    "H222": "Aérosol extrêmement inflammable",
    "H223": "Aérosol inflammable",
    "H224": "Liquide et vapeurs extrêmement inflammables",
    "H225": "Liquide et vapeurs très inflammables",
    "H226": "Liquide et vapeurs inflammables",
    "H227": "Liquide combustible",
    "H228": "Matière solide inflammable",
    "H229": "Récipient sous pression: peut éclater sous l'effet de la chaleur",
    "H230": "Peut réagir de manière explosive même en l'absence d'air",
    "H231": "Peut réagir de manière explosive même en l'absence d'air à pression et/ou température élevée(s)",
    "H232": "Peut s'enflammer spontanément au contact de l'air",
    # Self-reactive / Self-heating
    "H240": "L'échauffement peut provoquer une explosion",
    "H241": "L'échauffement peut provoquer un incendie ou une explosion",
    "H242": "L'échauffement peut provoquer un incendie",
    "H250": "S'enflamme spontanément au contact de l'air",
    "H251": "Matière auto-échauffante; peut s'enflammer",
    "H252": "Matière auto-échauffante en grandes quantités; peut s'enflammer",
    # Contact with water
    "H260": "Au contact de l'eau, dégage des gaz inflammables qui peuvent s'enflammer spontanément",
    "H261": "Au contact de l'eau, dégage des gaz inflammables",
    # Oxidizing
    "H270": "Peut provoquer ou aggraver un incendie; comburant",
    "H271": "Peut provoquer un incendie ou une explosion; comburant puissant",
    "H272": "Peut aggraver un incendie; comburant",
    # Gases under pressure
    "H280": "Contient un gaz sous pression; peut exploser sous l'effet de la chaleur",
    "H281": "Contient un gaz réfrigéré; peut provoquer des brûlures ou blessures cryogéniques",
    # Corrosive to metals
    "H290": "Peut être corrosif pour les métaux",
    # Acute toxicity - oral
    "H300": "Mortel en cas d'ingestion",
    "H301": "Toxique en cas d'ingestion",
    "H302": "Nocif en cas d'ingestion",
    "H303": "Peut être nocif en cas d'ingestion",
    "H304": "Peut être mortel en cas d'ingestion et de pénétration dans les voies respiratoires",
    "H305": "Peut être nocif en cas d'ingestion et de pénétration dans les voies respiratoires",
    # Acute toxicity - dermal
    "H310": "Mortel par contact cutané",
    "H311": "Toxique par contact cutané",
    "H312": "Nocif par contact cutané",
    "H313": "Peut être nocif par contact cutané",
    # Skin corrosion/irritation
    "H314": "Provoque de graves brûlures de la peau et des lésions oculaires",
    "H315": "Provoque une irritation cutanée",
    "H316": "Provoque une légère irritation cutanée",
    "H317": "Peut provoquer une allergie cutanée",
    # Serious eye damage/eye irritation
    "H318": "Provoque des lésions oculaires graves",
    "H319": "Provoque une sévère irritation des yeux",
    "H320": "Provoque une irritation des yeux",
    # Acute toxicity - inhalation
    "H330": "Mortel par inhalation",
    "H331": "Toxique par inhalation",
    "H332": "Nocif par inhalation",
    "H333": "Peut être nocif par inhalation",
    "H334": "Peut provoquer des symptômes allergiques ou d'asthme ou des difficultés respiratoires par inhalation",
    # Specific target organ toxicity
    "H335": "Peut irriter les voies respiratoires",
    "H336": "Peut provoquer somnolence ou des vertiges",
    # Germ cell mutagenicity
    "H340": "Peut induire des anomalies génétiques",
    "H341": "Susceptible d'induire des anomalies génétiques",
    "H342": "Peut induire des anomalies génétiques",
    # Carcinogenicity
    "H350": "Peut provoquer le cancer",
    "H351": "Susceptible de provoquer le cancer",
    # Reproductive toxicity
    "H360": "Peut nuire à la fertilité ou à l'enfant à naître",
    "H361": "Susceptible de nuire à la fertilité ou à l'enfant à naître",
    "H362": "Peut nuire aux enfants nourris au lait maternel",
    # Specific target organ toxicity - single exposure
    "H370": "Risque avéré d'effets graves sur les organes",
    "H371": "Risque présumé d'effets graves sur les organes",
    # Specific target organ toxicity - repeated exposure
    "H372": "Risque avéré d'effets graves sur les organes à la suite d'expositions répétées ou d'une exposition prolongée",
    "H373": "Risque présumé d'effets graves sur les organes à la suite d'expositions répétées ou d'une exposition prolongée",
    # Hazardous to the aquatic environment
    "H400": "Très toxique pour les organismes aquatiques",
    "H401": "Toxique pour les organismes aquatiques",
    "H402": "Nocif pour les organismes aquatiques",
    "H410": "Très toxique pour les organismes aquatiques, entraîne des effets néfastes à long terme",
    "H411": "Toxique pour les organismes aquatiques, entraîne des effets néfastes à long terme",
    "H412": "Nocif pour les organismes aquatiques, entraîne des effets néfastes à long terme",
    "H413": "Peut entraîner des effets néfastes à long terme pour les organismes aquatiques",
    # Hazardous to the ozone layer
    "H420": "Nuit à la santé publique et à l'environnement en détruisant l'ozone dans la haute atmosphère",
}

# P codes dictionary
P_CODES = {
    "P101": "If medical advice is needed, have product container or label at hand",
    "P102": "Keep out of reach of children",
    "P103": "Read label before use",
    "P210": "Keep away from heat, sparks, open flames, hot surfaces. No smoking",
    "P211": "Do not spray on an open flame or other ignition source",
    "P220": "Keep away from clothing and other combustible materials",
    "P221": "Take any precaution to avoid mixing with combustibles",
    "P222": "Do not allow contact with air",
    "P223": "Do not allow contact with water",
    "P230": "Keep wetted with ...",
    "P231": "Handle under inert gas",
    "P232": "Protect from moisture",
    "P233": "Keep container tightly closed",
    "P234": "Keep only in original packaging",
    "P235": "Keep cool",
    "P240": "Ground and bond container and receiving equipment",
    "P241": "Use explosion-proof electrical, ventilating, lighting equipment",
    "P242": "Use only non-sparking tools",
    "P243": "Take precautionary measures against static discharge",
    "P244": "Keep reduction valves free from grease and oil",
    "P250": "Do not subject to grinding, shock, friction",
    "P251": "Pressurized container. Do not pierce or burn, even after use",
    "P260": "Do not breathe dust, fume, gas, mist, vapours, spray",
    "P261": "Avoid breathing dust, fume, gas, mist, vapours, spray",
    "P262": "Do not get in eyes, on skin, or on clothing",
    "P263": "Avoid contact during pregnancy and while nursing",
    "P264": "Wash thoroughly after handling",
    "P270": "Do not eat, drink or smoke when using this product",
    "P271": "Use only outdoors or in a well-ventilated area",
    "P272": "Contaminated work clothing should not be allowed out of the workplace",
    "P273": "Avoid release to the environment",
    "P280": "Wear protective gloves, protective clothing, eye protection, face protection",
    "P281": "Use personal protective equipment as required",
    "P282": "Wear cold insulating gloves and face shield or eye protection",
    "P283": "Wear fire/flame resistant and retardant clothing",
    "P284": "Wear respiratory protection",
    "P285": "In case of inadequate ventilation, wear respiratory protection",
    "P301": "IF SWALLOWED",
    "P302": "IF ON SKIN",
    "P303": "IF ON SKIN (or hair)",
    "P304": "IF INHALED",
    "P305": "IF IN EYES",
    "P306": "IF ON CLOTHING",
    "P307": "IF exposed",
    "P308": "IF exposed or concerned",
    "P309": "IF exposed or if you feel unwell",
    "P310": "Immediately call a POISON CENTER or doctor",
    "P311": "Call a POISON CENTER or doctor",
    "P312": "Call a POISON CENTER or doctor if you feel unwell",
    "P313": "Get medical advice or attention",
    "P314": "Get medical advice or attention if you feel unwell",
    "P315": "Get immediate medical advice or attention",
    "P320": "Specific treatment is urgent (see ... on this label)",
    "P321": "Specific treatment (see ... on this label)",
    "P322": "Specific measures (see ... on this label)",
    "P330": "Rinse mouth",
    "P331": "Do NOT induce vomiting",
    "P332": "If skin irritation occurs",
    "P333": "If skin irritation or rash occurs",
    "P334": "Immerse in cool water or wrap with wet bandages",
    "P335": "Brush off loose particles from skin",
    "P336": "Thaw with lukewarm water. Do not rub affected area.",
    "P337": "If eye irritation persists",
    "P338": "Remove contact lenses if present and easy to do. Continue rinsing",
    "P340": "Remove person to fresh air and keep comfortable for breathing",
    "P341": "If breathing is difficult, remove person to fresh air and keep comfortable",
    "P342": "If experiencing respiratory symptoms",
    "P343": "If on clothing",
    "P350": "Gently wash with plenty of soap and water",
    "P351": "Rinse cautiously with water for several minutes",
    "P352": "Wash with plenty of soap and water",
    "P353": "Rinse skin with water or shower",
    "P354": "Immediately rinse with water for several minutes",
    "P360": "Rinse immediately contaminated clothing and skin with plenty of water before removing clothes",
    "P361": "Take off immediately all contaminated clothing",
    "P362": "Take off contaminated clothing",
    "P363": "Wash contaminated clothing before reuse",
    "P370": "In case of fire",
    "P371": "In case of major fire and large quantities",
    "P372": "Explosion risk in case of fire",
    "P373": "DO NOT fight fire when fire reaches explosives",
    "P374": "Fight fire with normal precautions from a reasonable distance",
    "P375": "Fight fire remotely due to risk of explosion",
    "P376": "Stop leak if safe to do so",
    "P377": "Leaking gas fire: Do not extinguish unless leak can be stopped safely",
    "P378": "Use ... for extinction",
    "P380": "Evacuate area",
    "P381": "In case of leakage, eliminate all ignition sources",
    "P390": "Absorb spillage to prevent material damage",
    "P391": "Collect spillage",
    "P401": "Store in accordance with ...",
    "P402": "Store in a dry place",
    "P403": "Store in a well-ventilated place",
    "P404": "Store in a closed container",
    "P405": "Store locked up",
    "P406": "Store in a corrosive resistant container with a resistant inner liner",
    "P407": "Maintain air gap between stacks or pallets",
    "P410": "Protect from sunlight",
    "P411": "Store at temperatures not exceeding ... °C",
    "P412": "Do not expose to temperatures exceeding 50 °C",
    "P413": "Store bulk masses greater than ... kg at temperatures not exceeding ... °C",
    "P420": "Store separately",
    "P422": "Store contents under ...",
    "P501": "Dispose of contents and container in accordance with local regulations",
    "P502": "Refer to manufacturer or supplier for information on recovery or recycling",
}

# P codes rabic dictionary
P_CODES_AR = {
    # General precautionary statements
    "P101": "في حالة الحاجة إلى استشارة طبية، احتفظ بحاوية المنتج أو الملصق",
    "P102": "يحفظ بعيداً عن متناول الأطفال",
    "P103": "اقرأ الملصق قبل الاستخدام",
    # Prevention - General
    "P201": "احصل على تعليمات خاصة قبل الاستخدام",
    "P202": "لا تتداول المنتج قبل قراءة وفهم جميع احتياطات السلامة",
    "P210": "يحفظ بعيداً عن الحرارة والأسطح الساخنة والشرر واللهب المكشوف ومصادر الاشتعال الأخرى. ممنوع التدخين",
    "P211": "لا ترش على لهب مكشوف أو مصدر اشتعال آخر",
    "P220": "يحفظ بعيداً عن الملابس والمواد القابلة للاحتراق",
    "P221": "اتخذ جميع الاحتياطات لتجنب الخلط مع المواد القابلة للاحتراق",
    "P222": "لا تسمح بملامسته للهواء",
    "P223": "لا تسمح بملامسته للماء",
    "P230": "يحفظ مبللاً بـ ...",
    "P231": "يتعامل تحت غاز خامل",
    "P232": "يحمى من الرطوبة",
    "P233": "يحفظ الحاوية محكمة الغلق",
    "P234": "يحفظ فقط في العبوة الأصلية",
    "P235": "يحفظ في مكان بارد",
    # Prevention - Electrical/static
    "P240": "يتم تأريض وتوصيل الحاوية والمعدات المستقبلة",
    "P241": "استخدم معدات كهربائية وتهوية وإضاءة مضادة للانفجار",
    "P242": "استخدم أدوات لا تسبب شراراً",
    "P243": "اتخذ احتياطات ضد التفريغ الكهربائي الساكن",
    "P244": "حافظ على صمامات التخفيض خالية من الشحوم والزيوت",
    "P250": "لا تعرض للطحن أو الصدم أو الاحتكاك",
    "P251": "وعاء مضغوط: لا تثقب أو تحرق، حتى بعد الاستخدام",
    # Prevention - Respiratory/contact
    "P260": "لا تستنشق الغبار/الدخان/الغاز/الضباب/الأبخرة/الرذاذ",
    "P261": "تجنب استنشاق الغبار/الدخان/الغاز/الضباب/الأبخرة/الرذاذ",
    "P262": "لا تلامس العينين أو الجلد أو الملابس",
    "P263": "تجنب التلامس أثناء الحمل وأثناء الرضاعة الطبيعية",
    "P264": "اغسل اليدين جيداً بعد المناولة",
    "P270": "لا تأكل أو تشرب أو تدخن عند استخدام هذا المنتج",
    "P271": "استخدم فقط في الهواء الطلق أو في مكان جيد التهوية",
    "P272": "لا تسمح بخروج الملابس الملوثة من مكان العمل",
    "P273": "تجنب إطلاقه في البيئة",
    # Prevention - Personal protective equipment
    "P280": "ارتدِ قفازات واقية وملابس واقية وواقي للعينين وواقي للوجه",
    "P281": "استخدم معدات الوقاية الشخصية حسب الحاجة",
    "P282": "ارتدِ قفازات عازلة للبرودة وواقي للوجه أو واقي للعينين",
    "P283": "ارتدِ ملابس مقاومة للحريق/اللهب",
    "P284": "ارتدِ معدات حماية الجهاز التنفسي",
    "P285": "في حالة عدم كفاية التهوية، ارتدِ معدات حماية الجهاز التنفسي",
    # Response - Ingestion
    "P301": "في حالة البلع",
    "P301+P310": "في حالة البلع: اتصل فوراً بمركز السموم أو الطبيب",
    "P301+P312": "في حالة البلع: اتصل بمركز السموم أو الطبيب إذا شعرت بتوعك",
    "P301+P330+P331": "في حالة البلع: اشطف الفم. لا تحرض على التقيؤ",
    # Response - Skin contact
    "P302": "في حالة ملامسة الجلد",
    "P302+P350": "في حالة ملامسة الجلد: اغسل بلطف بكمية كبيرة من الماء والصابون",
    "P302+P352": "في حالة ملامسة الجلد: اغسل بكمية كبيرة من الماء والصابون",
    # Response - Skin/hair
    "P303": "في حالة ملامسة الجلد (أو الشعر)",
    "P303+P361+P353": "في حالة ملامسة الجلد (أو الشعر): انزع فوراً جميع الملابس الملوثة. اشطف الجلد بالماء",
    # Response - Inhalation
    "P304": "في حالة الاستنشاق",
    "P304+P340": "في حالة الاستنشاق: انقل الشخص إلى الهواء الطلق وابقه في وضعية مريحة للتنفس",
    "P304+P341": "في حالة الاستنشاق: إذا كان التنفس صعباً، انقل الشخص إلى الهواء الطلق وابقه في وضعية مريحة للتنفس",
    # Response - Eye contact
    "P305": "في حالة ملامسة العينين",
    "P305+P351+P338": "في حالة ملامسة العينين: اشطف بحذر بالماء لعدة دقائق. انزع العدسات اللاصقة إن وجدت ويسهل إزالتها. استمر في الشطف",
    # Response - Clothing
    "P306": "في حالة ملامسة الملابس",
    "P306+P360": "في حالة ملامسة الملابس: اشطف فوراً الملابس والجلد الملوثين بكمية كبيرة من الماء قبل خلع الملابس",
    # Response - Exposure
    "P307": "في حالة التعرض",
    "P307+P311": "في حالة التعرض: اتصل بمركز السموم أو الطبيب",
    "P308": "في حالة التعرض أو القلق",
    "P308+P313": "في حالة التعرض أو القلق: احصل على استشارة/علاج طبي",
    "P309": "في حالة التعرض أو الشعور بتوعك",
    "P309+P311": "في حالة التعرض أو الشعور بتوعك: اتصل بمركز السموم أو الطبيب",
    # Response - Medical attention
    "P310": "اتصل فوراً بمركز السموم أو الطبيب",
    "P311": "اتصل بمركز السموم أو الطبيب",
    "P312": "اتصل بمركز السموم أو الطبيب إذا شعرت بتوعك",
    "P313": "احصل على استشارة/علاج طبي",
    "P314": "احصل على استشارة/علاج طبي إذا شعرت بتوعك",
    "P315": "احصل على استشارة/علاج طبي فوراً",
    # Response - Specific treatment
    "P320": "العلاج المحدد عاجل (انظر ... على هذا الملصق)",
    "P321": "علاج محدد (انظر ... على هذا الملصق)",
    "P322": "إجراءات محددة (انظر ... على هذا الملصق)",
    # Response - First aid measures
    "P330": "اشطف الفم",
    "P331": "لا تحرض على التقيؤ",
    "P332": "في حالة حدوث تهيج الجلد",
    "P332+P313": "في حالة حدوث تهيج الجلد: احصل على استشارة/علاج طبي",
    "P333": "في حالة حدوث تهيج أو طفح جلدي",
    "P333+P313": "في حالة حدوث تهيج أو طفح جلدي: احصل على استشارة/علاج طبي",
    "P334": "اغمر في ماء بارد أو لف بضمادات مبللة",
    "P335": "انفض الجزيئات السائبة عن الجلد",
    "P335+P334": "انفض الجزيئات السائبة عن الجلد. اغمر في ماء بارد أو لف بضمادات مبللة",
    "P336": "قم بإذابة الأجزاء المتجمدة بماء فاتر. لا تفرك المنطقة المصابة",
    "P337": "في حالة استمرار تهيج العينين",
    "P337+P313": "في حالة استمرار تهيج العينين: احصل على استشارة/علاج طبي",
    "P338": "انزع العدسات اللاصقة إن وجدت ويسهل إزالتها. استمر في الشطف",
    "P340": "انقل الشخص إلى الهواء الطلق وابقه في وضعية مريحة للتنفس",
    "P341": "إذا كان التنفس صعباً، انقل الشخص إلى الهواء الطلق وابقه في وضعية مريحة للتنفس",
    "P342": "في حالة ظهور أعراض تنفسية",
    "P342+P311": "في حالة ظهور أعراض تنفسية: اتصل بمركز السموم أو الطبيب",
    "P350": "اغسل بلطف بكمية كبيرة من الماء والصابون",
    "P351": "اشطف بحذر بالماء لعدة دقائق",
    "P352": "اغسل بكمية كبيرة من الماء والصابون",
    "P353": "اشطف الجلد بالماء",
    "P360": "اشطف فوراً الملابس والجلد الملوثين بكمية كبيرة من الماء قبل خلع الملابس",
    "P361": "انزع فوراً جميع الملابس الملوثة",
    "P362": "انزع الملابس الملوثة",
    "P362+P364": "انزع الملابس الملوثة واغسلها قبل إعادة الاستخدام",
    "P363": "اغسل الملابس الملوثة قبل إعادة الاستخدام",
    # Response - Fire
    "P370": "في حالة الحريق",
    "P370+P376": "في حالة الحريق: أوقف التسرب إذا كان ذلك آمناً",
    "P370+P378": "في حالة الحريق: استخدم ... للإطفاء",
    "P371": "في حالة حريق كبير وكميات كبيرة",
    "P371+P380+P375": "في حالة حريق كبير وكميات كبيرة: أخلِ المنطقة. حارب الحريق عن بعد بسبب خطر الانفجار",
    "P372": "خطر انفجار في حالة الحريق",
    "P373": "لا تحارب الحريق عندما تصل النيران إلى المتفجرات",
    "P374": "حارب الحريق باحتياطات عادية من مسافة معقولة",
    "P375": "حارب الحريق عن بعد بسبب خطر الانفجار",
    "P376": "أوقف التسرب إذا كان ذلك آمناً",
    "P377": "حريق غاز متسرب: لا تطفئ، إلا إذا أمكن إيقاف التسرب بأمان",
    "P378": "استخدم ... للإطفاء",
    "P380": "أخلِ المنطقة",
    "P381": "في حالة التسرب، أزل جميع مصادر الاشتعال",
    # Response - Spills
    "P390": "امتص الانسكاب لمنع تلف المواد",
    "P391": "اجمع الانسكاب",
    # Storage
    "P401": "خزن وفقاً لـ ...",
    "P402": "خزن في مكان جاف",
    "P403": "خزن في مكان جيد التهوية",
    "P403+P233": "خزن في مكان جيد التهوية. احفظ الحاوية محكمة الغلق",
    "P403+P235": "خزن في مكان جيد التهوية. يحفظ في مكان بارد",
    "P404": "خزن في حاوية مغلقة",
    "P405": "خزن مقفلاً",
    "P406": "خزن في حاوية مقاومة للتآكل مع بطانة داخلية مقاومة",
    "P407": "حافظ على فجوة هوائية بين الأكوام أو المنصات",
    "P410": "يحمى من أشعة الشمس",
    "P410+P403": "يحمى من أشعة الشمس. خزن في مكان جيد التهوية",
    "P411": "خزن في درجات حرارة لا تتجاوز ... درجة مئوية",
    "P412": "لا تعرض لدرجات حرارة تتجاوز 50 درجة مئوية",
    "P413": "خزن كتل كبيرة تزيد عن ... كجم في درجات حرارة لا تتجاوز ... درجة مئوية",
    "P420": "خزن منفصلاً عن المواد الأخرى",
    "P422": "خزن المحتويات تحت ...",
    # Disposal
    "P501": "تخلص من المحتويات والحاوية وفقاً للوائح المحلية",
    "P502": "ارجع إلى الشركة المصنعة أو المورد للحصول على معلومات حول الاسترداد أو إعادة التدوير",
}

# P codes french dictionary 

P_CODES_FR = {
    # General precautionary statements
    "P101": "En cas de consultation d'un médecin, garder le récipient ou l'étiquette à portée de main",
    "P102": "Tenir hors de portée des enfants",
    "P103": "Lire l'étiquette avant utilisation",
    # Prevention - General
    "P201": "Se procurer les instructions avant utilisation",
    "P202": "Ne pas manipuler avant d'avoir lu et compris toutes les précautions de sécurité",
    "P210": "Tenir à l'écart de la chaleur, des surfaces chaudes, des étincelles, des flammes nues et de toute autre source d'ignition. Ne pas fumer",
    "P211": "Ne pas vaporiser sur une flamme nue ou une autre source d'ignition",
    "P220": "Tenir à l'écart des vêtements et autres matières combustibles",
    "P221": "Prendre toutes les précautions nécessaires pour éviter tout mélange avec des matières combustibles",
    "P222": "Ne pas laisser au contact de l'air",
    "P223": "Ne pas laisser au contact de l'eau",
    "P230": "Maintenir humide avec ...",
    "P231": "Manipuler sous gaz inerte",
    "P232": "Protéger de l'humidité",
    "P233": "Maintenir le récipient fermé de manière étanche",
    "P234": "Conserver uniquement dans l'emballage d'origine",
    "P235": "Tenir au frais",
    # Prevention - Electrical/static
    "P240": "Mise à la terre/liaison équipotentielle du récipient et du matériel de réception",
    "P241": "Utiliser du matériel électrique/de ventilation/d'éclairage antidéflagrant",
    "P242": "Utiliser des outils ne produisant pas d'étincelles",
    "P243": "Prendre des mesures de précaution contre les décharges électrostatiques",
    "P244": "Conserver les vannes de détente exemptes de graisse et d'huile",
    "P250": "Ne pas soumettre à des chocs/à des frottements",
    "P251": "Récipient sous pression: ne pas percer ni brûler, même après usage",
    # Prevention - Respiratory/contact
    "P260": "Ne pas respirer les poussières/fumées/gaz/brouillards/vapeurs/aérosols",
    "P261": "Éviter de respirer les poussières/fumées/gaz/brouillards/vapeurs/aérosols",
    "P262": "Éviter tout contact avec les yeux, la peau ou les vêtements",
    "P263": "Éviter tout contact durant la grossesse et pendant l'allaitement",
    "P264": "Se laver les mains soigneusement après manipulation",
    "P270": "Ne pas manger, boire ou fumer en utilisant ce produit",
    "P271": "Utiliser seulement en plein air ou dans un endroit bien ventilé",
    "P272": "Les vêtements de travail contaminés ne doivent pas sortir du lieu de travail",
    "P273": "Éviter le rejet dans l'environnement",
    # Prevention - Personal protective equipment
    "P280": "Porter des gants de protection, des vêtements de protection, un équipement de protection des yeux et du visage",
    "P281": "Utiliser l'équipement de protection individuel requis",
    "P282": "Porter des gants isolants contre le froid et un écran facial ou une protection des yeux",
    "P283": "Porter des vêtements ignifuges/résistants au feu",
    "P284": "Porter un équipement de protection respiratoire",
    "P285": "En cas de ventilation insuffisante, porter un équipement de protection respiratoire",
    # Response - Ingestion
    "P301": "EN CAS D'INGESTION",
    "P301+P310": "EN CAS D'INGESTION: Appeler immédiatement un CENTRE ANTIPOISON ou un médecin",
    "P301+P312": "EN CAS D'INGESTION: Appeler un CENTRE ANTIPOISON ou un médecin en cas de malaise",
    "P301+P330+P331": "EN CAS D'INGESTION: Rincer la bouche. NE PAS faire vomir",
    # Response - Skin contact
    "P302": "EN CAS DE CONTACT AVEC LA PEAU",
    "P302+P350": "EN CAS DE CONTACT AVEC LA PEAU: Laver doucement avec beaucoup d'eau et de savon",
    "P302+P352": "EN CAS DE CONTACT AVEC LA PEAU: Laver abondamment à l'eau et au savon",
    # Response - Skin/hair
    "P303": "EN CAS DE CONTACT AVEC LA PEAU (ou les cheveux)",
    "P303+P361+P353": "EN CAS DE CONTACT AVEC LA PEAU (ou les cheveux): Enlever immédiatement tous les vêtements contaminés. Rincer la peau à l'eau",
    # Response - Inhalation
    "P304": "EN CAS D'INHALATION",
    "P304+P340": "EN CAS D'INHALATION: Transporter la personne à l'air frais et la maintenir dans une position confortable pour respirer",
    "P304+P341": "EN CAS D'INHALATION: Si la respiration est difficile, transporter la personne à l'air frais et la maintenir au repos dans une position confortable pour respirer",
    # Response - Eye contact
    "P305": "EN CAS DE CONTACT AVEC LES YEUX",
    "P305+P351+P338": "EN CAS DE CONTACT AVEC LES YEUX: Rincer avec précaution à l'eau pendant plusieurs minutes. Enlever les lentilles de contact si la personne en porte et si elles peuvent être facilement enlevées. Continuer à rincer",
    # Response - Clothing
    "P306": "EN CAS DE CONTACT AVEC LES VÊTEMENTS",
    "P306+P360": "EN CAS DE CONTACT AVEC LES VÊTEMENTS: Rincer immédiatement les vêtements et la peau contaminés avec beaucoup d'eau avant d'enlever les vêtements",
    # Response - Exposure
    "P307": "EN CAS D'EXPOSITION",
    "P307+P311": "EN CAS D'EXPOSITION:Appeler un CENTRE ANTIPOISON ou un médecin",
    "P308": "EN CAS d'exposition ou de risque",
    "P308+P313": "EN CAS d'exposition ou de risque: Consulter un médecin",
    "P309": "EN CAS d'exposition ou de malaise",
    "P309+P311": "EN CAS d'exposition ou de malaise: Appeler un CENTRE ANTIPOISON ou un médecin",
    # Response - Medical attention
    "P310": "Appeler immédiatement un CENTRE ANTIPOISON ou un médecin",
    "P311": "Appeler un CENTRE ANTIPOISON ou un médecin",
    "P312": "Appeler un CENTRE ANTIPOISON ou un médecin en cas de malaise",
    "P313": "Consulter un médecin",
    "P314": "Consulter un médecin en cas de malaise",
    "P315": "Consulter immédiatement un médecin",
    # Response - Specific treatment
    "P320": "Un traitement spécifique est urgent (voir ... sur cette étiquette)",
    "P321": "Traitement spécifique (voir ... sur cette étiquette)",
    "P322": "Mesures spécifiques (voir ... sur cette étiquette)",
    # Response - First aid measures
    "P330": "Rincer la bouche",
    "P331": "NE PAS faire vomir",
    "P332": "En cas d'irritation cutanée",
    "P332+P313": "En cas d'irritation cutanée: Consulter un médecin",
    "P333": "En cas d'irritation ou d'éruption cutanée",
    "P333+P313": "En cas d'irritation ou d'éruption cutanée: Consulter un médecin",
    "P334": "Plonger dans de l'eau froide ou envelopper avec des bandes humides",
    "P335": "Enlever les particules déposées sur la peau",
    "P335+P334": "Enlever les particules déposées sur la peau. Plonger dans de l'eau froide ou envelopper avec des bandes humides",
    "P336": "Dégeler les parties gelées avec de l'eau tiède. Ne pas frotter la zone touchée",
    "P337": "Si l'irritation oculaire persiste",
    "P337+P313": "Si l'irritation oculaire persiste: Consulter un médecin",
    "P338": "Enlever les lentilles de contact si la personne en porte et si elles peuvent être facilement enlevées. Continuer à rincer",
    "P340": "Transporter la personne à l'air frais et la maintenir dans une position confortable pour respirer",
    "P341": "Si la respiration est difficile, transporter la personne à l'air frais et la maintenir au repos dans une position confortable pour respirer",
    "P342": "En cas de symptômes respiratoires",
    "P342+P311": "En cas de symptômes respiratoires: Appeler un CENTRE ANTIPOISON ou un médecin",
    "P350": "Laver doucement avec beaucoup d'eau et de savon",
    "P351": "Rincer avec précaution à l'eau pendant plusieurs minutes",
    "P352": "Laver abondamment à l'eau et au savon",
    "P353": "Rincer la peau à l'eau",
    "P360": "Rincer immédiatement les vêtements et la peau contaminés avec beaucoup d'eau avant d'enlever les vêtements",
    "P361": "Enlever immédiatement tous les vêtements contaminés",
    "P362": "Enlever les vêtements contaminés",
    "P362+P364": "Enlever les vêtements contaminés et les laver avant réutilisation",
    "P363": "Laver les vêtements contaminés avant réutilisation",
    # Response - Fire
    "P370": "En cas d'incendie",
    "P370+P376": "En cas d'incendie: Arrêter la fuite si cela est possible sans danger",
    "P370+P378": "En cas d'incendie: Utiliser ... pour l'extinction",
    "P371": "En cas d'incendie important et de grandes quantités",
    "P371+P380+P375": "En cas d'incendie important et de grandes quantités: Évacuer la zone. Combattre l'incendie à distance à cause du risque d'explosion",
    "P372": "Risque d'explosion en cas d'incendie",
    "P373": "NE PAS combattre l'incendie lorsque le feu atteint les explosifs",
    "P374": "Combattre l'incendie avec les précautions normales à une distance raisonnable",
    "P375": "Combattre l'incendie à distance à cause du risque d'explosion",
    "P376": "Arrêter la fuite si cela est possible sans danger",
    "P377": "Fuite de gaz enflammé: Ne pas éteindre si la fuite ne peut pas être arrêtée sans danger",
    "P378": "Utiliser ... pour l'extinction",
    "P380": "Évacuer la zone",
    "P381": "En cas de fuite, éliminer toutes les sources d'ignition",
    # Response - Spills
    "P390": "Absorber le produit répandu pour éviter les dégâts matériels",
    "P391": "Recueillir le produit répandu",
    # Storage
    "P401": "Stocker conformément à ...",
    "P402": "Stocker dans un endroit sec",
    "P403": "Stocker dans un endroit bien ventilé",
    "P403+P233": "Stocker dans un endroit bien ventilé. Maintenir le récipient fermé de manière étanche",
    "P403+P235": "Stocker dans un endroit bien ventilé. Tenir au frais",
    "P404": "Stocker dans un récipient fermé",
    "P405": "Stocker sous clef",
    "P406": "Stocker dans un récipient résistant à la corrosion avec un revêtement intérieur résistant",
    "P407": "Maintenir un espace d'air entre les piles ou les palettes",
    "P410": "Protéger du rayonnement solaire",
    "P410+P403": "Protéger du rayonnement solaire. Stocker dans un endroit bien ventilé",
    "P411": "Stocker à une température ne dépassant pas ... °C",
    "P412": "Ne pas exposer à des températures supérieures à 50 °C",
    "P413": "Stocker les quantités en vrac supérieures à ... kg à des températures ne dépassant pas ... °C",
    "P420": "Stocker à l'écart des autres matières",
    "P422": "Stocker le contenu sous ...",
    # Disposal
    "P501": "Éliminer le contenu et le récipient conformément à la réglementation locale",
    "P502": "Consulter le fabricant ou le fournisseur pour des informations sur la récupération ou le recyclage",
}

# ============================================================
# GHS PICTOGRAM MAPPING
# ============================================================

PICTOGRAMS = {
    'GHS01': 'Explosive',
    'GHS02': 'Flammable',
    'GHS03': 'Oxidizing',
    'GHS04': 'Compressed Gas',
    'GHS05': 'Corrosive',
    'GHS06': 'Toxic',
    'GHS07': 'Harmful/Irritant',
    'GHS08': 'Health Hazard',
    'GHS09': 'Environmental Hazard',
}

# Map each H-code to its GHS pictogram(s)
H_TO_PICTOGRAM = {
    # Explosive (GHS01)
    'H200': 'GHS01', 'H201': 'GHS01', 'H202': 'GHS01', 'H203': 'GHS01', 
    'H204': 'GHS01', 'H205': 'GHS01',
    # Flammable (GHS02)
    'H220': 'GHS02', 'H221': 'GHS02', 'H222': 'GHS02', 'H223': 'GHS02',
    'H224': 'GHS02', 'H225': 'GHS02', 'H226': 'GHS02', 'H227': 'GHS02',
    'H228': 'GHS02', 'H229': 'GHS02', 'H230': 'GHS02', 'H231': 'GHS02',
    'H232': 'GHS02', 'H240': 'GHS02', 'H241': 'GHS02', 'H242': 'GHS02',
    'H250': 'GHS02', 'H251': 'GHS02', 'H252': 'GHS02', 'H260': 'GHS02',
    'H261': 'GHS02',
    # Oxidizing (GHS03)
    'H270': 'GHS03', 'H271': 'GHS03', 'H272': 'GHS03',
    # Compressed Gas (GHS04)
    'H280': 'GHS04', 'H281': 'GHS04',
    # Corrosive (GHS05)
    'H290': 'GHS05', 'H314': 'GHS05', 'H318': 'GHS05',
    # Toxic (GHS06)
    'H300': 'GHS06', 'H301': 'GHS06', 'H310': 'GHS06', 'H311': 'GHS06',
    'H330': 'GHS06', 'H331': 'GHS06', 'H340': 'GHS06', 'H350': 'GHS06',
    'H360': 'GHS06', 'H370': 'GHS06', 'H372': 'GHS06',
    # Health Hazard (GHS08)
    'H304': 'GHS08', 'H334': 'GHS08', 'H341': 'GHS08', 'H351': 'GHS08',
    'H361': 'GHS08', 'H362': 'GHS08', 'H371': 'GHS08', 'H373': 'GHS08',
    # Harmful/Irritant (GHS07)
    'H302': 'GHS07', 'H303': 'GHS07', 'H305': 'GHS07', 'H312': 'GHS07',
    'H313': 'GHS07', 'H315': 'GHS07', 'H316': 'GHS07', 'H317': 'GHS07',
    'H319': 'GHS07', 'H320': 'GHS07', 'H332': 'GHS07', 'H333': 'GHS07',
    'H335': 'GHS07', 'H336': 'GHS07',
    # Environmental Hazard (GHS09)
    'H400': 'GHS09', 'H401': 'GHS09', 'H402': 'GHS09', 'H410': 'GHS09',
    'H411': 'GHS09', 'H412': 'GHS09', 'H413': 'GHS09',
}

def translate(code):
    """Translate an H or P code to its meaning."""
    if code in H_CODES:
        return H_CODES[code]
    elif code in P_CODES:
        return P_CODES[code]
    else:
        return f"Code {code} not found"

def translate_multiple(codes):
    """Translate multiple codes at once."""
    results = {}
    for code in codes:
        results[code] = translate(code)
    return results

def translate_h(codes_string, language="en"):
    """
    Convert a string of H codes to human-readable text.
    
    Parameters:
    - codes_string: string of H-codes (e.g., "H301,H315,H319")
    - language: "en" (English), "ar" (Arabic), or "fr" (French)
    
    Returns:
    - String with translated descriptions
    """
    if not codes_string or codes_string == "nan":
        return ""
    
    lang_map = {
        "en": H_CODES,
        "ar": H_CODES_AR,
        "fr": H_CODES_FR
    }
    codes_dict = lang_map.get(language.lower(), H_CODES)
    
    codes = [c.strip() for c in codes_string.split(",") if c.strip()]
    
    translated = []
    for code in codes:
        # Check for combined codes (e.g., "H301+H311")
        if "+" in code:
            parts = code.split("+")
            combined_parts = []
            for p in parts:
                p = p.strip()
                if p in codes_dict:
                    combined_parts.append(codes_dict[p])
                else:
                    combined_parts.append(p)
            translated.append(" + ".join(combined_parts))
        elif code in codes_dict:
            translated.append(codes_dict[code])
        else:
            translated.append(code)
    
    return ". ".join(translated)


def translate_p(codes_string, language="en"):
    """
    Convert a string of P codes to human-readable text.
    
    Parameters:
    - codes_string: string of P-codes (e.g., "P264,P280,P301+P310")
    - language: "en" (English), "ar" (Arabic), or "fr" (French)
    
    Returns:
    - String with translated descriptions
    """
    if not codes_string or codes_string == "nan":
        return ""
    
    lang_map = {
        "en": P_CODES,
        "ar": P_CODES_AR,
        "fr": P_CODES_FR
    }
    codes_dict = lang_map.get(language.lower(), P_CODES)
    
    # Split by comma, but keep combined codes like "P301+P310" intact
    codes = []
    for part in codes_string.split(","):
        part = part.strip()
        if part:
            codes.append(part)
    
    translated = []
    for code in codes:
        # Check if it's a combined code like "P301+P310"
        if "+" in code:
            parts = code.split("+")
            combined_parts = []
            for p in parts:
                p = p.strip()
                if p in codes_dict:
                    combined_parts.append(codes_dict[p])
                else:
                    combined_parts.append(p)
            translated.append(" + ".join(combined_parts))
        elif code in codes_dict:
            translated.append(codes_dict[code])
        else:
            # Fallback: keep the code
            translated.append(code)
    
    return ". ".join(translated)

# ============================================================
# PICTOGRAM FUNCTIONS
# ============================================================

def get_pictograms(h_codes_string):
    """
    Return a list of pictogram codes for given H-codes.
    
    Parameters:
    - h_codes_string: string of H-codes (e.g., "H301,H315,H319")
    
    Returns:
    - List of pictogram codes (e.g., ['GHS06', 'GHS07'])
    """
    if not h_codes_string or h_codes_string == "nan":
        return []
    
    pictograms = []
    codes = [c.strip() for c in h_codes_string.split(",")]
    for code in codes:
        if code in H_TO_PICTOGRAM:
            pic = H_TO_PICTOGRAM[code]
            if pic not in pictograms:
                pictograms.append(pic)
    return pictograms

def get_pictogram_descriptions(h_codes_string):
    """
    Return human-readable pictogram descriptions for given H-codes.
    
    Parameters:
    - h_codes_string: string of H-codes (e.g., "H301,H315,H319")
    
    Returns:
    - List of pictogram descriptions (e.g., ['Toxic', 'Harmful/Irritant'])
    """
    pics = get_pictograms(h_codes_string)
    return [PICTOGRAMS[p] for p in pics if p in PICTOGRAMS]

def get_all_pictograms():
    """
    Return the complete pictogram dictionary.
    
    Returns:
    - Dictionary of pictogram codes and their descriptions
    """
    return PICTOGRAMS

__all__ = [
    'translate_h',
    'translate_p',
    'translate',
    'translate_multiple',
    'get_pictograms',
    'get_pictogram_descriptions',
    'get_all_pictograms',
    'H_CODES',
    'H_CODES_AR',
    'H_CODES_FR',
    'P_CODES',
    'P_CODES_AR',
    'P_CODES_FR',
    'PICTOGRAMS',
    'H_TO_PICTOGRAM',
]
