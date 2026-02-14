PORTNAME=	minimodem
DISTVERSION=	353.bb2f34c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A command-line program which decodes (or generates) audio modem tones at any specified baud rate, using various framing protocols.
WWW=		https://github.com/kamalmostafa/minimodem

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/alsa-lib \
		??/fftw \
		??/libpulse \
		??/sndio


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
