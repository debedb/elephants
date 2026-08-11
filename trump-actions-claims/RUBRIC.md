# Rubric v3

**v1 was frozen before any row was drawn or read.** Committed ahead of the sample
draw so that a reader can verify from git history that the procedure was fixed
before the results were known. Repository HEAD at freezing: `cfe569c`; the
pre-registration commit is `e58acf0` and contains the rubric and the draw and
nothing else.

Changing this file is expensive on purpose. Any change bumps the version, and
every row stamped with an older version is marked stale on the page until it is
re-adjudicated under the new one. A rubric that quietly moves to fit its results
is indistinguishable from no rubric.

## Version history

### v3 — after an argument about a referee, and about who a rule favours

Four changes, all of which make the rubric harder on us rather than on the rows.
One of them reversed a verdict we had already published.

1. **The `document` grade is split.** It covered both a Supreme Court order and a
   Justice Department press release. In one the utterance *is* the act; in the
   other a party describes its own conduct. Now `constitutive record` and
   `party account`. Index 348 was re-adjudicated against the filed complaints as
   a result, and its `agent` test went from `supported` to `unsupported`: the
   plaintiff on the instrument is the United States, and Pamela Bondi appears
   nowhere in either complaint. We had rested that test on DOJ's own press
   release about DOJ.
2. **Steelman prose is no longer exempt from the evidence rule.** Every factual
   assertion inside `forClaim` or `againstClaim` now carries an artifact and a
   quotation, or is explicitly labelled as our own unsourced reasoning. This was
   the single aperture through which a deflationary bias could enter the page —
   the tests were rigorous and the paragraphs that actually persuade required
   nothing — and we built it.
3. **A base-rate test, symmetric in both directions.** Where a claim asserts
   novelty ("in a highly unusual move") *or* a deflation asserts routineness
   ("there are hundreds of these every year"), whoever asserts it produces the
   reference class. See `OPEN-QUESTIONS.md` question 10: an artifact rule launders
   toward null unless deflations carry a burden too.
4. **Open states are no longer displayed as verdicts.** `awaiting fetch` and
   `not reachable` are refusals to conclude, and rendering them where results go
   made a permanently-open record read as a finished one. Per question 11: there
   is no whistle here, so nothing can be closed, and the presentation must not
   imply otherwise.

### v2 — after a five-row pilot, before the remaining twenty-five

The pilot existed to break v1 while breaking it was still cheap, and it did, in
five places. All five were failures of the procedure, not of any row, and none of
them changed a verdict in a direction that favours our argument — the three
adjudicated rows were `carried in part` under v1 and remain `carried in part`
under v2.

1. **`not reachable` conflated two different things.** *Nobody can reach this* is
   a finding about the record. *This fetcher cannot reach this* is a finding
   about us. v1 published the second as though it were the first. Split, and the
   second is now non-terminal.
2. **The `capture` grade assumed archives fail independently of publishers.** On
   one row the publisher, the Internet Archive and archive.today all failed
   inside the same minute. A fallback correlated with the thing it backs up is
   weaker than v1 assumed.
3. **No fetch provenance.** v1 recorded a URL as though reachability were a
   property of a document. It is a property of (document, fetcher, jurisdiction,
   moment). Every artifact now records how it was actually obtained, failures
   included.
4. **No test for a quantity.** A claim asserting "532,000" had no place to record
   that the artifact says "approximately 500,000." The number was neither graded
   nor visible in the verdict.
5. **Step 5 was not total.** `carried in part` with no motive clause fell through
   every case. The renderer silently produced the nearest plausible label, which
   is exactly the failure mode this page exists to catch. It now refuses to
   answer where the rubric does not define one, and says so on the page.

### v1 — pre-registered, superseded

Retained above in git history at `e58acf0`. Rows judged under v1 are marked stale
on the page until re-adjudicated.

## What this page does, and does not do

This page takes a small random sample of claims from a third party's dataset,
goes looking for the primary artifact behind each one, and reports **which
clauses of the claim the artifact carries**.

It does not decide whether claims are true. A clause our search did not support
is a clause we could not source. That is a statement about our search and the
available record, not about the world. The page must contain no sentence of the
form "this claim is false."

It is not about the curator. A claim we could not source is not a finding of bad
faith, incompetence, or error by anyone. `PROCESS.md` puts character out of
scope for this repository and that applies here with extra force, because this
page is pointed at one identifiable person's work.

