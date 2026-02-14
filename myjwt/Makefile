PORTNAME=	myjwt
DISTVERSION=	2.1.0.r1.gd2f4c8a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	This cli is for pentesters, CTF players, or dev. You can modify your jwt, sign, inject, etc.
WWW=		https://github.com/mBouamama/MyJWT

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/exrex \
		??/py-aiocmd@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-pyperclip@${PY_FLAVOR} \
		??/py-questionary@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
