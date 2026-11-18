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
CHAT_SVG = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.65.08-.3-.15-1.26-.46-2.39-1.47-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.61-.92-2.21-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.21 3.07c.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49 1.69.62.71.23 1.36.2 1.87.12.57-.08 1.76-.72 2.01-1.41.25-.7.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35m-5.42 7.4h-.01a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.89-9.88 2.64 0 5.12 1.03 6.99 2.9a9.82 9.82 0 0 1 2.89 6.99c0 5.45-4.44 9.88-9.88 9.88m8.41-18.3A11.82 11.82 0 0 0 12.05 0C5.5 0 .16 5.34.16 11.89c0 2.1.55 4.14 1.59 5.95L.06 24l6.3-1.65a11.88 11.88 0 0 0 5.68 1.45h.01c6.55 0 11.89-5.34 11.89-11.89 0-3.18-1.24-6.17-3.48-8.41Z"/></svg>'
MENU_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'

HOME_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11 12 3l9 8M5 9.5V21h5v-6h4v6h5V9.5"/></svg>'
GRID_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="3.5" y="3.5" width="7" height="7" rx="2"/><rect x="13.5" y="3.5" width="7" height="7" rx="2"/><rect x="3.5" y="13.5" width="7" height="7" rx="2"/><rect x="13.5" y="13.5" width="7" height="7" rx="2"/></svg>'
INFO_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="3.5"/><path d="M5 20c.6-3.6 3.4-5.5 7-5.5s6.4 1.9 7 5.5"/></svg>'
MORE_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="5.5" cy="12" r=".6"/><circle cx="12" cy="12" r=".6"/><circle cx="18.5" cy="12" r=".6"/></svg>'

NAV = [("apps.html", "Services"), ("tools.html", "Calculators"), ("about.html", "About"), ("tech.html", "Tech"), ("news.html", "News")]

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
COLORS = ["#1e6bd6", "#0b3a75", "#0f8b8d", "#e8a33d", "#0f3460", "#4aa3df"]


def _ic(path): return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">' + path + '</svg>'
I_TAG = _ic('<path d="M20 12 12 20 3 11V3h8z"/><circle cx="7.5" cy="7.5" r="1.2"/>')
I_SHIELD = _ic('<path d="M12 3 4 6v6c0 4.5 3.2 7.8 8 9 4.8-1.2 8-4.5 8-9V6z"/><path d="m9 12 2 2 4-4"/>')
I_HEAD = _ic('<path d="M4 13v-1a8 8 0 0 1 16 0v1"/><rect x="3" y="13" width="4" height="6" rx="1.5"/><rect x="17" y="13" width="4" height="6" rx="1.5"/>')
I_DOC = _ic('<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4M10 12h5M10 16h5"/>')
I_LANG = _ic('<path d="M4 5h9M8.5 3v2M6 5c.6 3 2.6 5.5 5.5 7M12 5c-.6 3-3 6-7 8M12.5 21l4.5-10 4.5 10M14 18h6"/>')
I_USERS = _ic('<circle cx="9" cy="8" r="3.2"/><path d="M3 20c.5-3.5 3-5.5 6-5.5s5.5 2 6 5.5M16 5.5a3 3 0 0 1 0 5.5M18 14.8c2 .6 3.4 2.3 3.8 5.2"/>')

def slug_cat(c): return c.lower().replace(" ", "-")

CAT_INFO = {
 "Savings": "Goal-based plans, monthly habits, and fixed terms.",
 "Investments": "Mutual funds, stocks, and gold with plain-language guidance.",
 "Loans": "Personal, business, home, and property loans compared for you.",
 "Insurance": "Health, life, motor, and business cover side by side.",
 "Payments": "Bills, transfers, and collections made simple.",
 "Business tools": "Accounting, tax, and payroll for small businesses.",
 "Mobile": "Gozza Mobile and WhatsApp support, always at hand.",
}

