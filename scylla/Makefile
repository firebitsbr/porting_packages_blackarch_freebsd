PORTNAME=	scylla
DISTVERSION=	99.621b7b8
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Find Advanced Information on a Username, Website, Phone Number, etc.
WWW=		https://github.com/josh0xA/Scylla

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-google@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-pythonwhois@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
