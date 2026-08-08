# Rubric v1 — pre-registered

**Frozen before any row was drawn or read.** Committed ahead of the sample draw so
that a reader can verify from git history that the procedure was fixed before the
results were known. Repository HEAD at freezing: `cfe569c`.

Changing this file is expensive on purpose. Any change bumps the version, and
every row stamped with an older version is marked stale on the page until it is
re-adjudicated under the new one. A rubric that quietly moves to fit its results
is indistinguishable from no rubric.

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
- `capture` — an Internet Archive capture; custody of a document, labelled as a
  capture
- `none found` — searched, not found. This is a finding and is published as one.

Anonymously sourced material is not admitted, per `PROCESS.md`.

## Step 2 — Clause tests

Each test takes one of four values: `supported`, `unsupported`, `contradicted`,
`n/a`.

| Test | Question |
|---|---|
| `agent` | Does the artifact establish that the actor was who the claim says? |
| `predicate` | Does the artifact establish that the thing described happened? |
| `date` | Does the artifact establish the date as claimed? |
| `modality` | Does the claim describe a completed act, and does the artifact show one? |

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
| `carried` | Artifact found; `agent`, `predicate`, `date`, `modality` all `supported` |
| `carried in part` | Artifact found; at least one `supported` and at least one not |
| `contradicted in part` | Artifact found; at least one test `contradicted` |
| `restated` | The only thing found is the reporting the row already cites; nothing independent |
| `not reachable` | Searched; no artifact found |

`restated` is not a criticism. Some acts genuinely leave no public instrument,
and for those, reporting is the record. The point of the label is that a reader
should know which case they are in.

Orthogonal flags, which are not verdicts: `motive present`, `plan not act`,
`third-party act`, `anonymous sourcing`.

## Step 5 — The good-faith question, also computed

The question this page was built to answer is whether a good-faith reader can
assert the claim. It is derived, never typed:

| Value | Condition |
|---|---|
| `yes — on the artifact` | `carried`, no `motive present` flag |
| `yes — on the act, not the characterization` | `carried` or `carried in part`, with `motive present` or characterization clauses |
| `only on the reporting` | `restated` |
| `not on what we found` | `not reachable` or `contradicted in part` |

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
