PORTNAME=	shellsploit-framework
DISTVERSION=	3.8c5231a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	New Generation Exploit Development Kit.
WWW=		https://github.com/b3mb4m/shellsploit-framework

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-capstone@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-pefile@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
