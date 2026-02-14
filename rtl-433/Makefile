PORTNAME=	rtl-433
DISTVERSION=	25.12+10.r3708.20260207.05438e48
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A generic software defined radio data receiver, mainly for the 433.92 MHz, 868 MHz (SRD), 315 MHz, 345 MHz, and 915 MHz ISM bands.
WWW=		https://github.com/merbanan/rtl_433

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		devel/git

RUN_DEPENDS=	??/libusb \
		??/rtl-sdr \
		??/soapysdr \
		security/openssl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
