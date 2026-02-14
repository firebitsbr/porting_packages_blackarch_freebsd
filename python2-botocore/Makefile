PORTNAME=	python2-botocore
DISTVERSION=	1.13.19
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Low-level, data-driven core of boto 3.
WWW=		https://pypi.org/project/botocore/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-dateutil@${PY_FLAVOR} \
		??/py-docutils@${PY_FLAVOR} \
		??/py-jmespath@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
