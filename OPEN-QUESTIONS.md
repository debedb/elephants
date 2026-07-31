# Open questions, and an invitation

This repository is a practical exercise: put documents on a timeline, say who
signed what and when, refuse to assert anything we cannot attribute. Doing that
carefully for a few months has produced a set of rules — and every one of those
rules turns out to sit on a question that philosophers, legal theorists and
epistemologists have been arguing about for a very long time.

**We are not claiming to have discovered any of this.** These are old questions,
and the people who work on them professionally are better equipped than we are.
What we have is an unusual thing to offer: a small, concrete, public artifact
where a rule can be applied, and where the cost of applying it is visible. When
our attribution rule excluded a significant intelligence assessment, that
exclusion is on the page. When it cost us the single most useful quotation on
another page, that is on the page too.

So this is an invitation to working philosophers, legal theorists, epistemologists,
journalists and archivists: **tell us where we have this wrong.** Not in the
abstract — on the rows.

## The questions we ran into and could not settle

### 1. Attribution and authority are two different things, and we conflated them

"The FBI assessed" raises two unrelated questions that a single sentence hides:

- *Epistemic*: who uttered this, and can a stranger verify it?
- *Deontic*: whose act is it, and were they competent to perform it?

They come apart in both directions. Anthony Fauci's 2024 congressional testimony
has excellent attribution — a sworn, released transcript — and minimal
institutional capacity, since he was by then a private citizen. An authenticated
leaked diplomatic cable is the reverse: the state's own act, with poor
attribution.

We currently grade rows on the first axis only. We think the second axis needs
its own field. We do not know what its values should be.

### 2. When does an officeholder speak *as* the institution?

An organisation's only ultimate voice is whoever holds its top office, so a
director speaking in that capacity is in some sense the institution speaking.
But officeholders also speculate, go off-message, and speak personally while
still holding the office.

Our working test is whether the speaker described an institutional position
("the FBI has assessed") rather than a personal one ("I suspect"), plus whether
the institution repudiated it. That is a heuristic we invented on the spot. We
would like to know what the actual literature says.

### 3. Leads are not evidence — but where exactly is the line?

We adopted a hard rule: claims resting on unnamed sources are not admitted,
regardless of the outlet.

The reasoning survived an argument we got wrong in public. One of us defended
anonymous sourcing by pointing out that Deep Throat's information was accurate.
The correction was immediate and decisive: **we did not know who Deep Throat was
until Mark Felt said so in 2005.** For thirty-three years the claim rested on a
reporter's assurance, and in that period several people were confidently and
wrongly named in print. Nixon did not fall because of Deep Throat; he fell
because of the tapes and sworn on-the-record testimony. The anonymous source
told reporters where to dig. What ended the presidency was what they dug up.

Hence: *anonymous sources are investigative leads, not evidence*. We think this
is right. We do not know how to state it so that it does not also exclude
categories of true knowledge that will never produce an artifact.

### 4. Where does a claim acquire authority it never earned?

Our strongest rule is the one against laundering through links: cite the
artifact, never a piece describing another piece. Each hop is where the
qualifiers fall off, and the drift is directional — always toward more
confidence, never less.

This looks structurally identical to something else we documented: the way
uncertainty written down in a regulatory review file disappeared between that
file and a podium. Same shape, different medium. Is that one phenomenon or two?

### 5. Does strict admissibility have a political direction?

Almost certainly yes, and against us. On-the-record-only systematically favours
people who can afford to speak on the record. Institutions hold press
conferences; whistleblowers go anonymous, because that is what the incentives do
to them. A project whose argument concerns institutional failure, built on a rule
that overweights institutional speech, is arguing with a handicap.

We think that is a feature and have kept the rule. We would like to know whether
that is naive.

### 6. What does it mean for a group to assert something?

"The CDC recommends", "the IC assesses", "27 scientists condemn". We treat these
as speech acts by a single agent because that is how they are written and how
they function. We are aware this is contested and that group positions can
diverge from every individual member's.

### 7. Is quantifying a judgement clarifying, or laundering?

One page assigns a numeric weight to each document and multiplies them into a
posterior probability. We exposed every weight as a slider, published the case
against the whole exercise, and shipped an independence discount because naive
multiplication overstates the movement.

