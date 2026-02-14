PORTNAME=	lazagne
DISTVERSION=	v2.4.7.r6.g858ff6f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An open source application used to retrieve lots of passwords stored on a local computer.
WWW=		https://github.com/AlessandroZ/LaZagne

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-libkeepass@${PY_FLAVOR} \
		??/py-pbkdf2@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-pydes@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
