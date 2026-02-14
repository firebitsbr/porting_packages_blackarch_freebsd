PORTNAME=	detectem
DISTVERSION=	276.bc5f073
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Detect software and its version on websites.
WWW=		https://github.com/spectresearch/detectem

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-click-log@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-docker@${PY_FLAVOR} \
		??/py-dukpy@${PY_FLAVOR} \
		??/py-environs@${PY_FLAVOR} \
		??/py-parsel@${PY_FLAVOR} \
		??/py-pytest@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		??/py-zope-interface@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