## Step 0 — Parse the claim into clauses

The quoted claim is split into clauses. Each is typed:

| Type | Definition | Adjudicated? |
|---|---|---|
| `act` | An agent did a thing at a time | **Yes** |
| `plan` | An agent intends, is considering, or is drawing up | No — flagged |
| `motive` | Why an act was done; what it was designed to achieve | **Never** |
| `characterization` | An evaluative label — "crackdown", "purge", "gut" | No — flagged |
| `context` | Background not asserting an act by the subject | No |
| `quote` | Reproduction of somebody's words | Adjudicated as `act` (did they say it) |

Motive is never adjudicated. Not because motive claims are worthless, but
because a document shows what was said, not why, and adjudicating motive is the
precise failure this repository criticises elsewhere. Motive clauses are
labelled and left standing.

## Step 1 — Search for the artifact

For the `act` clauses, search for the primary artifact. Record **what was
searched**, not only what was found. Registries to try, where applicable:

- Federal Register (executive orders, proclamations, rules, notices)
- The acting agency's own `.gov` publication
- CourtListener / PACER (filings, orders, dockets)
- Congress.gov (bills, hearings, testimony)
- The speaker's own account, transcript, or recording
- The acting private body's own release (for third-party compliance claims)
- Internet Archive, where the original has moved or vanished

The artifact is graded with this repository's existing custody grades from
`PROCESS.md`:

- `on the record` — the person's own words, in a transcript, recording, or paper
  they signed
- `constitutive record` — the instrument itself, where the utterance *is* the
  act: a court order, a roll call, a filed complaint, a Federal Register
  instrument. The document does not report the act; it performs it.
- `party account` — a body's own published description of its own conduct: a
  press release, an agency statement. Excellent provenance for *what was said*,
  and a claim like any other about *what was done*. **(v3)**
- `named reporting` — journalism whose source is named and on the record, or
  which publishes the underlying document
- `capture` — an Internet Archive or archive.today capture; custody of a
  document, labelled as a capture
- `none found` — searched, not found. This is a finding and is published as one.

Anonymously sourced material is not admitted, per `PROCESS.md`.

**Captures are not an independent fallback (v2).** v1 treated an archive as the
backstop for a publisher that has moved or removed something. That holds when the
failure is editorial. It does not hold when the failure is at the network or
fetcher layer, where a publisher and both major archives can refuse the same
requester in the same minute — which is what happened on the first row that
needed it. A capture is custody of a document; it is not a guarantee of access,
and it fails in correlation with everything else when the cause is the requester
rather than the record.

### Fetch provenance is recorded, including failures (v2)

Reachability is not a property of a document. It is a property of the tuple
**(document, fetcher, jurisdiction, moment)** — see `OPEN-QUESTIONS.md`
question 9, which this page produced. So each artifact records how it was
actually obtained:

    fetch: { by: agent | human, route, date, status, note }

and a row that could not be fetched records **every route tried, named**, rather
than a bare assertion that something is unavailable. `by: human` marks an
artifact supplied by a person whose tuple differs from the agent's. That is a
legitimate custody route and it reduces to trust assumption 4 in `PROCESS.md` —
*that we read what we say we read*. It carries a cost that must be printed rather
than buried: **human-supplied access widens what we can reach while narrowing
what a reader can independently check.** Where a human can supply either a route
the reader could also use — an archive link, a DOI, a docket number — or a
transcribed quotation from behind a wall, the route ranks above the quotation.

## Step 2 — Clause tests

Each test takes one of four values: `supported`, `unsupported`, `contradicted`,
`n/a`.

| Test | Question |
|---|---|
| `agent` | Does the artifact establish that the actor was who the claim says? |
| `predicate` | Does the artifact establish that the thing described happened? |
| `date` | Does the artifact establish the date as claimed? |
| `modality` | Does the claim describe a completed act, and does the artifact show one? |
| `quantity` | Where the claim asserts a number, does the artifact carry that number? |
| `base rate` | Where the claim asserts novelty or routineness, is the reference class produced? |

**Modality, explained, because it is the only one of the five that is jargon.**
Modality is the *mood* of a claim rather than its content. Grammar already has
the idea: *did*, *will*, *may*, *should*, *was ordered to*, *is considering* are
all different modes of asserting the same underlying event. A claim can name the
right actor, the right act and the right date and still be wrong about whether
the thing was **done**, **planned**, **proposed**, **threatened**, **permitted**
or merely **discussed**.

