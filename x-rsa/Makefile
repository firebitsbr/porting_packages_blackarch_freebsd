PORTNAME=	x-rsa
DISTVERSION=	166.291d4c7
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Contains a many of attack types in RSA such as Hasted, Common Modulus, Chinese Remainder Theorem.
WWW=		https://github.com/X-Vector/X-RSA

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/gmp \
		??/libmpc \
		??/mpfr \
		??/py-future@${PY_FLAVOR} \
		??/py-gmpy2@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-sympy@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
