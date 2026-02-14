PORTNAME=	multitun
DISTVERSION=	1.319a134
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Tunnel arbitrary traffic through an innocuous WebSocket.
WWW=		https://github.com/covertcodes/multitun

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-autobahn@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-dpkt@${PY_FLAVOR} \
		??/py-iniparse@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-pytun@${PY_FLAVOR} \
		??/py-streql@${PY_FLAVOR} \
		??/py-twistedx@${PY_FLAVOR} \
		??/py-typing@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
