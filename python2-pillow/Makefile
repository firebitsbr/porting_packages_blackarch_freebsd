PORTNAME=	python2-pillow
DISTVERSION=	6.2.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python Imaging Library (PIL) fork. Python2 version.
WWW=		https://python-pillow.github.io/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/freetype2 \
		??/libraqm \
		??/libwebp \
		??/tk \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/lcms2 \
		??/libimagequant \
		??/libtiff \
		??/openjpeg2 \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
