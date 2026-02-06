.PHONY: setup demo test clean

VENV := .venv
PY := $(VENV)/bin/python

setup:
	@test -x $(PY) || python3 -m venv $(VENV)
	$(PY) -m pip install --upgrade pip
	$(PY) -m pip install -r requirements.txt

demo:
	$(PY) src/run_demo.py

test:
	$(PY) -m pytest -q

clean:
	rm -f reports/coloc_demo_summary.csv \
		reports/coloc_demo_scatter.png
