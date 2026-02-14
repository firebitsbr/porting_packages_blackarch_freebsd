PORTNAME=	cpyrit-opencl
DISTVERSION=	0.4.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Pyrit support for Nvidia-CUDA.
WWW=		http://code.google.com/p/pyrit/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cuda-toolkit \
		??/gcc \
		lang/python3

RUN_DEPENDS=	??/libcl \
		??/nvidia \
		??/opencl-headers \
		??/pyrit \
		??/zlib \
		lang/python3 \
		security/openssl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
