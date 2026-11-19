# LawDAG

I study computer science and spend most of my time outside class preparing for the Japanese bar exam. I wanted to pick up a question on the train right where I got stuck at my desk. I built LawDAG to try that with a distinction that comes up in both quizzes and essays: who owns something, and who actually has control of it?

**[Try the demo](https://free-drag-zone.github.io/lawdag/)** in Japanese, or download [the single HTML file](docs/index.html) for offline practice. The exercises and audio are bundled in the file.

## Try a missed question

1. Open **短答を解く** (quiz). The first question asks whether the lender's ownership alone rules out the borrower's possession of a camera. Choose **正しい** (true), then **採点する** (check answer) to see what happens after a mistake.
2. Select **関連する基礎を復習** (review the underlying concept). Read the prompt, explain who controls the camera, then reveal the explanation. Use **短答に戻る** and **もう一度解く** to retry.
3. Open **耳で復習** (audio review). A 92-second Japanese recording uses a different example, a library tablet. It pauses so you can think through your answer aloud.

The demo includes one original essay exercise, two original true/false questions and five connected concepts. You can save a one-sentence study note in your browser. The layout has been tested at phone width in desktop Edge. Testing offline playback and resuming a session on my Android phone is next.

## One concept across three kinds of practice

In the library exercise, B borrows a tablet and keeps it beside them at a reading desk. A takes it. To explain whose possession A disturbed, a learner needs to identify who controlled the tablet just before A took it. LawDAG records that dependency in a directed acyclic graph (DAG). The camera quiz links to the same concept, so a mistake there already gives the learner a specific place to review.

I'd like to use that link in two more ways:

- **Audio review.** On the train, if I get stuck on the tablet question, I want to ask for a hint, hear “Who had the tablet within reach?”, and then try the original question again. The current recording has fixed pauses. Following a prerequisite and returning to the question is the next step.
- **Essay feedback.** If I write “The library owns the tablet, so A committed theft,” I want a rule-based checker to flag the jump and ask which facts establish possession. If I already wrote “B was using the tablet and had it beside them when A took it,” the checker should recognize that reasoning even if I never use the word *possession*. Those two drafts would make a first test case for the checker.

The public exercises are original. I also plan to support local links from a concept to a problem number or page in a learner's own books, so those materials can stay on their device.

## Run and verify

From the repository root, with Python 3.10 or later:

```sh
python -m unittest discover -s tests -v
python build.py
```

The build checks the graph and packages the course, player and audio into `docs/index.html`. The tests also check the committed release against its source. In `data/course.json` each node contains a title, question, recall note and list of prerequisite IDs. Each quiz links to a node. Source references in the course point to the Japanese statute and a court decision.
