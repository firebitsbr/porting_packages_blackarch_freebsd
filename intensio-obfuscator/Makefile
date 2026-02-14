PORTNAME=	intensio-obfuscator
DISTVERSION=	280.f66a22b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Obfuscate a python code 2 and 3.
WWW=		https://github.com/Hnfull/Intensio-Obfuscator

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-progress@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
