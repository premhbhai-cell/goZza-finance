import os, html

ROOT = os.path.dirname(os.path.abspath(__file__))
PHONE_DISPLAY = "+91 81301 12531"
PHONE_TEL = "+918130112531"
WA = "https://wa.me/918130112531"
CITY = "Faridabad, Haryana, India"
MAPS = "https://www.google.com/maps/search/?api=1&query=Faridabad%2C+Haryana%2C+India"

ARROW = '<svg viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 11 11 3M5 3h6v6"/></svg>'
PHONE_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>'
PIN_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>'
CHAT_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 21l2-5.4A8.4 8.4 0 1 1 21 11.5z"/></svg>'
MENU_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'

NAV = [("tech.html", "Tech"), ("about.html", "About"), ("apps.html", "Apps"), ("news.html", "News")]

ARTICLES = [
    ("article-smart-savings", "Smart Savings Accounts", "Product Update", "Nov 2026",
     [("What is changing", [
         "Gozza Finance is introducing Smart Savings: one place to park money, set goals, and watch it grow without paperwork or branch visits.",
         "Customers choose a goal, a monthly amount, and a time frame. Gozza organizes the plan, sends reminders, and shows progress in plain language."]),
      ("Why it matters", [
         "Most people save in several places and lose track of where their money is. A single view makes it easier to see what is available, what is committed, and what is growing.",
         "Every plan is explained before it starts, including costs and conditions, so there are no surprises later."])]),
    ("article-business-loans", "Business loan desk opens in Faridabad", "Company", "Oct 2026",
     [("A local desk for local businesses", [
         "Small traders and manufacturers in Faridabad now have a dedicated Gozza desk for working-capital and equipment financing.",
         "Our team walks owners through documents, eligibility, and repayment options in Hindi or English, and keeps them updated at every step."]),
      ("How to get started", [
         "Call or message us on WhatsApp with a short description of your business and the amount you need. We will reply with a checklist and a time to talk."])]),
    ("article-insurance-advisory", "Insurance advisory, explained simply", "Ecosystem", "Sep 2026",
     [("Advice before products", [
         "Choosing insurance is hard when every plan looks the same on paper. Gozza starts with your family, income, and goals, then compares options side by side.",
         "We explain what each policy covers, what it excludes, and what it costs over time."]),
      ("Our approach", [
         "No pressure and no jargon. If a plan is not right for you, we say so.",
         "Customers keep their policy documents, reminders, and renewal dates in one place."])]),
    ("article-gozza-mobile", "Gozza on mobile", "Product Update", "Aug 2026",
     [("Everything in your pocket", [
         "The Gozza mobile experience puts savings, loans, and advisory requests in one simple screen.",
         "Track goals, upload documents, and talk to the team by call or WhatsApp without visiting an office."]),
      ("What is next", [
         "We are adding bill reminders, goal sharing for families, and a clearer monthly summary of where your money went."])]),
]

PRESS = [
    ("Gozza Finance", "Nov 12, 2026", "Smart Savings Accounts now open for enquiries", "article-smart-savings.html"),
    ("Gozza Finance", "Oct 20, 2026", "Business loan desk opens in Faridabad", "article-business-loans.html"),
    ("Gozza Finance", "Sep 14, 2026", "Insurance advisory, explained simply", "article-insurance-advisory.html"),
    ("Gozza Finance", "Aug 05, 2026", "Gozza on mobile: savings, loans, and advice in one screen", "article-gozza-mobile.html"),
    ("Gozza Finance", "Jun 18, 2026", "Gozza launches financial planning workshops for families", "contact.html"),
    ("Gozza Finance", "Apr 02, 2026", "Gozza Finance begins operations in Faridabad", "about.html"),
]

def S(name, cat, short, tagline, intro, hl, who):
    return dict(name=name, cat=cat, short=short, tagline=tagline, intro=intro, hl=hl, who=who,
                slug="service-" + name.lower().replace(" ", "-"))

SV_CHART = {
    "Smart Savings": ("chart-growth", "Goal plan growth, illustrative"),
    "Recurring Plans": ("chart-fund", "Monthly plan, illustrative"),
    "Fixed Growth": ("chart-gold", "Term growth, illustrative"),
    "Family Fund": ("chart-growth", "Family goal progress, illustrative"),
    "Mutual Fund Advisory": ("chart-fund", "Fund NAV over time, illustrative"),
    "Stock Market Desk": ("chart-candles", "Candlestick chart with volume, illustrative"),
    "Gold Savings": ("chart-gold", "Gold accumulation, illustrative"),
    "Portfolio Review": ("chart-candles-2", "Holding performance, illustrative"),
}

