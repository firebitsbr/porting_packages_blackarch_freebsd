PORTNAME=	anubis-netsec
DISTVERSION=	1.1.3.r10.g52c4d62
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Subdomain enumeration and information gathering tool.
WWW=		https://github.com/jonluca/anubis

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-censys@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-docopt@${PY_FLAVOR} \
		??/py-nmap@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
