PORTNAME=	cpyrit-cuda
DISTVERSION=	0.5.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The famous WPA precomputed cracker for NVIDIA-CUDA.
WWW=		https://github.com/JPaulMora/Pyrit

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cuda \
		??/gcc \
		lang/python3

RUN_DEPENDS=	??/nvidia \
		??/zlib \
		lang/python3 \
		net/libpcap \
		security/openssl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
