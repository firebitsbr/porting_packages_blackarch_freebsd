PORTNAME=	kitty-framework
DISTVERSION=	352.cb07609
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Fuzzing framework written in python.
WWW=		https://github.com/cisco-sas/kitty

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-bitstring@${PY_FLAVOR} \
		??/py-docopt@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
