"""Shared site content for the design options (taken from the live site)."""

EYEBROW = "Chicago · independent consultant · software, web & data"
H1 = "Right-sized technology solutions for organizations big and small."
LEDE = ("I start by understanding the challenge you're facing, the systems you already have, and what success "
        "looks like. Then I plan, build, and implement a solution that fits, and grows with you.")
LEDE2 = ("I've done this for unions and nonprofits, pro sports leagues, presidential campaigns, and federal agencies, "
         "and I communicate clearly with technical and non-technical people alike.")
BUILT_FOR = ["AFSCME", "CPWR", "Robert Wood Johnson Foundation", "NFL, MLB & NHL properties",
             "Presidential campaigns", "Federal agencies"]

STATS = [("300+", "websites hosted on a CMS I designed and built"),
         ("1MM+", "pages a month served by that platform"),
         ("2", "decades leading development at a Chicago agency")]

SERVICES = [
    ("WordPress builds & rescues", "New sites, migrations from legacy CMS platforms, custom themes and plugins, and rescues of builds that went sideways.", "wp"),
    ("Advocacy & data tools", "Interactive maps, wage calculators, planning tools, and dashboards: software that turns your data into action.", "data"),
    ("Custom applications", "Ruby on Rails and React applications, from internal tools to public products, built to be maintained by your team.", "app"),
    ("Accessibility", "WCAG 2.2 AA audits and remediation, and accessible design and code from the start, tested by hand.", "a11y"),
    ("Integrations & automation", "Action Network, EveryAction, Mailchimp, Asana, and custom REST integrations that remove manual work.", "api"),
    ("AWS & AI", "Infrastructure setup, review, and cost savings, plus practical, well-scoped AI features inside the tools you use.", "cloud"),
]

PROJECTS = [
    dict(client="CPWR", url="silica-safe.org", title="Silica-Safe planning tool",
         img="silica-safe-org-thumbnail.png",
         alt="Silica-Safe.org homepage, with a call to build a silica safety plan",
         short="A WordPress site built around a custom multi-step planning tool that generates job-specific safety plans contractors can save, export to PDF, or email.",
         long="Built from the ground up: a WordPress site that helps contractors plan for working safely with silica-producing materials. Its centerpiece is a fully custom planning tool that walks users through a multi-step form and generates a detailed safety plan for their specific circumstances, with links to official guidance. Users can save plans to an account, export them to PDF, or email them.",
         tags="WordPress · custom plugin · PHP · JavaScript · MySQL"),
    dict(client="AFSCME", url="scorecard.afscme.org", title="Legislative scorecard",
         img="scorecard-afscme-org-thumbnail.png",
         alt="AFSCME legislative scorecard, showing a state delegation with grades",
         short="Tracks every U.S. House and Senate vote that matters to one of the nation's largest public-service unions, and lands visitors on their own state's delegation.",
         long="A scorecard that tracks the voting record of every member of the U.S. House and Senate and grades each legislator on alignment with the union's priorities, backed by a legislator data feed, with IP geolocation landing visitors on their own state's delegation. Rebuilt for the 2025–2026 edition, launched July 2026.",
         tags="JavaScript · HTML/CSS · REST APIs · geolocation"),
    dict(client="Dave Thomas Foundation for Adoption · Child Trends", url="", title="Wendy's Wonderful Kids database",
         img="", alt="",
         short="The secure database behind a national program that finds permanent families for children in foster care.",
         long="As lead developer, I built and supported the secure web application and database behind Wendy's Wonderful Kids. Recruiters around the country used it to track their work with each child, and evaluators at Child Trends relied on its reporting to measure what worked.",
         tags="Custom web application · database · reporting · role-based access"),
]

PROCESS = [
    ("Scope", "A short call to understand the problem, your current systems, and what success looks like, then a written scope with real estimates."),
    ("Build", "Short projects of one to three months, ongoing engagements, or extra capacity for agencies that need to extend their team."),
    ("Hand off", "Documentation and tools your own staff can run. I explain the why, not just the how."),
]

CTA_H = "Have a project in mind?"
CTA_P = ("Tell me what you're trying to build, fix, or replace. I'll tell you honestly whether I'm the right person "
         "for it, and if I'm not, I'll point you to someone in my network who is.")

WORK_INTRO = ("I've built software and technology for scores of clients: tools that keep workers safe, systems that help "
              "kids in foster care find families, and platforms that let organizations run their own websites.")

CAPABILITIES = [
    ("Enterprise CMS", "A Rails CMS I designed and built that hosted 300+ websites, with asset management, templating, taxonomies, and permissions.", "Ruby on Rails · React · MySQL · AWS"),
    ("AWS platform management", "Load-balanced EC2 with managed RDS, S3 and CloudFront delivery, monitoring, and long-term cost optimization.", "EC2 · RDS · CloudFront · S3"),
    ("Front-end advocacy tools", "A map of weapons dealers near users' homes, a union wage calculator, and other portable tools hostable anywhere.", "JavaScript · React · REST APIs"),
    ("WordPress development", "Custom themes and blocks, migrations from third-party CMS tools, and custom plugin work.", "WordPress · PHP · ACF · Gravity Forms"),
    ("API integrations", "Asana and Harvest tooling, and eCRM connections to Action Network, Mailchimp, and EveryAction.", "REST · OAuth · webhooks"),
    ("Federal subcontracting", "Site production and e-learning modules for the U.S. Office of Adolescent Health, under federal compliance standards.", "Section 508 · e-learning"),
    ("High-profile site builds", "High-availability sites for presidential candidates, the NFL, MLB, and NHL, and national nonprofits.", "CloudFront · Fastly · Cloudflare"),
    ("Custom applications", "An organizing toolkit that generates custom materials, a memorial wall of 1,500+ firefighter bios, and more.", "React · Rails · Docker"),
]

CLIENTS = [
    ("Labor", ["AFSCME", "Amalgamated Transit Union", "California Professional Firefighters", "Chicago Federation of Labor",
               "Chicago Teachers Union", "CPWR", "Illinois AFL-CIO", "National Association of Letter Carriers",
               "National Postal Mail Handlers Union", "SEIU Local 221", "UNITE HERE", "United Steelworkers"]),
    ("Nonprofits & foundations", ["Center for the Study of Social Policy", "Child Trends", "CLASP", "Community Catalyst",
               "Dave Thomas Foundation for Adoption", "Evergreen Action", "League of Conservation Voters", "Malala Fund",
               "National Skills Coalition", "Robert Wood Johnson Foundation", "Trust for Public Land", "Violence Policy Center"]),
    ("Campaigns & political", ["Elizabeth Warren for President", "Jay Inslee for President", "DCCC",
               "Democratic Governors Association", "Senate Majority PAC", "Emily Sirota for Colorado"]),
    ("Sports, arts & media", ["NFL, MLB, NHL & MLS team sites", "Madison Square Garden Network", "Atlanta Falcons",
               "Writers Theatre", "The Washington Post", "cars.com"]),
    ("Government & education", ["U.S. Office of Adolescent Health (HHS)", "University of Chicago"]),
]

EMAIL = "timgut@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/timgutowski/"
