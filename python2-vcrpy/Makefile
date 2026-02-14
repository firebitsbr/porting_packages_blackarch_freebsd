PORTNAME=	python2-vcrpy
DISTVERSION=	2.1.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Automatically mock your HTTP interactions to simplify and speed up testing.
WWW=		https://pypi.org/project/vcrpy/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-wrapt@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
