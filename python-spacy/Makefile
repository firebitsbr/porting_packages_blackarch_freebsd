PORTNAME=	python-spacy
DISTVERSION=	3.8.11
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Industrial-strength Natural Language Processing (NLP) in Python.
WWW=		https://pypi.org/project/spacy/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cython \
		??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-catalogue@${PY_FLAVOR} \
		??/py-cymem@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-murmurhash@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pathlib@${PY_FLAVOR} \
		??/py-plac@${PY_FLAVOR} \
		??/py-preshed@${PY_FLAVOR} \
		??/py-regex@${PY_FLAVOR} \
		??/py-srsly@${PY_FLAVOR} \
		??/py-thinc@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-typer@${PY_FLAVOR} \
		??/py-ujson@${PY_FLAVOR} \
		??/py-wasabi@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
