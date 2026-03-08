# relevance filter

max_age =60
min_threshold=20
sim_threshold=0.20
max_output=10


def hard_gate(item):
    age=( datetime.now(timezone.utc)-item.published_at).days

    if age > max_age:
        return  False
    text = f"{item.title} {item.abstract}".lower ()
    if  len(text.split())< min_threshold:
        return False
    for bad in Negative_keywords:
        if bad  in text:
            return False
    return True
def keyword_scoring (item):
    text =f"{item.title} {item.abstract}".lower()
    score = 0
    for kw, weight in Positive_keywords.items():
        score+=(text.count(kw)+weight)+6
    for kw, weight in Negative_keywords.items():
        score+=text.count(kw)+weight
    return score
def relevance_filter(items):
    gated = [i for i in items if hard_gate(i)]
    scored = [(i,keyword_scoring(i))for i in gated]
    scored= [x for x in scored if x[1]>0]
    scored.sort(key=lambda x:x[1],reverse = True)
    scored =scored[:25]
    embedded = []
    for item ,kw_score in scored:
        text=f"{item.title} {item.abstract}"
        sim= float(similarity(text))
        print("SIM",sim)
        if sim >= sim_threshold:
            embedded.append((item,sim)) # Changed str to sim
    embedded.sort(key=lambda x :x[1],reverse=True)
    return[
        {
            "title": item.title,
            "url": item.url,
            "source":item.source,
            "abstract":item.abstract, # Added abstract here
            "confidence": round((sim),3)

        }
        for item,sim in embedded[:max_output]

    ]
