# How these pages are made

This file exists because the pages make an argument, and an argument whose
construction is hidden is worth less than one whose construction you can audit.
Everything is here: the sourcing rules, the verification steps, the tools, and
the instructions that produced each round of work.

## The short version

1. An event or statement is proposed.
2. The primary document is located — the instrument, order, letter, study,
   transcript or release itself, not an article about it.
3. The document is opened and read. Quotations are copied out of it. Dates are
   taken from it, or from a machine-readable registry, never from coverage.
4. If no primary document exists, the entry says so in those words and cites
   the best available secondary source, labelled as secondary.
5. The entry records what it is, who issued it, and any judgment we made.
6. It ships. Corrections arrive as pull requests.

## Sourcing rules

**House rule, all pages.** Link the primary document. Reporting is labelled
`reporting` and demoted below the primary source. Where no document exists,
the row says `no document` and states that plainly rather than dressing up news
coverage as a record.

**Per-page rules may be stricter, and are stated on the page.**
`covid19-us-messaging/` is strictly `.gov`: every source must be a United
States government publication. The page enforces this in code — it checks each
link's host at render time and prints a warning in its own footer if any source
is not served from a `.gov` domain.

**The rules are applied against our own interest.** When a rule excludes
something useful, the exclusion is published, not quietly taken. Both pages
carry a list of material we went looking for and did not use, with the reason.

## Out of scope, deliberately

These pages record what was decided, by whom, on what date, with what stated
basis. They do not cover:

- **Reception.** How the record was received, who aligned with whom, which
  faction adopted which fact. That is a story about audiences, not about
  documents, and it cannot be sourced to an instrument.
- **Motive.** What anyone intended, believed privately, or was trying to
  achieve. A document shows what was said, not why. Where behaviour is
  suggestive, the row states the behaviour and stops.
- **Character.** Individual officials are named only as signatories and authors,
  because that is what the documents establish. The person who most nearly did
  the thing this repository asks for — publishing a reversal, its basis, and its
  awkward sequencing, in writing, under her own name — is also among the most
  frequently cast as a villain. That asymmetry is a good reason to keep the
  rule rather than an interesting subject for a page.

The line is not squeamishness. Reception and motive are where an argument stops
being checkable, and everything else here is built so a stranger who does not
trust us can check it.

## Verification steps actually used

- **Liveness.** Every URL is fetched before it ships. Dead links are replaced,
  not left as decoration.
- **Dates from registries, not from articles.** Preprint posting dates were
  taken from the Crossref API rather than from news coverage or the publisher's
  page. This caught a real error: secondary sources date the Nishiura
  closed-environment preprint to April 2020, which is its v2 repost; Crossref
  gives the original posting as 3 March 2020 — before the California beach
  closures rather than after them, which changes what the timeline shows.
- **Quotations read from the document.** Where a PDF was not machine-readable
  through the usual tools, it was downloaded and read directly. The Los Angeles
  County beach order and the FDA authorization memorandum were both handled this
  way.
- **Superseded documents.** Where an agency has withdrawn the original, the page
  cites the agency's own surviving successor document and says why. The LA
  County order of 27 March 2021 is cited through the consolidated order of
  10 April, which names it among those it supersedes.
- **Host checking.** The `.gov` page validates its own sources programmatically,
  so a bad link fails loudly on the page itself rather than silently.

## Tools

