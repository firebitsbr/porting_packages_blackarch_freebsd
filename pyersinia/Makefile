PORTNAME=	pyersinia
DISTVERSION=	49.73f4056
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Network attack tool like yersinia but written in Python.
WWW=		https://github.com/nottinghamprisateam/pyersinia

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-ipy@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-pcapy@${PY_FLAVOR} \
		??/py-pydnet@${PY_FLAVOR} \
		??/py-sphinx@${PY_FLAVOR} \
		??/py-sphinx_rtd_theme@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
