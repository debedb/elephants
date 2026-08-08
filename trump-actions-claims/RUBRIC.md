# Rubric v2

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
- `document` — published by the body whose act it is
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

**Modality, explained, because it is the only one of the five that is jargon.**
Modality is the *mood* of a claim rather than its content. Grammar already has
the idea: *did*, *will*, *may*, *should*, *was ordered to*, *is considering* are
all different modes of asserting the same underlying event. A claim can name the
right actor, the right act and the right date and still be wrong about whether
the thing was **done**, **planned**, **proposed**, **threatened**, **permitted**
or merely **discussed**.

It carries more weight here than on any other page in this repository, because
the dataset under examination is a tracker of *actions*, and its format presents
every row in the mode of something having been done. Drafts, intentions,
recommendations and interim procedural steps all arrive wearing the same clothes
as completed acts, and nothing in a date-plus-sentence row distinguishes them.

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