SV = [
 S("Smart Savings","Savings","Goal-based saving plans","Save for what matters, one goal at a time.",
   "Smart Savings turns a vague wish to save more into a plan with a target, a monthly amount, and a date. We help you pick the goal, set an amount you can sustain, and keep track without spreadsheets.",
   [("Goal first","Every plan starts with what you are saving for, such as a trip, a wedding, or a down payment."),("Comfortable amounts","We size the monthly amount to your income so the plan survives a tight month."),("Clear progress","You get a plain-language update on how far along you are and what is left.")],
   "Salaried professionals, first-time savers, and anyone with a specific goal and a date in mind."),
 S("Recurring Plans","Savings","Monthly saving made automatic","Saving that happens on its own.",
   "Recurring Plans move a fixed amount into your savings every month so you do not have to remember. We help you choose the amount, the date, and the destination that fit your cash flow.",
   [("Set it once","Pick the amount and date and the plan runs every month."),("Aligned to payday","We schedule contributions just after your income arrives."),("Easy to change","Increase, pause, or stop a plan whenever your situation changes.")],
   "People who find it hard to save by hand and want a steady habit."),
 S("Fixed Growth","Savings","Lock in for a set period","Commit for a period, plan with certainty.",
   "Fixed Growth options let you set money aside for a defined term in exchange for a stated outcome from the partner institution. We compare terms, explain the conditions, and show what happens if you need the money early.",
   [("Defined term","You know the period and the stated outcome before you commit."),("Side by side","We compare options from different institutions in one simple table."),("Exit rules explained","Early withdrawal terms are explained up front, in writing.")],
   "Savers with money they will not need for a while, and retirees looking for predictability."),
 S("Family Fund","Savings","Shared goals for the household","One fund, the whole family&rsquo;s goals.",
   "Family Fund gives the household a shared plan for big expenses such as education, weddings, and medical needs. Everyone can see the goals, the contributions, and the progress.",
   [("Shared view","Family members see the same goals and the same numbers."),("Goals by priority","We rank goals so the most important ones are funded first."),("Built for life events","Plans account for expected costs like fees, ceremonies, and emergencies.")],
   "Households planning for children&rsquo;s education, weddings, or a joint emergency reserve."),
 S("Mutual Fund Advisory","Investments","Guidance on fund selection","Understand a fund before you buy it.",
   "Our advisors explain what each fund invests in, what it costs, and how it has behaved in good and bad markets. You choose with the facts in front of you, and the units are held in your own name.",
   [("Plain-language factsheets","Every fund is summarized in a one-page note without jargon."),("Costs shown up front","Expense ratios and charges are listed before you decide."),("Matched to your comfort","We suggest options that fit your time frame and risk comfort.")],
   "First-time investors and anyone who wants a second opinion before choosing a fund."),
 S("Stock Market Desk","Investments","Research-led investing help","Research first, decisions second.",
   "The Stock Market Desk helps you understand companies, sectors, and risk before you invest. We focus on learning, planning, and discipline rather than tips.",
   [("Learn the basics","Short sessions on reading results, valuation, and risk."),("Plan your approach","Decide how much to invest, for how long, and what you will do if prices fall."),("Ongoing support","Ask questions by call or WhatsApp when markets move.")],
   "People starting in the stock market and those who want a structured approach."),
 S("Gold Savings","Investments","Build gold holdings in small steps","Build gold holdings in small steps.",
   "Gold Savings lets you add to gold regularly instead of buying in one large purchase. We explain the available forms of gold, their costs, and how each is stored and sold.",
   [("Small, regular amounts","Add to gold monthly without a large upfront purchase."),("Know the forms","Compare physical, digital, and bond forms with their charges."),("Clear exit","Understand how and when you can sell, and what it costs.")],
   "Families who like gold as part of long-term savings, including for festivals and weddings."),
 S("Portfolio Review","Investments","A second opinion on what you hold","A second pair of eyes on your money.",
   "Bring everything you hold and we map it on one page: what you own, what it costs, and where it overlaps. You leave with a short list of changes worth considering and the reason behind each.",
   [("One-page map","All holdings in a single view, whichever institution they sit with."),("Overlap and cost check","We highlight duplicated funds and charges that add up."),("Written summary","You keep a short note with our observations and suggestions.")],
   "Anyone with investments spread across several places who wants clarity."),
 S("Personal Loans","Loans","Clear terms and quick answers","Borrow with clear terms.",
   "For weddings, medical needs, travel, or a short-term gap, we help you compare personal loan offers, understand the true cost, and prepare the paperwork so decisions are quick.",
   [("True cost shown","Interest, processing fees, and charges are listed in one figure."),("Paperwork prepared","We prepare the documents so applications go through smoothly."),("Repayment that fits","We check that the monthly installment suits your budget.")],
   "Salaried and self-employed people who need funds for a specific purpose."),
 S("Business Loans","Loans","Working capital and equipment","Financing for the way your business runs.",
   "Working-capital loans, equipment finance, and expansion funding for traders, shopkeepers, and manufacturers. We study your cash cycle and match you with the structure that fits it.",
   [("Cash-cycle based","We design repayments around when your business actually earns."),("Document help","GST, bank statements, and filings organized before you apply."),("Local desk","A team in Faridabad that understands the market and its businesses.")],
   "Small traders, shop owners, and manufacturers in and around Faridabad."),
 S("Home Loans","Loans","Compare offers and manage paperwork","From shortlisting to sanction, step by step.",
   "Buying or building a home involves many documents and decisions. We compare lenders, check eligibility, explain the full cost, and guide you through sanction and disbursal.",
   [("Compare lenders","Rates, fees, and conditions side by side."),("Eligibility check","Know the amount you qualify for before you start house hunting."),("Process support","Property documents, valuation, and sanction handled step by step.")],
   "First-time home buyers and people moving or refinancing their existing loan."),
 S("Loan Against Property","Loans","Unlock value without selling","Use your property without selling it.",
   "A loan against property lets you raise funds for business or personal needs while keeping ownership. We explain the charges, the risks, and the repayment, and compare lenders for you.",
   [("Keep your property","Borrow against it without selling.") ,("Larger amounts","Typically suited to bigger funding needs and longer terms."),("Risks explained","We state clearly what happens if repayments are missed.")],
   "Business owners and families who need larger funds and own property."),
 S("Health Insurance","Insurance","Plans compared side by side","Cover that works when you need it.",
   "Health plans look alike until a claim. We compare coverage, waiting periods, hospital networks, and exclusions so you pick a policy that will actually help your family.",
   [("Side-by-side comparison","Coverage, limits, and exclusions in one simple table."),("Claims guidance","We explain the claim process before you buy, and help during it."),("Family fit","Individual, floater, and parent cover matched to your household.")],
   "Families, new parents, and people supporting parents or seniors."),
 S("Life Insurance","Insurance","Protect the people who depend on you","Protect the people who depend on you.",
   "Life insurance should do one job well: secure your family&rsquo;s future if you are not there. We calculate how much cover you need and compare plans so you pay for protection, not complexity.",
   [("Right-sized cover","We work out the amount based on income, loans, and goals."),("Plain terms","What is covered, what is not, and what you pay, in writing."),("Nominee guidance","Help with nominee details and keeping documents safe.")],
   "Earning members of a family, new homeowners, and people with loans."),
 S("Motor Insurance","Insurance","Renewals and claims support","Renew on time, claim without stress.",
   "Two-wheeler and car insurance made simple: reminders before renewal, comparisons of cover and add-ons, and support if you need to claim.",
   [("Renewal reminders","We remind you before the policy lapses."),("Add-ons explained","Zero depreciation, engine cover, and others, and when they are worth it."),("Claims support","Guidance on documents and the garage network when it matters.")],
   "Owners of cars and two-wheelers, including small fleets."),
 S("Business Insurance","Insurance","Cover for shops and factories","Cover for what keeps your business running.",
   "Fire, theft, stock, machinery, liability, and employee cover for shops and factories. We review your premises and operations and suggest cover that matches real risks.",
   [("Risk walkthrough","We look at stock, machinery, and premises to find real exposures."),("Right-sized cover","Avoid paying for cover you do not need and gaps you do."),("Renewal tracking","Policies and renewal dates are kept in one place.")],
   "Shopkeepers, traders, and factory owners."),
 S("Bill Payments","Payments","Utilities and reminders in one place","Pay on time, every time.",
   "Keep electricity, water, phone, and other bills in one list, get reminders before the due date, and pay without chasing multiple apps.",
   [("One list","All recurring bills in a single view."),("Timely reminders","A nudge before each due date."),("Payment records","Keep a simple history for budgeting and taxes.")],
   "Busy households and small offices that want fewer missed due dates."),
 S("Money Transfer","Payments","Send money safely","Send money with confidence.",
   "Domestic transfers and guidance for sending money to family and suppliers. We explain limits, charges, and the safest ways to pay so mistakes and scams are avoided.",
   [("Know the charges","Fees and limits explained before you send."),("Safety tips","How to verify beneficiaries and avoid common frauds."),("Help when stuck","Call us if a transfer is delayed or sent to the wrong place.")],
   "Families supporting relatives and businesses paying suppliers."),
 S("Business Collections","Payments","Get paid on time","Get paid on time, without awkward calls.",
   "Set up simple ways for customers to pay you, track what is outstanding, and send polite reminders. Improve your cash flow without chasing every invoice by hand.",
   [("Easy ways to pay","Set up payment options your customers actually use."),("Outstanding tracker","See who owes what and for how long."),("Polite reminders","Templates for follow-ups that keep relationships intact.")],
   "Traders and service businesses with many small invoices."),
 S("Accounting Support","Business tools","Books, GST, and filings","Books that are ready when you need them.",
   "Bookkeeping, GST returns, and monthly reports for small businesses. You send us bills and statements and we keep the records clean and filings on time.",
   [("Monthly books","Income, expenses, and balances kept up to date."),("GST filings","Returns prepared and filed before deadlines."),("Simple reports","A short monthly summary you can actually read.")],
   "Small businesses and professionals without an in-house accountant."),
 S("Tax Planning","Business tools","File with confidence","Plan early, pay what is due and no more.",
   "We review your income, deductions, and investments before the year ends, so you use the options available to you and file accurately and on time.",
   [("Year-round planning","Do not wait for March. We plan with you across the year."),("Accurate filing","Returns prepared with supporting documents in order."),("Notice help","Guidance if you receive a notice from the department.")],
   "Salaried individuals, professionals, and business owners."),
 S("Payroll Help","Business tools","Salaries made simple","Salaries and statutory dues, handled.",
   "Salary calculation, payslips, and statutory deductions for small teams. Staff are paid on time and the records stay tidy.",
   [("Accurate payslips","Clear payslips with every deduction explained."),("Statutory dues","Reminders and support for provident fund and other deductions."),("Scales with you","From a handful of staff to a growing team.")],
   "Shops, clinics, and small factories with regular staff."),
 S("Gozza Mobile","Mobile","Your finances on one screen","Your plans, goals, and documents in your pocket.",
   "Gozza Mobile brings your savings goals, loan reminders, policy documents, and requests into one simple screen so you always know where you stand.",
   [("One screen","Goals, policies, and loans in a single view."),("Document locker","Keep policy papers and statements safe and searchable."),("Direct line to us","Message or call the team from inside the app.")],
   "Customers who want everything in one place on their phone."),
 S("WhatsApp Support","Mobile","Talk to a person, fast","Real people, on the app you already use.",
   "Ask questions, share documents, and get updates over WhatsApp. A named advisor replies, and every request is logged so nothing falls through.",
   [("A named advisor","You talk to the same person each time."),("Share documents easily","Send photos of documents and we will organize them."),("Everything logged","Requests are tracked until they are resolved.")],
   "Anyone who prefers a quick message to a long phone call."),
]
SERVICES = [(s["name"], s["cat"], s["short"]) for s in SV]
BYNAME = {s["name"]: s for s in SV}
def sv_link(name): return BYNAME[name]["slug"] + ".html"
CATS = ["Savings", "Investments", "Loans", "Insurance", "Payments", "Business tools", "Mobile"]
COLORS = ["#2f6bff", "#1d4fd7", "#4d8dff", "#0f3aa8", "#06204a", "#6aa6ff"]


