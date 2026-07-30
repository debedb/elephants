# elephants

Elephants do not forget.

Sourced timelines of things that are easier to remember one at a time than side
by side. One folder per subject; each folder is a self-contained page published
to GitHub Pages.

Published at **[elephants.debedb.com](https://elephants.debedb.com/)**.

| Subject | Page |
|---|---|
| [`covid19/`](covid19/) | COVID-19, 2020 — [elephants.debedb.com/covid19/](https://elephants.debedb.com/covid19/) |

## Ethos

**We are making a point, and we are transparent about making it.** Both halves
of that sentence are load-bearing.

The point is in the *selection*: which events get put on one axis together, and
the fact that reading them in order does something that reading them apart does
not. That choice is ours, it is an argument, and we say so on the page rather
than pretending the list assembled itself.

Everything else is not ours, and we never claim it is:

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
- **A dead link or a wrong citation is a bug**, and is as welcome in the issue
  tracker as any other bug.

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
