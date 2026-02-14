PORTNAME=	wpa2-halfhandshake-crack
DISTVERSION=	29.3f42124
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A POC to show it is possible to capture enough of a handshake with a user from a fake AP to crack a WPA2 network without knowing the passphrase of the actual AP.
WWW=		https://github.com/dxa4481/WPA2-HalfHandshake-Crack

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-pbkdf2_ctypes@${PY_FLAVOR} \
		??/py-pcapfile@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