The pages are written with [Claude Code](https://claude.com/claude-code), an AI
coding agent, directed by the repository owner. The agent does the searching,
fetching, reading and writing; the owner sets the rules, pushes back, and
decides what ships. Neither the agent nor the owner is a source: nothing on
these pages rests on either one's assertion, which is the entire point of the
sourcing rules above.

Stack: one self-contained HTML file per page, no build step, no dependencies,
no framework, no database. The data is a plain array at the top of each file.
GitHub Pages serves it. If every tool used to make this vanished tomorrow, the
pages would still open in a browser and still be editable in a text editor.

## The instructions that shaped it

These are the directives that produced each round, in order. They are recorded
because "what were you actually asked to build" is part of the provenance of
any argument.

1. Build a table of six COVID-19 events with the most authoritative link for
   each.
2. Publish it as a graph on GitHub Pages. Time on the horizontal axis. Make it
   explorable. Public immediately.
3. *Pushback:* the beach-closure entry cites a press conference. Beaches along
   Route 1 were closed — **who authorized it, and when?** Cite the order.
4. The repository conceit is "elephants do not forget."
5. *Pushback:* provenance is not visible enough, so the page is not convincing.
   The vertical axis is not meaningful; it exists so the reader can find the
   provenance. **Never say "this is ours" — say "this is what we found."**
   Transparency is the ethos; put it in the README.
6. Write as someone with a position who is (a) open about having it, (b) open to
   being challenged on it, (c) transparent about sources — **and who is not
   merely opinionating.**
7. Disagreement is voiced as pull requests, or forks. The democracy of open
   source, put into practice by GitHub.
8. Say all that at a level a non-programmer can follow.
9. Do not try to do the whole thing at once. Incremental gets somewhere.
10. Add the first availability of each major vaccine.
11. The first entry was misread: "no known outside transmission" meant
    **outdoor** transmission, and there was a finding circa March 2020. Keep the
    WHO report, add the outdoor finding.
12. Split the subject in two. The second page covers US government and CDC
    messaging on vaccines and transmission. **Only official US government
    sites. No media analysis.**
13. State the `.gov` provenance rule on the page itself.
14. Add the remaining known gaps, and feature prominently on both pages that
    this is entirely open source — the argument, the criteria, the prompts, the
    source. The argument is conducted in the open, on GitHub.

15. Add a meta page: an animation of an unassuming *shoshin* figure doing
    Bayesian reasoning over the results cited here. It must never be pinned to a
    copy of the data — it is tied to a version of what we have, and it updates
    when we do.
16. *Aside, inviting pushback:* the ethos is "sunlight is the best disinfectant,
    do what you must and come what may." Fog of war is granted; what was owed
    was the repeated meta-statement that policy would change with the data, and
    that you deserved to know when and why. Discuss — including where it is
    wrong. (The pushback is recorded in the conversation rather than here; the
    load-bearing one was that "all you had to do" presumes a rhetorical choice
    where the record shows a systems artifact — the uncertainty was written down
    in the review file and fell out between there and the podium.)
17. Add a timeline graph of the running P(H) that responds to the weights. Put
    it in its own block at the bottom, responsive.
18. More contrast, and keep the graph on screen while scrolling the ledger and
    adjusting weights.

## Pages that reason rather than record

`covid19-bayes/` is the first page here that draws a conclusion instead of
recording a document, so it carries extra obligations:

- It cites nothing of its own. Every input is an entry on another page, fetched
  live at load time rather than copied.
- It stamps the fingerprint of the data it reasoned over, so the number on
  screen is always attributable to a specific state of the record.
- Its single opinion — one weight per document — is exposed as a slider and
  listed with a written reason, so a reader can re-run the whole argument on
  their own numbers without asking anyone's permission.
- Events with no recorded judgment default to a weight of 1.00 and are labelled
  unjudged. Nothing gains evidential weight by being added.
- Its own objections section argues that the exercise is the most contestable
  thing in the repository, including the point that Bayesian arithmetic can
  launder a judgment call as a calculation.

## Attribution, and the chain of custody

Added after a long argument about what "attributable" means. Three admissible
grades, and one that is not admitted at all:

- **on the record** — the person's own words in a transcript, a recording, or a
  paper they signed. You can watch or read them saying it.
- **document** — published by the body whose act it is: an agency report, a
  journal statement, a platform policy, a newspaper's own headline or correction.
- **named reporting** — journalism whose source is named and on the record, or
  which publishes the underlying document.
- **anonymously sourced — not admitted.** A claim resting on unnamed sources does
  not appear, regardless of the outlet's reputation or how widely it has been
  repeated. The reasoning: *anonymous sources are investigative leads, not
  evidence.* We did not know who Deep Throat was until Mark Felt said so in 2005,
  and in the intervening decades several people were confidently and wrongly
  named in print. Nixon fell because of the tapes and sworn testimony, not
  because of the source who pointed at them.

**No laundering through links.** A citation points at the artifact — the
recording, the transcript, the report — never at a piece describing another
piece. Every hop is where the qualifiers fall off, and the drift is directional,
always toward more confidence. Where the artifact cannot be reached, the row says
so; it does not cite the nearest hop as though it were the thing.

**An office is not a person, and the difference is dated.** An institution's
ultimate voice is whoever holds its top office, so a director speaking in that
capacity is the institution speaking — but only while they hold it, and only when
describing an institutional position rather than a personal one. The same human
being carries different authority before and after leaving office. Where this
gets genuinely hard, see [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md).

## What this file is not

It is not a claim that the process is neutral. The selection of events is an
editorial act and each page says so in its own words, under a heading that
marks the argument as ours. The process above is designed to make everything
*except* that selection checkable by a stranger who does not trust us.
