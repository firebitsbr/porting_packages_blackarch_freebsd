PORTNAME=	w13scan
DISTVERSION=	430.432b835
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Passive Security Scanner.
WWW=		https://github.com/boy-hack/w13scan

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-asn1crypto@${PY_FLAVOR} \
		??/py-certifi@${PY_FLAVOR} \
		??/py-cffi@${PY_FLAVOR} \
		??/py-chardet@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-cowpy@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-cssselect@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-pycparser@${PY_FLAVOR} \
		??/py-pyjsparser@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-pysocks@${PY_FLAVOR} \
		??/py-tld@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
