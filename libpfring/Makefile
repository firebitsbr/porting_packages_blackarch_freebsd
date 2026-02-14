PORTNAME=	libpfring
DISTVERSION=	7.6.0.r48.gb5d63335
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Library to interface with the PF_RING kernel module.
WWW=		https://github.com/ntop/PF_RING

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/binutils \
		??/bison \
		??/flex \
		??/linux-headers \
		??/make \
		devel/git \
		net/libpcap

RUN_DEPENDS=	??/numactl \
		??/pfring-dkms


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
