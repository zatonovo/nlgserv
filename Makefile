# You may have to `sudo mkdir /opt; sudo chmod a+w /opt` if it doesn't exist
# Expect to download 2.7G into /opt/spacy_data, 96M into /opt/nltk_data

PYTHON?=python3
.PHONY: all data run test clean
PROJECT = nlgd
PORT = 8099
HOST_DIR = $(shell pwd)

SPACY_PATH = "import spacy, os.path; print(os.path.join(os.path.dirname(spacy.__file__), 'data'))"
SPACY_DATA = $(shell docker run -it --rm zatonovo/pez_ai ${PYTHON} -c ${SPACY_PATH})
CORPORAOPTS = -v /opt/nltk_data:/usr/share/nltk_data -v /opt/spacy_data:${SPACY_DATA}
DOCKEROPTS = -v ${HOST_DIR}:/app ${CORPORAOPTS}
SERVEROPTS = -p $(PORT):$(PORT)

# There's not really anything to build.
all: 
	docker build -t zatonovo/$(PROJECT) .

# make CONF=tm.cfg run
run:
	docker run -it --rm $(DOCKEROPTS) $(SERVEROPTS) zatonovo/$(PROJECT) ./bin/nlgserv 0.0.0.0 $(PORT) server.log server.err


bash:
	docker run -it --rm $(DOCKEROPTS) zatonovo/$(PROJECT) bash

python:
	docker run -it --rm $(DOCKEROPTS) zatonovo/$(PROJECT) ${PYTHON}

clean:
	rm -f dist build


