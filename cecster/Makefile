PORTNAME=	cecster
DISTVERSION=	5.15544cb
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool to perform security testing against the HDMI CEC (Consumer Electronics Control) and HEC (HDMI Ethernet Channel) protocols.
WWW=		https://github.com/nccgroup/CECster

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-pyserial@${PY_FLAVOR} \
		??/py-pyusb@${PY_FLAVOR} \
		??/wxpython \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
