PORTNAME=	canalyzat0r
DISTVERSION=	41.6bc251e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Security analysis toolkit for proprietary car protocols.
WWW=		https://github.com/schutzwerk/CANalyzat0r

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/can-utils \
		??/ffmpeg \
		??/iproute2 \
		??/py-aenum@${PY_FLAVOR} \
		??/py-can@${PY_FLAVOR} \
		??/py-pyside@${PY_FLAVOR} \
		??/py-pyvit@${PY_FLAVOR} \
		??/py-sphinx_rtd_theme@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
