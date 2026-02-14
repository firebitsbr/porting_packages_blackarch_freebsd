PORTNAME=	trevorspray
DISTVERSION=	2.3.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A modular password sprayer with threading, clever proxying, loot modules, and more!
WWW=		https://github.com/blacklanternsecurity/TREVORspray

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-exchangelib@${PY_FLAVOR} \
		??/py-mechanicalsoup@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-pysocks@${PY_FLAVOR} \
		??/py-tldextract@${PY_FLAVOR} \
		??/trevorproxy


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