**Corrected after publication.** This section originally said the dataset
"presents every row in the mode of something having been done" and that drafts
and interim steps "arrive dressed as completed acts." That was an inference from
the shape of the CSV export, and the publisher's own site contradicts it. The
Trump Action Tracker states its scope in its About page disclaimer: it *"records
publicly reported actions, **statements**, policies, legal developments and
**plans**."* Plans and statements are declared, not smuggled. We read the export
and attributed to the project a property of the export — which is the same error
as citing a piece that describes a piece, committed by us, on the day we shipped
a page built to catch it. The original wording is preserved here rather than
deleted.

What survives the correction is narrower and still real: **the declared scope is
global, and modality is unmarked per row.** Nothing in the data or the display
distinguishes a row recording a completed act from a row recording a plan, a
proposal or a statement of intent. A reader of any single row cannot tell which
they are looking at, and the counters, charts and totals built on the dataset
cannot tell either, because a boolean tag matrix has nowhere to put a mood. A
declaration at the top of a site does not survive into a row, an export, or
anything computed from one.

The failure this test catches has a characteristic shape: **the event is real and
the mood is wrong.** It is also directional. A summary drifts toward the more
finished, more decided, more consequential reading — never toward "and then a
temporary procedural thing happened." That is the same directional drift
`PROCESS.md` describes for citations, appearing in tense rather than in
attribution.

A claim asserting a plan or an intention is not thereby false, and is often the
most important thing in a record. It is a *different kind of claim*, and it earns
the `plan not act` flag rather than being graded as though a document could
settle it.

**Quantity (v2).** A claim's number is load-bearing and v1 had nowhere to put it,
so a claim asserting "532,000" against an artifact saying "approximately 500,000"
scored clean. Numbers get their own test. `n/a` where the claim asserts none.
A number that is merely more precise than the artifact's is `unsupported`, not
`contradicted`: the artifact may be rounding, and a different artifact may carry
the exact figure. Say which artifact would settle it.

**Date tolerance.** A claim dated to the day the event was *reported* rather than
the day it *occurred* is marked `unsupported` on `date` with a note, not
`contradicted`. Reporting-date indexing is a defensible convention, and saying so
is cheaper than pretending it is an error.

**A quote is mandatory.** Any test marked `supported` or `contradicted` must
carry a verbatim span from the artifact and the artifact's URL. The page refuses
to render a row that violates this.

## Step 3 — Sourcing test on the row's own citation

Separately from our own search: does the URL the row itself cites rest on unnamed
sources? Values: `named`, `anonymous`, `mixed`, `n/a`. This describes their
citation. It is recorded because this repository does not admit anonymously
sourced claims, so a reader needs to know when a row would fail that rule here
regardless of what our search turned up.

## Step 4 — Verdict, computed

The verdict is **not written by hand**. It is a published function of the fields
above, evaluated at render time. If a row stores a verdict, the page flags it.
The opinion in this page is meant to live in one auditable rule that a reader can
read and re-run, not in thirty separate judgment calls.

| Verdict | Condition |
|---|---|
| `carried` | Artifact found; every applicable test `supported` |
| `carried in part` | Artifact found; at least one `supported` and at least one not |
| `contradicted in part` | Artifact found; at least one test `contradicted` |
| `restated` | The only thing found is the reporting the row already cites; nothing independent |
| `not reachable` | Searched every route we have; the artifact does not appear to exist or is reachable by nobody |
| `awaiting fetch` | **Non-terminal.** The artifact exists but this fetcher could not obtain it |

`restated` is not a criticism. Some acts genuinely leave no public instrument,
and for those, reporting is the record. The point of the label is that a reader
should know which case they are in.

**`awaiting fetch` is the v2 split (see version history).** v1 had one terminal
state where there are two situations, and so published an infrastructure accident
as though it were an evidentiary one. A row is `awaiting fetch` when the block is
plausibly at the requester's end — a 403, a 429, a paywall, a CAPTCHA, a 451 —
rather than at the record's. It is not a verdict about the claim, it never
resolves by the passage of time alone, and it must name every route tried. It is
the state in which a human with a different tuple can move the row, and nothing
else can.

Orthogonal flags, which are not verdicts: `motive present`,
`characterization present`, `plan not act`, `third-party act`,
`anonymous sourcing`, `reachability blocked`.

## Step 5 — The good-faith question, also computed

