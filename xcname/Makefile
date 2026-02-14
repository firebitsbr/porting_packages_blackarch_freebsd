PORTNAME=	xcname
DISTVERSION=	11.9c475a1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool for enumerating expired domains in CNAME records.
WWW=		https://github.com/mandatoryprogrammer/xcname

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-ipwhois@${PY_FLAVOR} \
		??/py-pywhois@${PY_FLAVOR} \
		??/py-tldextract@${PY_FLAVOR} \
		??/py-whois@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
