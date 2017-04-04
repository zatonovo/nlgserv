# Used for testing or running command line interface
# docker build -t zatonovo/pez_ai .
# docker run -it --rm zatonovo/pez_ai nose2
# docker run -it --rm zatonovo/pez_ai nose2 --log-capture test_tm
# docker run -it --rm zatonovo/pez_ai ./bin/pez_ai -c /pez_ai/conf/tm.cfg

FROM zatonovo/pez_ai:latest
MAINTAINER Brian Lee Yung Rowe "rowe@zatonovo.com"

# RUN pip install pytest nltk
# RUN python -m nltk.downloader punkt words stopwords maxent_ne_chunker \
#  averaged_perceptron_tagger maxent_treebank_pos_tagger

ENV PYTHONPATH='/app'
ADD . /app
WORKDIR /app

#RUN python setup.py install
CMD ["bash"]
