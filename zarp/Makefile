PORTNAME=	zarp
DISTVERSION=	0.1.8
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A network attack tool centered around the exploitation of local networks.
WWW=		https://github.com/hatRiot/zarp

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/mitmproxy \
		??/py-flask@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