The question this page was built to answer is whether a good-faith reader can
assert the claim. It is derived, never typed:

| Value | Condition |
|---|---|
| `yes — on the artifact` | `carried`, no motive or characterization clause |
| `yes — on the act, not the characterisation` | `carried` or `carried in part`, **with** a motive or characterization clause |
| `yes — on the documented act, not on every clause` | `carried in part`, **without** any such clause |
| `only on the reporting` | `restated` |
| `not on what we found` | `not reachable` or `contradicted in part` |
| `not yet asked` | `awaiting fetch`, or the row is parked |

**This table must be total (v2).** v1's version left `carried in part` with no
motive clause undefined, and the renderer quietly emitted the nearest plausible
label instead — inventing an answer the procedure did not authorise, which is the
precise failure this whole page is built to detect. The renderer now returns a
gap marker for any combination the table does not cover, and prints it on the
page as a defect in our procedure rather than filling it in. If a future
combination falls through, the page says so instead of guessing.

**`not on what we found` does not mean false.** The page says this next to every
occurrence of it, not once in a footer.

## Step 6 — Symmetric steelman, both mandatory

Every row carries two written fields:

- `forClaim` — the strongest good-faith reading under which the claim stands
- `againstClaim` — the strongest good-faith reading under which it does not

Both written to land. A row with either field empty does not render. This is the
only place on the page where our prose does any work, and it is required to cut
both ways on every single row.

## Step 7 — Enforced at render time

The page validates itself and prints failures in its own footer, in the manner of
the `.gov` host check on `covid19-us-messaging/`:

1. Every `supported` or `contradicted` test has a non-empty quote and an
   artifact URL.
2. `forClaim` and `againstClaim` are both non-empty on every row.
3. No row stores a `verdict` or `goodFaith` value; both are computed.
4. Every row stamps a rubric version; rows below the current version are marked
   stale.
5. Rows with verdict other than `restated` cite an artifact whose host differs
   from the host the upstream row cites.
6. Every artifact carries fetch provenance — who fetched it, by what route, when,
   and with what status. *(v2)*
7. Every parked or `awaiting fetch` row names every route tried. *(v2)*
8. Any row whose combination falls outside the step 5 table is reported as a
   rubric gap, in the page's own footer, and its good-faith value is left
   unanswered. *(v2)*

## Sample and selection

Uniform random draw over all rows of one named export, with a published seed, by
a script in this folder. **The drawn index list is committed before any
adjudication begins**, in its own commit, so that the draw is verifiable from git
history and no row can be quietly dropped for coming out inconveniently.

Every drawn row ships, including rows that come out fully carried, and including
rows we could not finish. A row we abandoned is published with the reason.

## Sourcing of the claims themselves

Claims are quoted verbatim from the upstream export, in quotation marks,
attributed on the row. They are not paraphrased: the claim's own wording is the
artifact under examination here, and summarising it would be the same
laundering-by-hop this repository refuses everywhere else.

The dataset is not mirrored into this repository and no file here permits its
reconstruction. Credit, link, export name and access date appear on the page.

## Known limits, stated up front

- **Thirty rows out of 3,466 is 0.9%.** Any rate computed from it carries sampling
  error large enough that the page should report counts, not percentages, and
  should not be read as a measurement of the dataset.
- **Our search is not exhaustive.** `none found` means we did not find it, with
  the registries we tried listed so the gap is visible and correctable.
- **We are not neutral about method** — this whole repository argues a position
  about sourcing. That position is what put this page here, and it is stated
  rather than hidden.
- **Strict admissibility has a direction**, discussed at `OPEN-QUESTIONS.md`
  question 5. It disfavours claims that will never produce an artifact, which is
  not the same as claims that are wrong.

## Fetching through a human's browser (v3)

archive.today refuses automated fetchers: rate limits, then a CAPTCHA. Row 527
needed it and could not have it. There is a route available — the page open in
the operator's own Chrome, read through a browser extension — and it is worth
being precise about what that is and is not, because "bypass" is the wrong word
for it.

**What the control is for.** A CAPTCHA establishes that a human is present. When
the operator opens the page in their own browser, in their own session, and
solves any challenge themselves, **a human is present**. The signal is satisfied,
not faked. That is materially different from automating a solve or driving a
browser at machine rates, both of which defeat the control rather than meeting
it, and neither of which we will do.

**Three constraints that follow, and they are strict.**

