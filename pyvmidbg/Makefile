PORTNAME=	pyvmidbg
DISTVERSION=	218.5c71d6d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	LibVMI-based GDB server, implemented in Python.
WWW=		https://github.com/Wenzel/pyvmidbg

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-docopt@${PY_FLAVOR} \
		??/py-libvmi@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
