PORTNAME=	wmd
DISTVERSION=	30.32e249a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python framework for IT security tools.
WWW=		https://github.com/ThomasTJdev/WMD

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-rarfile@${PY_FLAVOR} \
		??/scapy \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