def header(active, depth=""):
    left = '<a class="brand" href="index.html" aria-label="Gozza Finance home"><img src="assets/logo-icon.png" alt=""><span>Gozza <em>finance</em></span></a>'
    for href, label in NAV:
        cls = "pill active" if href == active else "pill"
        left += f'<a class="{cls}" href="{href}">{label}</a>'
    right = '<a class="pill" href="contact.html">Contact</a><a class="pill cta" href="tel:%s">Call now %s</a>' % (PHONE_TEL, ARROW)
    mob = '<a class="pill" href="index.html">Home</a>'
    for href, label in NAV:
        mob += f'<a class="pill" href="{href}">{label}</a>'
    mob += f'<a class="pill" href="contact.html">Contact</a><a class="pill cta" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>'
    return f'''<header class="site-header"><nav class="nav" aria-label="Main">
<div class="nav-left">{left}</div>
<div class="nav-right">{right}<button class="menu-btn" aria-label="Menu" aria-expanded="false">{MENU_SVG}</button></div>
</nav><div class="mobile-menu">{mob}</div></header>'''


def footer():
    return f'''<div class="bigword" aria-hidden="true"><div>Gozza <em>finance</em></div></div>
<footer class="foot2 sp" data-sp="dark" data-sp-density=".8"><div class="wrap">
<div class="cols">
<div><img class="fi" src="assets/logo-icon.png" alt="Gozza Finance"></div>
<div><h4>Learn</h4><a href="tech.html">Tech</a><a href="about.html">About</a><a href="apps.html">Apps</a><a href="news.html">News</a></div>
<div><h4>Services</h4><a href="{sv_link("Smart Savings")}">Savings</a><a href="{sv_link("Mutual Fund Advisory")}">Investments</a><a href="{sv_link("Personal Loans")}">Loans</a><a href="{sv_link("Health Insurance")}">Insurance</a></div>
<div><h4>Contact</h4><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a><a href="{MAPS}" target="_blank" rel="noopener">Faridabad</a><a href="contact.html">Enquiry form</a></div>
</div>
<div class="copy" style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;font-size:14px"><span>&copy; 2026 Gozza Finance. All rights reserved.</span><span>{CITY}</span></div>
</div></footer>
<div class="fab"><a class="wa" href="{WA}" target="_blank" rel="noopener">{CHAT_SVG}<span>WhatsApp</span></a><a class="call" href="tel:{PHONE_TEL}">{PHONE_SVG}<span>{PHONE_DISPLAY}</span></a></div>'''