CALCS = {
 "emi": dict(tab="Loan EMI", title="Loan EMI calculator", sub="See your monthly installment before you borrow.", svc="Personal Loans",
   f=[("amt", "Loan amount (₹)", 50000, 20000000, 500000, 10000), ("rate", "Interest rate (% per year)", 5, 30, 11, 0.1), ("yrs", "Tenure (years)", 1, 30, 5, 1)],
   lm="Monthly EMI", l1="Loan amount", l2="Total interest"),
 "sip": dict(tab="SIP", title="SIP calculator", sub="Estimate what a monthly investment could grow to.", svc="Mutual Fund Advisory",
   f=[("amt", "Monthly investment (₹)", 500, 200000, 10000, 500), ("rate", "Expected return (% per year)", 1, 30, 12, 0.5), ("yrs", "Time period (years)", 1, 40, 10, 1)],
   lm="Estimated value", l1="Amount invested", l2="Estimated gains"),
 "lump": dict(tab="Fixed growth", title="Lump sum calculator", sub="See how a one-time amount could grow over a fixed term.", svc="Fixed Growth",
   f=[("amt", "Amount (₹)", 10000, 20000000, 100000, 5000), ("rate", "Rate (% per year)", 1, 15, 7, 0.1), ("yrs", "Time period (years)", 1, 30, 5, 1)],
   lm="Maturity value", l1="Amount invested", l2="Estimated gains"),
 "goal": dict(tab="Goal planner", title="Goal planner", sub="Find the monthly amount needed to reach a target.", svc="Smart Savings",
   f=[("amt", "Target amount (₹)", 50000, 50000000, 1000000, 10000), ("yrs", "Time to goal (years)", 1, 30, 5, 1), ("rate", "Expected growth (% per year)", 0, 15, 6, 0.5)],
   lm="Monthly saving needed", l1="You save", l2="Growth earned"),
}
SVC_CALC = {"Personal Loans": "emi", "Business Loans": "emi", "Home Loans": "emi", "Loan Against Property": "emi",
            "Smart Savings": "goal", "Family Fund": "goal", "Recurring Plans": "sip", "Gold Savings": "sip",
            "Mutual Fund Advisory": "sip", "Stock Market Desk": "sip", "Fixed Growth": "lump"}

def calc_html(kind, hidden=False):
    c = CALCS[kind]
    flds = ""
    for k, lab, mn, mx, val, st in c["f"]:
        flds += (f'<div class="fld"><label class="lab"><span>{lab}</span><input type="number" data-k="{k}" min="{mn}" max="{mx}" step="{st}" value="{val}" inputmode="decimal"></label>'
                 f'<input type="range" data-r="{k}" min="{mn}" max="{mx}" step="{st}" value="{val}" aria-label="{lab}"></div>')
    h = " hidden" if hidden else ""
    q = c["svc"].replace(" ", "%20")
    return (f'<div class="calc" data-calc="{kind}" id="calc-{kind}"{h}><div><h3>{c["title"]}</h3><p class="sub">{c["sub"]}</p>{flds}</div>'
            f'<div class="res"><div class="big"><small>{c["lm"]}</small><b data-o="main">&#8377;0</b></div>'
            f'<div class="split"><div class="donut" data-o="donut"></div><ul><li><span>{c["l1"]}</span><b data-o="v1"></b></li><li class="b2"><span>{c["l2"]}</span><b data-o="v2"></b></li></ul></div>'
            f'<a class="btn" href="contact.html?service={q}">Talk to an advisor</a></div></div>')

CALC_NOTE = '<p class="calc-note">Calculators give illustrative estimates only. Actual rates, charges, and returns depend on the provider and the market, and returns are not guaranteed. Investments are subject to market risks.</p>'

DOCS = {
 "Loans": ["ID proof (Aadhaar or PAN)", "Address proof", "Last 3 to 6 months of bank statements", "Income proof: salary slips or ITR", "Business proof and GST returns (business loans)", "Property papers (home and property loans)"],
 "Insurance": ["ID and address proof", "Date of birth proof", "Existing policy documents, if any", "Medical history details (health and life)", "Vehicle RC and old policy (motor)", "Premises and stock details (business)"],
 "Investments": ["PAN card", "Aadhaar or other address proof", "Bank account details", "Passport-size photo", "Details of what you already hold (portfolio review)"],
 "Savings": ["PAN card", "ID and address proof", "Bank account details", "Your goal, amount, and target date"],
 "Payments": ["Bill account numbers", "Beneficiary bank details (transfers)", "Customer and invoice list (collections)"],
 "Business tools": ["PAN and GST details", "Sales and purchase invoices", "Bank statements", "Previous returns and filings", "Employee list and salaries (payroll)"],
 "Mobile": ["Your mobile number", "Documents you want to store", "A list of goals and policies to track"],
}
CAT_FAQ = {
 "Savings": [("Can I change or stop a plan?", "Yes. You can increase, pause, or stop a plan when your situation changes. We explain any conditions in writing before you start."), ("Is my money safe?", "Plans are held with regulated partner institutions in your own name. We keep a written record of every plan.")],
 "Investments": [("Do you guarantee returns?", "No. Investments are subject to market risk and nobody can promise returns. We explain risks, costs, and alternatives so you can decide."), ("In whose name are investments held?", "Units and holdings stay in your own name with the regulated provider. Gozza coordinates the paperwork.")],
 "Loans": [("How long does a loan take?", "It depends on the lender and how complete your documents are. We prepare the paperwork so there are fewer delays."), ("Will you show the full cost?", "Yes. Interest, processing fees, and other charges are listed before you commit.")],
 "Insurance": [("Will you push a particular policy?", "No. We start with your family and goals, compare options, and tell you plainly if a plan is not right for you."), ("Can you help with a claim?", "Yes. We explain the claim process before you buy and guide you on documents when you need to claim.")],
 "Payments": [("Are there fees?", "Charges depend on the method and provider. We show them before you send or set anything up."), ("What if a transfer goes wrong?", "Call or message us straight away and we will help you follow it up with the bank or provider.")],
 "Business tools": [("Do you work with very small businesses?", "Yes. Our tools are built for shops, clinics, traders, and small factories."), ("Who keeps my records?", "We keep clean copies and you keep full access. Nothing is shared without your consent.")],
 "Mobile": [("Is there a fee to use it?", "We confirm any charges before you start. Ask the team for the current details."), ("Can I talk to a person?", "Yes. You can message or call the same team any day.")],
}


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


