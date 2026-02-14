PORTNAME=	altdns
DISTVERSION=	78.6728272
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Generates permutations, alterations and mutations of subdomains and then resolves them.
WWW=		https://github.com/infosec-au/altdns

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-dnspython@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-tldextract@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