def page(filename, title, desc, active, body, extra_head=""):
    out = f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:image" content="assets/logo.png">
<link rel="icon" type="image/png" href="assets/favicon.png"><link rel="apple-touch-icon" href="assets/logo-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<meta name="theme-color" content="#f6f9ff">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@300;400;500;600&family=Inter:wght@400;500;600&family=Instrument+Serif:ital@0;1&display=swap">
<link rel="stylesheet" href="assets/styles.css">{extra_head}
</head><body>
{header(active)}
<main>{body}</main>
{footer()}
<script src="assets/main.js"></script>
</body></html>'''
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(out)


def news_rows(items, hide_from=None):
    s = ""
    for i, (src, dt, tt, href) in enumerate(items):
        h = ' hidden data-extra' if hide_from is not None and i >= hide_from else ""
        s += f'<a href="{href}"{h}><span class="src">{src}</span><span class="dt">{dt}</span><span class="tt">{tt}</span>{ARROW}</a>'
    return s


def art_block():
    bubbles = "".join(
        f'<i style="--x:{x}%;--s:{s}px;--d:{d}s;animation-delay:-{dl}s"></i>'
        for x, s, d, dl in [(8, 14, 9, 1), (22, 22, 12, 4), (35, 10, 8, 2), (50, 18, 11, 6), (63, 12, 9, 3), (76, 24, 13, 7), (88, 14, 10, 5)]
    )
    return f'<div class="art" aria-hidden="true">{bubbles}<img src="assets/logo-icon.png" alt=""></div>'


# ---------------- HOME ----------------
faq = [
    ("What is Gozza Finance?",
     ["Gozza Finance is a financial services company based in Faridabad. We help individuals, families, and small businesses with savings plans, investments, loans, insurance, and day-to-day money management.",
      "Our approach is simple: explain every option in plain language, show the costs up front, and stay reachable by phone and WhatsApp."]),
    ("What is Gozza Finance used for?",
     ["Planning and managing money: saving for goals, investing with guidance, borrowing with clear terms, protecting your family with insurance, and keeping a business&rsquo;s books and payments in order."]),
    ("What makes Gozza different?",
     ["We start with your goals, not a product. Every recommendation comes with the reason behind it, the cost, and the alternatives.",
      "You reach the same team by call, WhatsApp, or in person in Faridabad."]),
    ("How do I get started?",
     [f"Open any service page, read how it works, and call us on {PHONE_DISPLAY} or message on WhatsApp. You can also use the enquiry form on the Contact page."]),
]
faq_html = "".join(f'<details><summary>{q}</summary>' + "".join(f"<p>{p}</p>" for p in a_) + "</details>" for q, a_ in faq)

def chip(sv, i):
    return f'<a href="{sv["slug"]}.html"><i style="background:{COLORS[i % len(COLORS)]}">{sv["name"][0]}</i><span><b>{sv["name"]}</b><small>{sv["cat"]}</small></span></a>'
strip_items = "".join(chip(sv, i) for i, sv in enumerate(SV[:12])) * 2
strip_html = f'<div class="strip" aria-label="Services"><div class="marquee-track">{strip_items}</div></div>'

apps_rows = ""
for i, n in enumerate(["Smart Savings", "Mutual Fund Advisory", "Business Loans", "Health Insurance", "Tax Planning"]):
    sv = BYNAME[n]; idx = SV.index(sv)
    apps_rows += f'<a href="{sv["slug"]}.html"><span class="ic" style="background:{COLORS[idx % len(COLORS)]}">{n[0]}</span><span>{n}</span><span class="m">{sv["cat"]} &middot; {sv["short"]}</span>{ARROW}</a>'
apps_rows += f'<a href="apps.html"><span class="ic" style="background:var(--ink)">+</span><span>All apps</span><span class="m">View all services</span>{ARROW}</a>'

vision_pts = [
    "Gozza&rsquo;s vision is to make good financial advice available to every household and every business.",
    "Money decisions are often made in a hurry, with too little information. Gozza slows things down, explains every option, and shows the cost before you commit.",
    "Gozza was built around people, not products: no hidden charges, no pressure, and no jargon. Every plan comes with its conditions in writing, and every advisor can be reached by phone.",
    "Financial confidence belongs to everyone, not only to people with large balances.",
]
vision_html = "".join(f'<div class="vp"><i></i><p>{t}</p></div>' for t in vision_pts)

home = f"""
<section class="hero sp" data-sp="light" data-sp-density=".7">
<div class="hero-inner">
<h1 class="display">Smart finance for every family and business</h1>
<div><p class="lead">Savings, investments, loans, and insurance, explained in plain language by a team you can call any day.</p>
<a class="btn" href="apps.html">Explore {ARROW}</a></div>
</div>
{strip_html}
</section>
<section class="band sp" data-sp="dark" data-sp-density="1.3" aria-hidden="true"><canvas class="dots" data-mode="wave" data-color="#8bbcff"></canvas></section>

<section><div class="col">
<div class="col-stats"><div><b>24</b><span>Services</span></div><div><b>7</b><span>Categories</span></div><div><b>1</b><span>Team, one number</span></div><div><b>24/7</b><span>WhatsApp</span></div></div>
<div class="pad" style="padding-bottom:70px">
<div class="tile-ic sp" data-sp="dark" data-sp-density="1.6"><img src="assets/logo-icon.png" alt=""></div>
<span class="eyebrow">Everything in one place</span>
<h2 class="mid">Savings, loans, insurance, taxes, and more, handled by one team that never makes you chase.</h2>
<a class="btn" href="apps.html">Explore {ARROW}</a>
</div>
{strip_html}
<div class="mock sp" data-sp="dark" data-sp-density="1.4"><div class="chartframe"><div class="bar"><i></i><i></i><i></i><span>Gozza &middot; Market view</span><span class="live">Live demo</span></div>
<img src="assets/charts/chart-terminal.webp" width="1760" height="990" alt="Illustrative trading terminal with candlestick chart, volume bars and order book" loading="lazy"></div>
<p class="cap">Illustrative chart for demonstration. Not investment advice.</p></div>
<div class="pad hr">
<span class="eyebrow">Other apps</span>
<div class="apps-list">{apps_rows}</div>
</div>
<div class="pad hr">
<canvas class="dots dotsm" data-mode="strip" data-color="#2f6bff" aria-hidden="true"></canvas>
<span class="eyebrow">Partner with us</span>
<h2 class="mid">Integrate Gozza</h2>
<p class="body" style="max-width:680px;margin:18px 0 0;font-size:15px;color:var(--muted)">Shops, traders, and advisors can offer Gozza services to their own customers. You keep the relationship; our team handles the paperwork, follow-up, and support in the background.</p>
<a class="btn dark" href="contact.html?service=Partnership">Start partnering {ARROW}</a>
</div></div></section>

<section class="vision-dark sp" data-sp="dark" data-sp-density="1.1"><div class="in">
<img class="gl" src="assets/logo-icon.png" alt="">
{vision_html}
</div></section>

<section><div class="col">
<div class="pad">
<canvas class="dots dotsm" data-mode="strip" data-color="#4d8dff" aria-hidden="true" style="height:130px"></canvas>
<span class="eyebrow">Security</span>
<h2 class="mid">Gozza is built on consent, clear records, and regulated partners, so your information stays private and your money stays in your name.</h2>
<p style="margin-top:22px;font-size:14.5px;color:var(--muted);max-width:660px">We collect only the documents a service needs and never share them without your consent. Investments and policies are held in your own name with the regulated provider. <a href="tech.html#architecture" style="color:var(--blue);border-bottom:1px solid">See how the platform works</a>.</p>
<p style="margin-top:14px;font-size:14.5px;color:var(--muted);max-width:660px">Every conversation and quote is logged so you can always check what was promised. If something looks wrong, call us and we will look into it the same day.</p>
</div>
<div class="pad hr"><span class="eyebrow">News</span>
<div class="news-list tight">{news_rows(PRESS[:3])}</div>
<a class="btn ghost more" href="news.html">Read all {ARROW}</a></div>
<div class="pad hr" id="faq"><canvas class="dots dotsm" data-mode="strip" data-color="#2f6bff" aria-hidden="true" style="height:70px;margin-bottom:30px"></canvas><span class="eyebrow">FAQ</span>
<div class="faq" style="margin-top:20px">{faq_html}</div></div>
</div></section>
"""
page("index.html", "Gozza Finance – Smart finance for every family and business",
     "Savings, investments, loans, and insurance explained in plain language. Gozza Finance, Faridabad. Call +91 81301 12531.", "index.html", home)

# ---------------- TECH ----------------
tech = f'''
<section class="hero sp" data-sp="light" data-sp-density=".7"><div class="hero-inner" style="grid-template-columns:1fr 1fr">
<div><span class="eyebrow" style="color:var(--blue);opacity:1;margin:0 0 18px">Tech</span>
<h1 class="display">How Gozza works.</h1></div>
<div><p class="lead">Gozza Finance is a service platform built to keep finance simple: one profile, one team, and one clear record of every plan.</p>
<a class="btn" href="contact.html">Talk to us {ARROW}</a></div></div></section>

