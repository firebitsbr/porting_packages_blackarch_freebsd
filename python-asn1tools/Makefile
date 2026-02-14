PORTNAME=	python-asn1tools
DISTVERSION=	0.167.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	ASN.1 parsing, encoding and decoding.
WWW=		https://pypi.org/project/asn1tools/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/licenses \
		??/py-bitstruct@${PY_FLAVOR} \
		??/py-diskcache@${PY_FLAVOR} \
		??/py-prompt_toolkit@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
