PORTNAME=	openwebrx
DISTVERSION=	1.2.2.r389.g640c5b0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Open source, multi-user SDR receiver software with a web interface.
WWW=		https://github.com/jketterl/openwebrx

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/airspyhf \
		??/csdr \
		??/libsdrplay \
		??/netcat \
		??/owrx_connector \
		??/py-js8py@${PY_FLAVOR} \
		??/py-pycsdr@${PY_FLAVOR} \
		??/rtl-sdr \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
