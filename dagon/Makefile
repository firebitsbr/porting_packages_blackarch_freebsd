PORTNAME=	dagon
DISTVERSION=	244.f065d7b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Advanced Hash Manipulation.
WWW=		https://github.com/Ekultek/Dagon

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-bcrypt@${PY_FLAVOR} \
		??/py-colorlog@${PY_FLAVOR} \
		??/py-passlib@${PY_FLAVOR} \
		??/py-pydes@${PY_FLAVOR} \
		??/py-pysha3@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
