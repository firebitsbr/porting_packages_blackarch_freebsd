PORTNAME=	chapcrack
DISTVERSION=	17.ae2827f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool for parsing and decrypting MS-CHAPv2 network handshakes.
WWW=		https://github.com/moxie0/chapcrack

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-dpkt@${PY_FLAVOR} \
		??/py-m2crypto@${PY_FLAVOR} \
		??/py-passlib@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