<section class="sec" id="architecture"><div class="wrap">
<span class="eyebrow">Architecture</span>
<h2>Three layers, one experience.</h2>
<div class="arch">
<div class="card"><i>01</i><h3>Gozza <em>Core</em></h3><p>Your profile, goals, and documents are stored once and reused across every service, so you never repeat yourself.</p></div>
<div class="card"><i>02</i><h3>Gozza <em>Services</em></h3><p>Savings, investments, loans, and insurance, delivered with partner institutions and tracked in one place.</p></div>
<div class="card"><i>03</i><h3>Gozza <em>Support</em></h3><p>A human team reachable by phone, WhatsApp, and in person in Faridabad, with every request logged.</p></div>
</div>
<div class="diagram" aria-label="Gozza architecture diagram">
<div class="lane"><div class="node a">Savings</div><div class="node a">Loans</div><div class="node a">Insurance</div></div>
<div class="lane"><div class="node b">Investments</div><div class="node b">Payments</div><div class="node b">Business tools</div></div>
<div class="bar">Gozza Core: profile, goals, documents, and records</div>
</div></div></section>

<section class="sec tint" id="security"><div class="wrap two">
<div><span class="eyebrow">Security</span><h2>Built around consent and clear records.</h2></div>
<div><p class="body" style="margin-top:0">Documents are shared only for the service you ask for. Each plan is held in your own name with the regulated provider.</p>
<p class="body">We keep a written record of every plan, quote, and promise, so you can always check what was agreed.</p>
<a class="btn ghost" href="about.html">About our team {ARROW}</a></div></div></section>

