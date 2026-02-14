PORTNAME=	simtrace2
DISTVERSION=	1093.d0ad985
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Host utilities to communicate with SIMtrace2 USB Devices.
WWW=		https://osmocom.org/projects/simtrace2/wiki

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/lksctp-tools \
		devel/git

RUN_DEPENDS=	??/libosmocore \
		??/libusb \
		??/lksctp-tools \
		??/pcsclite \
		??/talloc


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
