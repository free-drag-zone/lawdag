# LawDAG

LawDAG helps a Japanese bar-exam learner turn a missed question into a short review session. When a student confuses ownership with possession, they can revisit that distinction and retry the same question. The essay and the quizzes use the same prerequisite graph.

**[Open the live demo](https://free-drag-zone.github.io/lawdag/)** or download [the single HTML file](docs/index.html) and open it in a browser. It includes the course and Japanese audio. The source links are optional.

1. Open **短答を解く** (quiz). On the first question choose **正しい**, then **採点する**. This deliberately misses the distinction.
2. Select **関連する基礎を復習** (review the underlying concept). Reveal the explanation, return with **短答に戻る**, select **もう一度解く** and try the other answer.
3. Open **耳で復習** (audio review). The recording leaves pauses to answer aloud. No account or microphone is needed.

The baseline is one original essay exercise, two original true/false questions, five connected concepts and about 92 seconds of audio. A learner can keep a one-sentence note in the browser. The app has been exercised at phone width in desktop Edge. Physical Android testing is a milestone for the first sprint.

## Run and verify

From the repository root, with Python 3.10 or later:

```sh
python -m unittest discover -s tests -v
python build.py
```

The build checks the graph and packages the course, player and audio into `docs/index.html`. The tests also check the committed release against its source. In `data/course.json` each node contains a title, question, recall note and list of prerequisite IDs. Each quiz links to a node. Source references in the course point to the Japanese statute and a court decision.

## What I want Devin Bots to own

| When | Work | Evidence |
| --- | --- | --- |
| Day 1 | A data agent implements a local importer for problem IDs, topic IDs and page references against three original fixtures. A QA agent independently defines acceptance cases for a missing reference, a cycle and an interrupted practice session. | An import report and reproducible test cases. |
| Days 2–3 | The mobile agent improves offline playback and session recovery while the data agent fixes faulty imports. I run the flow on my Android phone. | A device and browser version, plus pass/fail results for playback, navigation and recovery. |
| Days 4–5 | A reviewer checks new graph edges against sources. I review the legal reasoning before accepting changes. | Reviewed links over links proposed, including reasons for rejected edges. |
| Days 6–7 | Run the same cases on a clean checkout and summarize regressions and fixes. | A reproducible demo and a short results table. |

Additional credits would fund a second pass with mislabeled page references and interrupted sessions. A later essay checker could flag a missing issue for the learner to revisit. The importer, native-device results and essay checker are planned work. The public examples are original. Personal study materials stay with the learner.
