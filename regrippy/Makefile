PORTNAME=	regrippy
DISTVERSION=	2.0.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Framework for reading and extracting useful forensics data from Windows registry hives.
WWW=		https://pypi.org/project/regrippy/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-registry@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