<section class="sec"><div class="wrap">
<span class="eyebrow">Channels</span><h2>Reach us the way you prefer.</h2>
<div class="rows">
<a class="row" href="tel:{PHONE_TEL}"><span class="name">Phone</span><span class="meta">{PHONE_DISPLAY}</span>{ARROW}</a>
<a class="row" href="{WA}" target="_blank" rel="noopener"><span class="name">WhatsApp</span><span class="meta">{PHONE_DISPLAY}</span>{ARROW}</a>
<a class="row" href="{MAPS}" target="_blank" rel="noopener"><span class="name">Office</span><span class="meta">{CITY}</span>{ARROW}</a>
</div></div></section>

<section class="sec dark sp" data-sp="dark" data-sp-density=".9"><div class="wrap">
<span class="eyebrow">What you get</span>
<h2>Gozza gives every customer five <em>things.</em></h2>
<div class="vision">
<div class="v"><i>Plan</i><p>A written plan with goals, costs, and time frames.</p></div>
<div class="v"><i>Track</i><p>Simple progress updates by call or WhatsApp.</p></div>
<div class="v"><i>Protect</i><p>Insurance and safeguards matched to your family.</p></div>
<div class="v"><i>Borrow</i><p>Loan options compared before you commit.</p></div>
<div class="v"><i>Grow</i><p>Savings and investment guidance that fits your risk comfort.</p></div>
</div></div></section>
'''
tech = tech.replace('.vision .v i', '.vision .v i')
page("tech.html", "Tech – Gozza Finance", "How Gozza Finance delivers savings, loans, insurance, and advice from one platform and one team.", "tech.html", tech)

# ---------------- ABOUT ----------------
about = f'''
<section class="hero sp" data-sp="light" data-sp-density=".7"><div class="hero-inner" style="grid-template-columns:1fr 1fr">
<div><span class="eyebrow" style="color:var(--blue);opacity:1;margin:0 0 18px">About</span>
<h1 class="display">The people behind Gozza.</h1></div>
<div><p class="lead">A local team in Faridabad that believes money decisions deserve time, honesty, and a phone number that gets answered.</p>
<div class="subnav"><a class="chip" href="#community">Community</a><a class="chip" href="#team">Gozza team</a><a class="chip" href="#advisory">Advisory</a><a class="chip" href="#partners">Partners</a><a class="chip" href="#visit">Visit us</a></div></div></div></section>

<section class="sec"><div class="wrap five">
<div class="block" id="community"><i>01</i><div><h3>Local community</h3>
<p>Gozza grew out of conversations with families, shop owners, and professionals in Faridabad who wanted straight answers about money. We host workshops and Q&amp;A sessions in the city so people can ask questions without any sales pressure.</p>
<div class="photos" aria-hidden="true"><div class="sp" data-sp="dark" data-sp-density="1.2"><img src="assets/logo-icon.png" alt=""></div><div class="sp" data-sp="dark" data-sp-density="1.2"><img src="assets/logo-icon.png" alt=""></div><div class="sp" data-sp="dark" data-sp-density="1.2"><img src="assets/logo-icon.png" alt=""></div><div class="sp" data-sp="dark" data-sp-density="1.2"><img src="assets/logo-icon.png" alt=""></div></div></div></div>

<div class="block" id="team"><i>02</i><div><h3>Gozza team</h3>
<p>Our advisors lead every client relationship from the first call to the final paperwork. The team is independent, locally based, and focused on clear explanations and careful follow-up.</p>
<div class="news-list" style="max-width:820px"><span class="eyebrow" style="margin:24px 0 0;opacity:.6">Latest news</span>{news_rows(PRESS[:1])}</div></div></div>

<div class="block" id="advisory"><i>03</i><div><h3>Advisory desk</h3>
<p>The advisory desk reviews plans before they reach clients. It checks that costs are explained, risks are stated, and that each recommendation fits the person asking for it.</p>
<a class="link" href="service-portfolio-review.html">Book a review</a></div></div>

<div class="block" id="partners"><i>04</i><div><h3>Partners and institutions</h3>
<p>We work with banks, insurers, and licensed providers so that every product you hold sits with a regulated institution in your own name. Gozza coordinates the process and stays on call afterwards.</p>
<a class="link" href="contact.html?service=Partnership">Partner with Gozza</a></div></div>

