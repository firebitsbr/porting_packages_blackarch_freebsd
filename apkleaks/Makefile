PORTNAME=	apkleaks
DISTVERSION=	v2.6.3.r2.gdd5271a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Scanning APK file for URIs, endpoints & secrets.
WWW=		https://github.com/dwisiswant0/apkleaks

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/jadx \
		??/pyaxmlparser \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
