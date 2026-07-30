# elephants

Elephants do not forget.

Sourced timelines of things that are easier to remember one at a time than side
by side. One folder per subject; each folder is a self-contained page published
to GitHub Pages.

Published at **[elephants.debedb.com](https://elephants.debedb.com/)**.

| Subject | Page |
|---|---|
| [`covid19/`](covid19/) | COVID-19, 2020 — [elephants.debedb.com/covid19/](https://elephants.debedb.com/covid19/) |

The site is served from its own subdomain rather than
`debedb.github.io/elephants/` because the user site's domain (`www.debedb.com`)
has a wedged Let's Encrypt authorization, so every project repo that inherits it
is HTTP-only. A fresh subdomain gets a clean certificate in seconds.

## House rules

- **Every entry names its instrument.** Who signed it, under what authority, on
  what date. A press conference is not an order. When no signed instrument
  exists, the entry says so out loud instead of citing news coverage as if it
  were one.
- **Link to the primary document**, not to reporting about it. Reporting goes in
  `also`, underneath.
- **Caveats travel with the claim.** Where a date or a superlative is contested
  or depends on an interpretation, the entry carries the note that says which
  reading it took.
- **No build step.** Each page is one self-contained HTML file: open it, or
  serve the folder. The data is a plain array at the top of the file.

Default branch is `master`.