def bottom_nav(active):
    def a(href, label, svg):
        cls = ' class="on"' if href == active or (href == "news.html" and active.startswith("article")) else ""
        return f'<a{cls} href="{href}">{svg}<span>{label}</span></a>'
    return ('<nav class="bottom-nav" aria-label="Quick">' + a("index.html", "Home", HOME_SVG) + a("apps.html", "Services", GRID_SVG)
            + f'<a class="bn-call" href="tel:{PHONE_TEL}" aria-label="Call {PHONE_DISPLAY}">{PHONE_SVG}</a>'
            + a("about.html", "About", INFO_SVG) + f'<button class="bn-more menu-btn" type="button" aria-label="More pages" aria-expanded="false">{MORE_SVG}<span>More</span></button></nav>')


def footer():
    return f"""<footer class="foot2 sp" data-sp="dark" data-sp-density=".8"><div class="wrap">
<div class="cols">
<div><img class="fi" src="assets/logo-icon.png" alt="Gozza Finance"><p class="brandp">Savings, investments, loans, and insurance explained in plain language, by a team you can call any day.</p></div>
<div><h4>Explore</h4><a href="apps.html">Services</a><a href="tools.html">Calculators</a><a href="tech.html">Tech</a><a href="about.html">About</a><a href="news.html">News</a></div>
<div><h4>Services</h4><a href="{sv_link("Smart Savings")}">Savings</a><a href="{sv_link("Mutual Fund Advisory")}">Investments</a><a href="{sv_link("Personal Loans")}">Loans</a><a href="{sv_link("Health Insurance")}">Insurance</a><a href="{sv_link("Tax Planning")}">Tax planning</a></div>
<div><h4>Legal</h4><a href="privacy.html">Privacy policy</a><a href="terms.html">Terms and disclaimer</a><a href="index.html#faq">FAQ</a></div>
<div><h4>Contact</h4><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a><a href="{MAPS}" target="_blank" rel="noopener">Faridabad</a><a href="contact.html">Enquiry form</a></div>
</div>
<p class="risk">Gozza Finance helps you compare and apply for products offered by partner institutions. Investments are subject to market risks; read all scheme documents carefully. Charts and calculators on this site are illustrative and are not investment advice.</p>
<div class="copy" style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;font-size:14px"><span>&copy; 2026 Gozza Finance. All rights reserved.</span><span>{CITY}</span></div>
</div></footer>
<div class="fab"><a class="wa" href="{WA}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{CHAT_SVG}<span>WhatsApp</span></a><a class="call" href="tel:{PHONE_TEL}">{PHONE_SVG}<span>{PHONE_DISPLAY}</span></a></div>"""


def page(filename, title, desc, active, body, extra_head=""):
    out = f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:image" content="assets/logo.png">
