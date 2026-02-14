PORTNAME=	python2-mock
DISTVERSION=	3.0.5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Rolling backport of unittest.mock for all Pythons.
WWW=		https://pypi.org/project/mock/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-funcsigs@${PY_FLAVOR} \
		??/py-pbr@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
