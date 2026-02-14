PORTNAME=	python2-importlib_resources
DISTVERSION=	1.0.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Read resources from Python packages.
WWW=		https://github.com/python/importlib_resources

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-toml@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-zipp@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
