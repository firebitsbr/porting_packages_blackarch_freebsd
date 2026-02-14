PORTNAME=	pfring-dkms
DISTVERSION=	4164.3c5b344c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Linux kernel module for packet capture at wirespeed.
WWW=		https://github.com/ntop/PF_RING

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/dkms \
		??/linux-headers \
		??/numactl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
