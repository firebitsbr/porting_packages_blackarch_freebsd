PORTNAME=	tlsfuzzer
DISTVERSION=	1952.6bc3586
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	SSL and TLS protocol test suite and fuzzer.
WWW=		https://github.com/tomato42/tlsfuzzer

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-coverage@${PY_FLAVOR} \
		??/py-coveralls@${PY_FLAVOR} \
		??/py-pyaml@${PY_FLAVOR} \
		??/py-pylint@${PY_FLAVOR} \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}

RUN_DEPENDS=	??/py-ecdsa@${PY_FLAVOR} \
		??/py-tlslite-ng@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
