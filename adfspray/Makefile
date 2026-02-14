PORTNAME=	adfspray
DISTVERSION=	6.3d7745d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python3 tool to perform password spraying against Microsoft Online service using various methods.
WWW=		https://github.com/xFreed0m/ADFSpray

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-colorlog@${PY_FLAVOR} \
		??/py-requests-ntlm@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
