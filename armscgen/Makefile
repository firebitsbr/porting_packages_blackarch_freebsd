PORTNAME=	armscgen
DISTVERSION=	98.c51b7d6
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	ARM Shellcode Generator (Mostly Thumb Mode).
WWW=		https://github.com/alexpark07/ARMSCGen

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-capstone@${PY_FLAVOR} \
		??/py-keystone@${PY_FLAVOR} \
		??/py-unicorn@${PY_FLAVOR} \
		??/unicorn \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
