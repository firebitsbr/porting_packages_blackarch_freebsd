PORTNAME=	gostringsr2
DISTVERSION=	1.1.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Extract strings from a Go binary using radare2.
WWW=		https://github.com/CarveSystems/gostringsr2

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-click@${PY_FLAVOR} \
		??/py-r2pipe@${PY_FLAVOR} \
		??/radare2 \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
