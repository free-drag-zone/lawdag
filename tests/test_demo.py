"""Run from the repository root with python -m unittest discover -s tests."""
from graphlib import CycleError
import json
import unittest

from build import ROOT, render, validate


class DemoTests(unittest.TestCase):
    def setUp(self):
        self.course = json.loads((ROOT / "data/course.json").read_text(encoding="utf-8"))

    def test_release_matches_source(self):
        self.assertEqual((ROOT / "docs/index.html").read_text(encoding="utf-8"), render())

    def test_cycle_is_rejected(self):
        self.course["nodes"]["possession"][3].append("locker")
        with self.assertRaises(CycleError):
            validate(self.course)

    def test_unknown_prerequisite_is_rejected(self):
        self.course["nodes"]["locker"][3].append("missing")
        with self.assertRaises(ValueError):
            validate(self.course)

    def test_invalid_answer_is_rejected(self):
        self.course["quizzes"][0]["a"] = -1
        with self.assertRaises(ValueError):
            validate(self.course)

    def test_quiz_can_return_to_a_concept_used_in_the_essay(self):
        nodes = self.course["nodes"]
        reachable = set()
        pending = [self.course["lessons"][0]["key"]]
        while pending:
            key = pending.pop()
            if key not in reachable:
                reachable.add(key)
                pending.extend(nodes[key][3])
        for quiz in self.course["quizzes"]:
            self.assertIn(quiz["node"], reachable)
