PORTNAME=	dnscan
DISTVERSION=	209.281721e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A python wordlist-based DNS subdomain scanner.
WWW=		https://github.com/rbsec/dnscan

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-cryptography@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
