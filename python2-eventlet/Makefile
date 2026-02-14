PORTNAME=	python2-eventlet
DISTVERSION=	0.25.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Highly concurrent networking library.
WWW=		https://pypi.org/project/eventlet/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-dnspython@${PY_FLAVOR} \
		??/py-enum34@${PY_FLAVOR} \
		??/py-greenlet@${PY_FLAVOR} \
		??/py-monotonic@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
