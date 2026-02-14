PORTNAME=	canari
DISTVERSION=	3.3.10
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Maltego rapid transform development and execution framework.
WWW=		https://pypi.org/project/canari/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-argparse@${PY_FLAVOR} \
		??/py-boto3@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-future@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-mr.bob@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-safedexml@${PY_FLAVOR} \
		??/py-service-identity@${PY_FLAVOR} \
		??/py-stringcase@${PY_FLAVOR} \
		??/py-twistedx@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
