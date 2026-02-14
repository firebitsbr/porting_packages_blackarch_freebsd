PORTNAME=	python2-tldextract
DISTVERSION=	2.2.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Accurately separates the gTLD or ccTLD (generic or country code top-level domain) from the registered domain and subdomains of a URL.
WWW=		https://github.com/john-kurkowski/tldextract

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-requests-file@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