<link rel="icon" type="image/png" href="assets/favicon.png"><link rel="apple-touch-icon" href="assets/logo-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<meta name="theme-color" content="#f5f9ff">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;700;800&family=Mukta:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="assets/styles.css">{extra_head}
</head><body>
{header(active)}
<main>{body}</main>
{footer()}
{bottom_nav(active)}
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
faq += [
    ("Which services do you offer?", ["Savings plans, mutual fund and stock guidance, gold savings, personal, business, home, and property loans, health, life, motor, and business insurance, bill payments, transfers, collections, accounting, tax planning, and payroll. See the full list on the Services page."]),
    ("Do you charge for advice?", ["We explain every cost before you commit, including any fee we or the partner institution charge. Ask us on call or WhatsApp and we will tell you plainly."]),
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

cats_html = ""
for ci, c in enumerate(CATS):
    items = [x for x in SV if x["cat"] == c][:3]
    lis = "".join(f'<li><a href="{x["slug"]}.html">{x["name"]}{ARROW}</a></li>' for x in items)
    cats_html += (f'<div class="cat"><span class="ci" style="background:{COLORS[ci % len(COLORS)]}">{c[0]}</span><h3>{c}</h3><p>{CAT_INFO[c]}</p><ul>{lis}</ul>'
                  f'<a class="more-l" href="apps.html#{slug_cat(c)}">See all {c.lower()}</a></div>')

goal_items = [
 ("Buy a home", "Compare lenders, check eligibility, and manage the paperwork.", "Home Loans"),
 ("Grow my business", "Working capital and equipment finance built around your cash cycle.", "Business Loans"),
 ("Fund my child's education", "A shared family plan for fees and future costs.", "Family Fund"),
 ("Save for a wedding", "Set a target, a monthly amount, and a date.", "Smart Savings"),
 ("Protect my family", "Right-sized life cover, explained in plain terms.", "Life Insurance"),
 ("Plan for steady growth", "Lock in a defined term with the outcome stated up front.", "Fixed Growth"),
 ("Save tax and file on time", "Plan through the year, file accurately.", "Tax Planning"),
 ("Review what I already hold", "One page showing holdings, costs, and overlaps.", "Portfolio Review"),
]
goals_html = "".join(f'<a class="goal" href="{sv_link(n)}"><b>{t}</b><span>{d}</span><em>{n}{ARROW}</em></a>' for t, d, n in goal_items)
SEGS = [
 ("Families", "Saving, protecting, and planning together.", ["Smart Savings", "Health Insurance", "Family Fund"]),
 ("Salaried professionals", "Make your income work harder.", ["Tax Planning", "Mutual Fund Advisory", "Personal Loans"]),
 ("Traders and shop owners", "Credit, collections, and clean books.", ["Business Loans", "Business Collections", "Accounting Support"]),
 ("Factories and clinics", "Staff, assets, and cover in order.", ["Payroll Help", "Business Insurance", "Loan Against Property"]),
]
seg_html = "".join(
    f'<div class="seg"><h3>{t}</h3><p>{d}</p><ul>' + "".join(f'<li><a href="{sv_link(n)}">{n}{ARROW}</a></li>' for n in ns) + '</ul></div>'
    for t, d, ns in SEGS)
calc_tabs = '<div class="tabs" role="tablist">' + "".join(f'<button type="button" role="tab" data-tab="{k}" class="{"on" if n == 0 else ""}">{v["tab"]}</button>' for n, (k, v) in enumerate(CALCS.items())) + '</div>'
calc_home = calc_tabs + "".join(calc_html(k, hidden=(n != 0)) for n, k in enumerate(CALCS))
how_html = "".join(f"<div><b>{h}</b><span>{t}</span></div>" for h, t in [
    ("Tell us your goal", "Call or message us with what you want to achieve and by when."),
    ("We compare options", "Costs, risks, and conditions side by side, in plain language."),
    ("Review in writing", "You get the plan, charges, and terms on one page before you decide."),
    ("Start and track", "We handle the paperwork and keep you updated until it is done.")])
why_html = "".join(f"<div><i>{ic_}</i><b>{h}</b><span>{t}</span></div>" for ic_, h, t in [
    (I_TAG, "Costs shown up front", "Interest, fees, and charges are listed before you commit. No surprises later."),
    (I_SHIELD, "Held in your name", "Investments and policies sit with the regulated provider in your own name."),
    (I_HEAD, "A real person answers", "Call or WhatsApp the same team, any day. Every request is logged."),
    (I_DOC, "Everything in writing", "Plans, quotes, and conditions are recorded so you can always check."),
    (I_LANG, "Hindi and English", "We explain things in the language you are comfortable with."),
    (I_USERS, "Families and businesses", "From a first savings plan to a shop's GST filings, one team handles it.")])
cb_opts = "".join(f'<option value="{n}">{n}</option>' for n, _, _ in SERVICES) + '<option value="General enquiry">General enquiry</option>'
CB = f'''<section style="padding:clamp(40px,6vw,90px) 0 0"><div class="wrap"><div class="cb">
<div><h2>Want a call back from our team?</h2><p>Share your number and what you need. We will message you on WhatsApp to confirm a good time to talk.</p></div>
<form data-wa-form novalidate><input name="name" placeholder="Your name" autocomplete="name" aria-label="Your name"><input name="phone" type="tel" placeholder="Mobile number" autocomplete="tel" inputmode="tel" aria-label="Mobile number">
<select name="service" aria-label="Service">{cb_opts}</select>
<span class="err" role="alert"></span>
<button class="btn light" type="submit">{CHAT_SVG} Request call back on WhatsApp</button>
<small>This opens WhatsApp with your details ready to send to {PHONE_DISPLAY}.</small></form></div></div></section>'''

home = f'''
<section class="hero home sp" data-sp="light" data-sp-density=".7">
<div class="hero-inner">
<div><h1 class="display">Smart finance for every family and business</h1>
<p class="lead">Savings, investments, loans, and insurance, explained in plain language by a team you can call any day.</p>
<div class="acts"><a class="btn" href="apps.html">Explore services {ARROW}</a><a class="btn wa" href="{WA}" target="_blank" rel="noopener">{CHAT_SVG} Chat on WhatsApp</a></div>
<div class="trust"><span>Hindi and English</span><span>Costs shown up front</span><span>Held in your name</span></div></div>
<div class="hv" aria-hidden="true">
<div class="c c1"><span class="tag">Sample</span><small>Goal &middot; Wedding fund</small><div class="row2"><b>&#8377;6,40,000</b><small>of &#8377;10,00,000</small></div><div class="meter"><i></i></div></div>
<div class="c c2"><small>Monthly plan</small><b>&#8377;5,000</b><div class="ok">&#10003; Scheduled for the 5th</div></div>
<div class="c c3"><small>Savings growth</small><svg class="spark" viewBox="0 0 200 56" fill="none"><path d="M2 48 22 42 42 44 62 32 82 36 102 24 122 28 142 14 162 18 198 4" stroke="#1e6bd6" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M2 48 22 42 42 44 62 32 82 36 102 24 122 28 142 14 162 18 198 4V56H2Z" fill="rgba(30,107,214,.12)"/></svg></div>
</div></div>
{strip_html}
</section>

<section class="sec"><div class="wrap">
<div class="head"><span class="eyebrow">Services</span><h2>Everything money, handled by one team.</h2><p>Pick a category to see how each service works, what it costs, and how to start.</p></div>
<div class="cats">{cats_html}</div>
</div></section>

<section class="sec" style="padding-top:0"><div class="wrap">
<div class="head"><span class="eyebrow">Start with your goal</span><h2>What do you want your money to do?</h2><p>Choose the goal closest to yours and we will show you the service that fits.</p></div>
<div class="goals">{goals_html}</div>
</div></section>

<section class="sec soft" id="calculators"><div class="wrap">
<div class="head"><span class="eyebrow">Calculators</span><h2>Work out the numbers before you decide.</h2><p>Move the sliders to see an EMI, a SIP, a fixed term, or a savings goal. Then talk to us about the real options.</p></div>
{calc_home}
{CALC_NOTE}
<a class="calc-link" href="tools.html">Open all calculators</a>
</div></section>

<section class="sec"><div class="wrap">
<div class="head"><span class="eyebrow">How it works</span><h2>From first call to done, in four steps.</h2></div>
<div class="how">{how_html}</div>
</div></section>

<section class="seg-sec"><div class="wrap">
<div class="head"><span class="eyebrow">Who we help</span><h2>Finance that fits your kind of life or work.</h2></div>
<div class="segs">{seg_html}</div>
</div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><div class="stats">
<div><b>24</b><span>Services</span></div><div><b>7</b><span>Categories</span></div><div><b>1</b><span>Team, one number</span></div><div><b>24/7</b><span>WhatsApp</span></div></div></div></section>

<section class="sec soft"><div class="wrap">
<div class="head"><span class="eyebrow">Why Gozza</span><h2>Built around people, not products.</h2></div>
<div class="why">{why_html}</div>
</div></section>

<section class="sec"><div class="wrap">
<div class="head"><span class="eyebrow">Research</span><h2>See the market the way our advisors do.</h2><p>Charts, costs, and risk explained before you invest a rupee.</p></div>
<div class="mock sp" style="margin-top:34px;border-radius:32px;box-shadow:var(--sh-2)" data-sp="dark" data-sp-density="1.4"><div class="chartframe"><div class="bar"><i></i><i></i><i></i><span>Gozza &middot; Market view</span><span class="live">Live demo</span></div>
<img src="assets/charts/chart-terminal.webp" width="1760" height="990" alt="Illustrative trading terminal with candlestick chart, volume bars and order book" loading="lazy"></div>
<p class="cap">Illustrative chart for demonstration. Not investment advice.</p></div>
<a class="btn ghost" href="{sv_link("Stock Market Desk")}">Stock Market Desk {ARROW}</a>
</div></section>

<section class="vision-dark sp" data-sp="dark" data-sp-density="1.1"><div class="in">
<img class="gl" src="assets/logo-icon.png" alt="">
{vision_html}
</div></section>

<section class="sec"><div class="wrap two">
<div><span class="eyebrow">Security</span><h2>Built on consent, clear records, and regulated partners.</h2>
<p class="body">We collect only the documents a service needs and never share them without your consent. Investments and policies are held in your own name with the regulated provider.</p>
<p class="body">Every conversation and quote is logged so you can always check what was promised. <a href="tech.html#architecture" style="color:var(--red);border-bottom:2px solid var(--brass-hi)">See how the platform works</a>.</p></div>
<div class="card" style="min-height:0;align-self:center"><span class="eyebrow" style="margin:0">Partner with us</span><h3 style="font-size:30px">Integrate Gozza</h3>
<p>Shops, traders, and advisors can offer Gozza services to their own customers. You keep the relationship; our team handles the paperwork, follow-up, and support in the background.</p>
<div><a class="btn" href="contact.html?service=Partnership">Start partnering {ARROW}</a></div></div>
</div></section>

<section class="sec soft"><div class="wrap"><span class="eyebrow">News</span><h2>Latest from Gozza.</h2>
<div class="news-list tight">{news_rows(PRESS[:3])}</div>
<a class="btn ghost more" href="news.html">Read all {ARROW}</a></div></section>

<section class="sec" id="faq"><div class="wrap"><span class="eyebrow">FAQ</span><h2>Questions we hear most.</h2>
<div class="faq" style="margin-top:28px">{faq_html}</div></div></section>
{CB}
'''
page("index.html", "Gozza Finance – Smart finance for every family and business",
     "Savings, investments, loans, and insurance explained in plain language. Gozza Finance, Faridabad. Call +91 81301 12531.", "index.html", home)

# ---------------- TECH ----------------
tech = f'''
<section class="hero sp" data-sp="light" data-sp-density=".7"><div class="hero-inner" style="grid-template-columns:1fr 1fr">
<div><span class="eyebrow" style="color:var(--red);opacity:1;margin:0 0 18px">Tech</span>
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
<div><span class="eyebrow" style="color:var(--red);opacity:1;margin:0 0 18px">About</span>
<h1 class="display">The people behind Gozza.</h1></div>
<div><p class="lead">A local team in Faridabad that believes money decisions deserve time, honesty, and a phone number that gets answered.</p>
<div class="subnav"><a class="chip" href="#community">Community</a><a class="chip" href="#team">Gozza team</a><a class="chip" href="#advisory">Advisory</a><a class="chip" href="#partners">Partners</a><a class="chip" href="#visit">Visit us</a></div></div></div></section>

<section class="sec" style="padding-bottom:0"><div class="wrap"><span class="eyebrow">How we work</span><h2>Four promises we keep.</h2>
<div class="principles"><div><b>Plain language</b><span>No jargon. If we cannot explain it simply, we will not recommend it.</span></div><div><b>Costs up front</b><span>Every fee and condition is shown before you commit.</span></div><div><b>No pressure</b><span>If a plan is not right for you, we say so.</span></div><div><b>Always reachable</b><span>Call or WhatsApp the same team any day.</span></div></div></div></section>
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
<div><span class="eyebrow" style="color:var(--red);opacity:1;margin:0 0 18px">Services</span><h1 class="display">Services built around you.</h1></div>
<div><p class="lead">Save, invest, borrow, insure, and manage a business. Explore every Gozza service and start with one call.</p></div></div></section>
<section class="sec" style="padding-top:20px"><div class="wrap">
<div class="chips" style="margin-top:0">{chips}</div>
<div class="grid">{tiles}</div>
</div></section>
'''
page("apps.html", "Services – Gozza Finance", "Explore Gozza Finance services: savings, investments, loans, insurance, payments, and business tools.", "apps.html", apps)

# ---------------- NEWS ----------------
art_cards = "".join(
    f'<a class="acard" href="{slug}.html"><div class="th sp" data-sp="dark" data-sp-density="1.1"><img src="assets/charts/cover-{i+1}.webp" alt="" loading="lazy"></div><div class="tx"><small>{tag} &middot; {dt}</small><b>{title}</b></div></a>'
    for i, (slug, title, tag, dt, _) in enumerate(ARTICLES)
)
news = f'''
<section class="hero sp" data-sp="light" data-sp-density=".7"><div class="hero-inner" style="grid-template-columns:1fr 1fr">
<div><span class="eyebrow" style="color:var(--red);opacity:1;margin:0 0 18px">News</span><h1 class="display">Dispatches from Gozza.</h1></div>
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
    extra_html = ""
    if sv["name"] in SVC_CALC:
        extra_html += f'<section class="sec" style="padding-top:0"><span class="eyebrow">Try the numbers</span><h2>Estimate before you enquire.</h2><div style="margin-top:6px">{calc_html(SVC_CALC[sv["name"]])}</div>{CALC_NOTE}</section>'
    extra_html += '<section class="sec" style="padding-top:0"><span class="eyebrow">Documents</span><h2>Documents you may need.</h2><ul class="docs">' + "".join(f"<li>{d}</li>" for d in DOCS[sv["cat"]]) + '</ul><p class="note">The exact list depends on the provider. We confirm it with you before you apply.</p></section>'
    extra_html += '<section class="sec" style="padding-top:0"><span class="eyebrow">FAQ</span><h2>Common questions.</h2><div class="faq wide">' + "".join(f"<details><summary>{q_}</summary><p>{a_}</p></details>" for q_, a_ in CAT_FAQ[sv["cat"]]) + '</div></section>'
    body = f"""
<div class="wrap">
<section class="service-hero sp" data-sp="light" data-sp-density=".6">
<a class="crumb" href="apps.html">&larr; All services</a>
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
{extra_html}<section class="sec" style="padding-top:0"><span class="eyebrow">Related services</span><h2>You may also need</h2><div class="grid">{rel}</div></section>
<section style="padding-bottom:clamp(50px,7vw,100px)"><div class="cta-band sp" data-sp="dark" data-sp-density="1.2"><h2>Talk to a person about {sv["name"]}.</h2>
<div class="acts"><a class="btn" href="tel:{PHONE_TEL}">Call now {ARROW}</a><a class="btn light" href="{WA}?text=Hello%20Gozza%20Finance%2C%20I%20want%20to%20know%20about%20{q}" target="_blank" rel="noopener">{CHAT_SVG} WhatsApp</a></div></div></section>
</div>"""
    page(sv["slug"] + ".html", f'{sv["name"]} – Gozza Finance', f'{sv["name"]}: {sv["tagline"]} Gozza Finance, Faridabad.', "apps.html", body)

# ---------------- CONTACT ----------------
opts = "".join(f'<option value="{n}">{n}</option>' for n, _, _ in SERVICES) + '<option value="Partnership">Partnership</option><option value="General enquiry">General enquiry</option>'
contact = f'''
<section class="hero sp" data-sp="light" data-sp-density=".7"><div class="hero-inner" style="grid-template-columns:1fr 1fr">
<div><span class="eyebrow" style="color:var(--red);opacity:1;margin:0 0 18px">Contact</span><h1 class="display">Let&rsquo;s talk money.</h1></div>
<div><p class="lead">Call, message, or visit. Tell us what you want to achieve and we will suggest the next step.</p></div></div></section>
<section class="sec" style="padding-top:20px"><div class="wrap contact-grid">
<div><img src="assets/logo.png" alt="Gozza Finance" style="height:120px;width:auto">
<div class="info">
<a href="tel:{PHONE_TEL}"><span class="ic">{PHONE_SVG}</span><span><small>Phone</small><b>{PHONE_DISPLAY}</b></span></a>
<a href="{WA}" target="_blank" rel="noopener"><span class="ic wa-ic">{CHAT_SVG}</span><span><small>WhatsApp</small><b>Message us</b></span></a>
<a href="{MAPS}" target="_blank" rel="noopener"><span class="ic">{PIN_SVG}</span><span><small>Address</small><b>{CITY}</b></span></a>
</div></div>
<form class="enq" id="enquiry" autocomplete="on">
<label>Your name<input name="name" required placeholder="Full name"></label>
<label>Mobile number<input name="phone" type="tel" required placeholder="10-digit mobile number" autocomplete="tel" inputmode="tel"></label>
<label>Service<select name="service">{opts}</select></label>
<label>Message<textarea name="message" placeholder="Tell us briefly what you need"></textarea></label>
<span class="err" role="alert"></span>
<button class="btn wa" type="submit" style="margin-top:6px;justify-content:center">{CHAT_SVG} Send on WhatsApp</button>
<small style="color:var(--muted)">This opens WhatsApp with your message ready to send to {PHONE_DISPLAY}.</small>
</form></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><span class="eyebrow">What happens next</span><h2>Four steps after you write to us.</h2>
<div class="how"><div><b>You send your enquiry</b><span>By form, call, or WhatsApp.</span></div><div><b>We get back to you</b><span>A team member reaches out to understand your need.</span></div><div><b>We explain your options</b><span>Costs, risks, and conditions in plain language.</span></div><div><b>You decide</b><span>We handle the paperwork once you say go.</span></div></div></div></section>
'''
page("contact.html", "Contact – Gozza Finance", "Call +91 81301 12531 or visit Gozza Finance in Faridabad.", "contact.html", contact)

# ---------------- TOOLS (calculators) ----------------
tool_chips = "".join(f'<a class="chip" href="#calc-{k}">{v["tab"]}</a>' for k, v in CALCS.items())
tools = f"""
<section class="hero sp" data-sp="light" data-sp-density=".7"><div class="hero-inner" style="grid-template-columns:1fr 1fr">
<div><span class="eyebrow" style="color:var(--red);opacity:1;margin:0 0 18px">Calculators</span><h1 class="display">Plan the numbers first.</h1></div>
<div><p class="lead">Four simple tools for loans, SIPs, fixed terms, and savings goals. Use them, then talk to us for the real options.</p>
<div class="subnav">{tool_chips}</div></div></div></section>
<section class="sec" style="padding-top:20px"><div class="wrap">
<div class="calc-grid">{"".join(calc_html(k) for k in CALCS)}</div>
{CALC_NOTE}
</div></section>
<section style="padding-bottom:clamp(50px,7vw,100px)"><div class="wrap"><div class="cta-band sp" data-sp="dark" data-sp-density="1.2"><h2>Want help turning these numbers into a plan?</h2>
<div class="acts"><a class="btn" href="tel:{PHONE_TEL}">Call now {ARROW}</a><a class="btn light" href="{WA}?text=Hello%20Gozza%20Finance%2C%20I%20used%20your%20calculator" target="_blank" rel="noopener">{CHAT_SVG} WhatsApp</a></div></div></div></section>
"""
page("tools.html", "Calculators – Gozza Finance", "EMI, SIP, lump sum, and goal calculators from Gozza Finance, Faridabad.", "tools.html", tools)

# ---------------- LEGAL ----------------
def legal(slug, title, blurb, sections):
    prose = "".join(f"<h2>{h}</h2>" + "".join(f"<p>{p}</p>" for p in ps) for h, ps in sections)
    toc = "".join(f'<a href="#l{i}">{h}</a>' for i, (h, _) in enumerate(sections))
    prose = "".join(f'<h2 id="l{i}">{h}</h2>' + "".join(f"<p>{p}</p>" for p in ps) for i, (h, ps) in enumerate(sections))
    body = f"""<div class="wrap"><div class="article-head"><a class="crumb" href="index.html">&larr; Home</a><h1>{title}</h1><div class="tags"><span>Legal</span><span>Updated Nov 2026</span></div></div>
<div class="article-grid"><aside class="toc"><b>On this page</b>{toc}</aside>
<article class="prose"><p>{blurb}</p>{prose}<p>Questions? <a href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a> or <a href="{WA}" target="_blank" rel="noopener">message us on WhatsApp</a>.</p></article></div></div>"""
    page(slug + ".html", f"{title} – Gozza Finance", blurb, "contact.html", body)

legal("privacy", "Privacy policy", "How Gozza Finance collects, uses, and protects your information.", [
 ("What we collect", ["Your name, phone number, and the details you share in enquiry forms, calls, or WhatsApp messages.", "Documents you choose to send us for a specific service, such as ID, address, income, or policy papers."]),
 ("How we use it", ["To respond to your enquiry, prepare plans and comparisons, and complete paperwork for the service you asked for.", "To remind you of renewals, due dates, and follow-ups you have requested."]),
 ("Who we share it with", ["Only the partner institution that provides the service you asked for, and only with your consent. We do not sell your information."]),
 ("WhatsApp and calls", ["When you use a button or form that opens WhatsApp, your message is sent through WhatsApp and is subject to its own terms. Forms on this site do not store your details on our servers."]),
 ("Keeping it safe", ["We ask only for documents a service needs, keep access limited to the team members who handle your request, and delete documents you ask us to remove, unless the law requires us to keep them."]),
 ("Your choices", ["You can ask us to correct or delete your information or stop reminders at any time by calling or messaging us."]),
])
legal("terms", "Terms and disclaimer", "The terms for using this website and Gozza Finance services.", [
 ("About this website", ["This website gives general information about Gozza Finance and the services it helps you access. It is not an offer or a commitment to lend, insure, or invest."]),
 ("Not investment advice", ["Investments are subject to market risks; read all scheme documents carefully. Charts, calculators, and sample screens on this site are illustrative and do not predict or guarantee any result."]),
 ("Partner institutions", ["Loans, insurance, and investment products are provided by partner institutions under their own terms, rates, charges, and eligibility rules. We explain these in writing before you commit."]),
 ("Accuracy", ["We work to keep information correct and current, but rates, charges, and rules can change. Please confirm details with us before you decide."]),
 ("Contact", ["Gozza Finance, " + CITY + ". Phone and WhatsApp: " + PHONE_DISPLAY + "."]),
])

print("built")
