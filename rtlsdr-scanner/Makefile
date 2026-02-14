PORTNAME=	rtlsdr-scanner
DISTVERSION=	v1.3.2.r1.g3c032de
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A cross platform Python frequency scanning GUI for the OsmoSDR rtl-sdr library.
WWW=		https://github.com/EarToEarOak/RTLSDR-Scanner

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-matplotlib@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-pyrtlsdr@${PY_FLAVOR} \
		??/py-pyserial@${PY_FLAVOR} \
		??/rtl-sdr \
		??/wxpython \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
