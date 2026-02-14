PORTNAME=	python-unblob-native
DISTVERSION=	v0.1.6.r1.gd209cdb
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Performance critical parts of Unblob.
WWW=		https://github.com/onekey-sec/unblob-native

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR} \
		lang/rust

RUN_DEPENDS=	lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