<div class="block" id="visit"><i>05</i><div><h3>Visit us in Faridabad</h3>
<p>Call or message before visiting and we will keep time for you. Meetings can also be held by phone or WhatsApp.</p>
<div class="rows" style="max-width:640px">
<a class="row" href="tel:{PHONE_TEL}"><span class="name">Call</span><span class="meta">{PHONE_DISPLAY}</span>{ARROW}</a>
<a class="row" href="{MAPS}" target="_blank" rel="noopener"><span class="name">Open map</span><span class="meta">{CITY}</span>{ARROW}</a>
<a class="row" href="apps.html"><span class="name">All services</span><span class="meta">View all</span>{ARROW}</a></div></div></div>
</div></section>
'''
page("about.html", "About – Gozza Finance", "The local Faridabad team behind Gozza Finance.", "about.html", about)

# ---------------- APPS ----------------
chips = '<button class="chip on" data-filter="all">All</button>' + "".join(f'<button class="chip" data-filter="{c}">{c}</button>' for c in CATS)
tiles = ""
for i, (n, c, d) in enumerate(SERVICES):
    col = COLORS[i % len(COLORS)]
    tiles += f'<a class="tile" data-cat="{c}" href="{sv_link(n)}"><span class="ic" style="background:{col}">{n[0]}</span><span><b>{n}</b><small>{c} &middot; {d}</small></span></a>'
apps = f'''
<section class="hero sp" data-sp="light" data-sp-density=".7"><div class="hero-inner" style="grid-template-columns:1fr 1fr">
<div><span class="eyebrow" style="color:var(--blue);opacity:1;margin:0 0 18px">Apps</span><h1 class="display">Services built around you.</h1></div>
<div><p class="lead">Save, invest, borrow, insure, and manage a business. Explore every Gozza service and start with one call.</p></div></div></section>
<section class="sec" style="padding-top:20px"><div class="wrap">
<div class="chips" style="margin-top:0">{chips}</div>
<div class="grid">{tiles}</div>
</div></section>
'''
page("apps.html", "Apps – Gozza Finance", "Explore Gozza Finance services: savings, investments, loans, insurance, payments, and business tools.", "apps.html", apps)

# ---------------- NEWS ----------------
art_cards = "".join(
    f'<a class="acard" href="{slug}.html"><div class="th sp" data-sp="dark" data-sp-density="1.1"><img src="assets/charts/cover-{i+1}.webp" alt="" loading="lazy"></div><div class="tx"><small>{tag} &middot; {dt}</small><b>{title}</b></div></a>'
    for i, (slug, title, tag, dt, _) in enumerate(ARTICLES)
)
news = f'''
<section class="hero sp" data-sp="light" data-sp-density=".7"><div class="hero-inner" style="grid-template-columns:1fr 1fr">
<div><span class="eyebrow" style="color:var(--blue);opacity:1;margin:0 0 18px">News</span><h1 class="display">Dispatches from Gozza.</h1></div>
<div><p class="lead">Product updates, local events, and announcements from the team.</p></div></div></section>
<section class="sec" id="hero" style="padding-top:20px"><div class="wrap">
<span class="eyebrow">Recent updates</span>
<div class="news-list">{news_rows(PRESS, hide_from=4)}</div>
<button class="btn ghost more" id="load-more">Load more</button>
</div></section>
<section class="sec tint"><div class="wrap">
<span class="eyebrow">Articles</span>
<div class="articles">{art_cards}</div>
</div></section>
'''
page("news.html", "News – Gozza Finance", "Latest news and product updates from Gozza Finance.", "news.html", news)

# ---------------- ARTICLES ----------------
for ai, (slug, title, tag, dt, sections) in enumerate(ARTICLES):
    toc = "".join(f'<a href="#s{i}">{h}</a>' for i, (h, _) in enumerate(sections))
    prose = "".join(
        f'<h2 id="s{i}">{h}</h2>' + "".join(f"<p>{p}</p>" for p in ps) for i, (h, ps) in enumerate(sections)
    )
    body = f'''
