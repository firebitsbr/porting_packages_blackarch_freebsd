PORTNAME=	python-libvmi
DISTVERSION=	v3.7.1.r0.gc21af83
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python interface to LibVMI.
WWW=		https://github.com/libvmi/python

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/libvmi \
		??/py-cffi@${PY_FLAVOR} \
		??/py-future@${PY_FLAVOR} \
		??/py-pkgconfig@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
