PORTNAME=	sdrpp
DISTVERSION=	nightly.r307.g65a0e11
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The bloat-free SDR receiver.
WWW=		https://www.sdrpp.org

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/${_plugindeps[@]} \
		??/cmake \
		devel/git

RUN_DEPENDS=	??/fftw \
		??/glew \
		??/glfw \
		??/libvolk


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
