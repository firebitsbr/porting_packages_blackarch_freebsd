PORTNAME=	androwarn
DISTVERSION=	135.626c02d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Yet another static code analyzer for malicious Android applications.
WWW=		https://github.com/maaaaz/androwarn

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/androguard \
		??/py-future@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-play-scraper@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
