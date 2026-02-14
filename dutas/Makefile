PORTNAME=	dutas
DISTVERSION=	10.37fa3ab
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Analysis PE file or Shellcode.
WWW=		https://github.com/dungtv543/Dutas

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/capstone \
		??/py-capstone@${PY_FLAVOR} \
		??/py-pefile@${PY_FLAVOR} \
		??/py-unicorn@${PY_FLAVOR} \
		??/unicorn \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