1. Anything obtained this way is recorded `by: human` and carries the cost
   stated above: it widens what we can reach and narrows what a reader can check
   independently.
2. **The route must be one the reader can also take.** This is what makes the
   archive case unusually clean — a reader with a browser can open the same
   capture and see the same thing, which is not true of a paywalled article we
   transcribe. Reader-reproducible access ranks far above operator-only access.
3. Rate is human rate. A page at a time, because a person is reading it.

**The honest residue.** We are the party deciding that our own use satisfies the
spirit of somebody else's access control, and that is a self-serving judgment
however carefully argued. It is recorded here rather than left as an
undocumented convenience, so that a reader who disagrees can see exactly what
was done and object to it on the record.

## Classification notes, and one lens that keeps recurring (v3)

Our five tests ask whether a document carries a sentence. They cannot ask whether
an event belongs in the domain it was filed under. That question came from a
reader rather than from anything we built, and it needed somewhere to live.

A **classification note** records such an objection and refuses to settle it. It
quotes the publisher's own criterion in full, states the objection, states the
best case against it at its honest weight, and declines to rule. We do not grade
whether a classification is correct: that is an editorial judgement, and the rule
that stops us grading motive stops us grading this. What we can do is check an
action against a published criterion, and make the dispute visible instead of
leaving it invisible under a tag.

### Political pressure is not apparatus pressure

The first classification note produced a distinction general enough to name,
because it will recur:

| | |
|---|---|
| **Political pressure** | endorsement withdrawn, funding withheld, a committee seat lost, a primary challenger backed. Imposed by political actors, using political means, available to any party leader. |
| **Apparatus pressure** | investigation, prosecution, audit, deportation, clearance revocation, licence review. Machinery built for non-political purposes, redirected at a political target. |

**The test between them: does the target have a political remedy?** A primary
challenge can be answered by out-organising it. An investigation cannot be
answered by winning a vote. That asymmetry is checkable rather than atmospheric,
and it does not depend on anyone's view of the actors.

This matters for a tracker of democratic erosion because political pressure is
universal and ancient. In parliamentary systems it is formal and harsher than
anything an American president can do to a legislator — withdrawing the whip is
an explicit act, and twenty-one Conservative MPs lost it over Brexit votes in
2019, which nobody files as backsliding. So a domain whose criterion is read
broadly enough to include ordinary party discipline stops distinguishing
anything, and the reference class runs against the classification rather than
for it.

**It is a base-rate question, and therefore already testable under this rubric.**
The `base rate` test does not bite on a sentence that asserts nothing about
novelty. It bites on a classification, which by filing an event under an erosion
domain implicitly asserts the event is not ordinary politics. Where that is the
live dispute, produce the reference class.

### Statutory function performed is not departure from norm

The second instance of the same pattern, recorded because there will be a third.

| | |
|---|---|
| **The office doing its job** | the Solicitor General arguing the government's position in the Supreme Court; the Attorney General directing litigation; a President nominating judges. |
| **Departure from the office's own conventions** | reversing a long-held United States position without explanation; confessing error to unwind a case; bypassing the office that normally decides. |

The first is not erosion, however much one dislikes the position being argued.
The Solicitor General has argued the government's cases since the office was
created by the Act of 22 June 1870, ch. 150, sec. 2, 16 Stat. 162 — "an officer
learned in the law, to assist the Attorney-General in the performance of his
duties" — language that survives verbatim in 28 U.S.C. 505 today, with the
operative function at 28 U.S.C. 518(a) and 28 C.F.R. 0.20(a).

One qualification, because the statute is narrower than the shorthand. It says
suits "in which **the United States** is interested" and assistance to **the
Attorney General**, not the President's policy position. That gap is where the
Tenth Justice tradition lives — confessions of error, declining to seek
certiorari, a duty of candour that can cut against the administration's preferred
litigating position. So "argues the current government's position" is the core
function and not a complete description of the office.

Both halves reduce to the same testable thing: **produce the reference class.**
How often Solicitors General switch positions between administrations is a
studied number, not an atmosphere.

**Nothing in the dataset raises this.** Zero of 3,466 rows mention the Solicitor
General. The lens is recorded because the pattern will recur, not because this
particular error was made — and the absence is worth stating in the tracker's
favour, since it is not sweeping ordinary statutory functions into an erosion
count.

### A finding against this rubric, recorded on the first use

