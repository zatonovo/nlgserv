# Used for testing or running command line interface
# docker build -t zatonovo/pez_ai .
# docker run -it --rm zatonovo/pez_ai nose2
# docker run -it --rm zatonovo/pez_ai nose2 --log-capture test_tm
# docker run -it --rm zatonovo/pez_ai ./bin/pez_ai -c /pez_ai/conf/tm.cfg

FROM zatonovo/pez_ai:latest
MAINTAINER Brian Lee Yung Rowe "rowe@zatonovo.com"

#RUN pip3 install urllib2

ENV PYTHONPATH='/app:/pez_ai'
ADD . /app
WORKDIR /app

#RUN python setup.py install
CMD ["bash"]
