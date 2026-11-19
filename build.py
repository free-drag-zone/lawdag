"""Build the downloadable offline demo from its original course and audio."""
import base64
import json
from graphlib import TopologicalSorter
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def validate(course):
    nodes = course["nodes"]
    edges = {key: item[3] for key, item in nodes.items()}
    for key, parents in edges.items():
        if set(parents) - nodes.keys():
            raise ValueError(f"Unresolved prerequisite in {key}")
    list(TopologicalSorter(edges).static_order())
    for lesson in course["lessons"]:
        if lesson["key"] not in nodes:
            raise ValueError("Unknown lesson root")
    for quiz in course["quizzes"]:
        if quiz["node"] not in nodes or not 0 <= quiz["a"] < len(quiz["opts"]):
            raise ValueError(f"Invalid quiz {quiz['id']}")


def render():
    course = json.loads((ROOT / "data/course.json").read_text(encoding="utf-8"))
    validate(course)
    template = (ROOT / "src/demo.html").read_text(encoding="utf-8")
    audio = base64.b64encode((ROOT / "assets/practice.mp3").read_bytes()).decode("ascii")
    payload = json.dumps(course, ensure_ascii=False).replace("<", r"\u003c")
    return template.replace("__AUDIO__", audio).replace("__COURSE__", payload)


if __name__ == "__main__":
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "docs/index.html").write_bytes(render().encode("utf-8"))
