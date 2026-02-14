PORTNAME=	aiodnsbrute
DISTVERSION=	v0.3.2.r0.ge773a4c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python 3 DNS asynchronous brute force utility.
WWW=		https://github.com/blark/aiodnsbrute

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-aiodns@${PY_FLAVOR} \
		??/py-asyncio@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-uvloop@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
