PORTNAME=	weeman
DISTVERSION=	91.53c2efa
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	HTTP Server for phishing in python.
WWW=		https://github.com/Hypsurus/weeman

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-html5lib@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-pdb@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
