PORTNAME=	python2-nfqueue
DISTVERSION=	0.4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python bindings for libnetfilter_queue by Pierre Chifflier
WWW=		https://www.wzdftpd.net/redmine/projects/nfqueue-bindings/wiki/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		??/swig \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/libnetfilter_queue \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
