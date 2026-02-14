PORTNAME=	gasmask
DISTVERSION=	172.2527371
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	All in one Information gathering tool - OSINT.
WWW=		https://github.com/twelvesec/gasmask

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-censys@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		??/py-validators@${PY_FLAVOR} \
		??/py-whois@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
