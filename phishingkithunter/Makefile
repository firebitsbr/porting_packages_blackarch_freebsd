PORTNAME=	phishingkithunter
DISTVERSION=	20.ac9bd1e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Find phishing kits which use your brand/organizations files and image.
WWW=		https://github.com/t4d/PhishingKitHunter

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-pysocks@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-whois@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
