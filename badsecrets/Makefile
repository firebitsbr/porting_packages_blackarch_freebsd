PORTNAME=	badsecrets
DISTVERSION=	v0.13.47.r0.g4540a4a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A library for detecting known secrets across many web frameworks.
WWW=		https://github.com/blacklanternsecurity/badsecrets

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/flask-unsign \
		??/py-django@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-pyjwt@${PY_FLAVOR} \
		??/py-viewstate@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
