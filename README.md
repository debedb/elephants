# elephants

Elephants do not forget.

Sourced timelines of things that are easier to remember one at a time than side
by side. One folder per subject; each folder is a self-contained page published
to GitHub Pages.

Published at **[elephants.debedb.com](https://elephants.debedb.com/)**.

| Subject | Page |
|---|---|
| [`covid19/`](covid19/) | COVID-19, 2020–2021 — [elephants.debedb.com/covid19/](https://elephants.debedb.com/covid19/) |
| [`covid19-us-messaging/`](covid19-us-messaging/) | What the US government said about vaccines and transmission — [elephants.debedb.com/covid19-us-messaging/](https://elephants.debedb.com/covid19-us-messaging/) |
| [`covid19-bayes/`](covid19-bayes/) | Shoshin: a beginner's mind updates on the record — [elephants.debedb.com/covid19-bayes/](https://elephants.debedb.com/covid19-bayes/) |

### Pages that reason, rather than record

`covid19-bayes/` is a different kind of page: it makes no claims of its own and
cites no sources of its own. It reads the other two pages **live, at load time**,
walks their documents in date order, and updates a single belief using one
weight per document. Three properties keep it honest:

- **It is never pinned to a copy of the data.** Add, correct or remove an event
  on either timeline and the reasoning changes on next load, with no edit here.
  It stamps the fingerprint of the exact data it reasoned over, so you always
  know which version of the record produced the number you are looking at.
- **New events arrive weightless.** An event with no recorded judgment sits at
  exactly 1.00 and moves nothing, and is listed as unjudged. Nothing acquires
  evidential weight silently.
- **The weights are the only opinion, and they are sliders.** Set them all to
  1.00 and the belief never leaves 0.50. That is the shape of "none of this is
  evidence of anything", and the page will show it to you on request.

No automation is needed for the page to stay current — reading the source pages
at load time *is* the update mechanism. A scheduled job would only be worth
adding later, if we ever want stamped historical snapshots rather than a live
read.

### Per-page provenance rules

A page may narrow the house sourcing rule further, and if it does, it says so at
the top and enforces it in code.

- `covid19-us-messaging/` is **strictly .gov**. Every source is a United States
  government publication — FDA, CDC, MMWR, CDC Stacks, the CDC archive, the
  White House transcript archive. No journalism is cited on any point, including
  points where journalism would help the argument: the most quoted line in the
  whole controversy is absent from that page because it was said on television.
  The page checks its own links at render time and prints a warning in the
  footer if any source is not served from a `.gov` host.

## Open questions, and an invitation

Applying these rules carefully surfaced problems we cannot solve, and that
people have been arguing about for centuries — the difference between who said a
thing and whose act it was, when an officeholder speaks as the institution,
where a claim acquires authority it never earned, and whether an anonymous
source is a lead or evidence.

**[OPEN-QUESTIONS.md](OPEN-QUESTIONS.md)** states them, records where we already
got one wrong in public, and invites philosophers, legal theorists,
epistemologists, journalists and archivists to correct us. We make no claim to
originality. What we have is a small concrete artifact where a rule can be
applied and the cost of applying it is visible on the page.

## Everything here is open source, including the argument

Not just the data. The sources, the criteria that decide what counts as a
source, the argument itself, the case against the argument, the verification
process, and the prompts that produced each round of work are all in this
repository — see **[PROCESS.md](PROCESS.md)**.

That is the point rather than a side effect. An argument you cannot audit is
worth less than one you can, and the natural home for an argument that expects
to be checked is a place where checking it means opening a diff.

## Ethos

**We have a position. We state it, we publish the case against it, and we do not
smuggle it into anything else.**

That is the whole method. Having a point of view is not the problem; pretending
not to have one is. So each page does three things in the open:

1. **States its argument in its own section, in plain words.** An argument you
   have to infer from a layout is an argument that cannot be attacked. Ours is
   written down under a heading that says it is ours.
2. **Publishes the strongest objections to itself**, written to land rather than
   to be knocked down. If the argument loses, we expect it to lose on one of the
   objections we printed ourselves. An event that cuts *against* the argument is
   more valuable to the page than one that supports it, and gets added on the
   same terms.
3. **Keeps our voice out of everything else.** It appears in exactly two places:
   which events share an axis, and the lines explicitly marked "our call".
   Everywhere else the page reports what a source says and attributes it.

This is the difference between arguing and opinionating. We are not telling you
what to think about these documents; we are putting them where you can read them
in an order we chose, saying why we chose it, and handing you the argument
against.

Everything below the argument is not ours, and we never claim it is:

- **We never say "this is ours." We say "this is what we found."** No entry
  rests on our own assertion. Every claim on a page is a link to somebody
  else's document, named, dated and attributed. If we are the only source for
  something, it does not go on the page.
- **Provenance is visible without clicking.** The citation sits on the row, in
  the open. A visualization where you have to hover to find out who says so is
  a visualization asking to be trusted, and we would rather be checked.
- **Sources are labelled by what they are.** `primary` is the instrument, order,
  letter or study itself. `reporting` is a journalist's account, used only where
  no primary document exists. `no document` means no instrument was ever
  published — stated plainly, never papered over with news coverage dressed up
  as a record.
- **Our judgment calls are printed next to the thing they affect.** Where a
  source left a date ambiguous, or a superlative depends on which definition you
  pick, the row carries an explicit "our call" line. The reader can disagree with
  the call without having to reverse-engineer it.
- **We name what we could not verify.** "We looked for a signed order and did not
  find one" is a finding, and it is published as one.
- **A dead link or a wrong citation is a bug**, and is as welcome as any other
  bug. So is "your framing is wrong" — that is a bug report about the only part
  of the page we actually wrote.
- **Disagreement takes the form of a change, not a comment.** There is no
  comment section and no editor to get past: correct the file and send the
  correction (a pull request), and we either accept it in public or say in
  public why not. If you'd rather not argue with us at all, take a complete copy
  and publish your own version (a fork) — different events, different
  conclusion, no permission needed. That is not the argument failing; it is the
  argument working, because then two versions exist and both can be checked
  against the same documents. Send us yours and it gets linked from here.

The vertical axis of these charts carries no magnitude and no ranking. It exists
only so that every document has somewhere to sit where you can see and click its
citation. Time is the only real axis.

## House rules

- **No build step.** Each page is one self-contained HTML file: open it, or
  serve the folder. The data is a plain array at the top of the file, one entry
  per document.
- **Link to the primary document**, not to reporting about it, wherever a
  primary document exists. Reporting is labelled as such and demoted.
- **Colour is a grouping we chose**, so the page says that next to the legend.

Default branch is `master`.

The site is served from its own subdomain rather than
`debedb.github.io/elephants/` because the user site's domain (`www.debedb.com`)
has a wedged Let's Encrypt authorization, so every project repo that inherits it
is HTTP-only. A fresh subdomain gets a clean certificate in seconds.
