PORTNAME=	exitmap
DISTVERSION=	373.8155029
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A fast and modular scanner for Tor exit relays.
WWW=		https://github.com/NullHypothesis/exitmap

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-configparser@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-pysocks@${PY_FLAVOR} \
		??/py-stem@${PY_FLAVOR} \
		??/tor \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
