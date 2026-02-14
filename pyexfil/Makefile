PORTNAME=	pyexfil
DISTVERSION=	84.0297b46
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A couple of beta stage tools for data exfiltration.
WWW=		https://github.com/ytisf/PyExfil

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/impacket \
		??/py-base58@${PY_FLAVOR} \
		??/py-faker@${PY_FLAVOR} \
		??/py-librosa@${PY_FLAVOR} \
		??/py-luhn@${PY_FLAVOR} \
		??/py-names@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-progressbar@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-pycryptodomex@${PY_FLAVOR} \
		??/py-pytube3@${PY_FLAVOR} \
		??/py-qrcode@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
