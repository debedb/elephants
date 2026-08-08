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

**Read the site, not only the export — we did not, at first.** Entries here were
originally written from `trump-actions-6-26-26.csv` alone. The CSV is a derived
product: it strips the glossary that defines every domain, the About-page
disclaimer that declares scope, and the statement marking the classifications as
opinion. Several early conclusions were inferences from the export's format that
the publisher's own pages contradict. Corrections are marked inline below rather
than applied silently, and the error itself is recorded as entry 8, because it is
the most useful thing on this list.

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

### 8. Our own error: we audited the export and inferred the project from it

The largest finding here is about us. We built this page from the CSV export and
drew conclusions about the project's method from the export's shape — that
everything was presented as a completed act, that the taxonomy was unexplained,
that judgement was undeclared. All three are contradicted by pages the publisher
maintains and links from her front page:

- [The glossary](https://www.trumpactiontracker.info/glossary) defines all ten
  domains in detail and sources the framework to Levitsky & Ziblatt, Snyder and
  Applebaum.
- The same page states: *"There is always some element of subjectivity in
  assigning actions to different domains"* and *"These classifications are
  expressions of opinion based on the cited sources and should not be read as
  findings of criminality, legal liability, or unlawful conduct unless expressly
  supported by a court judgment or official finding."*
- [The About page](https://www.trumpactiontracker.info/about) declares scope:
  *"records publicly reported actions, statements, policies, legal developments
  and plans."*

The artifact is the site. The CSV is a description of it. We read the description
and attributed its properties to the thing — the exact shape of error this
repository exists to refuse, committed on the day we published a page built to
catch it. Recorded rather than quietly fixed.

### 9. What survives the correction, stated specifically

The disclaimers above are real and they are load-bearing. They are also global,
and they cover the classifications. These points are narrower and still stand:

- **The opinion disclaimer covers the tags, not the prose.** The `Title` field
  asserts facts in ordinary declarative sentences, and nothing on the site marks
  that prose as opinion — correctly, since it is not offered as opinion. Row 437
  renders as "he says" what its own cited source headlines as "White House says
  Trump believes." No classification disclaimer reaches a sentence like that.
- **No sourcing standard is stated anywhere.** The glossary is a classification
  document. 23 of 3,466 citations are `.gov`; executive orders carry Federal
  Register numbers and are cited to newspapers. Whether that is a considered
  choice or an artifact of how the rows were gathered, nothing published says.
- **Subjectivity is acknowledged globally and never locally.** "There is always
  some element of subjectivity" cannot be argued with on any particular row. This
  repository's rule is that a judgement call is printed next to the thing it
  affects, precisely so that it can be attacked specifically.
- **The framework is sourced; the assignments are not.** Three named books are
  credited with the ten domains. No row records which criterion it met. That is
  provenance at the level of the framework with none at the level of the
  application.
- **Modality is declared in scope but unmarked per row.** Actions, statements and
  plans are all admitted, and nothing in the data distinguishes them. A global
  declaration does not survive into a row, an export, or a chart computed from
  one.

### 10. There are two projects, and criticism of one is not criticism of the other

[trumpactiontracker.info](https://www.trumpactiontracker.info) is the source.
A separate third-party dashboard rebuilds the exported CSV into "Strategic
Volume", "Systemic Velocity" and "Tactical Complexity", adds a "Diagnostic
Projection" forecasting institutional collapse before 2028, and cites Russell,
Eco, Arendt, Paxton and Snyder as "Frameworks" without references. It carries
none of the glossary, the scope statement or the opinion disclaimer.

The derivative strips exactly the four things the source does carefully, and adds
claims the source does not make. We conflated the two in our first pass and the
conflation ran through the whole analysis.
