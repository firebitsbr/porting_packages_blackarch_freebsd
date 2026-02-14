PORTNAME=	spoofcheck
DISTVERSION=	16.8cce591
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Simple script that checks a domain for email protections.
WWW=		https://github.com/bishopfox/spoofcheck

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-dnslib@${PY_FLAVOR} \
		??/py-emailprotectionslib@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-requests-file@${PY_FLAVOR} \
		??/py-tldextract@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
