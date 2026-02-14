PORTNAME=	trusttrees
DISTVERSION=	102.a9b7399
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Tool for DNS Delegation Trust Graphing.
WWW=		https://github.com/mandatoryprogrammer/TrustTrees

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-boto3@${PY_FLAVOR} \
		??/py-dnsimple@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-pygraphviz@${PY_FLAVOR} \
		??/py-requests-file@${PY_FLAVOR} \
		??/py-tldextract@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
