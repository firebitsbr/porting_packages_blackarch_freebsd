PORTNAME=	rhodiola
DISTVERSION=	4.8bc08a0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Personalized wordlist generator with NLP, by analyzing tweets (A.K.A crunch2049).
WWW=		https://github.com/utkusen/rhodiola

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/nltk-data \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-exrex@${PY_FLAVOR} \
		??/py-gensim@${PY_FLAVOR} \
		??/py-geotext@${PY_FLAVOR} \
		??/py-hurry-filesize@${PY_FLAVOR} \
		??/py-nltk@${PY_FLAVOR} \
		??/py-textblob@${PY_FLAVOR} \
		??/py-tweepy@${PY_FLAVOR} \
		??/py-wikipedia@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
