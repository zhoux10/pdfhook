install:
	pip install -r requirements.txt

run:
	honcho start local

test:
	nosetests tests/