It still worries us. Arithmetic looks like objectivity. A number to one decimal
place implies a precision nobody has. We are not sure the mitigations are
sufficient, or whether the honest output is a direction and a rough size rather
than a percentage.

### 8. Every chain of verification stops somewhere. Where should ours stop, and who says?

The conversation that produced this section began with an objection: you rely on
git for your history, and git can in principle be tampered with, so you need
something stronger. Something stronger has the same problem, and so does the
thing after that. If the answer to distrust is always one more layer of
distrust, there is no answer.

**The strongest version of this objection refutes itself, and the receipt is on
its own ledger.** In 2016 an immutable blockchain produced an outcome its
community found intolerable, and the community forked it — decided, socially,
which history counted. The other branch still exists as Ethereum Classic. The
fork is recorded in Ethereum's own standards process as
[EIP-779, "Hardfork Meta: DAO Fork"](https://eips.ethereum.org/EIPS/eip-779).
Immutability held exactly until humans decided it should not, and then humans
chose which chain was real. The regress was not escaped; it was relocated into
consensus rules and a community vote, and then described as though it had been
eliminated. Git is more honest: it says plainly that it is hashes plus
maintainers plus convention.

**The structure is old.** Münchhausen's trilemma: every justification chain ends
in infinite regress, circularity, or a dogmatic stop, and there is no fourth
option. Wittgenstein's version in *On Certainty*: the spade turns, and what
remains is not a better reason but the hinge the door swings on.

The legal version is Hart's **rule of recognition** — the ultimate rule of a
system is not itself valid or invalid, it is simply practised and accepted.
Kelsen's alternative was to posit a basic norm at the top; Hart's objection was
that a fiction was doing work that a social fact could do honestly.

**And the sharpest statement of it is much older than either.** The Talmudic
account of the oven of Akhnai (Bava Metzia 59b): R. Eliezer proves his position
with miracles and finally with a voice from heaven, and R. Yehoshua stands and
answers *lo ba-shamayim hi* — it is not in heaven. The appeal chain is
terminated, and it is terminated by the highest possible authority renouncing
its standing as final arbiter. Not from lack of power. Because a community that
can always appeal upward is not an interpretive community. The reported response
is laughter: *nitzchuni banai*, my children have defeated me.

**The story does not end well, and we should not skip that.** R. Eliezer is
excommunicated. The text is ambivalent about its own victory, and the casualty is
the man who may have been right on the merits and lost on procedure. That is the
most useful warning here for a project like this one. Our rules will exclude true
claims — the assessment we ruled inadmissible may well be correct — and the
Talmud's warning is that you do not get to feel clean about it.

**So the reframing we think is right:** these rules were never about eliminating
trust. They are about placing it where a stranger can inspect it, and then saying
where it was placed. Not *trust nothing*, which is not available to anyone. Rather:
*here is the smallest set of things we are asking you to trust, named out loud.*

Ours, explicitly:

1. That git and GitHub have not silently altered this repository's history.
2. That the linked artifact is what it appears to be — that the video is not
   fabricated, the transcript not doctored, the archived page not forged.
3. That a publisher's website today shows what it showed then, except where an
   editor's note says otherwise.
4. That we read what we say we read.

Every one of those could fail. We are not defending against a determined
forger, and we want to be explicit that we are not: **the threat model here is
not Moriarty.** Someone committed to fabrication defeats an artifact-based rule
with a good enough forgery, and that contest gets settled somewhere else, by
other means, at some other waterfall. These rules are built for the honest
reader and the honest author — so that someone can follow a link, look at the
thing, and say *I had not thought about that*. That is the whole ambition, and
pretending to a stronger one would be its own kind of laundering.

The open question: is that the right place to stop? Is there a principled account
of where a public evidentiary artifact *should* terminate its chain, as opposed to
where it is convenient to?

## Prior art we are aware of

Split into what we have verified and what we have not, because a reading list is
a set of claims and this repository does not get to exempt its own.

### Verified against a resolvable record

- John Hardwig, "Epistemic Dependence", *The Journal of Philosophy* 82:7 (July
  1985), p. 335. [doi:10.2307/2026523](https://doi.org/10.2307/2026523)
- Sushil Bikhchandani, David Hirshleifer & Ivo Welch, "A Theory of Fads, Fashion,
  Custom, and Cultural Change as Informational Cascades", *Journal of Political
  Economy* 100 (October 1992), pp. 992–1026.
  [doi:10.1086/261849](https://doi.org/10.1086/261849) — the formal model of a
  claim gaining confidence purely by being repeated.
- Christian List & Philip Pettit, *Group Agency*, Oxford University Press, 2011.
  [doi:10.1093/acprof:oso/9780199591565.001.0001](https://doi.org/10.1093/acprof:oso/9780199591565.001.0001)
- Jennifer Lackey, *The Epistemology of Groups*, Oxford University Press (online
  December 2020).
  [doi:10.1093/oso/9780199656608.001.0001](https://doi.org/10.1093/oso/9780199656608.001.0001)
- Onora O'Neill, *Autonomy and Trust in Bioethics*, Cambridge University Press,
  2002. [doi:10.1017/CBO9780511606250](https://doi.org/10.1017/CBO9780511606250)
  — on trust and the limits of accountability machinery. Her Reith Lectures of
  the same year, *A Question of Trust*, are the more directly relevant text and
  are in the unverified list below.
- Bernard Williams, *Truth and Truthfulness*, Princeton University Press
  (Crossref records the digital edition; the original is 2002).
  [doi:10.1515/9781400825141](https://doi.org/10.1515/9781400825141) — accuracy
  and sincerity as virtues, and the risk that the drive to unmask consumes the
  value it serves.
- Ethereum Improvement Proposal 779, "Hardfork Meta: DAO Fork" —
  [eips.ethereum.org/EIPS/eip-779](https://eips.ethereum.org/EIPS/eip-779). The
  community's own record of choosing which history counted.
- Vienna Convention on the Law of Treaties, 1969 —
  [full text (PDF, UN)](https://legal.un.org/ilc/texts/instruments/english/conventions/1_1_1969.pdf).
  Article 7(2)(a) treats heads of state and government as representing their
  state by virtue of their functions; Article 8 concerns acts by unauthorised
  persons; Article 46 limits when a state may invoke its own internal
  competence rules. Question 1 above, already codified.

### Named from memory, not yet verified — corrections welcome

We believe these are relevant and have not checked editions, dates or that we
are characterising them correctly. Treat each as a lead, in the sense of
question 3.

- J.L. Austin, *How to Do Things with Words* — felicity conditions; the
  infelicity of the wrong person performing the act.
- John Searle, *The Construction of Social Reality* and *Making the Social
  World* — status functions and deontic powers.
- H.L.A. Hart, *The Concept of Law* — power-conferring versus duty-imposing
  rules.
- Hans Kelsen on imputation — an act is attributed to a state because a norm
  authorises the organ, not because of who physically performed it.
- Margaret Gilbert, *On Social Facts*; Deborah Tollefsen, *Groups as Agents*;
  Raimo Tuomela on we-mode versus I-mode intentionality.
- C.A.J. Coady, *Testimony: A Philosophical Study*; Miranda Fricker, *Epistemic
  Injustice*.
- Restatement (Third) of Agency — actual versus apparent authority, and
  ratification.
- Ludwig Wittgenstein, *On Certainty* — hinge propositions; justification coming
  to an end.
- Hans Albert on the Münchhausen trilemma.
- Onora O'Neill, *A Question of Trust* (Reith Lectures, 2002).
- Babylonian Talmud, Bava Metzia 59b — the oven of Akhnai. We are working from
  the standard account and would welcome correction from anyone who reads it
  properly, including on the aftermath, which we think matters more than the
  famous line does.

While assembling this list, two guessed identifiers resolved to entirely
different books — one to a work by a different author on a different subject,
one to a different book by the right author. Neither error would have been
visible to a reader. That is the whole argument for the split above, and for
the rule against citing at second hand.

## How to weigh in

Everything here is a file. Disagreement is a change to it.

- **[Open an issue](https://github.com/debedb/elephants/issues/new)** — including
  "your framing of X is wrong", which is the most useful kind.
- **Send a pull request.** Correcting a citation in the unverified list, or
  moving one into the verified list with a resolvable identifier, is a real
  contribution and will be merged on its merits.
- **Fork it.** Build the same thing with different rules and we will link to it
  from here. Two artifacts with different admissibility standards, applied to the
  same documents, would be more informative than either alone.

We will publish disagreement whether or not we accept it, and say why when we
don't. That is the only promise this repository makes that is entirely within
our control.
