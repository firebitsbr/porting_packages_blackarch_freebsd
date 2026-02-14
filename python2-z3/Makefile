PORTNAME=	python2-z3
DISTVERSION=	4.8.5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	High-performance theorem prover.
WWW=		https://github.com/Z3Prover/z3

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		??/gmp \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3

RUN_DEPENDS=	??/libz3 \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
