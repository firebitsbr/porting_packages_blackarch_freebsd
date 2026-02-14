PORTNAME=	pastemonitor
DISTVERSION=	12.bc5d326
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Scrape Pastebin API to collect daily pastes, setup a wordlist and be alerted by email when you have a match..
WWW=		https://github.com/pixelbubble/PasteMonitor

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
