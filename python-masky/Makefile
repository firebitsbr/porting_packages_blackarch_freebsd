PORTNAME=	python-masky
DISTVERSION=	0.2.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Remotely dump domain user credentials via an ADCS.
WWW=		https://github.com/Z4kSec/Masky

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/impacket \
		??/py-asn1crypto@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
