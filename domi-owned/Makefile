PORTNAME=	domi-owned
DISTVERSION=	41.583d0a5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool used for compromising IBM/Lotus Domino servers.
WWW=		https://github.com/coldfusion39/domi-owned

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-aiohttp@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-fake-useragent@${PY_FLAVOR} \
		??/py-inflect@${PY_FLAVOR} \
		??/py-simple-requests@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
