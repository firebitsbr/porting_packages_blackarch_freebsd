PORTNAME=	python2-pytest-twisted
DISTVERSION=	1.12
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A twisted plugin for py.test.
WWW=		https://pypi.org/project/pytest-twisted/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-pip@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-decorator@${PY_FLAVOR} \
		??/py-greenlet@${PY_FLAVOR} \
		??/py-pytest@${PY_FLAVOR} \
		??/py-twistedx@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
