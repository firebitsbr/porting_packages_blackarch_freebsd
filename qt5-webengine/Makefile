PORTNAME=	qt5-webengine
DISTVERSION=	5.15.19
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Provides support for web applications using the Chromium browser project
WWW=		https://www.qt.io

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/gperf \
		??/jsoncpp \
		??/ninja \
		??/pipewire \
		??/poppler \
		??/py-html5lib@${PY_FLAVOR} \
		??/qt5-tools \
		devel/git \
		lang/python \
		www/node

RUN_DEPENDS=	??/ffmpeg \
		??/libevent \
		??/libvpx \
		??/libxcomposite \
		??/libxdamage \
		??/libxkbfile \
		??/libxrandr \
		??/libxss \
		??/libxtst \
		??/minizip \
		??/nss \
		??/pciutils \
		??/qt5-location \
		??/qt5-webchannel \
		??/snappy \
		??/ttf-font \
		textproc/libxslt


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
