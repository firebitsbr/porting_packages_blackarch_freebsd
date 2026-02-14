PORTNAME=	dnstwist
DISTVERSION=	645.3413953
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Domain name permutation engine for detecting typo squatting, phishing and corporate espionage.
WWW=		https://github.com/elceef/dnstwist

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-dnspython@${PY_FLAVOR} \
		??/py-geoip@${PY_FLAVOR} \
		??/py-ppdeep@${PY_FLAVOR} \
		??/py-tld@${PY_FLAVOR} \
		??/py-whois@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
