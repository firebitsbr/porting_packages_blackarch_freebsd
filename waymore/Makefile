PORTNAME=	waymore
DISTVERSION=	v8.5.r0.g5d738a6
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Find way more from the Wayback Machine, Common Crawl, Alien Vault OTX, URLScan & VirusTotal.
WWW=		https://github.com/xnl-h4ck3r/waymore

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-psutil@${PY_FLAVOR} \
		??/py-pyaml@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-tldextract@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
