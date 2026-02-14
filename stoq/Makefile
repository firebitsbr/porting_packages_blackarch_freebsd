PORTNAME=	stoq
DISTVERSION=	769.8bfc78b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An open source framework for enterprise level automated analysis.
WWW=		https://github.com/PUNCH-Cyber/stoq

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-json-logger@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
