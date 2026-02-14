PORTNAME=	chopshop
DISTVERSION=	444.8bdd393
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Protocol Analysis/Decoder Framework.
WWW=		https://github.com/MITRECND/chopshop

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-dnslib@${PY_FLAVOR} \
		??/py-m2crypto@${PY_FLAVOR} \
		??/py-pylibemu@${PY_FLAVOR} \
		??/py-pymongo@${PY_FLAVOR} \
		??/py-pynids@${PY_FLAVOR} \
		??/py-yaraprocessor@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
