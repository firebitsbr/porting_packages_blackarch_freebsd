PORTNAME=	sleuthql
DISTVERSION=	9.29fc878
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python3 Burp History parsing tool to discover potential SQL injection points. To be used in tandem with SQLmap.
WWW=		https://github.com/RhinoSecurityLabs/SleuthQL

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
