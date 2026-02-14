PORTNAME=	mitmap
DISTVERSION=	89.b590f9a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A python program to create a fake AP and sniff data.
WWW=		https://github.com/xdavidhu/mitmAP

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-dnspython@${PY_FLAVOR} \
		??/py-pcapy@${PY_FLAVOR} \
		??/py-twisted@${PY_FLAVOR} \
		??/sslstrip \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
