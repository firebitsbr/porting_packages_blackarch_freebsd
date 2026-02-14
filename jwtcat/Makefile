PORTNAME=	jwtcat
DISTVERSION=	77.f80f3d9
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Script performs offline brute-force attacks against JSON Web Token (JWT)
WWW=		https://github.com/aress31/jwtcat

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-coloredlogs@${PY_FLAVOR} \
		??/py-pyjwt@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
