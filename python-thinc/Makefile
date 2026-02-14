PORTNAME=	python-thinc
DISTVERSION=	9.1.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Practical Machine Learning for NLP.
WWW=		https://pypi.org/project/thinc/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-blis@${PY_FLAVOR} \
		??/py-catalogue@${PY_FLAVOR} \
		??/py-cymem@${PY_FLAVOR} \
		??/py-hypothesis@${PY_FLAVOR} \
		??/py-mock@${PY_FLAVOR} \
		??/py-murmurhash@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pathlib@${PY_FLAVOR} \
		??/py-plac@${PY_FLAVOR} \
		??/py-preshed@${PY_FLAVOR} \
		??/py-pydantic@${PY_FLAVOR} \
		??/py-srsly@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-wasabi@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