The rubric requires a steelman in both directions on every row. On the first
classification note the honest weight was lopsided, and writing the counter as
though it balanced would have manufactured a controversy that does not exist.
**Mandatory symmetry can produce false balance, and a rule that always demands
two sides will sometimes invent one.** Where that happens, state the imbalance
rather than dressing it as a contest. This is not yet fixed in the machinery; the
render still requires both fields to be non-empty and cannot tell a strong
counter from a manufactured one.

## Memory is admissible for technique, never for sources (v3)

Added after a near-miss that would have produced a fabricated finding rather than
a missed one, which is the worse direction and the one this page is least
protected against.

**The rule.** *How* to obtain something may come from memory — that a browser
user-agent gets past hosts which refuse other fetchers, that a public-inspection
mirror sidesteps a redirect wall, that a layout-preserving extractor keeps columns
intact. *What is true about the world* may not. Every source, date, number,
officeholder, citation and page reference is fetched, every time, including when
it feels certain. Especially then.

**The case.** A claim under audit described a named person as Secretary of
Homeland Security. From memory that person held different office, so it was
passed to a research agent as a probable error in the dataset. The department's
own leadership page names him as Secretary, and the word "Acting" does not appear
on it. The claim was correct and we were one step from publishing against it.

Three compounding factors, each of which generalises:

1. **Recency inverts reliability.** Our knowledge of the world ends at a fixed
   point while the claims under audit are often more recent. The more recent a
   claim, the less admissible memory is about it — and that is exactly when a
   recollection feels most current.
2. **The error ran deflationary.** Treating a surprising claim as probably wrong
   is question 10 above, committed while auditing others for its mirror. A rule
   that discounts what it does not expect will manufacture findings, not merely
   miss them.
3. **A current page is not a contemporaneous one.** A leadership page establishes
   who holds an office now, not who held it on the claim's date. That gap is
   recorded rather than closed by assumption.

**Operationally:** when a claim contains a fact that memory contradicts, that is a
signal to fetch, not a signal to doubt the claim. Fetch first, form the view
after. This applies with extra force to delegated research, because a suspicion
passed downstream in a brief arrives looking like a finding.

## We inquire, we do not exploit (v3)

A stance, and the rules that fall out of it. Both were stated by the repository
owner, and both cost us something immediately, which is how we know they are not
decorative.

**Send a truthful user agent.** A user agent states who is asking, and a server
uses it to decide what to serve. A browser string sent by a script is a false
statement about the requester, however ordinary the practice.

We had been spoofing. It was in our fetch notes, in a skill we published for
others to follow, and in the brief we handed to five research agents. When
challenged we measured it across the nine hosts this audit actually depends on —
the Federal Register, the U.S. Code, Justice, the Supreme Court, the Clerk of the
House, a State Department embassy site, Homeland Security, a newspaper, and a
public API. **An honest identifying agent and a spoofed browser string returned
identical status codes on all nine. Every one 200.** The dishonesty bought
nothing.

Our original diagnosis had been wrong in a way worth naming, because it is a
common shape: what actually failed was one framework's own fetch tool, blocked at
the framework level, which plain curl never shared. A *fetcher* difference misread
as a *user-agent* difference, and a dishonest technique built on the misreading.
Diagnose in this order — change fetcher before you touch identity.

**Where a wall is a business model, respect it.** A paywall returning 401 is a
publisher declining to give away what it sells, and that is theirs to decide.
Recording that a source is unreachable to us is a finding about the evidentiary
landscape. Getting around it because we can is not inquiry.

**The dilemma we have not solved, stated rather than buried.** We read one
paywalled article through a capture opened in the operator's own browser. That
route sends the browser's own true agent and a human is genuinely present, so it
is not impersonation — and the publisher would still plainly rather we had paid,
and we are the party judging our own use acceptable. A rule you follow only when
it is free is not a rule.

**Columbo, not a gossip column.** Both figures ask questions; only one is trusted
with the answers. What separates them is not curiosity but what the asking is
*for*, and what becomes of what is found. Columbo's inquiry is bounded by the
case, aimed at establishing what happened, and conducted so the method survives
being examined. Gossip is unbounded, aimed at circulation, and collapses the
moment anyone asks how it was obtained.

This page's only claim on a reader is that its method holds up when inspected.
**So the moment we obtain something by a means we would not print, the method
stops being the thing we are offering.** The rule is not that we can reach
everything. It is that everything we reach was reached in a way we are willing to
describe on the row.
