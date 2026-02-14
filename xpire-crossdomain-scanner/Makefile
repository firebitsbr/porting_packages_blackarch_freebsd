PORTNAME=	xpire-crossdomain-scanner
DISTVERSION=	1.0cb8d3b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Scans crossdomain.xml policies for expired domain names.
WWW=		https://github.com/mandatoryprogrammer/xpire-crossdomain-scanner

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-defusedxml@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-tldextract@${PY_FLAVOR} \
		??/py-whois@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