<div class="wrap"><div class="article-head">
<a class="crumb" href="news.html#hero">&larr; News</a>
<h1>{title}</h1>
<div class="tags"><span>{tag}</span><span>{dt}</span></div></div>
<figure class="cover chartframe sp" data-sp="dark" data-sp-density="1.2"><img src="assets/charts/cover-{ai+1}.webp" width="1760" height="754" alt="Illustrative chart"></figure>
<div class="article-grid">
<aside class="toc"><b>On this page</b>{toc}</aside>
<article class="prose">{prose}<p>Questions? <a href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a> or <a href="{WA}" target="_blank" rel="noopener">message us on WhatsApp</a>.</p></article>
</div></div>'''
    page(f"{slug}.html", f"{title} – Gozza Finance", f"{title}: {tag}, {dt}.", "news.html", body)

# ---------------- SERVICE PAGES ----------------
STEPS = {
 "Savings": [("Tell us your goal","Call or message us with what you are saving for and by when."),("We size the plan","We suggest an amount and time frame that fits your income."),("Review in writing","You get the plan, costs, and conditions on one page."),("Start and track","We set it up with the provider and keep you updated on progress.")],
 "Investments": [("Share your situation","Your goals, time frame, and what you already hold."),("We explain the options","Costs, risks, and how each option could behave."),("You decide","Choices are yours; we prepare the paperwork."),("Review regularly","We check in on your plan and adjust when life changes.")],
 "Loans": [("Tell us what you need","Amount, purpose, and the repayment you are comfortable with."),("We compare offers","Rates, fees, and conditions from suitable lenders."),("Documents prepared","We organize papers so your application is complete the first time."),("Sanction and follow-up","We stay with you until the funds arrive and remind you of installments.")],
 "Insurance": [("Understand your needs","Family, assets, and the risks that worry you most."),("Compare plans","Cover, exclusions, and cost side by side."),("Buy with clarity","Policy terms explained before you pay."),("Renewals and claims","Reminders before renewal and help when you need to claim.")],
 "Payments": [("Tell us what you pay","The bills, transfers, or collections you handle today."),("We set up a simple system","Everything in one list with reminders."),("Start using it","We walk you through the first transactions."),("Ongoing help","Call us if anything is delayed or unclear.")],
 "Business tools": [("Share your records","Bills, statements, and what you file today."),("We organize them","Clean books and a clear calendar of due dates."),("Regular delivery","Monthly summaries and timely filings."),("Support all year","Questions answered by the same team.")],
 "Mobile": [("Get in touch","Call or message and tell us what you want to track."),("We set you up","Your goals and documents are added for you."),("Start using it","Simple screens, no learning curve."),("We stay reachable","Your advisor is a message away.")],
}

for i, sv in enumerate(SV):
    col = COLORS[i % len(COLORS)]
    hl = "".join(f'<div class="card"><i>0{j+1}</i><h3>{h}</h3><p>{t}</p></div>' for j, (h, t) in enumerate(sv["hl"]))
    steps = "".join(f"<li><div><b>{h}</b><span>{t}</span></div></li>" for h, t in STEPS[sv["cat"]])
    related = [x for x in SV if x["cat"] == sv["cat"] and x is not sv][:3]
    if len(related) < 3:
        related += [x for x in SV if x["cat"] != sv["cat"]][:3 - len(related)]
    rel = "".join(
        f'<a class="tile" href="{r["slug"]}.html"><span class="ic" style="background:{COLORS[SV.index(r) % len(COLORS)]}">{r["name"][0]}</span><span><b>{r["name"]}</b><small>{r["cat"]} &middot; {r["short"]}</small></span></a>' for r in related)
    q = sv["name"].replace(" ", "%20")
    chart_html = ""
    if sv["name"] in SV_CHART:
        cimg, ccap = SV_CHART[sv["name"]]
        chart_html = f'''<section style="padding:10px 0 0"><div class="chartframe solo sp" data-sp="dark" data-sp-density="1"><div class="bar"><i></i><i></i><i></i><span>{sv["name"]} &middot; Sample view</span><span class="live">Demo</span></div><img src="assets/charts/{cimg}.webp" width="1760" height="770" alt="{ccap}" loading="lazy"></div><p class="cap-l">{ccap}. Not investment advice.</p></section>'''
    body = f"""
<div class="wrap">
<section class="service-hero sp" data-sp="light" data-sp-density=".6">
<a class="crumb" href="apps.html">&larr; All apps</a>
<div class="sv-badge"><i style="background:{col}">{sv["name"][0]}</i><span>{sv["cat"]}</span></div>
<h1>{sv["name"]}</h1>
<p class="lead">{sv["tagline"]}</p>
<div class="acts"><a class="btn" href="contact.html?service={q}">Enquire about {sv["name"]} {ARROW}</a><a class="btn ghost" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a></div>
</section>
{chart_html}<section class="sec" style="padding-top:30px"><span class="eyebrow">Overview</span><h2>About {sv["name"]}</h2>
<p class="body">{sv["intro"]}</p>
<p class="body"><b>Who it is for:</b> {sv["who"]}</p>
<div class="sv-grid">{hl}</div></section>
<section class="sec" style="padding-top:0"><span class="eyebrow">How it works</span><h2>Four simple steps.</h2>
<ol class="steps">{steps}</ol>
<p class="note">Availability, rates, charges, and eligibility depend on the partner institution and your profile. We explain all of them in writing before you commit.</p></section>
<section class="sec" style="padding-top:0"><span class="eyebrow">Related services</span><h2>You may also need</h2><div class="grid">{rel}</div></section>
<section style="padding-bottom:clamp(50px,7vw,100px)"><div class="cta-band sp" data-sp="dark" data-sp-density="1.2"><h2>Talk to a person about {sv["name"]}.</h2>
<div class="acts"><a class="btn" href="tel:{PHONE_TEL}">Call now {ARROW}</a><a class="btn light" href="{WA}?text=Hello%20Gozza%20Finance%2C%20I%20want%20to%20know%20about%20{q}" target="_blank" rel="noopener">WhatsApp</a></div></div></section>
</div>"""
    page(sv["slug"] + ".html", f'{sv["name"]} – Gozza Finance', f'{sv["name"]}: {sv["tagline"]} Gozza Finance, Faridabad.', "apps.html", body)

# ---------------- CONTACT ----------------
opts = "".join(f'<option value="{n}">{n}</option>' for n, _, _ in SERVICES) + '<option value="Partnership">Partnership</option><option value="General enquiry">General enquiry</option>'
contact = f'''
<section class="hero sp" data-sp="light" data-sp-density=".7"><div class="hero-inner" style="grid-template-columns:1fr 1fr">
<div><span class="eyebrow" style="color:var(--blue);opacity:1;margin:0 0 18px">Contact</span><h1 class="display">Let&rsquo;s talk money.</h1></div>
<div><p class="lead">Call, message, or visit. Tell us what you want to achieve and we will suggest the next step.</p></div></div></section>
<section class="sec" style="padding-top:20px"><div class="wrap contact-grid">
<div><img src="assets/logo.png" alt="Gozza Finance" style="height:120px;width:auto">
<div class="info">
<a href="tel:{PHONE_TEL}"><span class="ic">{PHONE_SVG}</span><span><small>Phone</small><b>{PHONE_DISPLAY}</b></span></a>
<a href="{WA}" target="_blank" rel="noopener"><span class="ic">{CHAT_SVG}</span><span><small>WhatsApp</small><b>Message us</b></span></a>
<a href="{MAPS}" target="_blank" rel="noopener"><span class="ic">{PIN_SVG}</span><span><small>Address</small><b>{CITY}</b></span></a>
</div></div>
<form class="enq" id="enquiry" autocomplete="on">
<label>Your name<input name="name" required placeholder="Full name"></label>
<label>Service<select name="service">{opts}</select></label>
<label>Message<textarea name="message" placeholder="Tell us briefly what you need"></textarea></label>
<button class="btn" type="submit" style="margin-top:6px;justify-content:center">Send on WhatsApp {ARROW}</button>
<small style="color:var(--muted)">This opens WhatsApp with your message ready to send to {PHONE_DISPLAY}.</small>
</form></div></section>
'''
page("contact.html", "Contact – Gozza Finance", "Call +91 81301 12531 or visit Gozza Finance in Faridabad.", "contact.html", contact)
print("built")
