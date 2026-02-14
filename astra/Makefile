PORTNAME=	astra
DISTVERSION=	489.092804a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Automated Security Testing For REST APIs.
WWW=		https://github.com/flipkart-incubator/astra

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/mongodb \
		??/py-argparse@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-pyjwt@${PY_FLAVOR} \
		??/py-pymongo@${PY_FLAVOR} \
		??/sqlmap \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
