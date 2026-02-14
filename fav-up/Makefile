PORTNAME=	fav-up
DISTVERSION=	58.5ce68a8
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	IP lookup by favicon using Shodan.
WWW=		https://github.com/pielco11/fav-up

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-fake-useragent@${PY_FLAVOR} \
		??/py-ipwhois@${PY_FLAVOR} \
		??/py-mmh3@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
