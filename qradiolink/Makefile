PORTNAME=	qradiolink
DISTVERSION=	0.9.2.2.r0.g6a6966f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Multimode SDR transceiver for GNU radio, ADALM-Pluto, LimeSDR, USRP.
WWW=		https://github.com/qradiolink/qradiolink

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/boost \
		??/boost-libs \
		??/cppzmq \
		devel/git

RUN_DEPENDS=	??/alsa-lib \
		??/codec2 \
		??/gnuradio \
		??/gnuradio-osmosdr \
		??/gstreamer \
		??/libconfig \
		??/libftdi \
		??/libjpeg-turbo \
		??/libsndfile \
		??/libuhd \
		??/libvolk \
		??/limesuite \
		??/log4cpp \
		??/opus \
		??/pipewire-pulse \
		??/protobuf \
		??/qt5-base \
		??/qt5-multimedia \
		??/soapysdr \
		??/speexdsp \
		??/sqlite


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
