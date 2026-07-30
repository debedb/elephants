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
