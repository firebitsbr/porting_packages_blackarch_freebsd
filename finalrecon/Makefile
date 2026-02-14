PORTNAME=	finalrecon
DISTVERSION=	v1.1.7.r16.gac4681c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	OSINT Tool for All-In-One Web Reconnaissance.
WWW=		https://github.com/thewhiteh4t/FinalRecon

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-aiodns@${PY_FLAVOR} \
		??/py-aiohttp@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-dnslib@${PY_FLAVOR} \
		??/py-icmplib@${PY_FLAVOR} \
		??/py-ipwhois@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-psycopg2@${PY_FLAVOR} \
		??/py-tldextract@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
