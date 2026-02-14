PORTNAME=	interlace
DISTVERSION=	356.b9eb99f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Easily turn single threaded command line applications into a fast, multi-threaded application with CIDR and glob support.
WWW=		https://github.com/codingo/Interlace/releases

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-colorclass@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
