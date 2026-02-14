PORTNAME=	frisbeelite
DISTVERSION=	1.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A GUI-based USB device fuzzer.
WWW=		https://github.com/nccgroup/FrisbeeLite

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/libusb \
		??/py-pyusb@${PY_FLAVOR} \
		??/py-wxpython3@${PY_FLAVOR} \
		??/wxwidgets-gtk3 \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
