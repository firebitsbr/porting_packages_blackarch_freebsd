PORTNAME=	google-explorer
DISTVERSION=	140.0b21b57
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Google mass exploit robot - Make a google search, and parse the results for a especific exploit you define.
WWW=		https://github.com/anarcoder/google_explorer

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/chromium \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-docopt@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
