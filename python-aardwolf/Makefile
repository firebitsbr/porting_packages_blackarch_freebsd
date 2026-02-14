PORTNAME=	python-aardwolf
DISTVERSION=	0.2.13.r0.g5d44d39
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Asynchronous RDP protocol implementation.
WWW=		https://pypi.org/project/aardwolf/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-setuptools-rust@${PY_FLAVOR} \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-arc4@${PY_FLAVOR} \
		??/py-asn1crypto@${PY_FLAVOR} \
		??/py-asn1tools@${PY_FLAVOR} \
		??/py-asyauth@${PY_FLAVOR} \
		??/py-asysocks@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-minikerberos@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-pyperclip@${PY_FLAVOR} \
		??/py-rle@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-unicrypto@${PY_FLAVOR} \
		??/py-winsspi@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
