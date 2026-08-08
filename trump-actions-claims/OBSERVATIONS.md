# Observations about the upstream dataset

A running list, appended as rows are worked. Deliberately unambitious: things we
noticed about how this dataset was assembled, recorded so they are not lost, with
no obligation to resolve them.

**Where things go.** Narrow, and about this dataset: here. Generalises to any
evidentiary artifact: [OPEN-QUESTIONS.md](../OPEN-QUESTIONS.md). Unresolved and
needing argument: a GitHub issue.

**None of this is a finding about the curator.** These are properties of files,
checkable by anyone with the same export. The dataset is larger in scope than
anything in this repository and was assembled under constraints we have not had
to work under.

---

### 1. The citation layer encodes a browsing location

Of 3,466 citations, **1,067 (30.8%)** point at UK outlets or at publishers'
international-edition hostnames.

| Publisher | Non-US host | US host |
|---|---|---|
| CNN | `edition.cnn.com` — 80 | `www.cnn.com` — 15, `us.cnn.com` — 2 |
| BBC | `www.bbc.co.uk` — 73 | `www.bbc.com` — 5 |

Plus Guardian 826, Independent 63, HuffPost UK 9, LBC 3, Observer, Belfast
Telegraph. Those URLs were correct where they were collected. The consequence is
that a reader elsewhere following them is not guaranteed the document the curator
saw — which is question 9 in OPEN-QUESTIONS, arrived at from the data rather than
from theory.

### 2. Theme column names change between exports, silently

`Weakening Civil Rights` became `Dismantling social protections and civil
rights`; `Control of Science & Health to Align with State Ideology` became
`Politicisation of science and health`. There is no version field in the file, so
the only way to detect the change is the filename date. Any count spanning that
boundary is counting two different things.

### 3. One URL can back many rows

3,426 distinct URLs across 3,466 rows. One NBC executive-order tracker page is
cited by **16 separate rows**. "One action, one row, one source" does not hold.

### 4. `Index` is dense and may not be stable across exports

Contiguous 1..N of the current snapshot, ordered descending in the file. Whether
a given index refers to the same event in two exports is **unverified** — it
matters for whether the dated snapshots are a usable revision history. Not yet
checked.

### 5. A claim can be more precise than its own citation

Row 473 says "temporary legal status," which is correct for CHNV humanitarian
parole. The Guardian URL it cites has `temporary-protected-status` in its slug,
which is a different programme. The row is right and its source's slug is wrong.
Worth recording because the failure mode runs both ways, and only one direction
gets attention.

### 6. Attribution can tighten in a single hop

Row 437 renders as "he says" what its own cited source headlines as "White House
says Trump believes." Both documents are reachable and can be read side by side.
This is the drift PROCESS.md describes — every hop is where the qualifiers fall
off, and the drift is directional — observed at the smallest possible scale.

### 7. Licensing terms changed between exports

The 1 March 2026 export states CC BY 4.0. The 26 June 2026 export states CC BY-SA
4.0 for site content, adds an express permission for "journalism, research,
education, and other forms of public-interest analysis" with credit, and adds a
restriction on republishing or redistributing the dataset in whole or substantial
part. Anyone working from an older copy is working from different terms.
