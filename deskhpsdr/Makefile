PORTNAME=	deskhpsdr
DISTVERSION=	2.6.77.r50.g1c2d804
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	SDR App for HPSDR protocol and Soapy-API.
WWW=		https://github.com/dl1bz/deskhpsdr

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		??/libxml2 \
		devel/git

RUN_DEPENDS=	??/alsa-lib \
		??/fftw \
		??/gtk3 \
		??/i2c-tools \
		??/json-c \
		??/libgpiod \
		??/libpulse \
		??/libusb \
		??/pipewire \
		??/pipewire-pulse \
		??/soapysdr \
		ftp/curl \
		net/libpcap \
		security/openssl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
